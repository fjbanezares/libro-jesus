# Helper script to assemble all translations for sections 14, 15, 16, 17 in 11 languages
import json
import os
import markdown
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
TRANSLATIONS_FILE = os.path.join(BASE_DIR, 'translations.json')
SPANISH_CONTENT_FILE = os.path.join(BASE_DIR, 'spanish_content.json')

def md_to_clean_html(md_text):
    html = markdown.markdown(md_text)
    return html

print("Starting translation builder for 14, 15, 16, 17...")
