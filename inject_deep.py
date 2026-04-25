import re

def inject():
    with open("src/main.js", "r", encoding="utf-8") as f:
        js = f.read()
        
    with open("scratch/tyba_deep.json", "r", encoding="utf-8") as f:
        json_data = f.read()
        
    pattern_js = r'(const tybaData = )\{.*?\};(\s*// Search/Ask Logic)'
    match = re.search(pattern_js, js, re.DOTALL)
    
    if match:
        new_js = js[:match.start(1)] + "const tybaData = " + json_data + ";" + match.group(2) + js[match.end(2):]
        with open("src/main.js", "w", encoding="utf-8") as f:
            f.write(new_js)
        print("Updated src/main.js with deep extraction data.")
    else:
        print("Could not find tybaData in src/main.js")

if __name__ == "__main__":
    inject()
