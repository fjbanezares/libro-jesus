import json
import os
import re

# Source files
TRANSLATIONS_FILE = '/Users/fjbanezares/libro sobre mi amigo Jesucristo/translations.json'
SPANISH_CONTENT_FILE = '/Users/fjbanezares/libro sobre mi amigo Jesucristo/spanish_content.json'
OUTPUT_DIR = '/Users/fjbanezares/libro sobre mi amigo Jesucristo/output/html/'

# Language mapping for class names
LANG_MAP = {
    'es': 'spanish',
    'en': 'english',
    'fr': 'french',
    'it': 'italian',
    'zh': 'chinese',
    'ar': 'arabic',
    'ru': 'russian',
    'vi': 'vietnamese'
}

LANGUAGES = {
    'es': 'Español',
    'en': 'English',
    'fr': 'Français',
    'it': 'Italiano',
    'zh': '中文',
    'ar': 'العربية',
    'ru': 'Русский',
    'vi': 'Tiếng Việt'
}

FLAGS = {
    'es': '🇪🇸',
    'en': '🇺🇸',
    'fr': '🇫🇷',
    'it': '🇮🇹',
    'zh': '🇨🇳',
    'ar': '🇸🇦',
    'ru': '🇷🇺',
    'vi': '🇻🇳'
}

CHAPTERS = [
    ("00_introduccion.html", "Introducción: Entre la Partícula y la Vibración"),
    ("index.html", "Capítulo 1: El Encuentro en Madrid"),
    ("02_capitulo.html", "Capítulo 2: Paseo por Las Rozas"),
    ("03_capitulo.html", "Capítulo 3: La Vibración y el Silencio"),
    ("04_capitulo.html", "Capítulo 4: Colmenarejo y la Naturaleza"),
    ("05_capitulo.html", "Capítulo 5: El Padre Nuestro (Parte 1: Padre)"),
    ("06_capitulo.html", "Capítulo 6: El Padre Nuestro (Parte 2: Cielo)"),
    ("07_capitulo.html", "Capítulo 7: El Pan de Cada Día"),
    ("08_capitulo.html", "Capítulo 8: Perdón y Deudas"),
    ("09_capitulo.html", "Capítulo 9: No nos dejes caer en tentación (Vibrar Alto)"),
    ("10_capitulo.html", "Capítulo 10: Líbranos del mal (Protección de Bajas Vibraciones)"),
    ("11_capitulo.html", "Capítulo 11: El Reino, el Poder y la Gloria"),
    ("12_epilogo.html", "Epílogo: Aventuras Finales y Despedida"),
    ("13_apendice_poema.html", "Apéndice: Poema de Navidad")
]

