import json

# Load existing data
with open('src/tybaData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Refine 'Registro de procesos para Reparto'
data["registro_de_procesos_para_reparto"] = {
    "title": "REGISTRO DE PROCESOS PARA REPARTO",
    "objective": "Iniciar la creación de un nuevo expediente judicial en el sistema para que sea asignado a un despacho.",
    "requirements": "Documentos iniciales en PDF y datos básicos de las partes.",
    "steps": [
        {
            "title": "Módulo de Procesos",
            "text": "Ingrese al módulo principal de 'Procesos' y haga clic en el botón superior '+ Nuevo Proceso'.",
            "tip": "Verifique que se encuentre en la oficina judicial correcta."
        },
        {
            "title": "Datos Básicos",
            "text": "Seleccione la Clase, Subclase y Recurso. El sistema cargará automáticamente los campos necesarios según la especialidad.",
            "tip": "Si es una tutela, use el módulo específico de Tutela Digital."
        },
        {
            "title": "Sujetos Procesales",
            "text": "Agregue al Demandante y Demandado con sus respectivos números de identificación y correos electrónicos.",
            "tip": "Es vital que los correos sean correctos para las notificaciones automáticas."
        },
        {
            "title": "Adjuntar Demanda",
            "text": "Suba los archivos PDF de la demanda y sus anexos. El sistema permite archivos de hasta 15MB.",
            "tip": "Asegúrese de que los archivos no tengan virus y no estén protegidos con contraseña."
        },
        {
            "title": "Finalizar Reparto",
            "text": "Haga clic en el botón 'Repartir'. El sistema generará el acta de reparto con el despacho asignado y el número de radicado de 21 dígitos.",
            "tip": "Descargue y guarde el acta de reparto para su control."
        }
    ],
    "result": "El proceso queda radicado con éxito y se genera el número único de 21 dígitos.",
    "errors": [
        "Falta de sujetos obligatorios",
        "Error en la conexión al subir archivos pesados",
        "Especialidad no habilitada para el despacho"
    ],
    "terms": {
        "Reparto": "Distribución automática del proceso a un despacho.",
        "Radicado": "Identificador único de 21 dígitos del expediente.",
        "Sujetos": "Partes que intervienen en el proceso (Demandante/Demandado)."
    }
}

with open('src/tybaData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Refined 'Registro de procesos para Reparto' in tybaData.json")
