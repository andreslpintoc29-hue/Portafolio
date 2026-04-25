import re
import json

def clean_text(text):
    # Remove common headers/footers found in the manual
    text = re.sub(r'MANUAL DE PROCEDIMIENTOS.*?Fecha:.*?2023', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'SISTEMA DE GESTIÓN DE PROCESOS JUDICIALES.*?TYBA', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'Pǭgina: \d+/\d+', '', text)
    text = re.sub(r'--- PAGE \d+ ---', '', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()

def extract_massive():
    try:
        with open("scratch/full_text.txt", "r", encoding="utf-8") as f:
            full_text = f.read()
    except FileNotFoundError:
        print("Full text not found.")
        return

    # Table of Contents with Page Numbers
    toc = [
        ("Ingreso al Aplicativo", 10),
        ("Gestión de Contraseñas", 11),
        ("Notificación de Actuaciones", 15),
        ("Registro de procesos para Reparto", 17),
        ("Asociar los Sujetos Procesales", 20),
        ("Adjuntar Archivos", 24),
        ("Registro de Tutela Digital", 27),
        ("Consulta de Procesos", 31),
        ("Modificación de Procesos", 33),
        ("Ocultar Sujetos de un Proceso", 34),
        ("Anular sujetos procesales", 35),
        ("Registro de Actuaciones", 36),
        ("Anulación de Repartos", 42),
        ("Adjudicación por conocimiento previo", 43),
        ("Declaración de Impedimento", 60),
        ("Actuaciones que dan Salida al proceso", 61),
        ("Envío al Superior por Interpuestos", 61),
        ("Salida Finalizando Instancia", 65),
        ("Acumulación de Procesos", 65),
        ("Firma de un documento", 68),
        ("Recuperación Segunda Clave", 71),
        ("Fijación Estados", 73),
        ("Admisión de la Tutela", 77),
        ("Notificación Auto Admisorio", 78),
        ("Sentencia de Tutela", 79),
        ("Notificación de la Sentencia", 80),
        ("Impugnación de la Tutela", 81),
        ("Remisión al Superior de Tutela", 82),
        ("Actuaciones de Segunda Instancia", 83),
        ("Remisión a la Corte Constitucional", 86),
        ("Reingreso de procesos anulados", 98),
        ("Registro y Gestión de Audiencias", 104),
        ("Finalización de Audiencias", 110),
        ("Habeas Corpus", 121),
        ("Registro de Usuarios", 129),
        ("Traslado Masivo de Procesos", 137),
        ("Registro Nacional de Emplazados", 139),
        ("Consultas Públicas", 142)
    ]

    tyba_data = {}

    for i in range(len(toc)):
        title, start_page = toc[i]
        end_page = toc[i+1][1] if i+1 < len(toc) else 150
        
        # Search for page markers
        start_marker = f"--- PAGE {start_page} ---"
        end_marker = f"--- PAGE {end_page} ---"
        
        start_idx = full_text.find(start_marker)
        end_idx = full_text.find(end_marker)
        
        if start_idx == -1: continue
        if end_idx == -1: end_idx = len(full_text)
        
        content = full_text[start_idx:end_idx]
        cleaned = clean_text(content)
        
        # Simple step extraction (splitting by common action verbs or punctuation)
        # In a real scenario, this would be more complex, but for a chatbot we need blocks.
        parts = re.split(r'(?<=[\.!\?])\s+(?=[A-Z])', cleaned)
        valid_parts = [p.strip() for p in parts if len(p.strip()) > 30]
        
        if not valid_parts: continue
        
        # Construct module
        slug = title.lower().replace(' ', '_').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('(','').replace(')','')
        
        steps = []
        for j, part in enumerate(valid_parts[:6]): # Max 6 steps per module for clarity
            step_title = part.split(',')[0][:50]
            if len(step_title) < 10: step_title = " ".join(part.split()[:8])
            
            steps.append({
                "title": step_title,
                "text": part,
                "tip": "Siga las instrucciones del sistema en pantalla."
            })
            
        tyba_data[slug] = {
            "title": title,
            "objective": valid_parts[0] if valid_parts else f"Procedimiento de {title}.",
            "requirements": "Contar con acceso al sistema Justicia XXI Web y los permisos correspondientes.",
            "steps": steps,
            "result": f"Se completa el trámite de {title} exitosamente.",
            "errors": ["Datos incorrectos", "Falta de adjuntos PDF", "Sesión expirada"],
            "terms": {"Sistema": "Plataforma TYBA", "Manual": "Documento de referencia oficial"}
        }

    # Save to tybaData.json
    with open('src/tybaData.json', 'w', encoding='utf-8') as f:
        json.dump(tyba_data, f, ensure_ascii=False, indent=2)
    
    print(f"Extraction completed. Total modules: {len(tyba_data)}")

if __name__ == "__main__":
    extract_massive()