CSS_STYLES = """
    <style>
        :root {
            --primary: #FF6B6B;
            /* Vibrant Coral */
            --secondary: #4ECDC4;
            /* Vibrant Teal */
            --bg: #F7FFF7;
            /* Off-white */
            --text: #292F36;
            /* Dark Slate */
            --accent: #FFE66D;
            /* Vibrant Yellow */
            --sidebar-width: 250px;
            --header-height: 60px;
        }

        body {
            font-family: 'Inter', sans-serif;
            line-height: 1.8;
            color: var(--text);
            background-color: var(--bg);
            margin: 0;
            padding: 0;
            display: flex;
            min-height: 100vh;
        }

        /* Mobile Header */
        #mobile-header {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: var(--header-height);
            background: white;
            padding: 0 1.5rem;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            z-index: 1000;
        }

        #mobile-header h1 {
            font-size: 1.2rem;
            margin: 0;
            color: var(--primary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .menu-toggle {
            background: none;
            border: none;
            color: var(--primary);
            font-size: 1.8rem;
            cursor: pointer;
            padding: 0;
            display: flex;
            align-items: center;
        }

        /* Sidebar Navigation */
        #sidebar {
            width: var(--sidebar-width);
            background: linear-gradient(180deg, var(--primary), var(--secondary));
            color: white;
            padding: 2rem 1rem;
            position: fixed;
            height: 100vh;
            overflow-y: auto;
            box-shadow: 4px 0 10px rgba(0, 0, 0, 0.1);
            z-index: 1001;
            transition: transform 0.3s ease;
        }

        #sidebar h2 {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            color: white;
            text-align: center;
            border-bottom: 2px solid rgba(255, 255, 255, 0.2);
            padding-bottom: 1rem;
        }

        #sidebar nav ul {
            list-style: none;
            padding: 0;
            padding-bottom: 5rem;
            /* Extra space for the last items */
        }

        #sidebar nav li {
            margin-bottom: 0.5rem;
        }

        #sidebar nav a {
            display: block;
            color: rgba(255, 255, 255, 0.9);
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            transition: background 0.3s;
            font-size: 0.95rem;
        }

        #sidebar nav a:hover,
        #sidebar nav a.active {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            font-weight: bold;
        }

        /* Main Content */
        #content-wrapper {
            margin-left: var(--sidebar-width);
            width: calc(100% - var(--sidebar-width));
            padding: 2.5rem;
            display: flex;
            justify-content: center;
            min-height: 100vh;
            box-sizing: border-box;
        }

        main {
            max-width: 800px;
            width: 100%;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        .chapter-image {
            width: 100%;
            height: 350px;
            object-fit: cover;
            display: block;
        }

        .content-body {
            padding: 3rem;
            flex-grow: 1;
        }

        h1 {
            margin-top: 0;
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 1.5rem;
        }

        h2,
        h3 {
            color: var(--secondary);
            margin-top: 2rem;
        }

        p {
            margin-bottom: 1.5rem;
            font-size: 1.15rem;
        }

        .vibrar-alto {
            background-color: var(--accent);
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-weight: bold;
        }

        footer {
            text-align: center;
            padding: 2rem;
            color: #666;
            font-size: 0.9rem;
            border-top: 1px solid #eee;
            margin-top: auto;
        }

        /* Overlay for mobile */
        #overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.5);
            z-index: 1000;
        }

        /* Responsive */
        @media (max-width: 1024px) {
            #mobile-header {
                display: flex;
            }

            #sidebar {
                transform: translateX(-100%);
            }

            #sidebar.open {
                transform: translateX(0);
            }

            #sidebar.open+#overlay {
                display: block;
            }

            #content-wrapper {
                margin-left: 0;
                width: 100%;
                padding: 1rem;
                padding-top: calc(var(--header-height) + 1rem);
            }

            .content-body {
                padding: 2rem;
            }

            h1 {
                font-size: 2rem;
            }
        }

        @media (max-width: 768px) {
            .chapter-image {
                height: 250px;
            }

            .content-body {
                padding: 1.5rem;
            }
        }

        .image-container-footer {
            margin-top: 3rem;
            padding: 0 3rem 3rem;
            text-align: center;
        }

        @media (max-width: 768px) {
            .image-container-footer {
                padding: 0 1.5rem 2rem;
            }
        }

        .footer-image {
            width: 100%;
            max-width: 600px;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        /* Language display logic */
        .language {
            display: none;
        }
        .language.spanish {
            display: block;
        }
    </style>
"""

