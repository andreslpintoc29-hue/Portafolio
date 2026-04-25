import json

# Load existing data
with open('src/tybaData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Hyper-direct (puntual) refinement
data["registro_de_procesos_para_reparto"] = {
    "title": "REGISTRO DE PROCESOS PARA REPARTO",
    "objective": "Asignar un nuevo proceso a un despacho judicial de forma automática.",
    "requirements": "Acceso al módulo de Administración > Procesos.",
    "steps": [
        {
            "title": "Inicio",
            "text": "Vaya a Administración -> Procesos y clic en 'Agregar'.",
            "tip": "Módulo principal."
        },
        {
            "title": "Campos Clave",
            "text": "Seleccione Corporación, Especialidad y Clase del proceso.",
            "tip": "Defina el marco legal."
        },
        {
            "title": "Partes",
            "text": "Asocie al demandante y demandado en la pestaña 'Sujetos'.",
            "tip": "Obligatorio."
        },
        {
            "title": "Finalización",
            "text": "Cargue la demanda y presione 'Repartir'.",
            "tip": "Genera el acta final."
        }
    ],
    "result": "Se genera el radicado de 21 dígitos y se asigna el Juez.",
    "errors": [
        "Falta de archivos adjuntos",
        "Sujetos mal identificados"
    ],
    "terms": {
        "Reparto": "Asignación al azar.",
        "Radicado": "Número del proceso."
    }
}

# Add a separate module for "Consultar Reparto" (likely what the user wants if they say 'nothing to do with creation')
data["consulta_de_reparto"] = {
    "title": "CONSULTAR RESULTADOS DE REPARTO",
    "objective": "Ver qué procesos han sido asignados a un despacho específico.",
    "requirements": "Usuario de Juez o Secretario.",
    "steps": [
        {
            "title": "Bandeja de Entrada",
            "text": "Al ingresar al sistema, verá la cuadrícula de 'Notificaciones'.",
            "tip": "Es la primera pantalla."
        },
        {
            "title": "Aviso de Reparto",
            "text": "Busque el icono de la campana con el número de procesos asignados por reparto.",
            "tip": "Es puramente informativo."
        },
        {
            "title": "Filtro de Búsqueda",
            "text": "Use la casilla 'Filtrar' en la grilla para buscar por radicado o tipo de actuación 'Radicación y Reparto'.",
            "tip": "Agiliza la ubicación del expediente."
        }
    ],
    "result": "Acceso al expediente digital del proceso recién asignado.",
    "errors": ["El proceso no aparece si aún no se ha firmado el acta de reparto central."],
    "terms": {
        "Grilla": "Tabla donde se muestran los procesos.",
        "Campana": "Icono de aviso de nuevas asignaciones."
    }
}

with open('src/tybaData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Puntual refinement and addition of 'Consulta de Reparto' completed.")
