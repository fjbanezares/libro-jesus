import subprocess
import pypdf

tpl_orig = open('templates/template_kdp_hardcover.tex', 'r', encoding='utf-8').read()

for scale in [1.00, 1.05, 1.08, 1.10, 1.12]:
    if scale == 1.00:
        new_pkg = r'\usepackage{ebgaramond}'
    else:
        new_pkg = rf'\usepackage[scaled={scale:.2f}]{{ebgaramond}}'
    
    lines = tpl_orig.splitlines()
    new_lines = []
    for l in lines:
        if 'ebgaramond' in l:
            new_lines.append(new_pkg)
        else:
            new_lines.append(l)
    open('templates/template_kdp_hardcover.tex', 'w', encoding='utf-8').write('\n'.join(new_lines))
    
    subprocess.run(['python3', 'generate_kdp_bundle.py'], capture_output=True)
    reader_hc_es = pypdf.PdfReader('output/latex/libro_kdp_tapa_dura_es.pdf')
    reader_hc_en = pypdf.PdfReader('output/latex/libro_kdp_tapa_dura_en.pdf')
    print(f'Scale {scale:.2f}x -> Hardcover ES: {len(reader_hc_es.pages)} págs | Hardcover EN: {len(reader_hc_en.pages)} págs')

# Restore original
open('templates/template_kdp_hardcover.tex', 'w', encoding='utf-8').write(tpl_orig)