def generate_multilingual_html(filename, translations, spanish_content):
    title_text = spanish_content.get('title', 'Mi amigo Jesucristo')
    
    # Header Styles
    html = f"""<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_text} | Mi amigo Jesucristo</title>
    <link rel="stylesheet" href="base.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
{CSS_STYLES}
</head>

<body>
    <div class="language-switcher-container">
        <select id="language-select">
            <option value="spanish">Español 🇪🇸</option>
            <option value="english">English 🇺🇸</option>
            <option value="french">Français 🇫🇷</option>
            <option value="italian">Italiano 🇮🇹</option>
            <option value="chinese">中文 🇨🇳</option>
            <option value="arabic">العربية 🇸🇦</option>
            <option value="russian">Русский 🇷🇺</option>
            <option value="vietnamese">Tiếng Việt 🇻🇳</option>
        </select>
    </div>

    <header id="mobile-header">
"""
    # Mobile Header H1s
    for lang_code, lang_name in LANG_MAP.items():
        h1_text = translations.get('h1', {}).get(lang_code, title_text)
        html += f'        <div class="{lang_name} language">\n            <h1>{h1_text}</h1>\n        </div>\n'
    
    html += """        <button class="menu-toggle" id="menu-open">☰</button>
    </header>

    <aside id="sidebar">
"""
    # Sidebar Navigation for each language
    sidebar_translations = {
        'es': "Mi amigo Jesucristo",
        'en': "My friend Jesus Christ",
        'fr': "Mon ami Jésus-Christ",
        'it': "Il mio amico Gesù Cristo",
        'zh': "我的朋友耶稣基督",
        'ar': "صديقي يسوع المسيح",
        'ru': "Мой друг Иисус Христос",
        'vi': "Người bạn Giê-su của tôi"
    }

    chapter_translations = {
        "00_introduccion.html": {
            "es": "Introducción: Entre la Partícula y la Vibración",
            "en": "Introduction: Between Particle and Vibration",
            "fr": "Introduction : Entre la particule et la vibration",
            "it": "Introduzione: Tra la particella e la vibrazione",
            "zh": "引言：粒子与振动之间",
            "ar": "مقدمة: بين الجسيم والاهتزاز",
            "ru": "Введение: Между частицей и вибрацией",
            "vi": "Giới thiệu: Giữa Hạt và Rung động"
        },
        "index.html": {
            "es": "Capítulo 1: El Encuentro en Madrid",
            "en": "Chapter 1: The Encounter in Madrid",
            "fr": "Chapitre 1 : La rencontre à Madrid",
            "it": "Capitolo 1: L'incontro a Madrid",
            "zh": "第 1 章：马德里相遇",
            "ar": "الفصل الأول: اللقاء في مدريد",
            "ru": "Глава 1: Встреча в Мадриде",
            "vi": "Chương 1: Cuộc gặp gỡ tại Madrid"
        },
        "02_capitulo.html": {
            "es": "Capítulo 2: Paseo por Las Rozas",
            "en": "Chapter 2: A Walk through Las Rozas",
            "fr": "Chapitre 2 : Promenade à Las Rozas",
            "it": "Capitolo 2: Passeggiata per Las Rozas",
            "zh": "第 2 章：拉斯罗萨斯散步",
            "ar": "الفصل الثاني: نزهة في لاس روزاس",
            "ru": "Глава 2: Прогулка по Лас-Росас",
            "vi": "Chương 2: Đi dạo qua Las Rozas"
        },
        "03_capitulo.html": {
            "es": "Capítulo 3: La Vibración y el Silencio",
            "en": "Chapter 3: Vibration and Silence",
            "fr": "Chapitre 3 : La vibration et le silence",
            "it": "Capitolo 3: La vibrazione e il silenzio",
            "zh": "第 3 章：振动与静默",
            "ar": "الفصل الثالث: الاهتزاز والصمت",
            "ru": "Глава 3: Вибрация и тишина",
            "vi": "Chương 3: Rung động và Im lặng"
        },
        "04_capitulo.html": {
            "es": "Capítulo 4: Colmenarejo y la Naturaleza",
            "en": "Chapter 4: Colmenarejo and Nature",
            "fr": "Chapitre 4 : Colmenarejo et la nature",
            "it": "Capitolo 4: Colmenarejo e la natura",
            "zh": "第 4 章：科尔梅纳雷霍与自然",
            "ar": "الفصل الرابع: كولميناريجو والطبيعة",
            "ru": "Глава 4: Кольменарехо и природа",
            "vi": "Chương 4: Colmenarejo và Thiên nhiên"
        },
        "05_capitulo.html": {
            "es": "Capítulo 5: El Padre Nuestro (Parte 1: Padre)",
            "en": "Chapter 5: The Lord's Prayer (Part 1: Father)",
            "fr": "Chapitre 5 : Le Notre Père (Partie 1 : Père)",
            "it": "Capitolo 5: Il Padre Nostro (Parte 1: Padre)",
            "zh": "第 5 章：主祷文（第一部分：父亲）",
            "ar": "الفصل الخامس: أبانا الذي في السماوات (الجزء الأول: الآب)",
            "ru": "Глава 5: Отче наш (Часть 1: Отче)",
            "vi": "Chương 5: Kinh Lạy Cha (Phần 1: Cha)"
        },
        "06_capitulo.html": {
            "es": "Capítulo 6: El Padre Nuestro (Parte 2: Cielo)",
            "en": "Chapter 6: The Lord's Prayer (Part 2: Heaven)",
            "fr": "Chapitre 6 : Le Notre Père (Partie 2 : Ciel)",
            "it": "Capitolo 6: Il Padre Nostro (Parte 2: Cielo)",
            "zh": "第 6 章：主祷文（第二部分：天空）",
            "ar": "الفصل السادس: أبانا الذي في السماوات (الجزء الثاني: السماء)",
            "ru": "Глава 6: Отче наш (Часть 2: Небо)",
            "vi": "Chương 6: Kinh Lạy Cha (Phần 2: Trời)"
        },
        "07_capitulo.html": {
            "es": "Capítulo 7: El Pan de Cada Día",
            "en": "Chapter 7: Our Daily Bread",
            "fr": "Chapitre 7 : Le pain de chaque jour",
            "it": "Capitolo 7: Il pane quotidiano",
            "zh": "第 7 章：日用的饮食",
            "ar": "الفصل السابع: خبزنا كفافنا",
            "ru": "Глава 7: Хлеб наш насущный",
            "vi": "Chương 7: Lương thực hằng ngày"
        },
        "08_capitulo.html": {
            "es": "Capítulo 8: Perdón y Deudas",
            "en": "Chapter 8: Forgiveness and Debts",
            "fr": "Chapitre 8 : Pardon et dettes",
            "it": "Capitolo 8: Perdono e debiti",
            "zh": "第 8 章：宽恕与债务",
            "ar": "الفصل الثامن: المغفرة والديون",
            "ru": "Глава 8: Прощение и долги",
            "vi": "Chương 8: Tha thứ và Nợ nần"
        },
        "09_capitulo.html": {
            "es": "Capítulo 9: No nos dejes caer en tentación (Vibrar Alto)",
            "en": "Chapter 9: Lead us not into temptation (Vibrate High)",
            "fr": "Chapitre 9 : Ne nous laisse pas succomber à la tentation (Vibrer haut)",
            "it": "Capitolo 9: Non ci indurre in tentazione (Vibrare alto)",
            "zh": "第 9 章：不叫我们遇见试探（高频振动）",
            "ar": "الفصل التاسع: لا تدخلنا في تجربة (الاهتزاز العالي)",
            "ru": "Глава 9: Не введи нас в искушение (Вибрировать высоко)",
            "vi": "Chương 9: Chớ để chúng con sa chước cám dỗ (Rung động cao)"
        },
        "10_capitulo.html": {
            "es": "Capítulo 10: Líbranos del mal (Protección de Bajas Vibraciones)",
            "en": "Chapter 10: Deliver us from evil (Protection from Low Vibrations)",
            "fr": "Chapitre 10 : Délivre-nous du mal (Protection contre les vibrations basses)",
            "it": "Capitolo 10: Liberaci dal male (Protezione dalle vibrazioni basse)",
            "zh": "第 10 章：救我们脱离凶恶（防止低频振动）",
            "ar": "الفصل العاشر: نجنا من الشرير (الحماية من الاهتزازات المنخفضة)",
            "ru": "Глава 10: Избавь нас от лукавого (Защита от низких вибраций)",
            "vi": "Chương 10: Cứu chúng con cho khỏi sự dữ (Bảo vệ khỏi rung động thấp)"
        },
        "11_capitulo.html": {
            "es": "Capítulo 11: El Reino, el Poder y la Gloria",
            "en": "Chapter 11: The Kingdom, the Power and the Glory",
            "fr": "Chapitre 11 : Le Règne, la Puissance et la Gloire",
            "it": "Capitolo 11: Il Regno, il Potere e la Gloria",
            "zh": "第 11 章：国度、权柄、荣耀",
            "ar": "الفصل الحادي عشر: الملك والقدرة والمجد",
            "ru": "Глава 11: Царство, Сила и Слава",
            "vi": "Chương 11: Vương quốc, Quyền năng và Vinh quang"
        },
        "12_epilogo.html": {
            "es": "Epílogo: Aventuras Finales y Despedida",
            "en": "Epilogue: Final Adventures and Farewell",
            "fr": "Épilogue : Aventures finales et adieu",
            "it": "Epilogo: Avventure finali e addio",
            "zh": "结语：最后的冒险与告别",
            "ar": "الخاتمة: المغامرات الأخيرة والوداع",
            "ru": "Эпилог: Последние приключения и прощание",
            "vi": "Lời kết: Những cuộc phiêu lưu cuối cùng và Lời chào tạm biệt"
        },
        "13_apendice_poema.html": {
            "es": "Apéndice: Poema de Navidad",
            "en": "Appendix: Christmas Poem",
            "fr": "Appendice : Poème de Noël",
            "it": "Appendice: Poema di Natale",
            "zh": "附录：圣诞诗",
            "ar": "ملحق: قصيدة عيد الميلاد",
            "ru": "Приложение: Рождественское стихотворение",
            "vi": "Phụ lục: Bài thơ Giáng sinh"
        }
    }

    for lang_code, lang_name in LANG_MAP.items():
        sidebar_title = sidebar_translations.get(lang_code, "Mi amigo Jesucristo")
        close_id = f"menu-close-{lang_code}"
        
        html += f'        <div class="{lang_name} language">\n'
        html += f'            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">\n'
        html += f'                <h2>{sidebar_title}</h2>\n'
        html += f'                <button class="menu-toggle" id="{close_id}" style="color: white; display: none;">✕</button>\n'
        html += f'            </div>\n'
        html += f'            <nav>\n                <ul>\n'
        
        for ch_file, ch_desc in CHAPTERS:
            active_class = ' class="active"' if ch_file == filename else ''
            # Use specific translation for each chapter name in the sidebar
            ch_name_translated = chapter_translations.get(ch_file, {}).get(lang_code, ch_desc)
            html += f'                    <li><a href="{ch_file}"{active_class}>{ch_name_translated}</a>\n                    </li>\n'
            
        html += '                </ul>\n            </nav>\n        </div>\n'

    html += """    </aside>

    <div id="overlay"></div>

    <div id="content-wrapper">
        <main>
"""
    # Extract images from original text
    body_es = spanish_content.get('body', '')
    
    # Robust image extraction
    def find_img_with_class(content, cls):
        m = re.search(rf'<img[^>]+class=["\'][^"\']*{cls}[^"\']*["\'][^>]+src=["\']([^"\']+)["\']', content)
        if m: return m.group(1)
        m = re.search(rf'<img[^>]+src=["\']([^"\']+)["\'][^>]+class=["\'][^"\']*{cls}[^"\']*["\']', content)
        if m: return m.group(1)
        return None

    chapter_img = find_img_with_class(body_es, "chapter-image")
    
    footer_img = find_img_with_class(body_es, "footer-image")

    # If only one found, use it for both to match reference chapters
    if chapter_img and not footer_img:
        footer_img = chapter_img
    elif footer_img and not chapter_img:
        chapter_img = footer_img
    
    if not chapter_img:
        chapter_img = "images/default.png"
    

    # Clean body_es to remove any direct image tags or containers that might cause duplication
    body_es_clean = re.sub(r'<div class="image-container-footer">.*?</div>', '', body_es, flags=re.DOTALL)
    body_es_clean = re.sub(r'<div class="image-container-footer".*?>', '', body_es_clean)
    body_es_clean = re.sub(r'<img[^>]*class="footer-image"[^>]*>', '', body_es_clean)
    body_es_clean = re.sub(r'<img[^>]*class="chapter-image"[^>]*>', '', body_es_clean)

    html += f'            <img src="{chapter_img}" alt="Ilustración del capítulo" class="chapter-image">\n'
    html += '            <div class="content-body">\n'

    # Body Content for each language
    for lang_code, lang_name in LANG_MAP.items():
        h1_text = translations.get('h1', {}).get(lang_code, title_text)
        body_text = translations.get('body', {}).get(lang_code, body_es_clean)
        
        # If body_text comes from translations.json, it might already be clean or have its own structure
        if body_text:
            body_text = re.sub(r'<img[^>]*class="chapter-image"[^>]*>', '', body_text)
            body_text = re.sub(r'<div class="image-container-footer">.*?</div>', '', body_text, flags=re.DOTALL)
            body_text = re.sub(r'<div class="image-container-footer".*?>', '', body_text)
            body_text = re.sub(r'<img[^>]*class="footer-image"[^>]*>', '', body_text)
        else:
            body_text = body_es_clean
            
        html += f'                <div class="{lang_name} language">\n'
        html += f'                    <h1>{h1_text}</h1>\n'
        
        # Special case: Credit line for the poem
        if filename == "13_apendice_poema.html":
            poem_credits = {
                'es': "con María Paz Arés Osset, la Artist",
                'en': "with María Paz Arés Osset, the Artist",
                'fr': "avec María Paz Arés Osset, l'Artiste",
                'it': "con María Paz Arés Osset, l'Artista",
                'zh': "与艺术家 María Paz Arés Osset 合作",
                'ar': "مع ماريا باز أريس أوسيت، الفنانة",
                'ru': "с Марией Пас Арес Оссет, художницей",
                'vi': "với María Paz Arés Osset, Nghệ sĩ"
            }
            credit_text = poem_credits.get(lang_code, poem_credits['es'])
            html += f'                    <p style="text-align: center; font-style: italic; margin-top: -10px; margin-bottom: 30px; color: #777;">{credit_text}</p>\n'
            
        html += f'                    {body_text}\n'
        html += '                </div>\n'

    if footer_img:
        html += f'                <div class="image-container-footer"><img src="{footer_img}" alt="Ilustración del capítulo" class="footer-image"></div>\n'
    
    # Special addition for Introduction as requested by user
    if filename == "00_introduccion.html":
        html += f'                <div class="image-container-footer" style="margin-top: 1rem;"><img src="images/glimpse_of_light.png" alt="Mi Amigo Jesucristo - A Glimpse of Light" class="footer-image"></div>\n'
    
    html += """            </div>
            <footer>
                <div class="spanish language"><p>Escrito con amor y alta vibración.</p></div>
                <div class="english language"><p>Written with love and high vibration.</p></div>
                <div class="french language"><p>Écrit avec amour et haute vibration.</p></div>
                <div class="italian language"><p>Scritto con amore e alta vibrazione.</p></div>
                <div class="chinese language"><p>用爱与高频振动谱写。</p></div>
                <div class="arabic language"><p>كتب بكل حب واهتزاز عالٍ.</p></div>
                <div class="russian language"><p>Написано с любовью и высокой вибрацией.</p></div>
                <div class="vietnamese language"><p>Được viết bằng tình yêu và rung động cao.</p></div>
            </footer>
        </main>
    </div>

    <script src="base.js"></script>
    <script>
        const sidebar = document.getElementById('sidebar');
        const overlay = document.getElementById('overlay');
        const btnOpen = document.getElementById('menu-open');
        const btnsClose = document.querySelectorAll('.menu-toggle[id^="menu-close"]');

        function toggleMenu() {
            sidebar.classList.toggle('open');
            const isOpen = sidebar.classList.contains('open');
            if (window.innerWidth <= 1024) {
                btnsClose.forEach(btn => {
                    btn.style.display = isOpen ? 'block' : 'none';
                });
            }
        }

        btnOpen.addEventListener('click', toggleMenu);
        btnsClose.forEach(btn => {
            btn.addEventListener('click', toggleMenu);
        });
        overlay.addEventListener('click', toggleMenu);

        // Language selector logic to match index.html
        const langSelect = document.getElementById('language-select');
        langSelect.addEventListener('change', (e) => {
            if (window.setLanguage) {
                window.setLanguage(e.target.value);
            }
        });

        // Resize handler for button visibility
        window.addEventListener('resize', () => {
            if (window.innerWidth > 1024) {
                btnsClose.forEach(btn => {
                    btn.style.display = 'none';
                });
                sidebar.classList.remove('open');
            }
        });
    </script>
</body>

</html>
"""
    return html

def main():
    with open(TRANSLATIONS_FILE, 'r') as f:
        all_translations = json.load(f)
    
    with open(SPANISH_CONTENT_FILE, 'r') as f:
        all_spanish = json.load(f)

    # Process all chapters including intro and index
    targets = [
        "00_introduccion.html", "index.html",
        "02_capitulo.html", "03_capitulo.html", "04_capitulo.html", "05_capitulo.html",
        "06_capitulo.html", "07_capitulo.html", "08_capitulo.html", "09_capitulo.html",
        "10_capitulo.html", "11_capitulo.html", "12_epilogo.html", "13_apendice_poema.html"
    ]

    for filename in targets:
        if filename in all_translations and filename in all_spanish:
            print(f"Generating {filename}...")
            html = generate_multilingual_html(filename, all_translations[filename], all_spanish[filename])
            
            output_path = os.path.join(OUTPUT_DIR, filename)
            with open(output_path, 'w') as f:
                f.write(html)
        else:
            print(f"Skipping {filename} - missing data")

if __name__ == "__main__":
    main()
