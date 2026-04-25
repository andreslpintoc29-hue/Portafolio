import re
import json
import unicodedata

# Manual steps from manual (created from actual manual content)
MANUAL_STEPS = {
    "ingreso_al_aplicativo_justicia_xxi_web_tyba": {
        "title": "INGRESO AL APLICATIVO JUSTICIA XXI WEB (TYBA)",
        "steps": [
            {"num": 1, "text": "Abrir navegador Chrome o Edge recomendado", "tip": ""},
            {"num": 2, "text": "Copiar URL: https://procesojudicial.ramajudicial.gov.co/Justicia21/...", "tip": ""},
            {"num": 3, "text": "Pegar en la barra de direcciones y presionar Enter", "tip": ""},
            {"num": 4, "text": "Hacer clic en opción 'Justicia XXI Web' para ingresar", "tip": ""},
            {"num": 5, "text": "Digitar usuario y contraseña asignados", "tip": ""},
        ]
    },
    "ingreso_interfaz_de_usuario_al_aplicativo_justicia_xxi_web_tyba": {
        "steps": [
            {"num": 1, "text": "Ingresar con usuario y contraseña", "tip": ""},
            {"num": 2, "text": "Si olvida contraseña, usar opción 'Recordar Contraseña'", "tip": ""},
            {"num": 3, "text": "Verificar perfil y permisos asignados", "tip": ""},
            {"num": 4, "text": "Navegar por los menús del aplicativo", "tip": ""},
        ]
    },
    "registro_de_procesos_para_reparto": {
        "steps": [
            {"num": 1, "text": "Ingresar al menú Administración y seleccionar 'Procesos'", "tip": ""},
            {"num": 2, "text": "Hacer clic en botón 'Agregar'", "tip": ""},
            {"num": 3, "text": "Seleccionar Corporación, Especialidad y Tipo de Proceso", "tip": ""},
            {"num": 4, "text": "Seleccionar Clase y Subclase de proceso", "tip": ""},
            {"num": 5, "text": "Asociar los sujetos procesales (demandante y demandado)", "tip": ""},
            {"num": 6, "text": "Adjuntar archivo PDF de la demanda", "tip": ""},
            {"num": 7, "text": "Hacer clic en 'Guardar' para realizar reparto", "tip": ""},
        ]
    },
    "registro_de_tutela_digital": {
        "steps": [
            {"num": 1, "text": "Ir a Administración > Procesos > Agregar", "tip": ""},
            {"num": 2, "text": "Seleccionar Corporación según nível (Municipal/Circuito)", "tip": ""},
            {"num": 3, "text": "Seleccionar Especialidad: Constitutional", "tip": ""},
            {"num": 4, "text": "Tipo Proceso selecciona 'Acción de Tutela'", "tip": ""},
            {"num": 5, "text": "Clase Proceso: seleccionar 'Tutela'", "tip": ""},
            {"num": 6, "text": "Ingresar datos del accionante y accionado", "tip": ""},
            {"num": 7, "text": "Adjuntar tutela en PDF y guardar", "tip": ""},
        ]
    },
    "consulta_de_procesos": {
        "steps": [
            {"num": 1, "text": "Ir a Administración > Procesos", "tip": ""},
            {"num": 2, "text": "Digitar código de proceso (23 dígitos)", "tip": ""},
            {"num": 3, "text": "O seleccionar rango de fechas", "tip": ""},
            {"num": 4, "text": "Hacer clic en 'Consultar'", "tip": ""},
        ]
    },
    "registro_de_actuaciones": {
        "steps": [
            {"num": 1, "text": "Ir a Administración > Actuaciones", "tip": ""},
            {"num": 2, "text": "Buscar el proceso por código", "tip": ""},
            {"num": 3, "text": "Hacer clic en 'Consultar Registro'", "tip": ""},
            {"num": 4, "text": "Seleccionar Ciclo (Radicación, Generales, etc.)", "tip": ""},
            {"num": 5, "text": "Seleccionar Tipo de Actuación", "tip": ""},
            {"num": 6, "text": "Digitar la fecha y anotación", "tip": ""},
            {"num": 7, "text": "Adjuntar documento si es necesario", "tip": ""},
            {"num": 8, "text": "Guardar la actuación", "tip": ""},
        ]
    },
    "notificacion_de_actuaciones": {
        "steps": [
            {"num": 1, "text": "En la lista de actuaciones, hacer clic en icono 'notificar'", "tip": ""},
            {"num": 2, "text": "Seleccionar sujetos procesales a notificar", "tip": ""},
            {"num": 3, "text": "Elegir archivos adjuntos", "tip": ""},
            {"num": 4, "text": "Hacer clic en 'Guardar' para enviar notificación", "tip": ""},
        ]
    },
    "fijacion_estados": {
        "steps": [
            {"num": 1, "text": "Ir a Administración > Fijación Estados", "tip": ""},
            {"num": 2, "text": "Seleccionar fecha de fijación", "tip": ""},
            {"num": 3, "text": "Hacer clic en 'Consultar'", "tip": ""},
            {"num": 4, "text": "Revisar previsualización del estado", "tip": ""},
            {"num": 5, "text": "Confirmar para publicación", "tip": ""},
        ]
    },
    "creacion_de_procesos_para_reparto": {
        "steps": [
            {"num": 1, "text": "Ir a Administración > Procesos", "tip": ""},
            {"num": 2, "text": "Seleccionar Ley (906, 1826 o 600)", "tip": ""},
            {"num": 3, "text": "Elegir Tipo de Proceso (Audiencia Preliminar, etc.)", "tip": ""},
            {"num": 4, "text": "Ingresar código del proceso de Fiscalía", "tip": ""},
            {"num": 5, "text": "Agregar sujetos procesales", "tip": ""},
            {"num": 6, "text": "Guardar para ejecutar reparto automático", "tip": ""},
        ]
    },
    "registro_y_gestion_de_audiencias": {
        "steps": [
            {"num": 1, "text": "Seleccionar tipo de audiencia", "tip": ""},
            {"num": 2, "text": "Crear proceso para reparto", "tip": ""},
            {"num": 3, "text": "Programar fecha y hora", "tip": ""},
            {"num": 4, "text": "Registrar inicio de audiencia", "tip": ""},
            {"num": 5, "text": "Suspender o reanudar según sea necesario", "tip": ""},
            {"num": 6, "text": "Finalizar y guardar acta", "tip": ""},
        ]
    },
    "envio_de_procesos_al_superior_segunda_instancia": {
        "steps": [
            {"num": 1, "text": "Registrar actuación de apelación", "tip": ""},
            {"num": 2, "text": "Seleccionar tipo: 'Envío al Superior por Interpuestos'", "tip": ""},
            {"num": 3, "text": "Elegir efecto (devolutivo o suspensivo)", "tip": ""},
            {"num": 4, "text": "Adjuntar pruebas y guardar", "tip": ""},
            {"num": 5, "text": "Sistema genera reparto automático", "tip": ""},
        ]
    },
    "registro_de_usuarios": {
        "steps": [
            {"num": 1, "text": "Ingresar con usuario Administrador", "tip": ""},
            {"num": 2, "text": "Ir a Seguridad > Usuarios > Agregar", "tip": ""},
            {"num": 3, "text": "Ingresar datos básicos del usuario", "tip": ""},
            {"num": 4, "text": "Seleccionar Rol (Juez, Secretaría, Oficina Judicial)", "tip": ""},
            {"num": 5, "text": "Asociar al despacho correspondiente", "tip": ""},
            {"num": 6, "text": "Guardar - usuario recibe correo con contraseña", "tip": ""},
        ]
    },
    "asociar_los_sujetos_procesales": {
        "steps": [
            {"num": 1, "text": "En el proceso, ir a 'Información Sujetos Procesales'", "tip": ""},
            {"num": 2, "text": "Hacer clic en 'Buscar Sujeto'", "tip": ""},
            {"num": 3, "text": "Ingresar tipo y número de identificación", "tip": ""},
            {"num": 4, "text": "Seleccionar Tipo Sujeto (Demandante/Demandado)", "tip": ""},
            {"num": 5, "text": "Agregar datos de contacto (dirección, teléfono, email)", "tip": ""},
            {"num": 6, "text": "Guardar asociación", "tip": ""},
        ]
    },
    "adjuntar_archivos": {
        "steps": [
            {"num": 1, "text": "En sección 'Archivos Adjuntos', hacer clic en buscar", "tip": ""},
            {"num": 2, "text": "Seleccionar archivo PDF del computador", "tip": ""},
            {"num": 3, "text": "Elegir tipo de archivo (demanda, anexo, prueba)", "tip": ""},
            {"num": 4, "text": "Hacer clic en 'Agregar a la lista'", "tip": ""},
            {"num": 5, "text": "Guardar proceso", "tip": ""},
        ]
    },
}

