import json
import os
import re

def rollout():
    with open('translations.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)

    # Sidebar template (we will replace [[ACTIVE_FILE]] with the current file name)
    # This sidebar is taken from index.html/00_introduccion.html logic
    sidebar_langs = {
        "es": {
            "title": "Mi amigo Jesucristo",
            "items": [
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
                ("10_capitulo.html", "Capítulo 10: Líbranos del mal (Protección de bajas vibraciones)"),
                ("11_capitulo.html", "Capítulo 11: El Reino, el Poder y la Gloria"),
                ("12_epilogo.html", "Epílogo: Aventuras Finales y Despedida"),
                ("13_apendice_poema.html", "Apéndice: Poema de Navidad")
            ]
        },
        "en": {
            "title": "My friend Jesus Christ",
            "items": [
                ("00_introduccion.html", "Introduction: Between Particle and Vibration"),
                ("index.html", "Chapter 1: The Encounter in Madrid"),
                ("02_capitulo.html", "Chapter 2: A Walk through Las Rozas"),
                ("03_capitulo.html", "Chapter 3: Vibration and Silence"),
                ("04_capitulo.html", "Chapter 4: Colmenarejo and Nature"),
                ("05_capitulo.html", "Chapter 5: The Lord's Prayer (Part 1: Father)"),
                ("06_capitulo.html", "Chapter 6: The Lord's Prayer (Part 2: Heaven)"),
                ("07_capitulo.html", "Chapter 7: Our Daily Bread"),
                ("08_capitulo.html", "Chapter 8: Forgiveness and Debts"),
                ("09_capitulo.html", "Chapter 9: Lead us not into temptation (Vibrate High)"),
                ("10_capitulo.html", "Chapter 10: Deliver us from evil (Protection from Low Vibrations)"),
                ("11_capitulo.html", "Chapter 11: The Kingdom, the Power and the Glory"),
                ("12_epilogo.html", "Epilogue: Final Adventures and Farewell"),
                ("13_apendice_poema.html", "Appendix: Christmas Poem")
            ]
        },
        "fr": {
            "title": "Mon ami Jésus-Christ",
            "items": [
                ("00_introduccion.html", "Introduction : Entre la particule et la vibration"),
                ("index.html", "Chapitre 1 : La rencontre à Madrid"),
                ("02_capitulo.html", "Chapitre 2 : Promenade à Las Rozas"),
                ("03_capitulo.html", "Chapitre 3 : La vibration et le silence"),
                ("04_capitulo.html", "Chapitre 4 : Colmenarejo et la nature"),
                ("05_capitulo.html", "Chapitre 5 : Le Notre Père (Partie 1 : Père)"),
                ("06_capitulo.html", "Chapitre 6 : Le Notre Père (Partie 2 : Ciel)"),
                ("07_capitulo.html", "Chapitre 7 : Le pain de chaque jour"),
                ("08_capitulo.html", "Chapitre 8 : Pardon et dettes"),
                ("09_capitulo.html", "Chapitre 9 : Ne nous laisse pas succomber à la tentation (Vibrer haut)"),
                ("10_capitulo.html", "Chapitre 10 : Délivre-nous du mal (Protection contre les vibrations basses)"),
                ("11_capitulo.html", "Chapitre 11 : Le Règne, la Puissance et la Gloire"),
                ("12_epilogo.html", "Épilogue : Aventures finales et adieu"),
                ("13_apendice_poema.html", "Appendice : Poème de Noël")
            ]
        },
        "it": {
            "title": "Il mio amico Gesù Cristo",
            "items": [
                ("00_introduccion.html", "Introduzione: Tra la particella e la vibrazione"),
                ("index.html", "Capitolo 1: L'incontro a Madrid"),
                ("02_capitulo.html", "Capitolo 2: Passeggiata per Las Rozas"),
                ("03_capitulo.html", "Capitolo 3: La vibrazione e il silenzio"),
                ("04_capitulo.html", "Capitolo 4: Colmenarejo e la natura"),
                ("05_capitulo.html", "Capitolo 5: Il Padre Nostro (Parte 1: Padre)"),
                ("06_capitulo.html", "Capitolo 6: Il Padre Nostro (Parte 2: Cielo)"),
                ("07_capitulo.html", "Capitolo 7: Il pane quotidiano"),
                ("08_capitulo.html", "Capitolo 8: Perdono e debiti"),
                ("09_capitulo.html", "Capitolo 9: Non ci indurre in tentazione (Vibrare alto)"),
                ("10_capitulo.html", "Capitolo 10: Liberaci dal male (Protezione dalle vibrazioni basse)"),
                ("11_capitulo.html", "Capitolo 11: Il Regno, il Potere e la Gloria"),
                ("12_epilogo.html", "Epilogo: Avventure finali e addio"),
                ("13_apendice_poema.html", "Appendice: Poema di Natale")
            ]
        },
        "zh": {
            "title": "我的朋友耶稣基督",
            "items": [
                ("00_introduccion.html", "引言：粒子与振动之间"),
                ("index.html", "第 1 章：马德里相遇"),
                ("02_capitulo.html", "第 2 章：拉斯罗萨斯散步"),
                ("03_capitulo.html", "第 3 章：振动与静默"),
                ("04_capitulo.html", "第 4 章：科尔梅纳雷霍与自然"),
                ("05_capitulo.html", "第 5 章：主祷文（第一部分：父亲）"),
                ("06_capitulo.html", "第 6 章：主祷文（第二部分：天上）"),
                ("07_capitulo.html", "第 7 章：我们日用的饮食"),
                ("08_capitulo.html", "第 8 章：宽恕与债务"),
                ("09_capitulo.html", "第 9 章：不叫我们遇见试探（高频振动）"),
                ("10_capitulo.html", "第 10 章：救我们脱离凶恶（远离低频振动）"),
                ("11_capitulo.html", "第 11 章：国度、权柄、荣耀"),
                ("12_epilogo.html", "结语：最后的冒险与告别"),
                ("13_apendice_poema.html", "附录：圣诞诗歌")
            ]
        },
        "ar": {
            "title": "صديقي يسوع المسيح",
            "items": [
                ("00_introduccion.html", "مقدمة: بين الجسيم والاهتزاز"),
                ("index.html", "الفصل الأول: اللقاء في مدريد"),
                ("02_capitulo.html", "الفصل الثاني: نزهة في لاس روزاس"),
                ("03_capitulo.html", "الفصل الثالث: الاهتزاز والصمت"),
                ("04_capitulo.html", "الفصل الرابع: كولميناريجو والطبيعة"),
                ("05_capitulo.html", "الفصل الخامس: أبانا الذي في السماوات (الجزء الأول: الآب)"),
                ("06_capitulo.html", "الفصل السادس: أبانا الذي في السماوات (الجزء الثاني: السماء)"),
                ("07_capitulo.html", "الفصل السابع: خبزنا كفافنا"),
                ("08_capitulo.html", "الفصل الثامن: المغفرة والديون"),
                ("09_capitulo.html", "الفصل التاسع: لا تدخلنا في تجربة (الاهتزاز العالي)"),
                ("10_capitulo.html", "الفصل العاشر: نجنا من الشرير (الحماية من الاهتزازات المنخفضة)"),
                ("11_capitulo.html", "الفصل الحادي عشر: الملك والقدرة والمجد"),
                ("12_epilogo.html", "الخاتمة: المغامرات الأخيرة والوداع"),
                ("13_apendice_poema.html", "ملحق: قصيدة عيد الميلاد")
            ]
        },
        "ru": {
            "title": "Мой друг Иисус Христос",
            "items": [
                ("00_introduccion.html", "Введение: Между частицей и вибрацией"),
                ("index.html", "Глава 1: Встреча в Мадриде"),
                ("02_capitulo.html", "Глава 2: Прогулка по Лас-Росас"),
                ("03_capitulo.html", "Глава 3: Вибрация и тишина"),
                ("04_capitulo.html", "Глава 4: Кольменарехо и природа"),
                ("05_capitulo.html", "Глава 5: Отче наш (Часть 1: Отче)"),
                ("06_capitulo.html", "Глава 6: Отче наш (Часть 2: Небо)"),
                ("07_capitulo.html", "Глава 7: Хлеб наш насущный"),
                ("08_capitulo.html", "Глава 8: Прощение и долги"),
                ("09_capitulo.html", "Глава 9: Не введи нас в искушение (Вибрировать высоко)"),
                ("10_capitulo.html", "Глава 10: Избавь нас от лукавого (Защита от низких вибраций)"),
                ("11_capitulo.html", "Глава 11: Царство, Сила и Слава"),
                ("12_epilogo.html", "Эпилог: Последние приключения и прощание"),
                ("13_apendice_poema.html", "Приложение: Рождественское стихотворение")
            ]
        },
        "vi": {
            "title": "Người bạn Giê-su của tôi",
            "items": [
                ("00_introduccion.html", "Giới thiệu: Giữa Hạt và Rung động"),
                ("index.html", "Chương 1: Cuộc gặp gỡ tại Madrid"),
                ("02_capitulo.html", "Chương 2: Đi dạo qua Las Rozas"),
                ("03_capitulo.html", "Chương 3: Rung động và Im lặng"),
                ("04_capitulo.html", "Chương 4: Colmenarejo và Thiên nhiên"),
                ("05_capitulo.html", "Chương 5: Kinh Lạy Cha (Phần 1: Cha)"),
                ("06_capitulo.html", "Chương 6: Kinh Lạy Cha (Phần 2: Trời)"),
                ("07_capitulo.html", "Chương 7: Lương thực hằng ngày"),
                ("08_capitulo.html", "Chương 8: Tha thứ và Nợ nần"),
                ("09_capitulo.html", "Chương 9: Chớ để chúng con sa chước cám dỗ (Rung động cao)"),
                ("10_capitulo.html", "Chương 10: Cứu chúng con cho khỏi sự dữ (Bảo vệ khỏi rung động thấp)"),
                ("11_capitulo.html", "Chương 11: Vương quốc, Quyền năng và Vinh quang"),
                ("12_epilogo.html", "Lời kết: Những cuộc phiêu lưu cuối cùng và Lời chào tạm biệt"),
                ("13_apendice_poema.html", "Phụ lục: Bài thơ Giáng sinh")
            ]
        },
        "ko": {
            "title": "나의 친구 예수 그리스도",
            "items": [
                ("00_introduccion.html", "서문: 입자와 진동 사이에서"),
                ("index.html", "제1장: 마드리드에서의 만남"),
                ("02_capitulo.html", "제2장: 라스 로사스 산책"),
                ("03_capitulo.html", "제3장: 진동과 침묵"),
                ("04_capitulo.html", "제4장: 콜메나레호와 자연"),
                ("05_capitulo.html", "제5장: 주기도문 (제1부: 아버지)"),
                ("06_capitulo.html", "제6장: 주기도문 (제2부: 하늘)"),
                ("07_capitulo.html", "제7장: 우리에게 일용할 양식"),
                ("08_capitulo.html", "제8장: 용서와 빚"),
                ("09_capitulo.html", "제9장: 우리를 시험에 들게 하지 마시옵고 (높은 진동)"),
                ("10_capitulo.html", "제10장: 다만 악에서 구하시옵소서 (낮은 진동으로부터의 보호)"),
                ("11_capitulo.html", "제11장: 나라와 권능과 영광"),
                ("12_epilogo.html", "에필로그: 마지막 모험과 작별"),
                ("13_apendice_poema.html", "부록: 크리스마스 시")
            ]
        }
    }

    def generate_sidebar(active_file):
        sidebar_html = '<aside id="sidebar">\n'
        for lang, data in sidebar_langs.items():
            lang_class = "spanish" if lang == "es" else {
                "en": "english", "fr": "french", "it": "italian", "zh": "chinese", "ar": "arabic", "ru": "russian", "vi": "vietnamese", "ko": "korean"
            }[lang]
            sidebar_html += f'    <div class="{lang_class} language">\n'
            sidebar_html += f'        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">\n'
            sidebar_html += f'            <h2>{data["title"]}</h2>\n'
            sidebar_html += f'            <button class="menu-toggle" id="menu-close-{lang}" style="color: white; display: none;">✕</button>\n'
            sidebar_html += f'        </div>\n'
            sidebar_html += '        <nav>\n            <ul>\n'
            for href, text in data["items"]:
                active_class = ' class="active"' if href == active_file else ''
                sidebar_html += f'                <li><a href="{href}"{active_class}>{text}</a></li>\n'
            sidebar_html += '            </ul>\n        </nav>\n    </div>\n'
        sidebar_html += '</aside>'
        return sidebar_html

    def generate_header(chapter_id, trans):
        header_html = '<header id="mobile-header">\n'
        for lang, text in trans["h1"].items():
            lang_class = "spanish" if lang == "es" else {
                "en": "english", "fr": "french", "it": "italian", "zh": "chinese", "ar": "arabic", "ru": "russian", "vi": "vietnamese", "ko": "korean"
            }[lang]
            header_html += f'    <div class="{lang_class} language">\n        <h1>{text}</h1>\n    </div>\n'
        header_html += '    <button class="menu-toggle" id="menu-open">☰</button>\n'
        header_html += '</header>'
        return header_html

    lang_switcher = """
    <div id="language-select">
        <div class="lang-option" onclick="setLanguage('es')"><span class="flag-icon">🇪🇸</span> Español</div>
        <div class="lang-option" onclick="setLanguage('en')"><span class="flag-icon">🇺🇸</span> English</div>
        <div class="lang-option" onclick="setLanguage('vi')"><span class="flag-icon">🇻🇳</span> Tiếng Việt</div>
        <div class="lang-option" onclick="setLanguage('fr')"><span class="flag-icon">🇫🇷</span> Français</div>
        <div class="lang-option" onclick="setLanguage('it')"><span class="flag-icon">🇮🇹</span> Italiano</div>
        <div class="lang-option" onclick="setLanguage('zh')"><span class="flag-icon">🇨🇳</span> 中文</div>
        <div class="lang-option" onclick="setLanguage('ar')"><span class="flag-icon">🇸🇦</span> العربية</div>
        <div class="lang-option" onclick="setLanguage('ru')"><span class="flag-icon">🇷🇺</span> Русский</div>
        <div class="lang-option" onclick="setLanguage('ko')"><span class="flag-icon">🇰🇷</span> 한국어</div>
    </div>
    """

    for filename in os.listdir('output/html'):
        if filename in translations:
            print(f"Processing {filename}...")
            filepath = os.path.join('output/html', filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. Update Title based on translation
            trans = translations[filename]
            title_es = trans["title"]["es"]
            content = re.sub(r'<title>.*?</title>', f'<title>{title_es} | Mi amigo Jesucristo</title>', content)

            # 2. Add base.css
            if 'base.css' not in content:
                content = content.replace('</head>', '    <link rel="stylesheet" href="base.css">\n</head>')

            # 3. Replace mobile header
            content = re.sub(r'<header id="mobile-header">.*?</header>', generate_header(filename, trans), content, flags=re.DOTALL)

            # 4. Replace sidebar
            content = re.sub(r'<aside id="sidebar">.*?</aside>', generate_sidebar(filename), content, flags=re.DOTALL)

            # 5. Insert Language Switcher after mobile header
            if 'language-select' not in content:
                content = content.replace('</header>', '</header>\n' + lang_switcher)

            # 6. Transform Body Content
            # Find the main content body
            body_match = re.search(r'<div class="content-body">(.*?)<div class="image-container-footer">', content, re.DOTALL)
            if body_match:
                original_body = body_match.group(1).strip()
                # Remove the original <h1>Capítulo...</h1> if it exists inside
                original_body = re.sub(r'<h1>.*?</h1>', '', original_body, flags=re.DOTALL).strip()
                
                new_body_content = ""
                for lang in ["es", "en", "vi", "fr", "it", "zh", "ar", "ru", "ko"]:
                    lang_class = "spanish" if lang == "es" else {
                        "en": "english", "fr": "french", "it": "italian", "zh": "chinese", "ar": "arabic", "ru": "russian", "vi": "vietnamese", "ko": "korean"
                    }[lang]
                    h1_text = trans["h1"].get(lang, trans["h1"]["es"])
                    body_text = trans["body"].get(lang, original_body if lang == "es" else "")
                    
                    new_body_content += f'                <div class="{lang_class} language">\n'
                    new_body_content += f'                    <h1>{h1_text}</h1>\n'
                    new_body_content += f'                    {body_text}\n'
                    new_body_content += f'                </div>\n'
                
                content = content.replace(body_match.group(0), f'<div class="content-body">\n{new_body_content}                <div class="image-container-footer">')

            # 7. Add base.js and clean up old script
            content = re.sub(r'<script>.*?</script>', '<script src="base.js"></script>', content, flags=re.DOTALL)

            # 8. Set HTML lang and dir dynamically? No, the base.js handles the classes.
            # But the root html tag should probably be generic or just stay 'es'.
            content = content.replace('<html lang="es">', '<html>')

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

    print("Rollout complete.")

if __name__ == "__main__":
    rollout()
