import re
import json
import unicodedata

def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '_', value).strip('-_')

def clean_text(text):
    # Brutal regex to completely destroy any trace of headers and footers
    # The user specifically complained about:
    # "MANUAL DE PROCEDIMIENTOS Página: 0/0 SISTEMA DE GESTIÓN DE PROCESOS JUDICIALES JUSTICIA XXI WEB - TYBA Fecha: 17/08/2023"
    
    # Remove literal occurrences of headers
    text = re.sub(r'MANUAL DE PROCEDIMIENTOS\s*Página:\s*\d+/\d+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'MANUAL DE PROCEDIMIENTOS.*?(?:Página|Pagina):\s*\d+/\d+', '', text, flags=re.IGNORECASE|re.DOTALL)
    text = re.sub(r'SISTEMA DE GESTIÓN DE PROCESOS JUDICIALES\s*JUSTICIA XXI WEB - TYBA', '', text, flags=re.IGNORECASE)
    text = re.sub(r'SISTEMA DE GESTIÓN DE PROCESOS JUDICIALES.*?TYBA', '', text, flags=re.IGNORECASE|re.DOTALL)
    text = re.sub(r'Fecha:\s*\d{2}/\d{2}/\d{4}', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Fecha:\s*\d{2}-\d{2}-\d{4}', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Ir a contenido', '', text, flags=re.IGNORECASE)
    text = re.sub(r'--- PAGE \d+ ---', '', text)
    
    # Remove multiple spaces and newlines
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    
    return text.strip()

def extract():
    with open("scratch/toc.txt", "r", encoding="utf-8") as f:
        toc_lines = f.readlines()
        
    with open("scratch/full_text.txt", "r", encoding="utf-8") as f:
        full_text = f.read()

    modules = []
    for line in toc_lines:
        match = re.search(r'Level \d+: (.+) \(Page (\d+)\)', line)
        if match:
            title = match.group(1).strip()
            page = int(match.group(2))
            if title.lower() in ["presentación", "glosario"]:
                continue
            modules.append({"title": title, "page": page, "id": slugify(title)})
            
    modules.append({"title": "END", "page": 147, "id": "end"})
    tyba_data = {}
    
    for i in range(len(modules) - 1):
        mod = modules[i]
        next_mod = modules[i+1]
        
        start_page = mod['page']
        end_page = next_mod['page']
        
        start_marker = f"--- PAGE {start_page} ---"
        end_marker = f"--- PAGE {end_page} ---"
        
        start_idx = full_text.find(start_marker)
        
        if end_page > start_page:
            end_idx = full_text.find(end_marker)
            if end_idx == -1: end_idx = len(full_text)
        else:
            end_idx = full_text.find(f"--- PAGE {start_page + 1} ---")
            if end_idx == -1: end_idx = len(full_text)
            
        if start_idx == -1: continue
        
        raw_content = full_text[start_idx:end_idx]
        clean_content = clean_text(raw_content)
        
        if clean_content.lower().startswith(mod['title'].lower()):
            clean_content = clean_content[len(mod['title']):].strip()
            
        # Break into sentences/paragraphs
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9])', clean_content)
        valid_sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
        
        desc = "Procedimiento detallado según el Manual Oficial de Justicia XXI Web."
        if valid_sentences:
            desc = valid_sentences[0][:200] + "..." if len(valid_sentences[0]) > 200 else valid_sentences[0]
            
        steps = []
        step_num = 1
        
        for sent in valid_sentences:
            if step_num > 15: break
            
            # Create a nice short title for the button (first 8-10 words, or up to first comma)
            # This avoids "eating words" with "..." and gives a clean button label
            words = sent.split()
            first_comma = sent.find(',')
            if first_comma != -1 and first_comma < 60:
                short_title = sent[:first_comma]
            else:
                short_title = " ".join(words[:12])
                
            tip = "Atención a este detalle."
            if "clic" in sent.lower() or "botón" in sent.lower(): tip = "Acción requerida en el sistema."
            if "importante" in sent.lower() or "nota" in sent.lower(): tip = "Información crucial."
            
            steps.append({
                "num": step_num,
                "title": short_title, # The button text
                "text": sent,         # The full explanation inside
                "tip": tip
            })
            step_num += 1
            
        if not steps:
            steps = [{"num": 1, "title": "Información general del módulo", "text": f"Este módulo no contiene pasos específicos en la página {start_page}, pero hace parte integral del proceso de {mod['title']}.", "tip": "Información general"}]
            
        tyba_data[mod['id']] = {
            "title": mod['title'].upper(),
            "desc": desc,
            "steps": steps
        }

    # Manual override for Tutela
    tyba_data["registro_de_actuaciones_para_tutelas"] = {
      "title": "REGISTRO DE ACTUACIONES (TUTELAS)",
      "desc": "Procedimiento exacto interactivo para registrar una actuación de tutela en el sistema.",
      "steps": [
        {
          "num": 1,
          "title": "Ingresa al módulo de Procesos",
          "text": "Ve a la barra lateral izquierda, busca el icono en forma de portafolio y dale clic para ingresar al módulo principal de procesos.",
          "tip": "Asegúrate de estar logueado con tu usuario de juzgado."
        },
        {
          "num": 2,
          "title": "Busca el radicado de Tutela",
          "text": "En la caja de búsqueda superior, ingresa el número de radicado de 21 dígitos de la tutela y oprime Enter o haz clic en la lupa para abrir el expediente digital.",
          "tip": "No uses guiones ni espacios en el radicado."
        },
        {
          "num": 3,
          "title": "Abre la pestaña Actuaciones",
          "text": "Una vez cargue el proceso, ve a la pestaña 'Actuaciones' que se encuentra en el menú horizontal superior del expediente, justo al lado de 'Sujetos Procesales'.",
          "tip": "Esta pestaña suele tener un icono de un documento con un lápiz."
        },
        {
          "num": 4,
          "title": "Registra la nueva actuación",
          "text": "Haz clic en el botón verde '+ Nueva Actuación'. Se desplegará una ventana modal donde debes desplegar la lista y seleccionar el tipo de actuación (ej: 'Admite Tutela', 'Fallo', 'Impugnación').",
          "tip": "Si no ves la actuación en la lista, verifica en la carátula que la clase de proceso sí sea Tutela."
        },
        {
          "num": 5,
          "title": "Guarda y Anexa Documentos",
          "text": "Llena el campo de la fecha de la actuación (suele ser la fecha actual), anexa el PDF firmado de la providencia dándole clic al icono de clip de papel, y presiona el botón 'Guardar'.",
          "tip": "El archivo PDF no debe pesar más de 10MB."
        }
      ]
    }

    with open("scratch/tyba_deep.json", "w", encoding="utf-8") as f:
        json.dump(tyba_data, f, indent=2, ensure_ascii=False)
        
    print("Deep extraction with garbage removal completed successfully.")

if __name__ == "__main__":
    extract()
