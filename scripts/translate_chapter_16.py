import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANSLATIONS_FILE = os.path.join(BASE_DIR, 'translations.json')
SPANISH_CONTENT_FILE = os.path.join(BASE_DIR, 'spanish_content.json')

with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
    translations = json.load(f)

with open(SPANISH_CONTENT_FILE, 'r', encoding='utf-8') as f:
    spanish_content = json.load(f)

TITLES_16 = {
    "es": "Sobre el Autor y el Proyecto",
    "en": "About the Author and the Project",
    "fr": "À propos de l'Auteur et du Projet",
    "it": "Sull'Autore e sul Progetto",
    "zh": "关于作者与项目",
    "ar": "عن المؤلف والمشروع",
    "ru": "Об авторе и проекте",
    "vi": "Về Tác giả và Dự án",
    "ko": "저자와 프로젝트 소개",
    "pt": "Sobre o Autor e o Projeto",
    "ja": "著者とプロジェクトについて"
}

# The Spanish body is in spanish_content["16_sobre_el_autor.html"]["body"]
body_es = spanish_content["16_sobre_el_autor.html"]["body"]

# We will generate high quality translations in the other 10 languages, preserving all image divs:
# <div class="chapter-illustration-small" ...><img src="images/..." alt="..." ...></div>

print("Translating Chapter 16...")
