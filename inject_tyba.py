import re
import json

def inject():
    # 1. Update index.html
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
        
    with open("scratch/tyba_nodes.html", "r", encoding="utf-8") as f:
        nodes_html = f.read()
        
    # Find the tyba-grid container and replace its contents
    pattern_html = r'(<div class="grid-layout" id="tyba-grid">)(.*?)(<!-- VIEW 2: PROFILE)'
    
    # We will preserve the opening tag and just insert our nodes, then close the div
    # Wait, the end of the view-tyba div is two divs down.
    # Let's use a simpler marker. The tyba-grid div is closed right before <!-- VIEW 2
    
    match = re.search(pattern_html, html, re.DOTALL)
    if match:
        new_html = html[:match.start(2)] + "\n" + nodes_html + "\n                  </div>\n                </div>\n              </div>\n\n              " + match.group(3) + html[match.end(3):]
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(new_html)
        print("Updated index.html")
    else:
        print("Could not find tyba-grid in index.html")

    # 2. Update main.js
    with open("src/main.js", "r", encoding="utf-8") as f:
        js = f.read()
        
    with open("scratch/tyba_generated.json", "r", encoding="utf-8") as f:
        json_data = f.read()
        
    pattern_js = r'(const tybaData = )\{.*?\};(\s*// Search/Ask Logic)'
    match = re.search(pattern_js, js, re.DOTALL)
    
    if match:
        new_js = js[:match.start(1)] + "const tybaData = " + json_data + ";" + match.group(2) + js[match.end(2):]
        with open("src/main.js", "w", encoding="utf-8") as f:
            f.write(new_js)
        print("Updated src/main.js")
    else:
        print("Could not find tybaData in src/main.js")

if __name__ == "__main__":
    inject()
