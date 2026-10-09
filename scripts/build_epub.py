import os
import re
import json
import uuid
import zipfile
import markdown
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
IMAGES_DIR = os.path.join(BASE_DIR, 'content', 'images')
TRANSLATIONS_FILE = os.path.join(BASE_DIR, 'translations.json')
ENLACES_FILE = os.path.join(BASE_DIR, 'enlaces.json')
OUTPUT_EPUB_DIR = os.path.join(BASE_DIR, 'output', 'epub')

IMAGE_MAPPING = {
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
        13: "Estrella de Navidad: la luz que nace en el corazón."
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
        13: "Christmas Star: the light born within the heart."
    }
}

EPUB_CSS = """
@charset "utf-8";

/* Estilos tipográficos para Kindle y EPUB 3 */
body {
    font-family: "Georgia", "Palatino Linotype", "Book Antiqua", serif;
    line-height: 1.6;
    margin: 5% 5%;
    text-align: justify;
    color: #1a1a1a;
}

h1 {
    font-size: 1.8em;
    font-weight: bold;
    text-align: center;
    margin-top: 1.5em;
    margin-bottom: 0.8em;
    page-break-before: always;
    color: #111111;
}

h2 {
    font-size: 1.3em;
    font-weight: 600;
    margin-top: 1.2em;
    margin-bottom: 0.5em;
    text-align: center;
    color: #222222;
}

p {
    margin-top: 0;
    margin-bottom: 0.8em;
    text-indent: 1.2em;
}

p.no-indent {
    text-indent: 0;
}

/* Portada y páginas especiales */
.cover-page {
    text-align: center;
    margin: 0;
    padding: 0;
    page-break-before: always;
    page-break-after: always;
}

.cover-img {
    max-width: 100%;
    max-height: 100vh;
    height: auto;
    object-fit: contain;
}

.title-page {
    text-align: center;
    page-break-before: always;
    page-break-after: always;
    padding-top: 15%;
}

.title-page h1 {
    font-size: 2.2em;
    margin-bottom: 0.3em;
}

.title-page .subtitle {
    font-size: 1.3em;
    font-style: italic;
    color: #555555;
    margin-bottom: 2em;
}

.title-page .author {
    font-size: 1.2em;
    font-weight: bold;
    margin-top: 3em;
}

.copyright-page {
    font-size: 0.85em;
    text-align: center;
    page-break-before: always;
    padding-top: 40%;
    color: #666666;
}

/* Ilustraciones de capítulo */
.chapter-illustration {
    text-align: center;
    margin: 1.5em auto;
    page-break-inside: avoid;
}

.chapter-illustration img {
    max-width: 90%;
    height: auto;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.caption {
    font-size: 0.85em;
    font-style: italic;
    color: #555555;
    margin-top: 0.5em;
    text-align: center;
    text-indent: 0;
}

/* Poema / Versos */
.verse-container {
    margin: 1.5em auto;
    max-width: 85%;
    page-break-inside: avoid;
}

.verse-stanza {
    margin-bottom: 1.2em;
    line-height: 1.5;
    text-align: left;
}

.verse-stanza p {
    text-indent: 0;
    margin-bottom: 0.2em;
}

/* Sección de enlaces y llamada a la acción */
.links-section {
    margin-top: 2em;
    padding: 1.5em;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    background-color: #fafafa;
    text-align: center;
}

.links-section a {
    display: inline-block;
    padding: 10px 20px;
    margin: 8px;
    background-color: #2b4c7e;
    color: #ffffff !important;
    text-decoration: none;
    font-weight: bold;
    border-radius: 20px;
}

/* Soporte de modo oscuro */
@media (prefers-color-scheme: dark) {
    body {
        color: #e0e0e0;
        background-color: #121212;
    }
    h1, h2 {
        color: #ffffff;
    }
    .title-page .subtitle, .caption, .copyright-page {
        color: #aaaaaa;
    }
    .links-section {
        background-color: #1e1e1e;
        border-color: #333333;
    }
}
"""

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_for_xhtml(text):
    # Ensure valid XML/XHTML entities
    text = text.replace('&nbsp;', '&#160;')
    return text

def md_to_clean_xhtml(md_text, is_poem=False):
    if is_poem:
        stanzas = re.split(r'\n\s*\n', md_text)
        out = ['<div class="verse-container">']
        for stanza in stanzas:
            lines = stanza.strip().split('\n')
            clean_lines = []
            for l in lines:
                l = l.strip()
                if l.startswith('#'):
                    continue
                l = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', l)
                l = re.sub(r'\*(.*?)\*', r'<em>\1</em>', l)
                if l:
                    clean_lines.append(f'<p>{l}</p>')
            if clean_lines:
                out.append('<div class="verse-stanza">\n' + '\n'.join(clean_lines) + '\n</div>')
        out.append('</div>')
        return '\n'.join(out)
    else:
        md_text = re.sub(r'^# (.*)', '', md_text, flags=re.MULTILINE)
        html = markdown.markdown(md_text, extensions=['extra'])
        return clean_for_xhtml(html)

