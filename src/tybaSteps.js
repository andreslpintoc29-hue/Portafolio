export const tybaModules = [
  {
    id: 1,
    title: "GUÍA PASO A PASO: CÓMO RADICAR UNA TUTELA",
    icon: "🧠",
    viewerUrl: "tutela_viewer.html",
    videoUrl: "tutela_video.html"
  },
  {
    id: 2,
    title: "REGISTRO Y REPARTO TYBA",
    icon: "🧠",
    viewerUrl: "reparto_viewer.html",
    videoUrl: "reparto_video.html"
  },
  {
    id: 3,
    title: "CREACIÓN DE PROCESOS",
    icon: "🧠",
    hasIntro: true,
    introText: "En este módulo encontrarás el paso a paso para:",
    introList: [
      {
        title: "Creación de Procesos y Registro para Reparto",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Este módulo está habilitado para roles de Oficina Judicial o Centro de Servicios.</i></span><br><br>
        • <b>Ingreso:</b> Ve al menú Administración > Procesos y haz clic en el icono (+) Agregar.<br>
        • <b>Diligenciamiento:</b> Selecciona la Corporación, Especialidad y Tipo de Ley (esto último solo para penales).<br>
        • <b>Clasificación:</b> Elige el Tipo de Proceso (ej. CGP Civil Municipal) y la Clase de Proceso (el grupo de reparto correspondiente).<br>
        • <b>Datos adicionales:</b> Completa campos opcionales como cuantía o pretensiones si es necesario.`
      },
      {
        title: "Asociar los Sujetos Procesales",
        content: `• <b>Búsqueda:</b> En la sección "Información Sujetos Procesales", haz clic en Buscar Sujeto.<br>
        • <b>Identificación:</b> Ingresa el número de cédula. Si es Cédula de Ciudadanía, usa el botón <i>Validar con Registraduría</i> para cargar los nombres automáticamente.<br>
        • <b>Vinculación:</b> Marca la casilla Asociar al Proceso, define el Tipo de Sujeto (Demandante/Demandado) y haz clic en el check azul de asociar.<br>
        • <b>Contacto:</b> En "Datos de Contacto", pulsa Agregar para registrar el correo electrónico <span style="color: #ffaa00;">(vital para notificaciones)</span> y marca la casilla <b>Predeterminado</b>.<br>
        • <b>Guardar:</b> Haz clic en el icono del disquete al final de la sección de sujetos.`
      },
      {
        title: "Adjuntar Archivos",
        content: `• <b>Carga:</b> Haz clic en la barra azul <b>Adjuntar/Descargar Archivos</b>.<br>
        • <b>Selección:</b> Elige el Tipo Archivo, busca el documento en tu equipo <span style="color: #ffaa00;">(obligatoriamente en PDF)</span> y pulsa <b>Agregar a la lista</b>.<br>
        • <b>Finalización:</b> Haz clic en Guardar después de la sección de adjuntos y confirma en Aceptar.<br>
        • <b>Acta de Reparto:</b> El sistema generará el acta. Pulsa el icono de la lupa (Consultar) para visualizarla o descargarla.<br><br>
        <span style="color: #00ffff;"><i>El acta de reparto queda disponible para consulta inmediata una vez se confirma la operación.</i></span>`
      }
    ],
    viewerUrl: "procesos_viewer.html",
    videoUrl: "procesos_video.html"
  },
  {
    id: 4,
    title: "NOTIFICACIÓN DE ACTUACIONES",
    icon: "🧠",
    viewerUrl: "notificacion_viewer.html",
    videoUrl: "notificacion_video.html"
  },
  {
    id: 5,
    title: "CREAR UNA ACTUACIÓN",
    icon: "🧠",
    viewerUrl: "actuacion_viewer.html",
    videoUrl: "actuacion_video.html"
  },
  {
    id: 6,
    title: "ANULAR REPARTO",
    icon: "🧠",
    viewerUrl: "anular_viewer.html",
    videoUrl: "anular_video.html"
  },
  {
    id: 7,
    title: "GESTIÓN ESPECIALIZADA DE ACTUACIONES Y NOVEDADES",
    icon: "🧠",
    viewerUrl: "gestion_viewer.html",
    videoUrl: "gestion_video.html"
  },
  {
    id: 8,
    title: "REGISTRO DE ACTUACIONES PARA TUTELAS",
    icon: "🧠",
    hasIntro: true,
    introText: "En este módulo encontrarás el paso a paso para:",
    introList: [
      {
        title: "Registro de Actuaciones para Tutelas",
        content: `Para realizar el Registro de Actuaciones para Tutelas en TYBA, sigue estos pasos técnicos basados en el manual:<br><br>
        • <b>Ingreso al módulo:</b> Ve al menú Administración y selecciona la opción Actuaciones.<br>
        • <b>Búsqueda del proceso:</b> Digita los 23 dígitos del radicado y haz clic en el icono de la lupa para consultar.<br>
        • <b>Gestión de actuaciones:</b> En la grilla de resultados, haz clic en el icono Consultar Registro (ojo con el check azul) para ver el historial y habilitar nuevos registros.<br>
        • <b>Nueva actuación:</b> Presiona el botón (+) Nueva Actuación.<br>
        • <b>Configuración obligatoria para Tutelas:</b><br>
        &nbsp;&nbsp;&nbsp; - <b>Ciclo:</b> Selecciona obligatoriamente el ciclo CONSTITUCIONALES.<br>
        &nbsp;&nbsp;&nbsp; - <b>Tipo Actuación:</b> Elige la que corresponda según el estado del trámite (ej. Auto Admite, Sentencia, Solicitud Impugnación).<br>
        • <b>Adjuntar documento:</b> Es de carácter obligatorio adjuntar el soporte en formato PDF o realizar la Firma Electrónica desde el aplicativo.<br>
        • <b>Finalizar:</b> Haz clic en el icono de Guardar (disquete) y confirma la operación dando clic en Aceptar.<br><br>
        <span style="color: #ffaa00; font-style: italic;">Este procedimiento es vital para que el expediente pueda ser remitido correctamente a la Corte Constitucional sin ser devuelto.</span>`
      },
      {
        title: "Admisión de la Tutela",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> Selecciona el ciclo CONSTITUCIONALES.<br>
        • <b>Tipo de Actuación:</b> Auto Admite (Rol Juez).<br><br>
        <span style="color: #ffaa00;">Es obligatorio adjuntar el PDF o firmar electrónicamente.</span>`
      },
      {
        title: "Notificación Auto Admisorio",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> Usa el ciclo CONSTITUCIONALES.<br>
        • <b>Tipo de Actuación:</b> Notificación Auto Admisorio (Rol Secretaría).<br><br>
        <span style="color: #00ffff;">Si usas la notificación electrónica del sistema, este registro no es necesario.</span>`
      },
      {
        title: "Contestación",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> Selecciona el ciclo CONSTITUCIONALES.<br>
        • <b>Tipo de Actuación:</b> Contestación.<br>
        • <b>Acción:</b> Adjuntar el memorial recibido.`
      },
      {
        title: "Sentencia",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> Elige el ciclo CONSTITUCIONALES.<br>
        • <b>Tipo de Actuación:</b> Sentencia.<br>
        • <b>Acción:</b> Ingresa los datos de la providencia (fecha ejecutoria, tipo decisión).`
      },
      {
        title: "Notificación de la Sentencia",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> Usa el ciclo CONSTITUCIONALES.<br>
        • <b>Tipo de Actuación:</b> Notificación Sentencia.<br>
        • <b>Acción:</b> Adjuntar el soporte correspondiente.`
      },
      {
        title: "Impugnación de la Tutela",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> CONSTITUCIONALES.<br>
        • <b>Tipo de Actuación:</b> Solicitud Impugnación.<br>
        • <b>Acción:</b> Registra el memorial correspondiente.`
      },
      {
        title: "Respuesta a la Impugnación",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> CONSTITUCIONALES.<br>
        • <b>Tipo de Actuación:</b> Auto Concede / Rechaza Impugnación.<br>
        • <b>Nota:</b> Esta acción la debe realizar el Juez.`
      },
      {
        title: "Remisión al Superior",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> Selecciona el ciclo SALIDAS.<br>
        • <b>Tipo de Actuación:</b> Envío a Superior por Impugnación.<br>
        • <b>Acción:</b> Elige la especialidad del superior para generar automáticamente el acta de reparto.`
      },
      {
        title: "Actuaciones de Segunda Instancia",
        content: `• <b>Acción del Superior:</b> El superior consulta el proceso.<br>
        • <b>Revisión:</b> En la pestaña <i>Actuaciones Proceso Instancia Anterior</i>, revisa los adjuntos de la primera instancia.`
      },
      {
        title: "Sentencia de Segunda Instancia",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> Usa el ciclo CONSTITUCIONALES.<br>
        • <b>Tipo de Actuación:</b> Sentencia Segunda Instancia.`
      },
      {
        title: "Notificación de la Sentencia en Segunda Instancia",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> Registra en el ciclo CONSTITUCIONALES.<br>
        • <b>Tipo de Actuación:</b> Notificación Sentencia Segunda Instancia.`
      },
      {
        title: "Remisión a la Corte Constitucional",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> Elige el ciclo SALIDAS.<br>
        • <b>Tipo de Actuación:</b> Remite a la Corte Constitucional.<br>
        • <b>Acción:</b> Adjunta el oficio remisorio.`
      },
      {
        title: "Remite a Corte para Subsanar",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Contexto:</b> Ante una devolución de la Corte.<br>
        • <b>Ciclo:</b> Usa el ciclo SALIDAS.<br>
        • <b>Tipo de Actuación:</b> Remite a la Corte Constitucional por Subsanación.`
      },
      {
        title: "Remisión para Completar Expediente",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Ciclo:</b> Registra en el ciclo SALIDAS.<br>
        • <b>Tipo de Actuación:</b> Remite a Corte para Completar Expediente.<br>
        • <b>Nota:</b> El sistema enviará todo lo nuevo o modificado.`
      },
      {
        title: "Actuaciones que registra la Corte Constitucional / Devoluciones",
        content: `• <b>Acción Automática:</b> El sistema muestra automáticamente registros generados por la Corte.<br>
        • <b>Ejemplos:</b> <i>Devolución para Subsanar</i> o <i>Exclusión de Selección</i> cuando la Corte los genera.`
      },
      {
        title: "Remite para Custodia del Proceso",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Contexto:</b> En el Juzgado de Garantías (Rol Secretaría).<br>
        • <b>Ciclo:</b> Selecciona el ciclo SALIDAS.<br>
        • <b>Tipo de Actuación:</b> REMITE PARA CUSTODIA DEL PROCESO.<br>
        • <b>Acción:</b> Esto lo asignará al juez coordinador.`
      },
      {
        title: "Envío a Penal de Conocimiento",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Para cada trámite, el flujo inicia en Administración > Actuaciones, consultando el radicado y pulsando (+) Nueva Actuación.</i></span><br><br>
        • <b>Contexto:</b> En el Centro de Servicios.<br>
        • <b>Ciclo:</b> Usa el ciclo RADICACIÓN Y REPARTO.<br>
        • <b>Tipo de Actuación:</b> Envío A Penal De Conocimiento.<br>
        • <b>Acción:</b> Selecciona la especialidad destino.`
      },
      {
        title: "Procedimiento para reingreso de procesos anulados y archivados",
        content: `• <b>Búsqueda:</b> Busca el radicado desmarcando la opción <i>"Está Vigente"</i>.<br>
        • <b>Ciclo:</b> Crea la actuación en el ciclo RADICACIÓN Y REPARTO.<br>
        • <b>Tipo de Actuación:</b> REINGRESO DEL PROCESO.<br>
        • <b>Providencia:</b> REACTIVA PROCESO.`
      }
    ],
    viewerUrl: "tutelas2_viewer.html",
    videoUrl: "tutelas2_video.html"
  },
  {
    id: 9,
    title: "PROCEDIMIENTO PARA EL REGISTRO Y GESTIÓN DE AUDIENCIAS",
    icon: "🧠",
    hasIntro: true,
    noMedia: true,
    introText: "En este módulo encontrarás el paso a paso para:",
    introList: [
      {
        title: "Creación de Procesos para Reparto",
        content: `• <b>Ruta:</b> Ingresa a Administración > Procesos.<br>
        • <b>Definición:</b> Define la Corporación, Especialidad y Tipo de Ley (ej. Ley 906 o 1826).<br>
        • <b>Selección:</b> Selecciona el Tipo de Proceso (ej. Audiencia Preliminar Inmediata) y la Clase de Proceso según corresponda.<br>
        • <b>Complemento:</b> Completa la información de sujetos procesales y adjuntos como en cualquier proceso.`
      },
      {
        title: "Registro y Gestión de Audiencias",
        content: `• <b>Audiencia Preliminar Inmediata:</b> Si seleccionas esta opción, el sistema bloquea automáticamente al despacho ("No Disponible") para nuevos repartos preliminares hasta que se finalice.<br>
        • <b>Audiencia Programada:</b> Si seleccionas esta opción, el despacho sigue disponible hasta que registres manualmente el inicio.`
      },
      {
        title: "Inicio de Audiencias",
        content: `• <b>Búsqueda:</b> Ve a Administración > Actuaciones y busca el radicado.<br>
        • <b>Nueva Actuación:</b> Haz clic en Consultar Registro y luego en (+) Nueva Actuación.<br>
        • <b>Configuración:</b><br>
        &nbsp;&nbsp;&nbsp; - <b>Ciclo:</b> AUDIENCIAS.<br>
        &nbsp;&nbsp;&nbsp; - <b>Tipo:</b> INICIO AUDIENCIA.<br>
        • <b>Datos:</b> Ingresa fecha/hora de inicio y fecha/hora estimada de fin. Haz clic en Guardar.`
      },
      {
        title: "Suspensión de Audiencias",
        content: `• <b>Configuración:</b> Crea una nueva actuación en el ciclo AUDIENCIAS con el tipo SUSPENSIÓN AUDIENCIA.<br>
        • <b>Anotación:</b> Registra el motivo en las anotaciones y haz clic en Guardar.<br><br>
        <span style="color: #00ffff;"><i>Esto habilita nuevamente al despacho para recibir repartos preliminares urgentes.</i></span>`
      },
      {
        title: "Reanudación de Audiencias",
        content: `<span style="color: #ffaa00; font-size: 0.9em;"><i>Nota: Solo se puede usar si previamente hubo una suspensión.</i></span><br><br>
        • <b>Configuración:</b> Crea la actuación en el ciclo AUDIENCIAS, tipo REANUDACIÓN AUDIENCIA.<br>
        • <b>Datos:</b> Ingresa la nueva fecha/hora de inicio y fin estimado. Haz clic en Guardar.`
      },
      {
        title: "Finalización de Audiencias",
        content: `• <b>Configuración:</b> Crea la actuación en el ciclo AUDIENCIAS, tipo FINALIZA AUDIENCIA.<br>
        • <b>Providencias:</b> En la sección Providencias, selecciona preferiblemente "Acta de Audiencia" e indica el Tipo Decisión.<br><br>
        <span style="color: #00ffff;"><i>Al guardar, el despacho queda Disponible para nuevos procesos.</i></span>`
      }
    ]
  },
  {
    id: 10,
    title: "PROCEDIMIENTO PARA EL REPARTO DE PROCESOS PENALES FUERA DE HORARIO",
    icon: "🧠",
    hasIntro: true,
    noMedia: true,
    introText: "En este módulo encontrarás el paso a paso para:",
    introList: [
      {
        title: "Creación de Turnos en Horario Adicional",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Este proceso lo realiza el Líder del Centro de Servicios para definir qué despachos atenderán las audiencias urgentes.</i></span><br><br>
        • <b>Ruta:</b> Ingresa a Configuración > Turnos Proceso Penal.<br>
        • <b>Nuevo Turno:</b> Haz clic en el icono (+) Nuevo Turno.<br>
        • <b>Datos:</b> Selecciona los datos del despacho y el juez asignado.<br>
        • <b>Tipo de Proceso:</b> El sistema solo permitirá seleccionar "Audiencia Preliminar Inmediata".<br>
        • <b>Guardar:</b> Verifica las fechas y horas del turno (el sistema las sugiere automáticamente un minuto después del cierre de la jornada) y haz clic en Guardar.`
      },
      {
        title: "Consulta y Anulación de Turnos",
        content: `• <b>Búsqueda:</b> Ve a Configuración > Turnos Proceso Penal y haz clic en el icono de la Lupa (Buscar).<br>
        • <b>Parámetros:</b> Ingresa los parámetros de búsqueda para ver los turnos activos.<br>
        • <b>Anular:</b> Para anular, haz clic en el icono de la Caneca (Eliminar).<br>
        • <b>Confirmación:</b> Escribe obligatoriamente el motivo de la anulación, guarda y confirma la operación.`
      },
      {
        title: "Creación de Procesos para Reparto (Fuera de Horario)",
        content: `• <b>Ruta:</b> Ingresa con el rol de Centro de Servicios a Administración > Procesos.<br>
        • <b>Nuevo Proceso Especial:</b> Selecciona el icono de la derecha: (+) PROCESO PENAL FUERA DE HORARIO HABITUAL.<br>
        • <b>Configuración:</b> Selecciona el Tipo de Ley (Ley 906 o 1826). El sistema mostrará en una grilla informativa los Despachos en Turno disponibles para el reparto aleatorio.<br>
        • <b>Dato vital:</b> <span style="color: #ffaa00;">Ingresa el código de 21 dígitos de la Fiscalía y agrega "00" al final para completar los 23 dígitos requeridos.</span><br>
        • <b>Finalizar:</b> Asocia sujetos procesales, adjunta los archivos y haz clic en Grabar para generar el Acta de Reparto.`
      }
    ]
  },
  {
    id: 11,
    title: "PROCEDIMIENTO PARA EL REPARTO DE HABEAS CORPUS FUERA DE HORARIO LABORAL",
    icon: "🧠",
    hasIntro: true,
    noMedia: true,
    introText: "En este módulo encontrarás el paso a paso para:",
    introList: [
      {
        title: "Creación de Turnos en Horario Adicional",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Este paso lo realiza el Líder de Centro de Servicios o de Oficina Judicial.</i></span><br><br>
        • <b>Ruta:</b> Ingresa a Configuración > Turnos Habeas Corpus.<br>
        • <b>Nuevo Turno:</b> Haz clic en el icono (+) Nuevo Turno.<br>
        • <b>Datos:</b> Selecciona el despacho y el juez asignado.<br>
        • <b>Dato técnico:</b> <span style="color: #00ffff;">Los campos Tipo de Proceso (Constitucional) y Clase de Proceso (Habeas Corpus) se cargan automáticamente y no son modificables.</span><br>
        • <b>Fecha del turno:</b> Indica la fecha del turno. El sistema fijará automáticamente las horas disponibles antes y después de la jornada laboral habitual.<br>
        • <b>Guardar:</b> Haz clic en Guardar y confirma la operación.`
      },
      {
        title: "Consulta y Anulación de Turnos",
        content: `• <b>Búsqueda:</b> Ve a Configuración > Turnos Habeas Corpus y pulsa el icono de la Lupa (Buscar).<br>
        • <b>Parámetros:</b> Ingresa los parámetros de búsqueda para visualizar los turnos.<br>
        • <b>Anular:</b> Para anular un turno erróneo, haz clic en el icono de la Caneca (Eliminar).<br>
        • <b>Confirmación:</b> Es obligatorio escribir el motivo de la anulación antes de guardar y confirmar.`
      },
      {
        title: "Creación de Procesos para Reparto",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Este registro se hace bajo la modalidad de proceso histórico.</i></span><br><br>
        • <b>Ruta:</b> Ingresa a Administración > Procesos Históricos.<br>
        • <b>Nuevo Proceso:</b> Haz clic en el icono (+) Proceso Histórico.<br>
        • <b>Punto clave:</b> <span style="color: #ffaa00;">Selecciona la casilla "Habeas Corpus Fuera Del Horario Laboral" que aparece en la parte superior derecha.</span><br>
        • <b>Filtro automático:</b> El sistema filtrará automáticamente y solo te permitirá elegir los despachos que estén configurados en turno para esa ciudad y fecha.<br>
        • <b>Finalizar:</b> Asocia los sujetos procesales, carga los archivos adjuntos y pulsa Grabar.<br>
        • <b>Acta:</b> Confirma el reparto para generar y descargar el Acta Individual de Reparto.`
      }
    ]
  },
  {
    id: 12,
    title: "REGISTRO DE USUARIOS",
    icon: "🧠",
    hasIntro: true,
    noMedia: true,
    introText: "En este módulo encontrarás el paso a paso para:",
    introList: [
      {
        title: "Pasos para el ingreso de nuevos usuarios",
        content: `Para realizar el ingreso de nuevos usuarios en TYBA, sigue estos pasos técnicos:<br><br>
        • <b>Acceso al módulo:</b> Una vez dentro del sistema, haz clic en la opción (+) USUARIOS.<br>
        • <b>Datos Básicos:</b> Diligencia la información personal del servidor judicial: Login, nombres, apellidos, tipo y número de identificación.<br>
        • <b>Ubicación Laboral:</b> Ingresa los datos del despacho judicial al cual pertenece el usuario (Departamento, Ciudad, Corporación y Especialidad).<br>
        • <b>Perfil de Usuario:</b> Selecciona el Rol y el Tipo de Usuario según su función:<br>
        &nbsp;&nbsp;&nbsp; - <b>Magistrado/Juez:</b> Se debe marcar como "Responsable del Proceso".<br>
        &nbsp;&nbsp;&nbsp; - <b>Secretario:</b> Se asigna el rol y tipo "Secretaría".<br>
        &nbsp;&nbsp;&nbsp; - <b>Otros empleados:</b> Generalmente usan el rol "Despacho" y el tipo varía según su cargo (ej. Citadores en tipo "Secretaría").<br>
        • <b>Finalización:</b> Haz clic en el icono de Guardar (disquete).<br><br>
        <span style="color: #ffaa00; font-style: italic;">Nota importante: Tras el registro, el sistema enviará automáticamente un correo electrónico al servidor con su usuario y contraseña genérica, la cual deberá ser cambiada al primer ingreso.</span>`
      }
    ]
  },
  {
    id: 13,
    title: "CREACIÓN / TRANSFORMACIÓN DE DESPACHO JUDICIAL",
    icon: "🧠",
    hasIntro: true,
    noMedia: true,
    introText: "En este módulo encontrarás el paso a paso para:",
    introList: [
      {
        title: "Creación / Transformación de Despacho Judicial",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Este proceso lo realiza el Administrador Seccional.</i></span><br><br>
        • <b>Acceso:</b> Ingresa a Configuración > Despacho y haz clic en el icono (+) DESPACHOS.<br>
        • <b>Registro:</b> Diligencia los datos básicos y el código suministrado por la UDAE.<br>
        • <b>Bloqueo Temporal:</b> Configura el horario fuera de la jornada laboral para evitar que le llegue reparto antes de terminar la configuración.<br>
        • <b>Vinculación de Juez:</b> Crea al usuario en Seguridad > Usuarios con el rol "Magistrado/Juez" y tipo "Responsable del Proceso".<br>
        • <b>Activación:</b> <span style="color: #00ffff;">Informa a Soporte TYBA para verificar cargas y nivela el horario para abrir el reparto.</span>`
      },
      {
        title: "Intercambio de Juez en un Despacho",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Se utiliza para cambiar al titular de un despacho manteniendo la carga procesal.</i></span><br><br>
        • <b>Ubicación:</b> Ve a Seguridad > Usuarios y consulta al juez que será reemplazado.<br>
        • <b>Liberación:</b> <span style="color: #ffaa00;">Si el nuevo juez ya está en otro despacho, primero debes "liberarlo" usando un usuario comodín o trasladándolo de unidad.</span><br>
        • <b>Ejecución:</b> En el registro del juez actual, haz clic en el icono de Intercambio Juez (dos flechas azules).<br>
        • <b>Asignación:</b> En el campo "Reemplazar por", selecciona al nuevo titular de la lista y guarda.<br><br>
        <span style="color: #00ffff;"><i>El sistema traspasa automáticamente la carga procesal.</i></span>`
      },
      {
        title: "Traslado Masivo de Procesos",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Nota: Este trámite no se hace directamente en la interfaz, sino mediante solicitud técnica.</i></span><br><br>
        • <b>Requisito:</b> Tener el documento oficial (Acuerdo o Resolución) que autoriza la redistribución.<br>
        • <b>Documentación:</b> Diligencia el Excel <i>"Formato para traslado masivo de procesos.xlsx"</i> indicando despacho origen, destino y los 23 dígitos de cada radicado.<br>
        • <b>Envío:</b> Remite la solicitud y el Excel al correo:<br>
        &nbsp;&nbsp;&nbsp;<span style="color: #00ffff;">soporte_ri_tyba@deaj.ramajudicial.gov.co</span><br>
        • <b>Finalización:</b> Soporte confirmará por correo cuando los procesos hayan sido trasladados y las cargas niveladas.`
      }
    ]
  },
  {
    id: 14,
    title: "PROCEDIMIENTO PARA EL REGISTRO NACIONAL DE PERSONAS EMPLAZADAS",
    icon: "🧠",
    hasIntro: true,
    noMedia: true,
    introText: "En este módulo encontrarás el paso a paso para:",
    introList: [
      {
        title: "Identificación de los sujetos a emplazar",
        content: `• <b>Acceso:</b> Ingresa a Administración > Procesos y consulta el radicado.<br>
        &nbsp;&nbsp;&nbsp;<span style="color: #ffaa00;">Si no existe en el sistema, debes crearlo primero como "Proceso Histórico".</span><br>
        • <b>Modificación:</b> Haz clic en el icono del lápiz (editar) para habilitar los cambios en el proceso.<br>
        • <b>Marcación:</b> En la sección "Información del Sujeto", ubica a la persona y marca la casilla de la columna <b>Emplazado</b>.<br>
        • <b>Finalización:</b> Guarda los cambios para que el sistema reconozca al sujeto como parte del registro nacional.`
      },
      {
        title: "Registro de Actuaciones (Rol Secretaría)",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Una vez el interesado aporte las pruebas del emplazamiento, sigue esta ruta:</i></span><br><br>
        • <b>Nueva Actuación:</b> Ve a Administración > Actuaciones, busca el proceso y pulsa el botón (+) Nueva Actuación.<br>
        • <b>Configuración:</b><br>
        &nbsp;&nbsp;&nbsp; - <b>Ciclo:</b> Selecciona GENERALES.<br>
        &nbsp;&nbsp;&nbsp; - <b>Tipo Actuación:</b> Elige <i>Auto Emplaza</i> (para personas) o <i>Emplaza Pertenencia</i> (para bienes inmuebles).<br>
        • <b>Soportes:</b> Adjunta las pruebas documentales en formato PDF, haz clic en el icono de clip (agregar a la lista) y luego en Guardar.<br><br>
        <span style="color: #00ffff;"><i>Este procedimiento garantiza que la información sea pública y pueda ser consultada por cualquier ciudadano en el portal de la Rama Judicial.</i></span>`
      }
    ]
  },
  {
    id: 15,
    title: "CONSULTAS PÚBLICAS",
    icon: "🧠",
    hasIntro: true,
    noMedia: true,
    introText: "En este módulo encontrarás el acceso a las consultas públicas del sistema:",
    introList: [
      {
        title: "Consulta Pública de Procesos Judiciales",
        content: `• <b>Descripción:</b> Permite a los ciudadanos consultar procesos y sus soportes anexos.<br><br>
        • <b>Enlace de acceso:</b><br>
        &nbsp;&nbsp;&nbsp;<a href="http://procesojudicial.ramajudicial.gov.co/Justicia21/Administracion/Ciudadanos/frmConsulta" target="_blank" style="color: #00ffff; text-decoration: underline; word-break: break-all;">http://procesojudicial.ramajudicial.gov.co/Justicia21/Administracion/Ciudadanos/frmConsulta</a><br><br>
        <span style="color: #ffaa00;"><i>Dato clave: Para que un proceso aparezca en esta consulta, el usuario con rol de Secretaría debe configurarlo previamente como Público.</i></span>`
      },
      {
        title: "Consulta de Fijaciones de Estado",
        content: `• <b>Descripción:</b> Se utiliza para visualizar los estados electrónicos emitidos por los despachos.<br><br>
        • <b>Enlace de acceso:</b><br>
        &nbsp;&nbsp;&nbsp;<a href="http://procesojudicial.ramajudicial.gov.co/Justicia21/Administracion/Descargas/frmArchivosEstados" target="_blank" style="color: #00ffff; text-decoration: underline; word-break: break-all;">http://procesojudicial.ramajudicial.gov.co/Justicia21/Administracion/Descargas/frmArchivosEstados</a>`
      },
      {
        title: "Validación de Documentos / Archivos",
        content: `• <b>Descripción:</b> Permite validar como originales los documentos emitidos por el poder judicial.<br><br>
        • <b>Enlace de acceso:</b><br>
        &nbsp;&nbsp;&nbsp;<a href="http://procesojudicial.ramajudicial.gov.co/Justicia21/Administracion/Descargas/frmValidarArchivos" target="_blank" style="color: #00ffff; text-decoration: underline; word-break: break-all;">http://procesojudicial.ramajudicial.gov.co/Justicia21/Administracion/Descargas/frmValidarArchivos</a>`
      },
      {
        title: "Descarga Archivos de Notificaciones",
        content: `• <b>Descripción:</b> Sirve para bajar los documentos remitidos mediante enlaces en las notificaciones electrónicas.<br><br>
        • <b>Enlace de acceso:</b><br>
        &nbsp;&nbsp;&nbsp;<a href="http://procesojudicial.ramajudicial.gov.co/Justicia21/Administracion/Descargas/frmDescargaArchivosAdjuntosNotificacion" target="_blank" style="color: #00ffff; text-decoration: underline; word-break: break-all;">http://procesojudicial.ramajudicial.gov.co/Justicia21/Administracion/Descargas/frmDescargaArchivosAdjuntosNotificacion</a>`
      },
      {
        title: "Consulta Pública de Emplazamiento",
        content: `• <b>Paso 1:</b> Ingresa a:<br>
        &nbsp;&nbsp;&nbsp;<a href="http://procesojudicial.ramajudicial.gov.co/Justicia21/" target="_blank" style="color: #00ffff; text-decoration: underline;">http://procesojudicial.ramajudicial.gov.co/Justicia21/</a><br>
        • <b>Paso 2:</b> Haz clic en la opción <b>Ingreso</b> del menú <b>Emplazados</b>.<br>
        • <b>Paso 3:</b> Selecciona el icono <i>Consulta Rama Judicial de Registros Nacionales</i>.<br>
        • <b>Paso 4:</b> Ingresa los criterios de búsqueda (número de identificación o despacho específico), marca la casilla de Captcha y pulsa <b>Consultar</b>.<br>
        • <b>Paso 5:</b> Si el proceso es público, haz clic en el icono de la lupa para ver los detalles y luego en <b>Descargar</b> para visualizar el soporte.<br><br>
        <span style="color: #ffaa00;"><i>Dato clave: Para que un proceso aparezca aquí, el usuario con rol de Secretaría debe configurarlo previamente como Público.</i></span>`
      }
    ]
  },
  {
    id: 16,
    title: "CASOS DE USO REGISTRO DE ACTUACIONES",
    icon: "🧠",
    hasIntro: true,
    noMedia: true,
    introText: "En este módulo encontrarás el paso a paso para:",
    introList: [
      {
        title: "Anulación de Repartos",
        content: `<span style="color: #ffaa00; font-size: 0.9em;"><i>Solo permitida para el Jefe de Oficina Judicial por errores o causas justificadas.</i></span><br><br>
        • <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Anula Reparto Oficina Judicial.<br>
        • <b>Datos requeridos:</b> Ingresa las fechas de actuación y anulación, la descripción y adjunta el soporte en PDF.`
      },
      {
        title: "Adjudicación por conocimiento previo Tribunal",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Cuando un Tribunal ordena la adjudicación directa.</i></span><br><br>
        • <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Novedad Adjudicación por Conocimiento Previo Tribunal.<br>
        • <b>Acción:</b> Selecciona el juez correspondiente y adjunta el PDF.`
      },
      {
        title: "Asignación por reparto a otro despacho de la misma Especialidad",
        content: `• <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Novedad por Cambio de Ponente.<br>
        • <b>Acción:</b> Incluye la anotación y el soporte documental.`
      },
      {
        title: "Asignación o traslado de proceso a un despacho específico de la misma especialidad",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Se usa por pérdida de competencia (Art. 121 CGP) o traslados previos del Tribunal.</i></span><br><br>
        • <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Novedad por Cambio de Ponente Directo.<br>
        • <b>Acción:</b> Selecciona al juez destino y adjunta el archivo.`
      },
      {
        title: "Envío de procesos al Superior – Segunda Instancia",
        content: `• <b>Contexto:</b> Para efectos devolutivos.<br>
        • <b>Ciclo:</b> Salidas.<br>
        • <b>Actuación:</b> Envío al Superior por Interpuestos Sin Finalización.<br><br>
        <span style="color: #00ffff;"><i>Esto genera automáticamente el reparto en la instancia superior.</i></span>`
      },
      {
        title: "Anulación de Actuaciones",
        content: `<span style="color: #ffaa00; font-size: 0.9em;"><i>Solo el usuario que registró la actuación puede anularla (excepto la sentencia, que solo la anula el Juez).</i></span><br><br>
        • <b>Acción:</b> Haz clic en el icono de la caneca al lado de la actuación.<br>
        • <b>Restricción:</b> <span style="color: #ffaa00;">Solo se puede anular la última actuación registrada.</span>`
      },
      {
        title: "Actuaciones que Modifican el Reparto",
        content: `• <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Tipos:</b> Incluyen novedades por impedimento, competencia o acumulación.<br><br>
        <span style="color: #00ffff;"><i>Estas actuaciones afectan directamente las cargas procesales del despacho.</i></span>`
      },
      {
        title: "Actuaciones que generan Estado",
        content: `• <b>Cuándo:</b> Al registrar Autos o Sentencias.<br>
        • <b>Acción:</b> En la sección de Providencias, selecciona las opciones de <b>Estado 0 días en Secretaría</b>.<br><br>
        <span style="color: #00ffff;"><i>Al guardar, el sistema crea automáticamente el registro "Fijación Estado".</i></span>`
      },
      {
        title: "Notificación de Actuaciones",
        content: `• <b>Ubicación:</b> Ubica la actuación registrada y haz clic en el icono del sobre (notificar).<br>
        • <b>Selección:</b> Selecciona los sujetos con correo electrónico y marca los archivos a enviar.<br>
        • <b>Finalizar:</b> Haz clic en Guardar.`
      },
      {
        title: "Consulta de la Notificación enviada / Datos de la Notificación Electrónica",
        content: `• <b>Acción:</b> Haz clic en el icono de la lupa (consultar) de la actuación.<br>
        • <b>Información disponible:</b> Destinatarios, fecha de entrega y descarga del soporte de envío.<br><br>
        <span style="color: #00ffff;"><i>El sistema genera un certificado de integridad para cada documento remitido.</i></span>`
      }
    ]
  },
  {
    id: 17,
    title: "ACTUACIONES DE SECRETARÍA, ANULACIONES Y NOVEDADES DE REPARTO",
    icon: "🧠",
    hasIntro: true,
    noMedia: true,
    introText: "En este módulo encontrarás el paso a paso para:",
    introList: [
      {
        title: "Anulación por Permiso del Juez",
        content: `• <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Novedad Devuelve Por Permiso del Juez / Sin Juez.<br>
        • <b>Datos requeridos:</b> Ingresa fechas de actuación y anulación, motivo y adjunta el PDF de soporte.`
      },
      {
        title: "Anulación porque no es un proceso",
        content: `• <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Novedad Error en Reparto No Es Proceso.<br>
        • <b>Datos requeridos:</b> Ingresa descripción, fecha de anulación y adjunta soporte PDF.`
      },
      {
        title: "Asignación a otro despacho (Misma Especialidad)",
        content: `• <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Novedad por Cambio de Ponente.<br>
        • <b>Acción:</b> Adjunta el soporte.<br><br>
        <span style="color: #00ffff;"><i>El sistema genera un acta de reparto aleatoria entre los demás despachos.</i></span>`
      },
      {
        title: "Asignación a despacho específico",
        content: `<span style="color: #aaa; font-size: 0.9em;"><i>Usado por pérdida de competencia o conocimiento previo.</i></span><br><br>
        • <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Novedad por Cambio de Ponente Directo.<br>
        • <b>Acción:</b> Selecciona el Juez destino y adjunta el PDF.`
      },
      {
        title: "Cambio de Clase de Proceso",
        content: `• <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Novedad por Cambio de Clasificación.<br>
        • <b>Acción:</b> Selecciona el nuevo Tipo, Clase y Subclase de proceso.`
      },
      {
        title: "Cambio de Competencia",
        content: `• <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Novedad por Competencia.<br><br>
        <span style="color: #ffaa00;"><i>El proceso queda "Sin Vigencia". Debes avisar por correo a la Oficina Judicial para el nuevo reparto.</i></span>`
      },
      {
        title: "Declaración de Impedimento",
        content: `• <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Novedad por Impedimento / Recusación.<br><br>
        <span style="color: #00ffff;"><i>Al guardar, el proceso finaliza instancia y se genera automáticamente un nuevo radicado en el siguiente juzgado.</i></span>`
      },
      {
        title: "Acumulación de Procesos",
        content: `• <b>Ciclo:</b> Radicación y Reparto.<br>
        • <b>Actuación:</b> Novedad por Acumulación.<br>
        • <b>Acción:</b> Digita y valida el código del proceso donde se acumulará.<br><br>
        <span style="color: #00ffff;"><i>El sistema finaliza el radicado actual y crea un enlace en el proceso destino.</i></span>`
      },
      {
        title: "Envío al Superior – Efecto Devolutivo",
        content: `• <b>Ciclo:</b> Salidas.<br>
        • <b>Actuación:</b> Envío a Superior por Interpuestos Sin Finalización.<br>
        • <b>Acción:</b> Selecciona el Superior y el Tipo de Acción.<br><br>
        <span style="color: #00ffff;"><i>El proceso se mantiene vigente en el origen.</i></span>`
      },
      {
        title: "Envío al Superior – Efecto Suspensivo",
        content: `• <b>Ciclo:</b> Salidas.<br>
        • <b>Actuación:</b> Envío Expediente al Superior por Interpuestos.`
      },
      {
        title: "Si el Superior no usa TYBA",
        content: `• <b>Ciclo:</b> Salidas.<br>
        • <b>Actuación:</b> Envío a Reparto por Interpuestos (Superior sin JXXI Web).`
      },
      {
        title: "No aceptación de impedimento",
        content: `• <b>Ciclo:</b> Salidas.<br>
        • <b>Actuación:</b> Auto No Acepta Impedimento / Recusación.<br><br>
        <span style="color: #00ffff;"><i>Esto deja sin vigencia el proceso en el despacho actual y reactiva el original.</i></span>`
      },
      {
        title: "Salida Finalizando Instancia",
        content: `• <b>Ciclo:</b> Salidas.<br>
        • <b>Actuación:</b> Salida Finalizando Instancia.`
      },
      {
        title: "Actuaciones de ámbito General",
        content: `• <b>Ciclo:</b> Generales.<br>
        • <b>Ejemplos:</b> Agregar Memorial, Constancia, entre otras.<br>
        • <b>Acción:</b> Selecciona la actuación, anota la observación y adjunta PDF.`
      },
      {
        title: "Preparación para Firma",
        content: `• <b>Ciclo:</b> Generales.<br>
        • <b>Actuación:</b> Documento para Firma.<br>
        • <b>Formato:</b> <span style="color: #ffaa00;">Adjunta el archivo obligatoriamente en formato .doc o .docx</span>`
      },
      {
        title: "Firma del Documento",
        content: `• <b>Ruta:</b> Administración > Actuaciones > busca el proceso.<br>
        • <b>Paso 1:</b> Haz clic en <b>Modificar</b> sobre la actuación "Documento para Firma".<br>
        • <b>Paso 2:</b> Pulsa <b>Aplica para firma</b>.<br>
        • <b>Paso 3:</b> Selecciona la actuación definitiva (ej. Auto Admite).<br>
        • <b>Paso 4:</b> Haz clic en <b>Confirmar Firma</b>.`
      },
      {
        title: "Fijación de Estados",
        content: `• <b>Paso 1:</b> Al registrar una actuación, selecciona en Providencias: <i>Auto Interlocutorio/Sustanciación (Estado 0 días Secretaría)</i>.<br>
        • <b>Paso 2:</b> Ve al menú <b>Administración > Fijación Estados</b>.<br>
        • <b>Paso 3:</b> Verifica la lista y haz clic en el botón <b>Pin</b> para publicar el documento oficial.<br><br>
        <span style="color: #00ffff;"><i>El estado queda publicado y disponible para consulta pública en el portal.</i></span>`
      }
    ]
  }
];
