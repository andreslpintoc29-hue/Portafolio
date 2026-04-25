import fitz
import json

def extract_toc():
    doc = fitz.open("ManualUsoJXXIWeb.pdf")
    toc = doc.get_toc()
    
    if toc:
        with open("scratch/toc.txt", "w", encoding="utf-8") as f:
            for item in toc:
                f.write(f"Level {item[0]}: {item[1]} (Page {item[2]})\n")
        print("TOC extracted from metadata.")
    else:
        # If no TOC metadata, try to extract first 10 pages to look for "Contenido"
        text = ""
        for i in range(min(10, len(doc))):
            text += f"\n--- Page {i+1} ---\n"
            text += doc[i].get_text("text")
        
        with open("scratch/toc.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("No metadata TOC. Extracted text from first 10 pages.")

if __name__ == "__main__":
    import os
    os.makedirs("scratch", exist_ok=True)
    extract_toc()
