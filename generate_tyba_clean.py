import json

data = {
  "ingreso_seguridad": {
    "title": "Ingreso al Sistema y Seguridad",
    "cat": "ACCESO",
    "desc": "Todo lo que necesitas saber para entrar a la plataforma TYBA (Justicia XXI Web) y qué hacer si olvidas tu contraseña o se bloquea tu cuenta.",
    "steps": [
      {
        "title": "1. Entrar por la puerta correcta",
        "text": "Siempre usa Google Chrome o Microsoft Edge. No busques 'TYBA' en Google porque podrías entrar a un enlace viejo o de consulta ciudadana. Usa el enlace oficial de 'Inicio Aplicaciones' de la Rama Judicial.",
        "tip": "Guarda el enlace oficial en tus Favoritos (la estrellita del navegador) para no tener que buscarlo nunca más."
      },
      {
        "title": "2. Iniciar Sesión",
        "text": "Escribe tu usuario y contraseña. Recuerda que la contraseña es sensible a mayúsculas y minúsculas. Si fallas 3 veces seguidas, el sistema bloqueará tu cuenta automáticamente por seguridad.",
        "tip": "Si copias y pegas tu contraseña desde un bloc de notas, asegúrate de no estar copiando un 'espacio en blanco' al final."
      },
      {
        "title": "3. Recuperar clave o desbloquear cuenta",
        "text": "Si te bloqueaste, no tienes que llamar al ingeniero de inmediato. En la ventana de inicio de sesión hay un botón que dice 'Recordar Contraseña / Desbloquear Usuario'. Dale clic, pon tu usuario y el sistema te enviará un código a tu correo institucional oficial.",
        "tip": "El código de verificación vence rápido. Abre tu correo institucional antes de solicitarlo para copiarlo de inmediato."
      }
    ]
  },
  "registro_procesos": {
    "title": "Registro de Procesos (Reparto)",
    "cat": "REGISTROS",
    "desc": "El primer paso indispensable: Cómo ingresar un proceso nuevo al despacho que llega por reparto o que debe registrarse inicialmente.",
    "steps": [
      {
        "title": "1. Entrar al menú de Procesos",
        "text": "En el menú principal de la izquierda, haz clic en 'Administración' y luego selecciona 'Procesos'. Esta es la central de mando para crear nuevos expedientes.",
        "tip": "Asegúrate de tener a la mano el número de radicado completo (21 dígitos) antes de empezar."
      },
      {
        "title": "2. Agregar un proceso por Reparto",
        "text": "Haz clic en la pestaña superior que dice 'Reparto' y luego en el botón 'Agregar'. El sistema te pedirá el número de radicación que le asignó la oficina de reparto.",
        "tip": "Al escribir los 21 dígitos, no uses guiones, puntos ni espacios. Solo los números de corrido."
      },
      {
        "title": "3. Asociar Sujetos Procesales",
        "text": "Una vez creado el proceso, es obligatorio registrar quiénes participan (Demandante, Demandado, Abogados). Ve a la pestaña 'Información Sujetos Procesales' dentro del proceso y agrégalos uno a uno con su número de cédula.",
        "tip": "Un proceso sin sujetos procesales correctamente identificados no podrá ser notificado electrónicamente de forma correcta en el futuro."
      }
    ]
  },
  "registro_actuaciones": {
    "title": "Registro de Actuaciones (Memoriales y Oficios)",
    "cat": "REGISTROS",
    "desc": "El pan de cada día en el juzgado. Cómo alimentar el expediente con cada paso legal que se da (autos, oficios, memoriales de los abogados).",
    "steps": [
      {
        "title": "1. Buscar el Expediente",
        "text": "Ve a 'Administración' > 'Actuaciones'. Escribe los últimos 5 dígitos del radicado (o el número completo) y oprime la lupa para encontrar el proceso al que le vas a agregar la actuación.",
        "tip": "Verifica muy bien los nombres de los sujetos procesales en pantalla antes de registrar la actuación, ¡para no meter un auto en el proceso equivocado!"
      },
      {
        "title": "2. Crear la Actuación",
        "text": "Haz clic en la pestaña 'Agregar Actuación'. Debes seleccionar la clase de actuación (Ej. 'Auto que admite', 'Memorial aportando pruebas') y seleccionar a qué sujeto procesal afecta o quién lo presentó.",
        "tip": "Escribe un resumen muy claro en el campo de 'Anotación'. Esto es lo que verán los abogados en la consulta pública."
      },
      {
        "title": "3. Adjuntar Archivos (El PDF)",
        "text": "En la parte de abajo de la ventana de actuación, verás un botón para examinar o subir un archivo. Ahí es donde subes el PDF firmado del auto o el memorial escaneado.",
        "tip": "Los archivos PDF no deben ser pesados. Si el PDF pesa más de lo permitido por TYBA, usa un compresor de PDF antes de subirlo."
      }
    ]
  },
  "notificaciones_electronicas": {
    "title": "Notificaciones Electrónicas Judiciales",
    "cat": "NOTIFICACIONES",
    "desc": "Cómo enviar autos y sentencias a los correos de las partes de forma legal y dejar constancia automática en el sistema.",
    "steps": [
      {
        "title": "1. Iniciar el envío",
        "text": "En la lista de actuaciones del proceso, busca la actuación que acabas de subir (por ejemplo, el Auto Admisorio). A la derecha verás un icono que parece un 'sobrecito de correo'. Haz clic ahí.",
        "tip": "Si el icono del sobre está gris o inhabilitado, significa que el proceso está oculto, archivado, o no tienes permisos."
      },
      {
        "title": "2. Seleccionar destinatarios",
        "text": "El sistema te mostrará a todos los sujetos procesales (Demandante, Demandado, etc.). Marca la casilla junto a los nombres de a quiénes quieres notificar.",
        "tip": "Si a un sujeto no le aparece el correo electrónico al lado, significa que olvidaste ponérselo cuando lo registraste. Tienes que ir a modificar el sujeto y ponerle el correo."
      },
      {
        "title": "3. Redactar y Enviar",
        "text": "Escribe el asunto (Ej: Notificación Auto Admisorio Rad. 2023-00123) y un texto corto en el cuerpo del correo. Revisa que el PDF esté adjunto y haz clic en Enviar.",
        "tip": "El sistema TYBA guardará automáticamente el certificado de que el correo salió exitosamente. No necesitas imprimir pantallazos."
      }
    ]
  },
  "firma_expediente": {
    "title": "Firma Electrónica del Expediente",
    "cat": "SEGURIDAD",
    "desc": "El proceso para validar y dar autenticidad a las actuaciones que subes al sistema con tu usuario.",
    "steps": [
      {
        "title": "1. ¿Qué es la segunda clave?",
        "text": "Además de tu contraseña para entrar a TYBA, el sistema exige una 'Segunda Clave' específica solo para firmar documentos o actuaciones críticas. Es como la clave del cajero automático.",
        "tip": "Nunca anotes esta clave en un Post-it pegado al monitor. Lo que se firme con ella tiene validez legal como si lo hubieras firmado con esfero."
      },
      {
        "title": "2. Momento de Firmar",
        "text": "Cuando el Juez o Secretario aprueba un auto y se va a registrar definitivamente en el sistema, aparecerá una ventana emergente pidiendo esta Segunda Clave de firma electrónica.",
        "tip": "Si el documento ya fue firmado electrónicamente, no podrá ser modificado ni borrado sin dejar un rastro de auditoría severo."
      },
      {
        "title": "3. Si olvidaste la clave de firma",
        "text": "Ve a la sección de tu perfil o configuración de usuario en TYBA, y busca 'Recuperar Segunda Clave'. El sistema te enviará un PIN de reinicio a tu correo electrónico institucional.",
        "tip": "Asegúrate de que tu navegador no esté bloqueando las ventanas emergentes (pop-ups), a veces el cuadro para firmar no sale por eso."
      }
    ]
  },
  "tutela_digital": {
    "title": "Registro de Tutela Digital",
    "cat": "TUTELAS",
    "desc": "Procedimiento especial, rápido y prioritario para ingresar Acciones de Tutela que llegan al despacho.",
    "steps": [
      {
        "title": "1. Módulo Especial",
        "text": "Debido a la prioridad constitucional, las Tutelas tienen su propia dinámica. Aunque entran por Reparto, debes marcar la clase de proceso como 'Tutela' o 'Acción de Tutela' desde el primer segundo.",
        "tip": "Las tutelas no esperan. Si llega a las 4:55 PM, los términos cuentan inmediatamente, ¡no el siguiente día hábil!"
      },
      {
        "title": "2. Carga del expediente inicial",
        "text": "Adjunta de inmediato el escrito de tutela y sus anexos como el primer documento (Actuación) del proceso. Asígnale el Sujeto Accionante y el Sujeto Accionado.",
        "tip": "Asegúrate de marcar los correos electrónicos de las partes como 'Prioritarios' si el sistema lo permite."
      },
      {
        "title": "3. Vinculación y Traslado",
        "text": "Al registrar el Auto Admisorio de la tutela, notifica inmediatamente por correo usando el sistema de Notificaciones de TYBA a las entidades accionadas.",
        "tip": "En tutelas contra EPS o entidades públicas, asegúrate de usar el buzón oficial de notificaciones judiciales de esa entidad, no correos genéricos."
      }
    ]
  },
  "fijacion_estados": {
    "title": "Fijación de Estados Electrónicos",
    "cat": "OFICIAL",
    "desc": "Cómo publicar la lista diaria de autos que dicta el despacho para conocimiento público de todos los abogados y ciudadanos.",
    "steps": [
      {
        "title": "1. Generación del Estado",
        "text": "Al final del día (o a primera hora de la mañana), ve al módulo de 'Administración' y busca la opción 'Fijación de Estados'. El sistema recopilará automáticamente los autos que marcaste como 'Genera Estado'.",
        "tip": "Si un auto no sale en el estado, es porque al registrar la actuación olvidaste marcarle la casilla 'Generar Estado'."
      },
      {
        "title": "2. Revisión y Firma",
        "text": "El sistema generará un documento en PDF (o tabla) con el listado de todos los radicados y autos del día. El Secretario debe firmar este estado con su firma electrónica.",
        "tip": "Revisa bien la lista antes de firmarla. Un error en un estado electrónico puede causar la nulidad de notificaciones."
      },
      {
        "title": "3. Publicación automática",
        "text": "Una vez firmado, el sistema TYBA publicará este estado automáticamente en el portal web de la Rama Judicial (sección Consulta Pública), donde cualquier ciudadano puede descargarlo.",
        "tip": "El estado se 'desfija' automáticamente al finalizar el horario laboral del día siguiente, por lo que no tienes que quitarlo a mano."
      }
    ]
  },
  "anulacion_actuaciones": {
    "title": "Anulación de Actuaciones",
    "cat": "ERRORES",
    "desc": "Qué hacer cuando te equivocas y subes un auto en el proceso incorrecto o con el documento que no era.",
    "steps": [
      {
        "title": "1. Identificar el error rápido",
        "text": "En TYBA no existe el botón 'Eliminar'. Todo lo que haces deja rastro. Si te equivocaste, debes usar la función 'Anular Actuación'.",
        "tip": "Si el auto ya fue notificado a las partes y los términos empezaron a correr, ya no puedes anularlo tan fácil; requiere una providencia del Juez decretando nulidad."
      },
      {
        "title": "2. Procedimiento de Anulación",
        "text": "Ve a la lista de actuaciones del proceso, selecciona la actuación errada y busca la opción 'Anular' o el icono de reversión. El sistema te exigirá escribir una Justificación Obligatoria.",
        "tip": "Escribe una razón clara en la justificación: Ej. 'Error involuntario de digitación, documento corresponde al proceso terminado en 0014'."
      },
      {
        "title": "3. Dejar la constancia",
        "text": "La actuación no desaparecerá por arte de magia. Quedará tachada o marcada en rojo como 'ANULADA' para que los auditores sepan qué pasó. Luego, debes subir la actuación correcta como un nuevo paso.",
        "tip": "No te asustes si la actuación sigue ahí tachada. Es la prueba legal de transparencia del juzgado."
      }
    ]
  }
}

with open('src/tybaData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Created src/tybaData.json successfully with clean data.")
