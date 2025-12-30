import os
import re
import json

def extract_content(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract Title - simple regex
    title_match = re.search(r'<title>(.*?) \|', html)
    title = title_match.group(1).strip() if title_match else ""
    
    # Extract H1 inside content-body
    # First find content-body block
    content_body_match = re.search(r'<div class="content-body">(.*?)</div>', html, re.DOTALL)
    if not content_body_match:
        # Try without the class if it's different
        return None
    
    content_body = content_body_match.group(1)
    
    # Extract H1
    h1_match = re.search(r'<h1>(.*?)</h1>', content_body)
    h1_text = h1_match.group(1).strip() if h1_match else ""
    
    # Remove H1 from body for easier translation handling
    body_content = re.sub(r'<h1>.*?</h1>', '', content_body, count=1).strip()
    
    # Remove image-container-footer
    body_content = re.sub(r'<div class="image-container-footer">.*?</div>', '', body_content, flags=re.DOTALL).strip()
    
    return {
        "title": title,
        "h1": h1_text,
        "body": body_content
    }

files = [
    "02_capitulo.html", "03_capitulo.html", "04_capitulo.html", "05_capitulo.html",
    "06_capitulo.html", "07_capitulo.html", "08_capitulo.html", "09_capitulo.html",
    "10_capitulo.html", "11_capitulo.html", "12_epilogo.html", "13_apendice_poema.html"
]

results = {}
for f in files:
    path = os.path.join("output/html", f)
    if os.path.exists(path):
        data = extract_content(path)
        if data:
            results[f] = data

with open('spanish_content.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Extraction complete. Results saved in spanish_content.json")