def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '_', value).strip('-_')

def get_manual_steps(mod_id, mod_title, page_num):
    """Get manually created steps from manual"""
    if mod_id in MANUAL_STEPS:
        steps = MANUAL_STEPS[mod_id]["steps"]
    else:
        # Generic fallback based on title keywords
        steps = [
            {"num": 1, "text": f"Ir a la sección correspondiente del menú", "tip": ""},
            {"num": 2, "text": "Realizar la acción según el proceso", "tip": ""},
            {"num": 3, "text": "Confirmar y guardar cambios", "tip": ""},
        ]
        
        if "consulta" in mod_title.lower():
            steps = [
                {"num": 1, "text": "Ir a Administración > Consultar", "tip": ""},
                {"num": 2, "text": "Ingresar criterios de búsqueda", "tip": ""},
                {"num": 3, "text": "Revisar resultados", "tip": ""},
            ]
        elif "crear" in mod_title.lower() or "registrar" in mod_title.lower():
            steps = [
                {"num": 1, "text": "Ir a opción correspondiente", "tip": ""},
                {"num": 2, "text": "Diligenciar formulario", "tip": ""},
                {"num": 3, "text": "Adjuntar documentos si aplica", "tip": ""},
                {"num": 4, "text": "Guardar cambios", "tip": ""},
            ]
        elif "modificar" in mod_title.lower():
            steps = [
                {"num": 1, "text": "Buscar proceso a modificar", "tip": ""},
                {"num": 2, "text": "Hacer clic en 'Modificar'", "tip": ""},
                {"num": 3, "text": "Realizar cambios", "tip": ""},
                {"num": 4, "text": "Guardar", "tip": ""},
            ]
        elif "anular" in mod_title.lower():
            steps = [
                {"num": 1, "text": "Buscar elemento a anular", "tip": ""},
                {"num": 2, "text": "Confirmar anulación", "tip": ""},
                {"num": 3, "text": "Verificar que sea la última acción", "tip": ""},
            ]
    
    # Add title if not in manual steps
    title = mod_title.upper()
    if mod_id in MANUAL_STEPS:
        title = MANUAL_STEPS[mod_id].get("title", title)
    
    desc = f"PASO A PASO: {steps[0]['text'][:50]}..."
    
    return {
        "title": title,
        "desc": desc,
        "steps": steps
    }

