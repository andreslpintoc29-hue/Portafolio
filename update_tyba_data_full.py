import json

data = {
    "ingreso_seguridad": {
        "title": "Ingreso al Sistema y Seguridad",
        "objective": "Garantizar el acceso seguro de los servidores judiciales a la plataforma Justicia XXI Web – TYBA y la gestión de credenciales.",
        "requirements": "Contar con usuario institucional activo y acceso al correo electrónico de la Rama Judicial.",
        "steps": [
            {
                "title": "Acceso al portal oficial",
                "text": "Ingresar a través del navegador Google Chrome o Microsoft Edge al enlace de 'Inicio Aplicaciones' de la Rama Judicial.",
                "tip": "No use enlaces de buscadores externos; acceda siempre desde el portal oficial para evitar sitios de solo consulta."
            },
            {
                "title": "Autenticación",
                "text": "Digitar usuario y contraseña asignados. El sistema es sensible a mayúsculas y minúsculas.",
                "tip": "Tras 3 intentos fallidos, la cuenta se bloqueará automáticamente por seguridad."
            },
            {
                "title": "Gestión de olvido o bloqueo",
                "text": "Si la cuenta está bloqueada, usar la opción 'Recordar Contraseña / Desbloquear Usuario' para recibir un código de validación al correo.",
                "tip": "El código tiene una vigencia limitada; asegúrese de tener abierto su correo antes de solicitarlo."
            }
        ],
        "result": "El sistema permite el ingreso al escritorio virtual del despacho judicial.",
        "errors": [
            "Usuario bloqueado: Use la opción de recuperación de contraseña.",
            "Contraseña inválida: Verifique mayúsculas o espacios extra al final."
        ],
        "terms": {
            "Usuario": "Identificación única del servidor en el sistema.",
            "Bloqueo": "Estado de inactividad de la cuenta por seguridad."
        }
    },
    "registro_procesos": {
        "title": "Registro de Procesos (Reparto)",
        "objective": "Incorporar formalmente expedientes nuevos al inventario del despacho judicial tras recibir el acta de reparto.",
        "requirements": "Acta de reparto oficial y número de radicado completo (21 dígitos).",
        "steps": [
            {
                "title": "Navegación al módulo",
                "text": "Dirigirse al menú 'Administración' y seleccionar la opción 'Procesos'.",
                "tip": "Este es el panel central para el control de inventario de expedientes."
            },
            {
                "title": "Carga por Reparto",
                "text": "Ingresar a la pestaña 'Reparto', presionar 'Agregar' e introducir los 21 dígitos del radicado.",
                "tip": "No incluya puntos, guiones ni espacios; solo los caracteres numéricos."
            },
            {
                "title": "Identificación de Sujetos",
                "text": "En la pestaña 'Información Sujetos Procesales', registrar a cada interviniente con su tipo y número de documento.",
                "tip": "La identificación correcta de sujetos es crítica para las notificaciones electrónicas posteriores."
            }
        ],
        "result": "El expediente queda asignado al despacho y listo para el registro de la primera actuación.",
        "errors": [
            "Radicado no encontrado: Verifique el número contra el acta de reparto física.",
            "Sujeto ya registrado: Evite duplicar partes procesales."
        ],
        "terms": {
            "Reparto": "Asignación aleatoria de un proceso a un juzgado.",
            "Radicado": "Identidad numérica única de un proceso judicial."
        }
    },
    "registro_actuaciones": {
        "title": "Registro de Actuaciones (Memoriales y Oficios)",
        "objective": "Documentar cronológicamente cada paso procesal y adjuntar los soportes digitales al expediente.",
        "requirements": "Expediente ya registrado y documento en formato PDF.",
        "steps": [
            {
                "title": "Búsqueda del proceso",
                "text": "En 'Administración' > 'Actuaciones', buscar el radicado por sus últimos 5 dígitos.",
                "tip": "Verifique siempre el nombre de las partes para evitar errores de registro en procesos similares."
            },
            {
                "title": "Definición de la actuación",
                "text": "Presionar 'Agregar Actuación', elegir el tipo de decisión (Auto, Oficio, etc.) y asociar el sujeto procesal pertinente.",
                "tip": "Redacte una anotación clara; este texto será el que vean los abogados en el portal público."
            },
            {
                "title": "Carga de soportes",
                "text": "Subir el archivo PDF en el campo de adjuntos. Guardar para finalizar.",
                "tip": "Si el PDF es muy pesado, deberá comprimirlo antes de subirlo; TYBA tiene límites de tamaño por archivo."
            }
        ],
        "result": "La actuación aparece en el historial del proceso y es visible para el público (si no tiene reserva).",
        "errors": [
            "Archivo no permitido: Asegúrese de que sea formato PDF.",
            "Error de radicado: Anule la actuación si la registró en el proceso equivocado."
        ],
        "terms": {
            "Actuación": "Cualquier hito o documento que se suma al expediente.",
            "Anotación": "Breve resumen público de lo que trata la actuación."
        }
    },
    "notificaciones_electronicas": {
        "title": "Notificaciones Electrónicas Judiciales",
        "objective": "Comunicar las decisiones judiciales a las partes a través del buzón electrónico oficial con validez legal.",
        "requirements": "Actuación registrada previamente y correos electrónicos de los sujetos procesales actualizados.",
        "steps": [
            {
                "title": "Selección de la actuación",
                "text": "En el historial del proceso, identificar la actuación a notificar y presionar el icono del 'sobre'.",
                "tip": "Si el sobre no aparece, verifique que la actuación esté correctamente guardada y firmada."
            },
            {
                "title": "Configuración de destinatarios",
                "text": "Marcar los sujetos procesales a los que se enviará el correo. Validar las direcciones mostradas.",
                "tip": "Si falta un correo, deberá editar la información del sujeto antes de continuar."
            },
            {
                "title": "Envío y certificación",
                "text": "Completar el asunto y cuerpo del mensaje. Presionar 'Enviar'.",
                "tip": "El sistema genera automáticamente un certificado de envío; no necesita capturas de pantalla manuales."
            }
        ],
        "result": "Se envía el correo y el sistema marca la actuación como notificada.",
        "errors": [
            "Correo rebotado: Verifique la dirección en la pestaña de sujetos.",
            "Error de servidor: Intente el envío nuevamente tras unos minutos."
        ],
        "terms": {
            "Notificación": "Acto de informar legalmente una decisión.",
            "Certificado": "Prueba técnica de que el mensaje salió del sistema oficial."
        }
    },
    "tutela_digital": {
        "title": "Registro de Tutela Digital",
        "objective": "Gestionar con prioridad constitucional las acciones de tutela recibidas en el despacho.",
        "requirements": "Escrito de tutela y anexos digitalizados.",
        "steps": [
            {
                "title": "Clasificación inicial",
                "text": "Al registrar por Reparto, asegúrese de elegir 'Acción de Tutela' como tipo de proceso.",
                "tip": "Los términos de las tutelas son perentorios; el registro debe ser inmediato."
            },
            {
                "title": "Carga de la demanda",
                "text": "Registrar la primera actuación como 'Ingreso Tutela' y subir el archivo completo.",
                "tip": "Identifique claramente al Accionante y Accionado para facilitar el trámite."
            },
            {
                "title": "Auto Admisorio",
                "text": "Registrar el auto que admite la tutela y proceder a la notificación inmediata de los vinculados.",
                "tip": "Use siempre los correos institucionales de notificación judicial para entidades públicas."
            }
        ],
        "result": "El proceso de tutela queda activo y con los términos de ley corriendo en el sistema.",
        "errors": [
            "Falta de anexos: Verifique que toda la información enviada por el accionante esté cargada.",
            "Error de prioridad: No confunda el trámite de tutela con procesos ordinarios."
        ],
        "terms": {
            "Accionante": "Persona que solicita la protección de derechos.",
            "Accionado": "Entidad o persona contra quien se dirige la tutela."
        }
    },
    "firma_expediente": {
        "title": "Firma Electrónica del Expediente",
        "objective": "Validar jurídicamente las actuaciones cargadas mediante el uso de la segunda clave de seguridad.",
        "requirements": "Segunda clave configurada y permiso de firma asignado.",
        "steps": [
            {
                "title": "Uso de la segunda clave",
                "text": "Al intentar finalizar una actuación crítica, el sistema desplegará un cuadro para ingresar la clave de firma.",
                "tip": "Esta clave es personal e intransferible; equivale a su firma manuscrita."
            },
            {
                "title": "Validación del documento",
                "text": "El sistema cruza el contenido del PDF con su certificado digital para estampar la firma.",
                "tip": "Una vez firmado, el documento no puede ser alterado sin invalidar la firma."
            },
            {
                "title": "Gestión de claves",
                "text": "Si olvida la clave, use la opción 'Reiniciar Segunda Clave' en su perfil de usuario.",
                "tip": "Evite tener bloqueadores de ventanas emergentes activados en su navegador."
            }
        ],
        "result": "El documento queda con sello de autenticidad legal y plena validez judicial.",
        "errors": [
            "Clave incorrecta: Verifique que no esté usando la clave de ingreso general.",
            "Ventana no abre: Desactive bloqueadores de pop-ups."
        ],
        "terms": {
            "Segunda Clave": "Pin de seguridad exclusivo para actos administrativos y judiciales.",
            "Certificado Digital": "Identidad electrónica del servidor."
        }
    },
    "fijacion_estados": {
        "title": "Fijación de Estados Electrónicos",
        "objective": "Publicar oficialmente las decisiones del día para garantizar la publicidad de los actos judiciales.",
        "requirements": "Actuaciones del día marcadas como 'Genera Estado' y firma del Secretario.",
        "steps": [
            {
                "title": "Consolidación de datos",
                "text": "Ingresar a 'Administración' > 'Fijación de Estados'. El sistema listará los autos listos para publicar.",
                "tip": "Si un auto falta, regrese a la actuación y marque la casilla 'Generar Estado'."
            },
            {
                "title": "Generación del PDF",
                "text": "Revisar el listado generado y proceder a la firma electrónica del Secretario.",
                "tip": "Un error en el estado puede acarrear nulidades procesales; revise bien cada radicado."
            },
            {
                "title": "Publicación",
                "text": "El sistema sube el archivo automáticamente al micrositio del juzgado en la web oficial.",
                "tip": "La desfijación es automática al vencimiento del término legal."
            }
        ],
        "result": "La lista de estados es visible para abogados y ciudadanos en el portal de la Rama Judicial.",
        "errors": [
            "Auto faltante: Olvido de marcado en la creación de la actuación.",
            "Firma fallida: Error de conexión con el servidor de certificados."
        ],
        "terms": {
            "Estado": "Lista pública de providencias dictadas en un día.",
            "Desfijación": "Retiro oficial de la lista tras cumplirse el tiempo de ley."
        }
    },
    "anulacion_actuaciones": {
        "title": "Anulación de Actuaciones",
        "objective": "Corregir errores de registro o carga de documentos en el historial del expediente.",
        "requirements": "Justificación clara y que la actuación no haya surtido efectos legales irreversibles.",
        "steps": [
            {
                "title": "Identificación del error",
                "text": "Ubicar la actuación errada en el historial. Recuerde que en TYBA no se borra, se anula.",
                "tip": "La anulación deja una trazabilidad permanente por transparencia judicial."
            },
            {
                "title": "Solicitud de anulación",
                "text": "Presionar el botón 'Anular' y escribir obligatoriamente el motivo del error.",
                "tip": "Sea preciso: 'Documento cargado no corresponde al proceso' es una buena justificación."
            },
            {
                "title": "Verificación visual",
                "text": "La actuación aparecerá marcada como 'Anulada'. Proceda a registrar la correcta si es necesario.",
                "tip": "No intente 'ocultar' el error; la anulación es el procedimiento legal correcto."
            }
        ],
        "result": "La actuación queda invalidada en el historial y se permite el nuevo registro.",
        "errors": [
            "Efecto notificado: Si ya se notificó, consulte con el Juez antes de anular.",
            "Falta de justificación: El sistema rechazará campos vacíos."
        ],
        "terms": {
            "Anulación": "Acto de dejar sin efecto un registro administrativo en el sistema.",
            "Trazabilidad": "Historial de quién, cuándo y por qué se hizo un cambio."
        }
    }
}

with open('src/tybaData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Updated enriched tybaData.json")
