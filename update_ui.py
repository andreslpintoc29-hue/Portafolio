import os

def update_ui():
    # 1. Update style.css
    with open("src/style.css", "r", encoding="utf-8") as f:
        css = f.read()
        
    css_to_add = """
/* SMALLER TYBA NODES FOR MEGA LIBRARY */
#tyba-grid {
  grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
  gap: 25px;
  max-width: 1200px;
}
.tyba-node {
  width: 110px !important;
  height: 110px !important;
  border-width: 2px !important;
}
.tyba-node .brain-label {
  font-size: 0.65rem !important;
  bottom: -30px !important;
  padding: 3px 6px !important;
  white-space: normal !important;
  text-align: center;
  width: 130%;
  line-height: 1.1;
}
.tyba-node .brain-icon {
  width: 50%;
  height: 50%;
}
"""
    if "SMALLER TYBA NODES" not in css:
        with open("src/style.css", "a", encoding="utf-8") as f:
            f.write(css_to_add)
        print("Updated style.css")
        
    # 2. Update main.js search logic
    with open("src/main.js", "r", encoding="utf-8") as f:
        js = f.read()
        
    old_search = """  if (tybaSearch) {
    tybaSearch.addEventListener('input', (e) => {
      const term = e.target.value.toLowerCase();
      tybaNodes.forEach(node => {
        const label = node.querySelector('.brain-label').innerText.toLowerCase();
        const desc = node.querySelector('.hologram-data p').innerText.toLowerCase();
        if (label.includes(term) || desc.includes(term)) {
          node.style.display = 'flex';
          gsap.to(node, { scale: 1, opacity: 1, duration: 0.3 });
        } else {
          gsap.to(node, { scale: 0.5, opacity: 0.3, duration: 0.3, onComplete: () => {
            if (term !== "") node.style.display = 'none';
          }});
        }
      });
    });
  }"""
  
    new_search = """  if (tybaSearch) {
    tybaSearch.addEventListener('input', (e) => {
      const term = e.target.value.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
      tybaNodes.forEach(node => {
        const label = node.querySelector('.brain-label').innerText.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        const desc = node.querySelector('.hologram-data p').innerText.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        if (label.includes(term) || desc.includes(term)) {
          node.style.display = 'flex';
          gsap.set(node, { scale: 1, opacity: 1 }); // Instant for performance
        } else {
          if (term !== "") {
            node.style.display = 'none';
          } else {
            node.style.display = 'flex';
            gsap.set(node, { scale: 1, opacity: 1 });
          }
        }
      });
    });
  }"""
  
    if "const label =" in js and "gsap.to(node, { scale: 0.5" in js:
        # We need a more flexible regex to replace it because formatting might differ slightly
        import re
        pattern = re.compile(r'if\s*\(tybaSearch\)\s*\{\s*tybaSearch\.addEventListener\(\'input\',\s*\(e\)\s*=>\s*\{.*?(?=\s*// Node Click Handlers)', re.DOTALL)
        
        match = pattern.search(js)
        if match:
            new_js = js[:match.start()] + new_search + "\n\n" + js[match.end():]
            with open("src/main.js", "w", encoding="utf-8") as f:
                f.write(new_js)
            print("Updated main.js search logic")
        else:
            print("Regex did not match search block in main.js")
    else:
        print("Could not find exact old search logic in main.js")

if __name__ == "__main__":
    update_ui()
