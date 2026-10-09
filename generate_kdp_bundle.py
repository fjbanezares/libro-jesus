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

def format_quotes_for_latex(text, lang='es'):
    # Normalize curly double quotes
    text = text.replace('“', '"').replace('”', '"')
    if lang == 'es':
        # Replace matched pairs of double quotes with Spanish «...»
        text = re.sub(r'"([^"]+?)"', r'«\1»', text)
    else:
        # Replace matched pairs of double quotes with English ``...''
        text = re.sub(r'"([^"]+?)"', r"``\1''", text)
    return text

def clean_html_for_latex(text, is_poem=False, lang='es'):
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
        res = '\n\n\\bigskip\\bigskip\n\n'.join(processed_stanzas)
        return format_quotes_for_latex(res, lang=lang)
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
        return format_quotes_for_latex(text.strip(), lang=lang)

def md_to_latex(md_content, is_poem=False, lang='es'):
    # Standardize
    md_content = md_content.replace('\r\n', '\n')

    # Remove main H1 title
    md_content = re.sub(r'^# (.*)', '', md_content, flags=re.MULTILINE)

    if is_poem:
        # Split into stanzas
        stanzas = re.split(r'\n\s*\n', md_content)
        processed_stanzas = []
        for idx, stanza in enumerate(stanzas):
            stanza = re.sub(r'^\s*#+.*', '', stanza, flags=re.MULTILINE)
            lines = stanza.strip().split('\n')
            processed_lines = []
            for line in lines:
                line_clean = line.strip()
                if idx == 0 and ('Navidad de Alta Frecuencia' in line_clean or 'High Frequency Christmas' in line_clean):
                    title_clean = re.sub(r'[\*\_]', '', line_clean).strip()
                    processed_lines.append(f"{{\\LARGE\\bfseries {title_clean}}}")
                elif idx == 0 and ('Maria Paz' in line_clean or 'Arés' in line_clean or 'Ares' in line_clean or 'By ' in line_clean or 'Por ' in line_clean):
                    sub_clean = re.sub(r'[\*\_]', '', line_clean).strip()
                    processed_lines.append(f"{{\\large\\itshape {sub_clean}}}\\\\[0.3cm]")
                else:
                    line_formatted = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', line_clean)
                    line_formatted = re.sub(r'\*(.*?)\*', r'\\textit{\1}', line_formatted)
                    line_formatted = line_formatted.replace('&', '\\&').replace('$', '\\$').replace('%', '\\%').replace('#', '\\#').replace('_', '\\_')
                    if line_formatted:
                        processed_lines.append(line_formatted)
            if processed_lines:
                processed_stanzas.append(' \\\\\n'.join(processed_lines))
        res_poem = '\n\n\\vspace{0.4cm}\n\n'.join(processed_stanzas)
        return format_quotes_for_latex(res_poem, lang=lang)

    # 1. Convert small inline illustrations
    def img_replacer(match):
        img_src = match.group(1).replace('images/', '').strip()
        return f"\n\n\\vspace{{0.4cm}}\n\\begin{{center}}\n\\nopagebreak\n\\includegraphics[width=0.62\\textwidth,cfbox=gray!50 0.5pt 3pt]{{{img_src}}}\n\\end{{center}}\n\\vspace{{0.4cm}}\n\n"

    md_content = re.sub(r'<div class="chapter-illustration-small"[^>]*>\s*<img src="images/([^"]+)"[^>]*>\s*</div>', img_replacer, md_content)
    md_content = re.sub(r'<div class="image-container-footer"[^>]*>.*?</div>', '', md_content, flags=re.DOTALL)
    
    # 2. Dividers
    rule_tex = "\n\n\\vspace{0.4cm}\n\\begin{center}\n\\rule{0.35\\textwidth}{0.4pt}\n\\end{center}\n\\vspace{0.4cm}\n\n"
    md_content = re.sub(r'<hr\s*/?>', lambda m: rule_tex, md_content)
    md_content = re.sub(r'^\s*---\s*$', lambda m: rule_tex, md_content, flags=re.MULTILINE)

    # 3. Blockquotes
    def quote_replacer(m):
        q = m.group(1).strip()
        return f"\n\n\\begin{{quote}}\n\\itshape {q}\n\\end{{quote}}\n\n"
    md_content = re.sub(r'^>\s*(.*)', quote_replacer, md_content, flags=re.MULTILINE)

    # 4. Headers: ### and ##
    md_content = re.sub(r'^###\s*(.*)', lambda m: f"\\subsection*{{{m.group(1).strip()}}}", md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^##\s*(.*)', lambda m: f"\\section*{{{m.group(1).strip()}}}", md_content, flags=re.MULTILINE)

    # 5. Bold & Italic
    md_content = re.sub(r'\*\*(.*?)\*\*', lambda m: f"\\textbf{{{m.group(1)}}}", md_content)
    md_content = re.sub(r'<strong>(.*?)</strong>', lambda m: f"\\textbf{{{m.group(1)}}}", md_content)
    md_content = re.sub(r'\*(.*?)\*', lambda m: f"\\textit{{{m.group(1)}}}", md_content)
    md_content = re.sub(r'<em>(.*?)</em>', lambda m: f"\\textit{{{m.group(1)}}}", md_content)

    # 6. Lists
    md_content = re.sub(r'^\s*[\*\-]\s+(.*)', lambda m: f"\\noindent\\textbullet~~{m.group(1).strip()}\\\\\n", md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^\s*(\d+)\.\s+(.*)', lambda m: f"\\noindent\\textbf{{{m.group(1)}.}}~~{m.group(2).strip()}\\\\\n", md_content, flags=re.MULTILINE)

    # 7. Clean remaining HTML
    md_content = re.sub(r'<br\s*/?>', lambda m: "\\\\\n", md_content)
    md_content = re.sub(r'</?p>', '\n\n', md_content)
    md_content = re.sub(r'<[^>]+>', '', md_content)

    # 8. Escape lone special characters outside LaTeX commands
    lines = md_content.split('\n')
    processed_lines = []
    for l in lines:
        if not l.strip().startswith('\\'):
            l = l.replace('&', '\\&').replace('$', '\\$').replace('%', '\\%').replace('#', '\\#')
        processed_lines.append(l)

    result = '\n'.join(processed_lines).strip()
    return format_quotes_for_latex(result, lang=lang)

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
        13: 'christmas_star_modern.png',
        14: 'vibration.png',
        15: 'silence_vibration.png',
        16: 'intro_quantum_luther.png',
        17: 'heaven_state.png'
    }
    return mapping.get(chapter_num, 'vibration.png')

IMAGE_CAPTIONS = {
    'es': {
        0: "Entre la partícula y la vibración: el despertar de la conciencia.",
        1: "El encuentro en la ciudad: la presencia viva en lo cotidiano.",
        2: "El silencio del parque: afinando el templo interior.",
        3: "La vibración del silencio: trascendiendo el ruido mental.",
        4: "La rendición y la paz: el flujo natural del Ser.",
        5: "Abwoon: la Fuente cósmica de toda la creación.",
        6: "El Reino de los Cielos: una frecuencia presente aquí y ahora.",
        7: "El pan de cada día: confianza absoluta y sustento.",
        8: "El perdón consciente: liberando los lazos cuánticos del pasado.",
        9: "Sintonizar alto: elevándose sobre las emociones densas.",
        10: "Líbranos del mal: la protección de la fe elevada.",
        11: "El Reino, el Poder y la Gloria: la resonancia eterna.",
        12: "El atardecer en el camino: la caminata del alma continúa.",
        13: "Estrella de Navidad: la luz que nace en el corazón.",
        14: "El puente luminoso entre la física cuántica y la sabiduría del Cristo.",
        15: "La música y el arte: vehículos directos de alta vibración.",
        16: "A Glimpse of Light: un destello de luz y servicio en la oscuridad.",
        17: "El templo interior: guía de presencia, silencio y coherencia cuántica."
    },
    'en': {
        0: "Between particle and vibration: the awakening of consciousness.",
        1: "Meeting in the city: living presence in everyday life.",
        2: "The silence of the park: tuning the inner temple.",
        3: "The vibration of silence: transcending mental noise.",
        4: "Surrender and peace: the natural flow of Being.",
        5: "Abwoon: the cosmic Source of all creation.",
        6: "The Kingdom of Heaven: a wave frequency present here and now.",
        7: "Daily bread: absolute trust and spiritual nourishment.",
        8: "Conscious forgiveness: breaking quantum ties to the past.",
        9: "Vibrating high: rising above dense emotions.",
        10: "Deliver us from evil: protection under elevated faith.",
        11: "The Kingdom, Power, and Glory: eternal resonance.",
        12: "Sunset on the road: the soul's journey continues.",
        13: "Christmas Star: the light born within the heart.",
        14: "The luminous bridge between quantum physics and Christ's wisdom.",
        15: "Music and art: direct vehicles of high vibrational frequency.",
        16: "A Glimpse of Light: a beam of light and selfless service in the darkness.",
        17: "The inner temple: practical guide to presence and quantum coherence."
    }
}

TEMPLATE_KDP_HARDCOVER = os.path.join(BASE_DIR, 'templates', 'template_kdp_hardcover.tex')

def generate_kdp_book(lang_code, is_hardcover=False):
    translations = read_json(TRANSLATIONS_FILE)
    links = read_json(ENLACES_FILE)
    template_path = TEMPLATE_KDP_HARDCOVER if is_hardcover else TEMPLATE_KDP
    template = read_file(template_path)
    
    lang_babel = 'spanish,es-noquoting' if lang_code == 'es' else 'english'
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
        {"trans": "13_apendice_poema.html", "md": "13_apendice_poema.md"},
        {"trans": "14_glosario_cuantico.html", "md": "14_glosario_cuantico.md"},
        {"trans": "15_musica_frecuencias.html", "md": "15_musica_frecuencias.md"},
        {"trans": "16_sobre_el_autor.html", "md": "16_sobre_el_autor.md"},
        {"trans": "17_guia_meditacion.html", "md": "17_guia_meditacion.md"}
    ]
    
    chap_dir = os.path.join(OUTPUT_DIR, f"capitulos_{lang_code}")
    os.makedirs(chap_dir, exist_ok=True)
    
    full_content = ""
    
    for i, item in enumerate(chapter_map):
        trans_key = item["trans"]
        md_file = item["md"]
        chapter_data = translations.get(trans_key, {})
        h1 = chapter_data.get('h1', {}).get(lang_code, "")
        
        body_latex = ""
        if lang_code == 'es' or i >= 14: # For newly added sections 14-17 or Spanish
            md_path = os.path.join(CONTENT_DIR, md_file)
            if os.path.exists(md_path):
                raw_md = read_file(md_path)
                if not h1:
                    match = re.match(r'^# (.*)', raw_md)
                    if match: h1 = match.group(1)
                body_latex = md_to_latex(raw_md, is_poem=(i == 13), lang=lang_code)
            else:
                continue
        else:
            body_html = chapter_data.get('body', {}).get(lang_code, "")
            if not body_html: continue
            body_latex = clean_html_for_latex(body_html, is_poem=(i == 13), lang=lang_code)

        if not h1: h1 = f"Chapter {i}"
        
        chap_content = ""
        if i == 0 or i >= 13: # Introduction, Appendix, Glossary, Music, Author, Meditation
            chap_content += f"\\chapter*{{{h1}}}\n\\addcontentsline{{toc}}{{chapter}}{{{h1}}}\n\\markboth{{{h1}}}{{{h1}}}\n"
        else:
            title_text = re.sub(r'^(Capítulo|Chapter|제\d+장)\s+\d*[:\.]?\s*', '', h1, flags=re.IGNORECASE)
            chap_content += f"\\chapter{{{title_text}}}\n"
            
        img_name = get_image_for_chapter(i)
        caption_text = IMAGE_CAPTIONS.get(lang_code, {}).get(i, "")
        
        if i == 13: # Poem: compact hero image so the poem begins immediately on the same page
            chap_content += "\\vspace{0.3cm}\n"
            chap_content += f"\\begin{{center}}\n\\nopagebreak\n\\includegraphics[width=0.45\\textwidth,cfbox=gray!60 0.6pt 3pt]{{{img_name}}}\\\\\n\\vspace{{3pt}}\n{{\\small\\itshape {caption_text}}}\n\\end{{center}}\n\n"
            chap_content += "\\vspace{0.4cm}\n"
            chap_content += "{\\centering\n" + body_latex + "\n\\par}\n"
        else:
            chap_content += "\\vspace{0.6cm}\n"
            chap_content += f"\\begin{{center}}\n\\nopagebreak\n\\includegraphics[width=0.75\\textwidth,cfbox=gray!60 0.6pt 4pt]{{{img_name}}}\\\\\n\\vspace{{4pt}}\n{{\\small\\itshape {caption_text}}}\n\\end{{center}}\n\n"
            chap_content += "\\vspace{0.6cm}\n"
            chap_content += body_latex
        
        if i == 13 or i == 15:
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
            
            chap_content += f"\n\n\\vspace{{1.5cm}}\n\\begin{{center}}\n"
            chap_content += f"\\textit{{{invitation_intro}}}\\\\\n"
            chap_content += f"\\vspace{{1cm}}\n"
            chap_content += f"\\begin{{minipage}}{{0.45\\textwidth}}\n\\centering\n"
            chap_content += f"\\qrcode[height=3.2cm]{{{spotify_url}}}\\\\\n"
            chap_content += f"\\vspace{{0.4cm}}\\textbf{{{label_spotify}}}\n"
            chap_content += f"\\end{{minipage}}\\hfill\n"
            chap_content += f"\\begin{{minipage}}{{0.45\\textwidth}}\n\\centering\n"
            chap_content += f"\\qrcode[height=3.2cm]{{https://pazaresosset.es}}\\\\\n"
            chap_content += f"\\vspace{{0.4cm}}\\textbf{{{label_web}}}\n"
            chap_content += f"\\end{{minipage}}\n"
            chap_content += f"\\end{{center}}"
            
        chap_filename = f"cap_{i:02d}.tex"
        write_file(os.path.join(chap_dir, chap_filename), chap_content)
        
        break_cmd = "\\cleardoublepage\n\n" if is_hardcover else "\\newpage\n\n"
        full_content += f"\\input{{capitulos_{lang_code}/{chap_filename}}}\n{break_cmd}"

    output = template
    output = output.replace('{{LANG}}', lang_babel)
    output = output.replace('{{BOOK_TITLE}}', book_title)
    output = output.replace('{{SUBTITLE}}', subtitle)
    output = output.replace('{{AUTHOR}}', author)
    output = output.replace('{{CONTENT}}', full_content)
    
    if '\\usepackage{url}' not in output and '\\usepackage{hyperref}' not in output:
        output = output.replace('\\begin{document}', '\\usepackage{url}\n\\usepackage{hyperref}\n\\begin{document}')
    
    suffix = "_tapa_dura" if is_hardcover else ""
    filename_out = f"libro_kdp{suffix}_{lang_code}.tex"
    write_file(os.path.join(OUTPUT_DIR, filename_out), output)
    print(f"Generated: {filename_out}")

if __name__ == "__main__":
    ensure_dirs()
    # Paperback editions (Tapa Blanda)
    generate_kdp_book('es', is_hardcover=False)
    generate_kdp_book('en', is_hardcover=False)
    # Hardcover editions (Tapa Dura)
    generate_kdp_book('es', is_hardcover=True)
    generate_kdp_book('en', is_hardcover=True)


