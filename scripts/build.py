import os
import re
import shutil
import markdown

# Configuration
CONTENT_DIR = 'content'
IMAGES_DIR = 'content/images'
OUTPUT_HTML_DIR = 'output/html'
OUTPUT_HTML_IMAGES_DIR = 'output/html/images'
OUTPUT_LATEX_DIR = 'output/latex'
OUTPUT_LATEX_IMAGES_DIR = 'output/latex/images'
TEMPLATE_HTML = 'templates/template.html'
TEMPLATE_LATEX = 'templates/template.tex'

def ensure_dirs():
    os.makedirs(OUTPUT_HTML_DIR, exist_ok=True)
    os.makedirs(OUTPUT_HTML_IMAGES_DIR, exist_ok=True)
    os.makedirs(OUTPUT_LATEX_DIR, exist_ok=True)
    os.makedirs(OUTPUT_LATEX_IMAGES_DIR, exist_ok=True)

def copy_images():
    if os.path.exists(IMAGES_DIR):
        for img in os.listdir(IMAGES_DIR):
            src = os.path.join(IMAGES_DIR, img)
            # Copy to HTML images
            shutil.copy(src, os.path.join(OUTPUT_HTML_IMAGES_DIR, img))
            # Copy to LaTeX images
            shutil.copy(src, os.path.join(OUTPUT_LATEX_IMAGES_DIR, img))

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def get_image_for_chapter(filename, title):
    # Enhanced logic to assign images
    lower_title = title.lower()
    lower_filename = filename.lower()
    
    if 'introduccion' in lower_filename or 'introducción' in lower_title:
        return 'images/intro_quantum_luther.png'
    elif 'poema' in lower_filename or 'navidad' in lower_title:
        return 'images/christmas_star_modern.png'
    elif 'pan' in lower_title:
        return 'images/bread_sparrows.png'
    elif 'perdón' in lower_title or 'perdon' in lower_title or 'deudas' in lower_title:
        return 'images/forgiveness_chains.png'
    elif 'líbranos' in lower_title or 'libranos' in lower_title or 'mal' in lower_title:
        return 'images/eagle_protection.png'
    elif 'madrid' in lower_title or 'encuentro' in lower_title:
        return 'images/madrid.png'
    elif 'rozas' in lower_title:
        return 'images/las_rozas_park.png'
    elif 'vibración' in lower_title or 'vibracion' in lower_title:
        # Check context, if it's chapter 3 use silence/vibration
        if 'silencio' in lower_title:
            return 'images/silence_vibration.png'
        # If it's chapter 9 (tentación / vibrar alto) reuse vibration or fog/light
        if 'tentación' in lower_title or 'tentacion' in lower_title:
            return 'images/fog_light.png'
        return 'images/vibration.png'
    elif 'naturaleza' in lower_title or 'colmenarejo' in lower_title:
        return 'images/nature.png'
    elif 'cielo' in lower_title:
        return 'images/heaven_state.png'
    elif 'padre' in lower_title:
        return 'images/cosmic_father.png'
    elif 'reino' in lower_title or 'poder' in lower_title or 'gloria' in lower_title:
        return 'images/kingdom_power.png'
    elif 'epílogo' in lower_title or 'epilogo' in lower_title:
        return 'images/sunset_road.png'
    else:
        # Default rotation or generic
        return 'images/vibration.png'

def md_to_html(md_content, title, menu_html, image_path):
    html_body = markdown.markdown(md_content)
    
    # Append image to the end of the body
    html_body += f'\n<div class="image-container-footer"><img src="{image_path}" alt="Ilustración del capítulo" class="footer-image"></div>'
    
    template = read_file(TEMPLATE_HTML)
    
    output = template.replace('{{TITLE}}', title)
    output = output.replace('{{CONTENT}}', html_body)
    output = output.replace('{{MENU_ITEMS}}', menu_html)
    # Still replace IMAGE_PATH for the hero if we keep it, but user complained about cropping.
    # We will keep the hero image but user asked to ALSO insert at the end "so they see it whole".
    output = output.replace('{{IMAGE_PATH}}', image_path)
    
    return output

