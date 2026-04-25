import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new view-tyba content
new_tyba_content = """<div id="view-tyba" class="content-view hidden">
                <div class="tyba-project-dashboard">
                  <div class="tyba-header">
                    <div class="tyba-header-left">
                      <span class="tyba-icon">🧠</span>
                      <div>
                        <h2 class="tyba-title">CENTRO DE APRENDIZAJE JUSTICIA XXI</h2>
                        <p class="tyba-subtitle">Módulos de entrenamiento interactivo impulsados por IA</p>
                      </div>
                    </div>
                  </div>

                  <div class="tyba-projects-grid">
                    <!-- Project 1 -->
                    <div class="tyba-project-card">
                      <div class="tyba-project-icon">🛡️</div>
                      <div class="tyba-project-info">
                        <h3>Guía paso a paso: Registro de Tutela Digital</h3>
                        <p>Aprende el procedimiento exacto para registrar y dar reparto a una Tutela en el sistema TYBA.</p>
                      </div>
                      <div class="tyba-project-actions">
                        <button class="tyba-btn tyba-btn-slides" onclick="openTybaProject('slides', '/public/slides_tutela.pdf')">
                          📄 VER DIAPOSITIVAS
                        </button>
                        <button class="tyba-btn tyba-btn-video" onclick="openTybaProject('video', '/public/video_tutela_raw.mp4')">
                          🎬 VER VIDEO
                        </button>
                      </div>
                    </div>
                    
                    <!-- Placeholder for future projects (up to 90) -->
                    <div class="tyba-project-card disabled">
                      <div class="tyba-project-icon">🔒</div>
                      <div class="tyba-project-info">
                        <h3>Módulo 2: En Construcción</h3>
                        <p>Próximamente más de 90 procedimientos interactivos.</p>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Project Viewer Overlay -->
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

# Replace everything from <div id="view-tyba"... to the closing </div> right before <!-- Modal para el Curso TYBA -->
pattern = re.compile(r'<div id="view-tyba" class="content-view hidden">.*?</div>\s*<!-- Modal para el Curso TYBA -->', re.DOTALL)

new_content = pattern.sub(new_tyba_content + '\n\n              <!-- Modal para el Curso TYBA -->', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("index.html updated successfully!")
