import json
import re

def update_all():
    print("Updating index.html...")
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    old_html = """            <div class="gema-instructions" id="gema-modal-steps">
              <h4>¿Qué debes hacer en la Gema?</h4>
              <p>1. Simplemente pega en la caja de chat el borrador de tu investigación, un testimonio en bruto o una lista de pruebas sueltas.</p>
              <p>2. La Inteligencia Artificial estructurará automáticamente la narrativa cronológica y te indicará los códigos FPJ (Formatos de Policía Judicial) adecuados para tu informe pericial.</p>
            </div>"""
            
    new_html = """            <div id="tyba-step-list" class="tyba-step-list-container">
              <!-- Interactive Step Buttons -->
            </div>
            
            <div id="tyba-step-detail" class="tyba-step-detail-container hidden">
              <div class="detail-header">
                <button id="btn-back-steps" class="back-btn">⬅ Volver a los pasos</button>
                <h3 id="detail-step-title">Paso X</h3>
              </div>
              <div class="detail-content">
                <p id="detail-step-text">Contenido detallado del paso...</p>
                <div id="detail-step-tip" class="step-tip">💡 Tip</div>
              </div>
            </div>"""
    
    html = html.replace(old_html, new_html)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    print("Updating style.css...")
    css_to_add = """
/* INTERACTIVE STEP UI */
.tyba-step-list-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  max-height: 400px;
  overflow-y: auto;
  margin: 20px 0;
  padding-right: 10px;
}
.tyba-step-btn {
  background: rgba(0, 40, 60, 0.5);
  border: 1px solid rgba(0, 245, 255, 0.3);
  border-radius: 8px;
  padding: 15px 20px;
  display: flex;
  align-items: center;
  gap: 15px;
  cursor: pointer;
  transition: all 0.3s;
  color: white;
  text-align: left;
}
.tyba-step-btn:hover {
  background: rgba(0, 245, 255, 0.15);
  border-color: var(--accent-cyan);
  transform: translateX(5px);
}
.tyba-step-btn .step-num {
  font-family: var(--font-header);
  color: var(--accent-cyan);
  font-weight: bold;
  font-size: 1.1rem;
  min-width: 80px;
}
.tyba-step-btn .step-action {
  font-size: 1rem;
  opacity: 0.9;
}

.tyba-step-detail-container {
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(0, 245, 255, 0.2);
  border-radius: 10px;
  padding: 25px;
  margin: 20px 0;
  animation: overlayFadeIn 0.3s ease;
}
.detail-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
  border-bottom: 1px solid rgba(0, 245, 255, 0.2);
  padding-bottom: 15px;
}
.back-btn {
  background: transparent;
  border: 1px solid var(--accent-cyan);
  color: var(--accent-cyan);
  padding: 8px 15px;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s;
}
.back-btn:hover {
  background: var(--accent-cyan);
  color: black;
}
#detail-step-title {
  color: white;
  margin: 0;
  font-size: 1.4rem;
}
.detail-content {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #ddd;
}
.step-tip {
  margin-top: 20px;
  background: rgba(0, 255, 136, 0.1);
  border-left: 4px solid #00ff88;
  padding: 15px;
  color: #00ff88;
  font-style: italic;
  font-size: 0.95rem;
}
"""
    with open("src/style.css", "a", encoding="utf-8") as f:
        f.write(css_to_add)

    print("Updating tyba_deep.json manual entries...")
    with open("scratch/tyba_deep.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    # Manual rewrite for Tutela
    data["registro_de_actuaciones_para_tutelas"] = {
      "title": "REGISTRO DE ACTUACIONES (TUTELAS)",
      "desc": "Este es el procedimiento exacto interactivo para registrar una actuación de tutela en el sistema.",
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
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print("Updating main.js logic...")
    with open("src/main.js", "r", encoding="utf-8") as f:
        js = f.read()

    # We need to inject the new json data again
    pattern_js = r'(const tybaData = )\{.*?\};(\s*// Search/Ask Logic)'
    match = re.search(pattern_js, js, re.DOTALL)
    
    if match:
        new_js = js[:match.start(1)] + "const tybaData = " + json.dumps(data, ensure_ascii=False) + ";" + match.group(2) + js[match.end(2):]
    else:
        new_js = js

    # Now replace the rendering logic
    old_render = """        // Update Modal Content Dynamically
        modalTitle.innerHTML = data.title;
        modalDesc.innerHTML = data.desc;
        modalSteps.innerHTML = data.steps;"""
        
    new_render = """        // Update Modal Content Dynamically
        modalTitle.innerHTML = data.title;
        modalDesc.innerHTML = data.desc;
        
        // Render Interactive Steps
        const stepListContainer = document.getElementById('tyba-step-list');
        const stepDetailContainer = document.getElementById('tyba-step-detail');
        if (stepListContainer && stepDetailContainer) {
          stepListContainer.innerHTML = '';
          stepDetailContainer.classList.add('hidden');
          stepListContainer.classList.remove('hidden');

          if (Array.isArray(data.steps)) {
            data.steps.forEach(step => {
              const btn = document.createElement('button');
              btn.className = 'tyba-step-btn';
              
              const words = step.text.split(' ');
              let actionTitle = step.title || (words.slice(0, 8).join(' ') + "...");
              
              btn.innerHTML = `<span class="step-num">Paso ${step.num}</span><span class="step-action">${actionTitle}</span>`;
              
              btn.addEventListener('click', () => {
                stepListContainer.classList.add('hidden');
                stepDetailContainer.classList.remove('hidden');
                
                document.getElementById('detail-step-title').innerText = `Paso ${step.num}: ${step.title || 'Instrucción'}`;
                document.getElementById('detail-step-text').innerText = step.text;
                document.getElementById('detail-step-tip').innerText = `💡 ${step.tip || 'Importante'}`;
              });
              
              stepListContainer.appendChild(btn);
            });
          } else {
             stepListContainer.innerHTML = `<div class="gema-instructions">${data.steps}</div>`;
          }
        }"""
        
    if "modalSteps.innerHTML = data.steps;" in new_js:
        new_js = new_js.replace(old_render, new_render)
    else:
        print("WARNING: Could not find old render logic in main.js")
        
    # Add back button listener if not exists
    if "btn-back-steps" not in new_js:
        back_listener = """
  // Back button logic for interactive steps
  const btnBackSteps = document.getElementById('btn-back-steps');
  if (btnBackSteps) {
    btnBackSteps.addEventListener('click', () => {
      document.getElementById('tyba-step-detail').classList.add('hidden');
      document.getElementById('tyba-step-list').classList.remove('hidden');
    });
  }
"""
        new_js += back_listener
        
    with open("src/main.js", "w", encoding="utf-8") as f:
        f.write(new_js)
        
    print("Done updating all files.")

if __name__ == "__main__":
    update_all()