def build_epub(lang_code='es'):
    os.makedirs(OUTPUT_EPUB_DIR, exist_ok=True)
    translations = read_json(TRANSLATIONS_FILE) if os.path.exists(TRANSLATIONS_FILE) else {}
    links = read_json(ENLACES_FILE) if os.path.exists(ENLACES_FILE) else {}
    
    book_title = "Mi Amigo Jesucristo" if lang_code == 'es' else "My Friend Jesus Christ"
    subtitle = "Una guía cuántica para el alma moderna" if lang_code == 'es' else "A Quantum Guide for the Modern Soul"
    author = "A Glimpse of Light"
    collaborator = "Maria Paz Arés Osset"
    
    book_id = f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_DNS, f'pazaresosset.es.mi_amigo_jesucristo.{lang_code}')}"
    mod_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    chapter_map = [
        {"trans": "00_introduccion.html", "md": "00_introduccion.md", "type": "intro"},
        {"trans": "index.html", "md": "01_capitulo.md", "type": "chapter", "num": 1},
        {"trans": "02_capitulo.html", "md": "02_capitulo.md", "type": "chapter", "num": 2},
        {"trans": "03_capitulo.html", "md": "03_capitulo.md", "type": "chapter", "num": 3},
        {"trans": "04_capitulo.html", "md": "04_capitulo.md", "type": "chapter", "num": 4},
        {"trans": "05_capitulo.html", "md": "05_capitulo.md", "type": "chapter", "num": 5},
        {"trans": "06_capitulo.html", "md": "06_capitulo.md", "type": "chapter", "num": 6},
        {"trans": "07_capitulo.html", "md": "07_capitulo.md", "type": "chapter", "num": 7},
        {"trans": "08_capitulo.html", "md": "08_capitulo.md", "type": "chapter", "num": 8},
        {"trans": "09_capitulo.html", "md": "09_capitulo.md", "type": "chapter", "num": 9},
        {"trans": "10_capitulo.html", "md": "10_capitulo.md", "type": "chapter", "num": 10},
        {"trans": "11_capitulo.html", "md": "11_capitulo.md", "type": "chapter", "num": 11},
        {"trans": "12_epilogo.html", "md": "12_epilogo.md", "type": "epilogue"},
        {"trans": "13_apendice_poema.html", "md": "13_apendice_poema.md", "type": "appendix"}
    ]
    
    docs = []
    
    # 1. Cover
    docs.append({
        'id': 'cover',
        'href': 'text/cover.xhtml',
        'title': 'Portada' if lang_code == 'es' else 'Cover',
        'content': f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang_code}" lang="{lang_code}">
<head>
    <title>{"Portada" if lang_code == 'es' else "Cover"}</title>
    <link rel="stylesheet" type="text/css" href="../styles/stylesheet.css"/>
</head>
<body class="cover-page">
    <div>
        <img src="../images/cover.png" alt="{book_title}" class="cover-img"/>
    </div>
</body>
</html>""",
        'is_linear': 'yes'
    })
    
    # 2. Title & Copyright
    docs.append({
        'id': 'titlepage',
        'href': 'text/titlepage.xhtml',
        'title': 'Portada Interior' if lang_code == 'es' else 'Title Page',
        'content': f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang_code}" lang="{lang_code}">
<head>
    <title>{book_title}</title>
    <link rel="stylesheet" type="text/css" href="../styles/stylesheet.css"/>
</head>
<body>
    <div class="title-page">
        <h1>{book_title}</h1>
        <div class="subtitle">{subtitle}</div>
        <div class="author">{author}</div>
    </div>
</body>
</html>""",
        'is_linear': 'yes'
    })
    
    docs.append({
        'id': 'copyright',
        'href': 'text/copyright.xhtml',
        'title': 'Créditos' if lang_code == 'es' else 'Copyright',
        'content': f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang_code}" lang="{lang_code}">
<head>
    <title>{"Créditos" if lang_code == 'es' else "Copyright"}</title>
    <link rel="stylesheet" type="text/css" href="../styles/stylesheet.css"/>
</head>
<body>
    <div class="copyright-page">
        <p><strong>{book_title}</strong></p>
        <p><em>{subtitle}</em></p>
        <p>© 2024 {author}</p>
        <p>Ilustraciones y música original: {collaborator}</p>
        <p>Todos los derechos reservados.</p>
        <p>Publicado para Amazon Kindle KDP</p>
        <p style="margin-top: 2em;"><a href="https://pazaresosset.es">pazaresosset.es</a></p>
    </div>
</body>
</html>""",
        'is_linear': 'yes'
    })
    
    # Process Chapters
    for i, item in enumerate(chapter_map):
        md_file = item["md"]
        trans_key = item["trans"]
        chapter_data = translations.get(trans_key, {})
        
        h1 = ""
        body_html = ""
        
        if lang_code == 'es':
            md_path = os.path.join(CONTENT_DIR, md_file)
            if os.path.exists(md_path):
                raw_md = read_file(md_path)
                match = re.match(r'^# (.*)', raw_md)
                if match:
                    h1 = match.group(1).strip()
                body_html = md_to_clean_xhtml(raw_md, is_poem=(i == 13))
        else:
            h1 = chapter_data.get('h1', {}).get(lang_code, "")
            raw_body = chapter_data.get('body', {}).get(lang_code, "")
            if not raw_body and os.path.exists(os.path.join(CONTENT_DIR, md_file)):
                raw_body = read_file(os.path.join(CONTENT_DIR, md_file))
            body_html = md_to_clean_xhtml(raw_body, is_poem=(i == 13))
            
        if not h1:
            h1 = f"Capítulo {i}" if lang_code == 'es' else f"Chapter {i}"
            
        img_name = IMAGE_MAPPING.get(i, 'vibration.png')
        caption = IMAGE_CAPTIONS.get(lang_code, {}).get(i, "")
        
        doc_body = f"""<h1 class="chapter-title">{h1}</h1>
<div class="chapter-illustration">
    <img src="../images/{img_name}" alt="{h1}"/>
    <p class="caption">{caption}</p>
</div>
<div class="chapter-body">
    {body_html}
</div>"""

        if i == 13:
            spotify_info = links.get('spotify', {}).get(lang_code, {})
            spotify_album = spotify_info.get('album_id')
            spotify_url = f"https://open.spotify.com/album/{spotify_album}" if spotify_album else "https://open.spotify.com/artist/3P9x9Y0y0I3p6e5g9mG4Xk"
            
            call_text = "Para completar esta experiencia vibracional, te invito a sumergirte en la música y frecuencias originales del libro:" if lang_code == 'es' else "To complete this vibrational experience, I invite you to immerse yourself in the book's music:"
            spotify_label = "🎵 Escuchar en Spotify" if lang_code == 'es' else "🎵 Listen on Spotify"
            web_label = "🌐 Visitar Web Oficial (pazaresosset.es)" if lang_code == 'es' else "🌐 Official Website (pazaresosset.es)"
            
            doc_body += f"""
<div class="links-section">
    <p class="no-indent"><strong>{call_text}</strong></p>
    <p class="no-indent"><a href="{spotify_url}">{spotify_label}</a></p>
    <p class="no-indent"><a href="https://pazaresosset.es">{web_label}</a></p>
</div>"""

        doc_content = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang_code}" lang="{lang_code}">
<head>
    <title>{h1}</title>
    <link rel="stylesheet" type="text/css" href="../styles/stylesheet.css"/>
</head>
<body>
    {doc_body}
</body>
</html>"""
        
        doc_id = f"chap_{i:02d}"
        doc_href = f"text/chap_{i:02d}.xhtml"
        docs.append({
            'id': doc_id,
            'href': doc_href,
            'title': h1,
            'content': doc_content,
            'is_linear': 'yes',
            'in_toc': True
        })
        
    # Nav XHTML (EPUB3)
    nav_li = []
    for d in docs:
        if d.get('in_toc'):
            nav_li.append(f'        <li><a href="{d["href"]}">{d["title"]}</a></li>')
    nav_list_str = '\n'.join(nav_li)
    
    nav_content = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang_code}" lang="{lang_code}">
