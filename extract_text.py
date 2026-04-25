import fitz

def extract_full_text():
    doc = fitz.open("ManualUsoJXXIWeb.pdf")
    text = ""
    for page_num in range(len(doc)):
        page = doc[page_num]
        text += f"\n\n--- PAGE {page_num + 1} ---\n\n"
        text += page.get_text("text")
        
    with open("scratch/full_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Full text extracted successfully to scratch/full_text.txt")

if __name__ == "__main__":
    import os
    os.makedirs("scratch", exist_ok=True)
    extract_full_text()
