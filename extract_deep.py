import re
import json
import unicodedata

def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '_', value).strip('-_')

def clean_text(text):
    # Aggressive cleaning of headers and footers
    # The header pattern is usually: MANUAL DE PROCEDIMIENTOS Página: X/Y SISTEMA DE GESTIÓN DE PROCESOS JUDICIALES JUSTICIA XXI WEB - TYBA Fecha: DD/MM/YYYY
    
    # Pre-process: join lines but keep double newlines for paragraph separation if needed
    # Actually, the current extract() already passes the raw chunk.
    
    # Remove the specific multi-line header/footer pattern
    patterns = [
        r'MANUAL\s+DE\s+PROCEDIMIENTOS.*?P[áa]gina:\s*\d+/\d+.*?SISTEMA\s+DE\s+GESTI[ÓO]N\s+DE\s+PROCESOS\s+JUDICIALES.*?JUSTICIA\s+XXI\s+WEB\s+-\s+TYBA.*?Fecha:.*?\d{2}/\d{2}/\d{4}',
        r'SISTEMA\s+DE\s+GESTI[ÓO]N\s+DE\s+PROCESOS\s+JUDICIALES.*?TYBA',
        r'MANUAL\s+DE\s+PROCEDIMIENTOS.*?P[áa]gina:\s*\d+/\d+',
        r'RAMA\s+JUDICIAL.*?CONSEJO\s+SUPERIOR.*?JUDICATURA',
        r'Fecha:\s*\d{2}[/\-]\d{2}[/\-]\d{4}',
        r'Ir\s+a\s+contenido',
        r'--- PAGE \d+ ---'
    ]
    
    for p in patterns:
        text = re.sub(p, ' ', text, flags=re.IGNORECASE|re.DOTALL)
    
    # Remove multiple spaces and newlines
    text = re.sub(r'\s+', ' ', text)
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
            if title.lower() in ["presentación", "glosario", "contenido"]:
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
        
        # Remove the title from the start of content if it's there
        if clean_content.upper().startswith(mod['title'].upper()):
            clean_content = clean_content[len(mod['title']):].strip()
            
        # Break into sentences/paragraphs
        # Split by dots followed by space and capital letter
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ0-9])', clean_content)
        valid_sentences = [s.strip() for s in sentences if len(s.strip()) > 30]
        
        desc = f"Capacitación técnica sobre {mod['title']} según el manual oficial."
        if valid_sentences:
            desc = valid_sentences[0]
            if len(desc) > 250: desc = desc[:247] + "..."
            
        steps = []
        step_num = 1
        
        # If we have very few sentences, try to split by other markers like numbers or bullets
        if len(valid_sentences) < 3:
            # Try splitting by numbers like "1. ", "2. "
            parts = re.split(r'\s+\d+\.\s+', clean_content)
            if len(parts) > 2:
                valid_sentences = [p.strip() for p in parts if len(p.strip()) > 10]

        for sent in valid_sentences:
            if step_num > 12: break
            
            # Clean up the sentence from any remaining page numbers or headers
            sent = re.sub(r'P[áa]gina:\s*\d+/\d+', '', sent)
            sent = sent.strip()
            if not sent: continue

            # Generate a better title
            words = sent.split()
            short_title = " ".join(words[:8])
            if len(short_title) > 60: short_title = short_title[:57] + "..."
            
            tip = "Dato del manual"
            if any(k in sent.lower() for k in ["clic", "botón", "seleccione", "ingrese", "digite"]):
                tip = "Acción en el sistema TYBA"
            elif any(k in sent.lower() for k in ["importante", "nota", "atención", "recuerde"]):
                tip = "Observación importante"
            
            steps.append({
                "num": step_num,
                "title": short_title.upper(),
                "text": sent,
                "tip": tip
            })
            step_num += 1
            
        if not steps:
            steps = [{
                "num": 1, 
                "title": "CONSULTAR MANUAL", 
                "text": f"Para este módulo ({mod['title']}), consulte la página {start_page} del manual para detalles específicos.", 
                "tip": "Referencia manual"
            }]
            
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
