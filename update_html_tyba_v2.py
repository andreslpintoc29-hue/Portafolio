import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new view-tyba content using the original holographic classes
new_tyba_content = """<div id="view-tyba" class="content-view hidden">
                <div class="it-dashboard">
                  <div class="it-header">
                    <div class="it-header-left">
                      <span class="it-icon">🧠</span>
                      <div>
                        <h2 class="it-title">CENTRO DE APRENDIZAJE JUSTICIA XXI</h2>
                        <p class="it-subtitle">Módulos de entrenamiento interactivo impulsados por IA (NotebookLM Bridge)</p>
                      </div>
                    </div>
                  </div>

                  <div class="grid-layout" style="margin-top: 2rem;">
                    
                    <!-- NODO 1: TUTELA DIGITAL -->
                    <div class="ai-brain-node">
                      <img src="/Portafolio/ai_brain_icon.png" alt="Brain Icon" class="brain-icon" style="filter: hue-rotate(280deg) drop-shadow(0 0 15px #d946ef);">
                      <div class="neural-pulse"></div>
                      <span class="brain-label">REGISTRO DE TUTELA</span>
                      <div class="hologram-data" style="padding-bottom: 3.5rem;">
                        <h3>MÓDULO 1: TUTELA DIGITAL</h3>
                        <p>Aprende el procedimiento exacto para registrar y dar reparto a una Tutela en el sistema TYBA.</p>
                        <span class="status-online" style="color: #d946ef;">ESTADO: GENERADO POR IA</span>
                      </div>
                      
                      <!-- Botones de Acción integrados en el nodo -->
                      <div style="position: absolute; bottom: 15px; left: 0; right: 0; display: flex; gap: 10px; justify-content: center; padding: 0 15px; z-index: 10;">
                        <button class="action-btn neon-pulse" onclick="openTybaProject('slides', 'slides_tutela.pdf')" style="font-size: 0.7rem; padding: 0.5rem; flex: 1; background: rgba(0, 240, 255, 0.1); border-color: #00f0ff; color: #00f0ff;">
                          📄 VER GUÍA
                        </button>
                        <button class="action-btn neon-pulse" onclick="openTybaProject('video', 'video_tutela_raw.mp4')" style="font-size: 0.7rem; padding: 0.5rem; flex: 1; background: rgba(217, 70, 239, 0.1); border-color: #d946ef; color: #d946ef;">
                          🎬 VER VIDEO
                        </button>
                      </div>
                    </div>

                    <!-- NODO 2: PROXIMAMENTE -->
                    <div class="ai-brain-node" style="opacity: 0.6; filter: grayscale(1);">
                      <img src="/Portafolio/ai_brain_icon.png" alt="Brain Icon" class="brain-icon">
                      <div class="neural-pulse"></div>
                      <span class="brain-label">MÓDULO 2 (PRÓXIMAMENTE)</span>
                      <div class="hologram-data">
                        <h3>90 MÓDULOS EN COLA</h3>
                        <p>Próximamente se añadirán 90 procedimientos interactivos generados por NotebookLM.</p>
                        <span class="status-offline">ESTADO: EN CONSTRUCCIÓN</span>
                      </div>
                    </div>

                  </div>
                </div>

                <!-- Project Viewer Overlay (Visor Modal) -->
                <div id="tyba-viewer-overlay" class="tyba-viewer-overlay hidden">
                  <div class="tyba-viewer-container">
                    <div class="tyba-viewer-header">
                      <span id="tyba-viewer-title">VISOR DE PROYECTO</span>
                      <button id="tyba-viewer-close" class="tyba-btn-close">✕</button>
                    </div>
                    <div class="tyba-viewer-content" id="tyba-viewer-content">
                      <!-- Video or PDF will be injected here -->
                    </div>
                  </div>
                </div>
              </div>"""

# Reemplazamos el contenedor antiguo por el nuevo
pattern = re.compile(r'<div id="view-tyba" class="content-view hidden">.*?</div>\s*<!-- Modal para el Curso TYBA -->', re.DOTALL)
new_content = pattern.sub(new_tyba_content + '\n\n              <!-- Modal para el Curso TYBA -->', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("index.html updated successfully with holographic nodes!")
