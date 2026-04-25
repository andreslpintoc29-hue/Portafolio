import json
import re

def slugify(value):
    import unicodedata
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).lower()
    return re.sub(r'[-\s]+', '_', value).strip('-_')

def generate_grid():
    with open('scratch/tyba_deep.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Categories for grouping/coloring (optional, but looks nice)
    icons = {
        "documentos": "📄",
        "actuaciones": "⚖️",
        "memoriales": "📝",
        "notificaciones": "📧",
        "firma": "🖋️",
        "ingreso": "🔑",
        "reparto": "🔄",
        "tutela": "🛡️",
        "consulta": "🔍",
        "anulacion": "🚫",
        "audiencia": "🎤",
        "usuario": "👤",
        "default": "🧠"
    }

    nodes_html = ""
    for key, value in data.items():
        # Choose icon based on key
        icon = icons["default"]
        for k, v in icons.items():
            if k in key:
                icon = v
                break
        
        nodes_html += f'''
                  <div class="ai-brain-node tyba-node" data-case="{key}">
                    <div class="tyba-node-icon">{icon}</div>
                    <div class="neural-pulse"></div>
                    <span class="brain-label">{value['title']}</span>
                    <div class="hologram-data">
                      <h3>{value['title']}</h3>
                      <p>{value['desc']}</p>
                      <span class="status-online">MODULO: MANUAL OFICIAL</span>
                    </div>
                  </div>'''

    # Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the new view content
    new_view_tyba = f'''
              <div id="view-tyba" class="content-view hidden">
                <div class="tyba-search-container">
                  <span class="tyba-search-icon">🔍</span>
                  <input type="text" id="tyba-search-input" class="tyba-search-bar" placeholder="Buscar procedimiento (ej: reparto, tutela, firma)...">
                </div>
                <div class="tyba-brain-grid" id="tyba-grid">
                  {nodes_html}
                </div>
              </div>'''

    # Use regex to replace the entire <div id="view-tyba" ... </div> block
    # This is tricky because of nesting. We'll target the start and end of that specific view.
    start_tag = '<div id="view-tyba"'
    # Find the matching closing div for view-tyba
    start_idx = content.find(start_tag)
    if start_idx != -1:
        # Simple approach: find the next <!-- Modal para el Curso TYBA --> or similar
        end_marker = '<!-- Modal para el Curso TYBA -->'
        end_idx = content.find(end_marker)
        if end_idx != -1:
            # We want to keep the modal, so we replace up to end_idx
            # But wait, view-tyba ends before the modal.
            # Let's find the closing div of view-tyba.
            # In the original file, view-tyba is lines 320 to 361.
            # The modal starts at 364.
            new_content = content[:start_idx] + new_view_tyba + "\n\n              " + content[end_idx:]
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Successfully updated index.html with TYBA grid")
        else:
            print("Could not find end marker for view-tyba")
    else:
        print("Could not find view-tyba start tag")

if __name__ == "__main__":
    generate_grid()