<head>
    <title>{"Índice de Contenido" if lang_code == 'es' else "Table of Contents"}</title>
    <link rel="stylesheet" type="text/css" href="../styles/stylesheet.css"/>
</head>
<body>
    <nav epub:type="toc" id="toc">
        <h1>{"Índice de Contenido" if lang_code == 'es' else "Table of Contents"}</h1>
        <ol>
{nav_list_str}
        </ol>
    </nav>
    <nav epub:type="landmarks" hidden="">
        <ol>
            <li><a epub:type="cover" href="text/cover.xhtml">{"Portada" if lang_code == 'es' else "Cover"}</a></li>
            <li><a epub:type="toc" href="nav.xhtml">{"Índice" if lang_code == 'es' else "Table of Contents"}</a></li>
            <li><a epub:type="bodymatter" href="text/chap_00.xhtml">{"Comenzar a leer" if lang_code == 'es' else "Begin Reading"}</a></li>
        </ol>
    </nav>
</body>
</html>"""

    # NCX (EPUB2 compatibility for older Kindles)
    ncx_points = []
    play_order = 1
    for d in docs:
        if d.get('in_toc'):
            ncx_points.append(f"""    <navPoint id="navPoint-{play_order}" playOrder="{play_order}">
      <navLabel><text>{d['title']}</text></navLabel>
      <content src="{d['href']}"/>
    </navPoint>""")
            play_order += 1
    ncx_str = '\n'.join(ncx_points)
    
    toc_ncx_content = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{book_id}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>{book_title}</text>
  </docTitle>
  <docAuthor>
    <text>{author}</text>
  </docAuthor>
  <navMap>
{ncx_str}
  </navMap>
</ncx>"""

    # Manifest items
    manifest_items = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '<item id="css" href="styles/stylesheet.css" media-type="text/css"/>',
        '<item id="cover-image" href="images/cover.png" media-type="image/png" properties="cover-image"/>'
    ]
    
    for d in docs:
        manifest_items.append(f'<item id="{d["id"]}" href="{d["href"]}" media-type="application/xhtml+xml"/>')
        
    added_imgs = {'cover.png'}
    for i, img_file in IMAGE_MAPPING.items():
        if img_file not in added_imgs:
            added_imgs.add(img_file)
            manifest_items.append(f'<item id="img_{i:02d}" href="images/{img_file}" media-type="image/png"/>')
            
    manifest_str = '\n    '.join(manifest_items)
    
    spine_items = []
    for d in docs:
        linear_attr = ' linear="yes"' if d.get('is_linear') == 'yes' else ''
        spine_items.append(f'<itemref idref="{d["id"]}"{linear_attr}/>')
    spine_str = '\n    '.join(spine_items)
    
    content_opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookID" version="3.0" xml:lang="{lang_code}">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:identifier id="BookID">{book_id}</dc:identifier>
    <dc:title>{book_title}</dc:title>
    <dc:creator id="creator">{author}</dc:creator>
    <meta refines="#creator" property="role" scheme="marc:relators">aut</meta>
    <dc:contributor id="contrib1">{collaborator}</dc:contributor>
    <meta refines="#contrib1" property="role" scheme="marc:relators">ill</meta>
    <dc:language>{lang_code}</dc:language>
    <dc:publisher>A Glimpse of Light</dc:publisher>
    <dc:rights>© 2024 {author}. All rights reserved.</dc:rights>
    <dc:description>{subtitle}</dc:description>
    <meta property="dcterms:modified">{mod_time}</meta>
    <meta name="cover" content="cover-image"/>
  </metadata>
  <manifest>
    {manifest_str}
  </manifest>
  <spine toc="ncx">
    {spine_str}
  </spine>
  <guide>
    <reference type="cover" title="Portada" href="text/cover.xhtml"/>
    <reference type="toc" title="Índice" href="nav.xhtml"/>
    <reference type="text" title="Inicio" href="text/chap_00.xhtml"/>
  </guide>
