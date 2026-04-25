import json

def update_index_cards():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    with open('src/tybaData.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Generate HTML cards
    cards_html = ""
    for key, info in data.items():
        cards_html += f"""
                    <div class="tyba-card tyba-node" data-case="{key}">
                      <div class="tyba-card-icon">🧠</div>
                      <div class="tyba-card-content">
                        <span class="tyba-card-cat">{info['cat']}</span>
                        <h3 class="tyba-card-title">{info['title']}</h3>
                        <p class="tyba-card-desc">{info['desc']}</p>
                      </div>
                      <div class="tyba-card-action">
                        <span>LEER GUÍA</span>
                        <span class="tyba-arrow">→</span>
                      </div>
                    </div>
"""

    new_view_tyba = f"""              <div id="view-tyba" class="content-view hidden">
                <div class="tyba-search-container">
                  <input type="text" id="tyba-search-input" placeholder="Buscar función o módulo... (ej. Tutelas, Notificaciones)" class="tyba-search-bar" autocomplete="off">
                  <span class="tyba-search-icon">🔍</span>
                </div>
                <div class="tyba-dashboard" id="tyba-dashboard">
{cards_html}
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
    
    closing_tags = """
            </div>
          </section>
        </main>
      </div>

      """
    end_str = '<!-- Holographic PDF Viewer Modal -->'

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + start_str + '\n' + new_view_tyba + '\n' + closing_tags + content[end_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated index.html successfully with cards.")
    else:
        print("Could not find start or end strings in index.html")

if __name__ == '__main__':
    update_index_cards()
