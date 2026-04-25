import re

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    with open('scratch/tyba_nodes.html', 'r', encoding='utf-8') as f:
        nodes = f.read()

    new_view_tyba = f"""              <div id="view-tyba" class="content-view hidden">
                <div class="tyba-search-container">
                  <input type="text" id="tyba-search-input" placeholder="Buscar función o módulo... (ej. Tutelas, Notificaciones)" class="tyba-search-bar" autocomplete="off">
                  <span class="tyba-search-icon">🔍</span>
                </div>
                <div class="tyba-brain-grid" id="tyba-brain-grid">
{nodes}
                </div>
              </div>

              <!-- Modal para el Curso TYBA -->
              <div id="tyba-course-modal" class="tyba-course-modal hidden">
                <div class="tyba-modal-content">
                  <button class="tyba-modal-close" id="tyba-modal-close">✕</button>
                  <div class="tyba-modal-header">
                    <div class="tyba-modal-icon">🧠</div>
                    <div class="tyba-modal-titles">
                      <span class="tyba-modal-subtitle" id="tyba-modal-subtitle">Módulo</span>
                      <h2 class="tyba-modal-title" id="tyba-modal-title">Título del Módulo</h2>
                    </div>
                  </div>
                  <div class="tyba-modal-body" id="tyba-modal-body">
                    <!-- Dynamic Steps injected here -->
                  </div>
                </div>
              </div>
"""

    start_str = '<!-- VIEW 4: APRENDE TYBA -->'
    end_str = '<!-- Holographic PDF Viewer Modal -->'

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx != -1 and end_idx != -1:
        # We need to preserve the closing tags for main and wrapper which are between view-tyba and the PDF modal
        # Actually, let's just replace from <!-- VIEW 4: APRENDE TYBA --> to <div id="pdf-modal"
        
        # Let's find where view-tyba ends by finding the closing tags before pdf-modal
        # The structure is:
        # </div> <!-- end view-tyba -->
        # </div> <!-- end right-panel -->
        # </section>
        # </main>
        # </div> <!-- end env-wrapper -->
        
        closing_tags = """
            </div>
          </section>
        </main>
      </div>

      """
        
        new_content = content[:start_idx] + start_str + '\n' + new_view_tyba + '\n' + closing_tags + content[end_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated index.html successfully")
    else:
        print("Could not find start or end strings in index.html")

if __name__ == '__main__':
    update_index()
