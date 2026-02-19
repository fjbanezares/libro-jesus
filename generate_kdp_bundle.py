import json
import os
import re

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSLATIONS_FILE = os.path.join(BASE_DIR, 'translations.json')
ENLACES_FILE = os.path.join(BASE_DIR, 'enlaces.json')
TEMPLATE_KDP = os.path.join(BASE_DIR, 'templates', 'template_kdp.tex')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output', 'latex')
CONTENT_DIR = os.path.join(BASE_DIR, 'content')

def ensure_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def clean_html_for_latex(text, is_poem=False):
    # Escape early
    text = text.replace('&', '\\&').replace('$', '\\$').replace('%', '\\%').replace('#', '\\#').replace('_', '\\_')
    
    if is_poem:
        # Split by <p> or <br><br> to identify stanzas
        # First normalize the input: remove headers if present in body
        text = re.sub(r'<h2>.*?</h2>', '', text)
        text = re.sub(r'<strong>.*?</strong>', '', text, count=1) # Remove the title if it's there
        
        # Convert <br> to newlines
        text = re.sub(r'<br\s*/?>', '\n', text)
        # Split by stanzas (usually <p>)
        stanzas = re.split(r'</?p>', text)
        processed_stanzas = []
        for stanza in stanzas:
            lines = stanza.strip().split('\n')
            processed_lines = [l.strip() for l in lines if l.strip()]
            if processed_lines:
                processed_stanzas.append(' \\\\\n'.join(processed_lines))
        return '\n\n\\bigskip\\bigskip\n\n'.join(processed_stanzas)
    else:
        # Standard cleaning
        text = re.sub(r'<br\s*/?>\s*\n?', r'\\\\\n', text)
        text = re.sub(r'<strong>(.*?)</strong>', r'\\textbf{\1}', text)
        text = re.sub(r'<b>(.*?)</b>', r'\\textbf{\1}', text)
        text = re.sub(r'<em>(.*?)</em>', r'\\textit{\1}', text)
        text = re.sub(r'<i>(.*?)</i>', r'\\textit{\1}', text)
        text = text.replace('</p>', '\n\n')
        text = text.replace('<p>', '')
        lines = [line.strip() for line in text.split('\n')]
        text = '\n'.join(lines)
        text = re.sub(r'<[^>]+>', '', text)
        return text.strip()

def md_to_latex(md_content, is_poem=False):
    # Standardize
    md_content = md_content.replace('\r\n', '\n')
    # Escape
    md_content = md_content.replace('&', '\\&').replace('$', '\\$').replace('%', '\\%').replace('#', '\\#').replace('_', '\\_')

    if is_poem:
        # Split into stanzas
        stanzas = re.split(r'\n\s*\n', md_content)
        processed_stanzas = []
        for stanza in stanzas:
            # Clean boldness or headers that might be in the poem content
            stanza = re.sub(r'^\s*#+.*', '', stanza, flags=re.MULTILINE)
            lines = stanza.strip().split('\n')
            processed_lines = []
            for line in lines:
                # Remove Markdown bold/italic but keep the text
                line = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', line)
                line = re.sub(r'\*(.*?)\*', r'\\textit{\1}', line)
                line = line.replace('  ', '').strip()
                if line:
                    processed_lines.append(line)
            if processed_lines:
                processed_stanzas.append(' \\\\\n'.join(processed_lines))
        return '\n\n\\bigskip\\bigskip\n\n'.join(processed_stanzas)
    else:
        # Standard Markdown
        md_content = re.sub(r'  \n', r'\\\\\n', md_content)
        md_content = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', md_content)
        md_content = re.sub(r'\*(.*?)\*', r'\\textit{\1}', md_content)
        md_content = re.sub(r'^## (.*)', r'\\section*{\1}', md_content, flags=re.MULTILINE)
        md_content = re.sub(r'^# (.*)', '', md_content, flags=re.MULTILINE)
        lines = [line.lstrip() for line in md_content.split('\n')]
        return '\n'.join(lines).strip()

def get_image_for_chapter(chapter_num):
    mapping = {
        0: 'intro_quantum_luther.png',
        1: 'madrid.png',
        2: 'las_rozas_park.png',
        3: 'silence_vibration.png',
        4: 'nature.png',
        5: 'cosmic_father.png',
        6: 'heaven_state.png',
        7: 'bread_sparrows.png',
        8: 'forgiveness_chains.png',
        9: 'fog_light.png',
        10: 'eagle_protection.png',
        11: 'kingdom_power.png',
        12: 'sunset_road.png',
        13: 'christmas_star_modern.png'
    }
    return mapping.get(chapter_num, 'vibration.png')