</package>"""

    out_filename = f"mi_amigo_jesucristo_{lang_code}.epub" if lang_code == 'es' else f"my_friend_jesus_christ_{lang_code}.epub"
    epub_path = os.path.join(OUTPUT_EPUB_DIR, out_filename)
    
    with zipfile.ZipFile(epub_path, 'w') as zf:
        zf.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        
        container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>"""
        zf.writestr('META-INF/container.xml', container_xml, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr('OEBPS/content.opf', content_opf, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr('OEBPS/nav.xhtml', nav_content, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr('OEBPS/toc.ncx', toc_ncx_content, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr('OEBPS/styles/stylesheet.css', EPUB_CSS, compress_type=zipfile.ZIP_DEFLATED)
        
        for d in docs:
            zf.writestr(f"OEBPS/{d['href']}", d['content'], compress_type=zipfile.ZIP_DEFLATED)
            
        cover_src = os.path.join(IMAGES_DIR, 'cover_kdp.png')
        if os.path.exists(cover_src):
            zf.write(cover_src, 'OEBPS/images/cover.png', compress_type=zipfile.ZIP_DEFLATED)
            
        for img_file in added_imgs:
            if img_file == 'cover.png': continue
            img_src = os.path.join(IMAGES_DIR, img_file)
            if os.path.exists(img_src):
                zf.write(img_src, f'OEBPS/images/{img_file}', compress_type=zipfile.ZIP_DEFLATED)
                
    print(f"EPUB generado con éxito: {epub_path} ({os.path.getsize(epub_path)} bytes)")
    return epub_path

if __name__ == '__main__':
    build_epub('es')
    build_epub('en')
