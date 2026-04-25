import json

# Load existing data
with open('src/tybaData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Ultra-specific refinement of 'Registro de procesos para Reparto'
data["registro_de_procesos_para_reparto"] = {
    "title": "REGISTRO DE PROCESOS PARA REPARTO",
    "objective": "Someter un proceso a la asignación aleatoria y equitativa entre los despachos de una especialidad bajo premisas de transparencia.",
    "requirements": "Rol de Oficina Judicial, Jefe de Oficina o Líder del Centro de Servicios.",
    "steps": [
        {
            "title": "Ruta de Ingreso",
            "text": "Diríjase al menú 'Administración', seleccione la opción 'Procesos' y haga clic en el botón 'Agregar'.",
            "tip": "Solo los usuarios con roles de administración de reparto verán esta opción."
        },
        {
            "title": "Configuración de Corporación",
            "text": "Seleccione la Corporación y la Especialidad (ej: Jueces Civiles del Circuito). Para despachos Penales, es obligatorio definir el 'Tipo Ley'.",
            "tip": "Verifique que la especialidad coincida con la naturaleza del proceso."
        },
        {
            "title": "Definición del Tipo de Proceso",
            "text": "Elija el 'Tipo de Proceso' (ej: CGP Civil Circuito). Esto habilitará la lista de 'Clase Proceso' que corresponde a los Grupos de Reparto oficiales.",
            "tip": "La Clase Proceso rige el algoritmo de aleatoriedad del sistema."
        },
        {
            "title": "Subclase y Campos Especiales",
            "text": "Seleccione la Subclase. Si es un proceso Ejecutivo, el sistema le pedirá obligatoriamente el 'Número Pagaré' y 'Valor Pagaré'.",
            "tip": "En otros procesos, puede completar opcionalmente Cuantía, Valor Pretensiones y Observaciones."
        },
        {
            "title": "Ejecución del Reparto",
            "text": "Tras asociar sujetos y archivos, confirme el registro. El sistema asignará el despacho por equidad y generará el radicado de 21 dígitos.",
            "tip": "El acta de reparto se genera automáticamente al finalizar este paso."
        }
    ],
    "result": "El proceso es asignado aleatoriamente a un despacho y se inicia el expediente digital único.",
    "errors": [
        "Especialidad incorrecta: El proceso no entrará al grupo de reparto deseado.",
        "Falta de Tipo de Ley en Penales: El botón de guardar permanecerá inhabilitado."
    ],
    "terms": {
        "Clase Proceso": "Grupos de reparto definidos en los acuerdos del Consejo Superior.",
        "Tipo Ley": "Marco jurídico aplicable (especialmente en procesos Penales).",
        "Aleatoriedad": "Principio técnico que garantiza que el reparto sea al azar."
    }
}

with open('src/tybaData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated 'Registro de procesos para Reparto' with full manual details.")
