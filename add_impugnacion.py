import json

# Load existing data
with open('src/tybaData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add Impugnación module
data["impugnacion_tutela"] = {
    "title": "Impugnación de la Tutela",
    "objective": "Registrar formalmente la inconformidad de las partes contra el fallo de tutela y gestionar su remisión a la segunda instancia.",
    "requirements": "Fallo de tutela notificado y escrito de impugnación recibido dentro de los 3 días hábiles siguientes.",
    "steps": [
        {
            "title": "Registro del Recurso",
            "text": "Buscar el expediente y registrar la actuación 'Solicitud Impugnación'. Es obligatorio adjuntar el archivo PDF con el escrito interpuesto por el ciudadano.",
            "tip": "Verifique que el escrito haya llegado dentro del término legal (3 días después de la notificación)."
        },
        {
            "title": "Trámite del Despacho",
            "text": "Una vez recibido el escrito, el Juez debe dictar una providencia. Debe registrar la actuación 'Auto Concede / Rechaza Impugnación' según corresponda.",
            "tip": "Si se concede, la actuación debe marcarse para generar estado si así lo requiere el trámite."
        },
        {
            "title": "Remisión al Superior",
            "text": "Ingresar al módulo de remisiones y generar el registro 'Envío a Superior por Impugnación'. El sistema pedirá confirmar qué actuaciones se envían.",
            "tip": "Asegúrese de que el fallo y las notificaciones estén debidamente firmados electrónicamente antes de enviar."
        },
        {
            "title": "Verificación de Envío",
            "text": "Confirmar que el proceso cambie de estado a 'Enviado a Superior'. El sistema generará una guía de remisión automática.",
            "tip": "No es necesario enviar oficios físicos; el expediente digital viaja íntegramente por TYBA."
        }
    ],
    "result": "El expediente es remitido electrónicamente al superior jerárquico para su revisión en segunda instancia.",
    "errors": [
        "Impugnación extemporánea: El sistema permite el registro pero el Juez debe rechazarla.",
        "Falta de piezas procesales: El superior puede devolver el proceso si faltan actas o firmas."
    ],
    "terms": {
        "Impugnación": "Derecho a que una autoridad superior revise el fallo de tutela.",
        "Segunda Instancia": "Etapa de revisión por parte de un Juzgado del Circuito o Tribunal.",
        "Remisión": "Acto de transferir el control del expediente digital a otro despacho."
    }
}

with open('src/tybaData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Added Impugnación de la Tutela to tybaData.json")
