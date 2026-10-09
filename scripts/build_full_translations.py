import json
import os
import markdown
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANSLATIONS_FILE = os.path.join(BASE_DIR, 'translations.json')
SPANISH_CONTENT_FILE = os.path.join(BASE_DIR, 'spanish_content.json')
CONTENT_DIR = os.path.join(BASE_DIR, 'content')

with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
    translations = json.load(f)

with open(SPANISH_CONTENT_FILE, 'r', encoding='utf-8') as f:
    spanish_content = json.load(f)

def clean_md_for_html(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'^# .*\n+', '', text)
    return markdown.markdown(text, extensions=['extra'])

# Spanish Base Content
html_14_es = clean_md_for_html(os.path.join(CONTENT_DIR, '14_glosario_cuantico.md'))
html_15_es = clean_md_for_html(os.path.join(CONTENT_DIR, '15_musica_frecuencias.md'))
html_16_es = clean_md_for_html(os.path.join(CONTENT_DIR, '16_sobre_el_autor.md'))
html_17_es = clean_md_for_html(os.path.join(CONTENT_DIR, '17_guia_meditacion.md'))

spanish_content["14_glosario_cuantico.html"] = {"title": "Glosario Cuántico y Espiritual", "h1": "Glosario Cuántico y Espiritual", "body": html_14_es}
spanish_content["15_musica_frecuencias.html"] = {"title": "La Música y las Frecuencias", "h1": "La Música y las Frecuencias", "body": html_15_es}
spanish_content["16_sobre_el_autor.html"] = {"title": "Sobre el Autor y el Proyecto", "h1": "Sobre el Autor y el Proyecto", "body": html_16_es}
spanish_content["17_guia_meditacion.html"] = {"title": "Guía de Reflexión y Meditación", "h1": "Guía de Reflexión y Meditación", "body": html_17_es}

# TITLES
TITLES_14 = {
    "es": "Glosario Cuántico y Espiritual",
    "en": "Quantum and Spiritual Glossary",
    "fr": "Glossaire Quantique et Spirituel",
    "it": "Glossario Quantistico e Spirituale",
    "zh": "量子与灵性词汇表",
    "ar": "معجم الكم والروحانية",
    "ru": "Квантовый и духовный глоссарий",
    "vi": "Thuật ngữ Lượng tử và Tâm linh",
    "ko": "양자 및 영적 용어집",
    "pt": "Glossário Quântico e Espiritual",
    "ja": "量子とスピリチュアル用語集"
}

TITLES_15 = {
    "es": "La Música y las Frecuencias",
    "en": "Music and Frequencies",
    "fr": "La Musique et les Fréquences",
    "it": "La Musica e le Frequenze",
    "zh": "音乐与频率",
    "ar": "الموسيقى والترددات",
    "ru": "Музыка и частоты",
    "vi": "Âm nhạc và Tần số",
    "ko": "음악과 주파수",
    "pt": "A Música e as Frequências",
    "ja": "音楽と周波数"
}

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

TITLES_17 = {
    "es": "Guía de Reflexión y Meditación",
    "en": "Reflection and Meditation Guide",
    "fr": "Guide de Réflexion et Méditation",
    "it": "Guida di Riflessione e Meditazione",
    "zh": "反思与冥想指南",
    "ar": "دليل التأمل والتفكر",
    "ru": "Руководство по размышлению и медитации",
    "vi": "Hướng dẫn Suy ngẫm và Thiền định",
    "ko": "성찰과 명상 가이드",
    "pt": "Guia de Reflexão e Meditação",
    "ja": "内省と瞑想のガイド"
}

import sys
sys.path.append(BASE_DIR)
import scripts.prepare_translations_14_17 as pt14
BODY_14 = pt14.BODY_14
BODY_15 = pt14.BODY_15
BODY_17 = pt14.BODY_17

# Load body 16 from build_full_chapter_16.py
import scripts.build_full_chapter_16 as bfc16
BODY_16 = bfc16.BODY_16

translations["14_glosario_cuantico.html"] = {"h1": TITLES_14, "body": BODY_14}
translations["15_musica_frecuencias.html"] = {"h1": TITLES_15, "body": BODY_15}
translations["16_sobre_el_autor.html"] = {"h1": TITLES_16, "body": BODY_16}
translations["17_guia_meditacion.html"] = {"h1": TITLES_17, "body": BODY_17}

with open(TRANSLATIONS_FILE, 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=4)

with open(SPANISH_CONTENT_FILE, 'w', encoding='utf-8') as f:
    json.dump(spanish_content, f, ensure_ascii=False, indent=4)

print("Updated translations.json and spanish_content.json with full native multilingual texts!")
