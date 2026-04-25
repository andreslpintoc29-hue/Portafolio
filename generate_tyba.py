import re
import json
import unicodedata

def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '_', value).strip('-_')

def extract_modules():
    with open("scratch/toc.txt", "r", encoding="utf-8") as f:
        toc_lines = f.readlines()
        
    with open("scratch/full_text.txt", "r", encoding="utf-8") as f:
        full_text = f.read()

    modules = []
    
    for line in toc_lines:
        match = re.search(r'Level \d+: (.+) \(Page (\d+)\)', line)
        if match:
            title = match.group(1).strip()
            page = int(match.group(2))
            if title.lower() in ["presentación", "glosario"]:
                continue
            modules.append({"title": title, "page": page, "id": slugify(title)})
            
    modules.append({"title": "END", "page": 9999, "id": "end"})

    tyba_data = {}
    html_nodes = ""

    for i in range(len(modules) - 1):
        mod = modules[i]
        next_mod = modules[i+1]
        
        # Start searching from the specific page to avoid hitting the TOC
        start_marker = f"--- PAGE {mod['page']} ---"
        start_idx = full_text.find(start_marker)
        if start_idx == -1:
            start_idx = 0
            
        search_area = full_text[start_idx:]
        
        escaped_title = re.escape(mod["title"])
        escaped_next = re.escape(next_mod["title"])
        
        pattern = f"{escaped_title}(.*?)(?:{escaped_next}|--- PAGE)"
        match = re.search(pattern, search_area, re.IGNORECASE | re.DOTALL)
        
        content = ""
        if match:
            content = match.group(1).strip()
            # if content is just dots, it means we might have hit a TOC-like structure on the page itself or something
            if len(content.replace('.', '').strip()) < 10:
                # fallback, just grab the next 1000 characters
                content = search_area[match.end(1):match.end(1)+1000]
        else:
            # Fallback
            content = search_area[:1500]
                
        content = re.sub(r'\n+', ' ', content)
        content = re.sub(r'\s+', ' ', content)
        content = content.replace('...', '')
        
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', content) if len(s.strip()) > 20]
        
        desc = "Procedimiento oficial según el Manual de Justicia XXI."
        if sentences:
            desc = sentences[0][:150] + "..." if len(sentences[0]) > 150 else sentences[0]
            
        steps = []
        for j, sent in enumerate(sentences[1:5]):
            # Avoid garbage steps
            if len(sent) > 10 and not sent.startswith("Ir a contenido"):
                steps.append({
                    "num": j + 1,
                    "text": sent,
                    "tip": "Revise el manual para más detalles."
                })
            
        if not steps:
            steps = [{"num": 1, "text": f"Consulte la página {mod['page']} del manual para {mod['title']}.", "tip": ""}]
            
        tyba_data[mod["id"]] = {
            "title": mod["title"].upper(),
            "desc": desc,
            "steps": steps
        }
        
        category = "MODULO OFICIAL"
        if "tutela" in mod["title"].lower(): category = "TUTELAS"
        elif "audiencia" in mod["title"].lower(): category = "AUDIENCIAS"
        elif "notificaci" in mod["title"].lower() or "estado" in mod["title"].lower(): category = "NOTIFICACIONES"
        elif "reparto" in mod["title"].lower() or "ingreso" in mod["title"].lower() or "proceso" in mod["title"].lower(): category = "GESTIÓN PROCESOS"
        
        html_nodes += f"""
                    <!-- Categoría: {category} -->
                    <div class="ai-brain-node tyba-node" data-case="{mod['id']}">
                      <img src="/ai_brain_icon.png" alt="Brain Icon" class="brain-icon" style="filter: hue-rotate(10deg) drop-shadow(0 0 15px var(--accent-cyan));">
                      <div class="neural-pulse"></div>
                      <span class="brain-label" style="font-size: 0.6rem;">{mod['title'][:25].upper()}</span>
                      <div class="hologram-data">
                        <h3>{category}</h3>
                        <p>{desc}</p>
                        <span class="status-online">PÁGINA {mod['page']}</span>
                      </div>
                    </div>\n"""

    with open("scratch/tyba_generated.json", "w", encoding="utf-8") as f:
        json.dump(tyba_data, f, indent=2, ensure_ascii=False)
        
    with open("scratch/tyba_nodes.html", "w", encoding="utf-8") as f:
        f.write(html_nodes)

if __name__ == "__main__":
    extract_modules()