def extract_modules():
    with open("scratch/toc.txt", "r", encoding="utf-8") as f:
        toc_raw = f.read()
    
    toc_lines = [l for l in toc_raw.split('\n') if 'Level' in l]
    
    modules = []
    for line in toc_lines:
        match = re.search(r'Level \d+: (.+) \(Page (\d+)\)', line)
        if match:
            title = match.group(1).strip()
            page = int(match.group(2))
            if title.lower() not in ["presentación", "glosario"]:
                modules.append({"title": title, "page": page, "id": slugify(title)})
    
    modules.append({"title": "END", "page": 9999, "id": "end"})
    
    html_nodes = ""
    tyba_data = {}
    
    for i in range(len(modules) - 1):
        mod = modules[i]
        
        data = get_manual_steps(mod["id"], mod["title"], mod["page"])
        
        tyba_data[mod["id"]] = {
            "title": data["title"],
            "desc": data["desc"],
            "steps": data["steps"]
        }
        
        # Category
        category = "MODULO OFICIAL"
        if "tutela" in mod["title"].lower(): category = "TUTELAS"
        elif "audiencia" in mod["title"].lower(): category = "AUDIENCIAS"
        elif "notificaci" in mod["title"].lower(): category = "NOTIFICACIONES"
        elif "reparto" in mod["title"].lower() or "proceso" in mod["title"].lower(): category = "GESTIÓN PROCESOS"
        
        short_title = mod["title"][:22] + "..." if len(mod["title"]) > 22 else mod["title"]
        
        html_nodes += f"""
                    <!-- Categoría: {category} -->
                    <div class="ai-brain-node tyba-node" data-case="{mod['id']}">
                      <img src="/ai_brain_icon.png" alt="Brain Icon" class="brain-icon" style="filter: hue-rotate(10deg) drop-shadow(0 0 15px var(--accent-cyan));">
                      <div class="neural-pulse"></div>
                      <span class="brain-label" style="font-size: 0.6rem;">{short_title.upper()}</span>
                      <div class="hologram-data">
                        <h3>{category}</h3>
                        <p>{data['desc']}</p>
                        <span class="status-online">PÁGINA {mod['page']}</span>
                      </div>
                    </div>\n"""
    
    with open("scratch/tyba_generated.json", "w", encoding="utf-8") as f:
        json.dump(tyba_data, f, indent=2, ensure_ascii=False)
    
    with open("scratch/tyba_nodes.html", "w", encoding="utf-8") as f:
        f.write(html_nodes)
    
    print(f"Generados {len(tyba_data)} módulos con pasos del manual")

if __name__ == "__main__":
    extract_modules()