def generate_kdp_book(lang_code):
    translations = read_json(TRANSLATIONS_FILE)
    links = read_json(ENLACES_FILE)
    template = read_file(TEMPLATE_KDP)
    
    lang_babel = 'spanish' if lang_code == 'es' else 'english'
    book_title = "Mi amigo Jesucristo" if lang_code == 'es' else "My Friend Jesus Christ"
    subtitle = "Una guía cuántica para el alma moderna" if lang_code == 'es' else "A Quantum Guide for the Modern Soul"
    author = "A Glimpse of Light"
    
    chapter_map = [
        {"trans": "00_introduccion.html", "md": "00_introduccion.md"},
        {"trans": "index.html", "md": "01_capitulo.md"},
        {"trans": "02_capitulo.html", "md": "02_capitulo.md"},
        {"trans": "03_capitulo.html", "md": "03_capitulo.md"},
        {"trans": "04_capitulo.html", "md": "04_capitulo.md"},
        {"trans": "05_capitulo.html", "md": "05_capitulo.md"},
        {"trans": "06_capitulo.html", "md": "06_capitulo.md"},
        {"trans": "07_capitulo.html", "md": "07_capitulo.md"},
        {"trans": "08_capitulo.html", "md": "08_capitulo.md"},
        {"trans": "09_capitulo.html", "md": "09_capitulo.md"},
        {"trans": "10_capitulo.html", "md": "10_capitulo.md"},
        {"trans": "11_capitulo.html", "md": "11_capitulo.md"},
        {"trans": "12_epilogo.html", "md": "12_epilogo.md"},
        {"trans": "13_apendice_poema.html", "md": "13_apendice_poema.md"}
    ]
    
    full_content = ""
    
    for i, item in enumerate(chapter_map):
        trans_key = item["trans"]
        md_file = item["md"]
        chapter_data = translations.get(trans_key, {})
        h1 = chapter_data.get('h1', {}).get(lang_code, "")
        
        body_latex = ""
        if lang_code == 'es':
            md_path = os.path.join(CONTENT_DIR, md_file)
            if os.path.exists(md_path):
                raw_md = read_file(md_path)
                if not h1:
                    match = re.match(r'^# (.*)', raw_md)
                    if match: h1 = match.group(1)
                body_latex = md_to_latex(raw_md, is_poem=(i == 13))
            else:
                continue
        else:
            body_html = chapter_data.get('body', {}).get(lang_code, "")
            if not body_html: continue
            body_latex = clean_html_for_latex(body_html, is_poem=(i == 13))

        if not h1: h1 = f"Chapter {i}"
            
        if i == 0 or i == 13: # Introduction or Appendix
            full_content += f"\\chapter*{{{h1}}}\n\\addcontentsline{{toc}}{{chapter}}{{{h1}}}\n\\markboth{{{h1}}}{{{h1}}}\n"
        else:
            title_text = re.sub(r'^(Capítulo|Chapter|제\d+장)\s+\d*[:\.]?\s*', '', h1, flags=re.IGNORECASE)
            full_content += f"\\chapter{{{title_text}}}\n"
            
        full_content += "\\vspace{1.5cm}\n"
        
        img_name = get_image_for_chapter(i)
        full_content += f"\\begin{{figure}}[h!]\n\\centering\n\\includegraphics[width=0.85\\textwidth,cfbox=gray 0.5pt 3pt]{{{img_name}}}\n\\end{{figure}}\n\n"
        
        full_content += "\\vspace{1cm}\n"
        
        if i == 13:
            # Verse environment alone allows page breaks. Removed minipage and mdframed.
            full_content += "\\begin{verse}\n" + body_latex + "\n\\end{verse}"
        else:
            full_content += body_latex
        
        if i == 13:
            spotify_data = links.get('spotify', {}).get(lang_code, {})
            album_id = spotify_data.get('album_id')
            spotify_url = f"https://open.spotify.com/album/{album_id}" if album_id else "https://open.spotify.com/artist/3P9x9Y0y0I3p6e5g9mG4Xk"
            
            if lang_code == 'es':
                invitation_intro = "Para completar esta experiencia vibracional, te invito a seguir los enlaces y sumergirte en la música del libro."
                label_spotify = "Escuchar en Spotify"
                label_web = "pazaresosset.es"
            else:
                invitation_intro = "To complete this vibrational experience, I invite you to follow the links and immerse yourself in the book's music."
                label_spotify = "Listen on Spotify"
                label_web = "pazaresosset.es"
            
            full_content += f"\n\n\\vspace{{3cm}}\n\\begin{{center}}\n"
            full_content += f"\\textit{{{invitation_intro}}}\\\\\n"
            full_content += f"\\vspace{{2cm}}\n"
            full_content += f"\\begin{{minipage}}{{0.45\\textwidth}}\n\\centering\n"
            full_content += f"\\qrcode[height=3.8cm]{{{spotify_url}}}\\\\\n"
            full_content += f"\\vspace{{0.5cm}}\\textbf{{{label_spotify}}}\n"
            full_content += f"\\end{{minipage}}\\hfill\n"
            full_content += f"\\begin{{minipage}}{{0.45\\textwidth}}\n\\centering\n"
            full_content += f"\\qrcode[height=3.8cm]{{https://pazaresosset.es}}\\\\\n"
            full_content += f"\\vspace{{0.5cm}}\\textbf{{{label_web}}}\n"
            full_content += f"\\end{{minipage}}\n"
            full_content += f"\\end{{center}}"
            
        full_content += "\n\\newpage\n"

    output = template
    output = output.replace('{{LANG}}', lang_babel)
    output = output.replace('{{BOOK_TITLE}}', book_title)
    output = output.replace('{{SUBTITLE}}', subtitle)
    output = output.replace('{{AUTHOR}}', author)
    output = output.replace('{{CONTENT}}', full_content)
    
    if '\\usepackage{url}' not in output and '\\usepackage{hyperref}' not in output:
        output = output.replace('\\begin{document}', '\\usepackage{url}\n\\usepackage{hyperref}\n\\begin{document}')
    
    filename_out = f"libro_kdp_{lang_code}.tex"
    write_file(os.path.join(OUTPUT_DIR, filename_out), output)
    print(f"Generated: {filename_out}")

if __name__ == "__main__":
    ensure_dirs()
    generate_kdp_book('es')
    generate_kdp_book('en')