def md_to_latex(md_content, title, image_path):
    latex_body = md_content
    
    # 1. Handle Chapter Titles
    # Remove "Capítulo X: " redundancy for LaTeX \chapter command
    # We want to capture the title text AFTER the prefix
    
    def title_replacer(match):
        full_line = match.group(1) # The content after '# '
        # Check if it starts with "Capítulo X: " or "Introducción"
        clean_title = full_line
        is_intro = False
        
        if "Introducción" in full_line:
            is_intro = True
            clean_title = full_line # Keep full title for Intro
        elif "Apéndice" in full_line:
            is_intro = True # Treat appendix like intro (unnumbered)
        else:
            # Regex to strip "Capítulo \d+: " or just "Capítulo \d+ "
            # Handles optional colon and varying spacing
            clean_title = re.sub(r'^Capítulo\s+\d+[:\.]?\s*', '', full_line, flags=re.IGNORECASE)
        
        if is_intro:
            return f'\\chapter*{{{clean_title}}}\n\\addcontentsline{{toc}}{{chapter}}{{{clean_title}}}'
        else:
            return f'\\chapter{{{clean_title}}}'

    latex_body = re.sub(r'^# (.*)', title_replacer, latex_body, flags=re.MULTILINE)
    
    latex_body = re.sub(r'^# (.*)', title_replacer, latex_body, flags=re.MULTILINE)
    
    # 2. Handle Sections
    # Determine if we should use unnumbered sections
    # 'title' variable is passed to this function. We can check it.
    is_unnumbered_chapter = "introducción" in title.lower() or "introduccion" in title.lower() or "apéndice" in title.lower() or "apendice" in title.lower()

    def section_replacer(match):
        sec_title = match.group(1)
        # Add needspace to prevent orphaned headers
        prefix = r'\needspace{5\baselineskip}' + '\n'
        if is_unnumbered_chapter:
            return f'{prefix}\\section*{{{sec_title}}}'
        else:
            return f'{prefix}\\section{{{sec_title}}}'

    latex_body = re.sub(r'^## (.*)', section_replacer, latex_body, flags=re.MULTILINE)
    
    # 3. Handle Formatting
    latex_body = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', latex_body)
    latex_body = re.sub(r'\*(.*?)\*', r'\\textit{\1}', latex_body)
    
    # 4. Handle Line Breaks (Markdown "  \n" to LaTeX "\\")
    # We look for two spaces followed by a newline. 
    # IMPORTANT: We must ensure we don't break paragraph separation (double newline).
    # But "  \n" usually appears within a paragraph (verse).
    latex_body = latex_body.replace('  \n', '\\\\\n')
    
    # 5. Insert Image
    # We insert the image after the chapter command.
    lines = latex_body.split('\n')
    new_lines = []
    image_inserted = False
    
    latex_image_code = f"""
\\begin{{figure}}[h]
    \\centering
    \\includegraphics[width=0.8\\textwidth]{{{image_path}}}
\\end{{figure}}
"""
    
    for line in lines:
        new_lines.append(line)
        # Check for both numbered and unnumbered chapters
        if (line.startswith(r'\chapter{') or line.startswith(r'\chapter*{')) and not image_inserted:
            new_lines.append(latex_image_code)
            image_inserted = True
            
    if not image_inserted:
        new_lines.insert(0, latex_image_code)
        
    return '\n'.join(new_lines)

def build():
    ensure_dirs()
    copy_images()
    
    files = sorted([f for f in os.listdir(CONTENT_DIR) if f.endswith('.md')])
    
    # Pass 1: Collect Metadata for Menu
    chapters = []
    for filename in files:
        filepath = os.path.join(CONTENT_DIR, filename)
        content = read_file(filepath)
        lines = content.strip().split('\n')
        title = lines[0].replace('# ', '') if lines and lines[0].startswith('# ') else filename
        chapters.append({'filename': filename, 'title': title})

    # Generate Menu HTML
    menu_html = ""
    for chap in chapters:
        html_filename = chap['filename'].replace('.md', '.html')
        if chap['filename'] == '01_capitulo.md':
            html_filename = 'index.html'
        menu_html += f'<li><a href="{html_filename}">{chap["title"]}</a></li>\n'

    # Pass 2: Generate Content
    full_latex_content = ""
    
    for chap in chapters:
        filename = chap['filename']
        title = chap['title']
        filepath = os.path.join(CONTENT_DIR, filename)
        content = read_file(filepath)
        
        # Determine Image
        image_path = get_image_for_chapter(filename, title)
        
        # HTML
        # HTML
        if filename == '01_capitulo.md':
            target_html = 'index.html'
        else:
            target_html = filename.replace('.md', '.html')
            
        current_menu = menu_html.replace(f'href="{target_html}"', f'href="{target_html}" class="active"')
        html_content = md_to_html(content, title, current_menu, image_path)
        write_file(os.path.join(OUTPUT_HTML_DIR, target_html), html_content)
        print(f"Generated HTML: {target_html}")
        
        # LaTeX
        full_latex_content += md_to_latex(content, title, image_path) + "\n\\newpage\n"

    # Write Full Book LaTeX
    master_template = read_file(TEMPLATE_LATEX)
    final_latex_book = master_template.replace('{{TITLE}}', "Mi amigo Jesucristo").replace('{{CONTENT}}', full_latex_content)
    write_file(os.path.join(OUTPUT_LATEX_DIR, 'libro_completo.tex'), final_latex_book)
    print("Generated LaTeX: libro_completo.tex")

if __name__ == "__main__":
    build()
