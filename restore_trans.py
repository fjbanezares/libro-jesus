import json
import os
import re

def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def read_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def extract_body_from_html_snippet(html_content):
    # Determine the language based on class or content, but here we just want the inner HTML
    # existing txt files have <div class="lang">...</div>
    # We want content inside the div, and specifically paragraphs.
    # Actually translate_all_chapters expects 'body' content.
    # If the txt file has h1, h2, p, we should keep them?
    # translate_all_chapters puts h1 separately.
    # So we should strip h1.
    
    # Remove h1
    content = re.sub(r'<h1>.*?</h1>', '', html_content, flags=re.DOTALL)
    # Remove wrapper div if present
    content = re.sub(r'<div class="[^"]*">', '', content)
    content = re.sub(r'</div>\s*$', '', content)
    return content.strip()

def main():
    translations = load_json('translations.json')
    
    # 1. Restore 00_introduccion.html
    print("Restoring Introduction...")
    intro_langs = {
        'en': 'english_intro.txt',
        'fr': 'french_intro.txt',
        'it': 'italian_intro.txt',
        'ru': 'russian_intro.txt',
        'ar': 'arabic_intro.txt',
        'es': 'spanish_intro.txt'
    }
    
    if "00_introduccion.html" not in translations:
        translations["00_introduccion.html"] = {"title": {}, "h1": {}, "body": {}}

    titles_intro = {
        "es": "Introducción: Entre la Partícula y la Vibración",
        "en": "Introduction: Between Particle and Vibration",
        "fr": "Introduction : Entre la particule et la vibration",
        "it": "Introduzione: Tra la particella e la vibrazione",
        "ru": "Введение: Между частицей и вибрацией",
        "ar": "مقدمة: بين الجسيم والاهتزاز",
        "zh": "引言：粒子与振动之间",
        "vi": "Giới thiệu: Giữa Hạt và Rung động"
    }

    # Vietnamese and Chinese might be missing from txt files?
    # I'll check if they are in the JSON already (from my ko add).
    # If not, I'll need to provide them. 
    # Current JSON has 'ko'.
    
    for lang, filename in intro_langs.items():
        content = read_file(filename)
        if content:
            # Extract h1 if needed, but we have titles dict
            # Just get body
            body = extract_body_from_html_snippet(content)
            translations["00_introduccion.html"]["body"][lang] = body
            translations["00_introduccion.html"]["h1"][lang] = titles_intro.get(lang, "")
            translations["00_introduccion.html"]["title"][lang] = titles_intro.get(lang, "")

    # manually add zh and vi for intro if missing (I'll translate them if I have to, or check if they were there)
    # Actually, previous session summary didn't mention zh/vi txt files.
    # I will provide translations for zh and vi for Intro to be safe.
    
    translations["00_introduccion.html"]["title"]["zh"] = "引言：粒子与振动之间"
    translations["00_introduccion.html"]["h1"]["zh"] = "引言：粒子与振动之间"
    if "zh" not in translations["00_introduccion.html"]["body"]:
         translations["00_introduccion.html"]["body"]["zh"] = """<h2>I. 灵魂的不安</h2>
<p>从我有记忆以来，每当我走进巨大的石筑庙宇，总感觉到一种不和谐的振动。那并不是因为缺乏信仰；相反，我一直直觉地感到，在现实的面纱背后，存在着一个取之不尽的爱的源头。我的冲突，我无声的折磨，源于对无限上帝的直觉与我们试图将其装入狭小盒子之间的反差。</p>
<p>我在天主教的怀抱中长大，呼吸着香烛的气息，赞美着礼拜仪式，但很快，这种美就被一种不舒服的感觉所笼罩：傲慢。听到暗示或明示说我们拥有“真理”而其他人没有，这让我的灵魂感到刺痛。创造了一千亿个星系的造物主怎么会偏爱某个特定的精神邮编呢？我觉得我们犯了可怕的无知之罪，不承认其他信仰的救赎，用怜悯或优越感看待那些通过其他途径寻找光明的人。这种排他性在我看来，矛盾的是，是最不虔诚的行为：将上帝的仁慈限制在我们人类的边界之内。</p>
<h2>II. 权力中心的阴影</h2>
<p>但我的折磨超越了神学。学习历史时，我面对的是染血的墙壁。宗教裁判所、十字军东征、绝罚……我忍不住想：我们是如何从“爱你的邻居”走到“如果他想法和你不一样就烧死他”的？</p>
<p>多年来，这让我远离。我感到愤怒。我看到的是制度，只看到了阴影。然而，随着时间的推移和成熟，我明白了一个根本道理：教会，像任何人类结构一样，是由人组成的。而人是天线。当恐惧在权力中心扎根，当控制的需要超过服务的需要，集体的振动就会下降。</p>
<p>宗教裁判所不是上帝的工作，甚至不是抽象的“宗教”的工作。它是安装在顶层的<strong>低频振动</strong>的必然结果。害怕失去权力，害怕不同，伪装成热情的仇恨……所有这些都是稠密、沉重的频率。当这种密度占据等级制度时，结果就是痛苦。显然，这是基督本人，我的朋友耶稣，绝不会允许的事情。阻止人们用石头打通奸妇女的他，绝不会点燃篝火。</p>
<p>理解这一点让我能够原谅。我明白失败的不是“教会”，而是在黑暗时刻领导它的人的振动。而在那个权力穹顶之下，总有成千上万的神父、修女和普通人振动着高频，在这个黑暗的领导层下，给饥饿者食物，安慰悲伤者，保持光明的燃烧。</p>
<h2>III. 精神的量子物理学</h2>
<p>我最终的和解来自科学。我一直对量子物理学着迷，这个知识领域告诉我们现实并不像看起来那么坚固。它教导我们，每一个亚原子粒子同时既是物质又是波。它是具体的东西，同时，它是纯粹的振动，纯粹的可能性。</p>
<p>那就是一切豁然开朗的地方。主祷文、耶稣的教导……它们不是僵化的道德规则，它们是量子物理学说明书！</p>
<p>当耶稣告诉我们“不要害怕”时，他不是在给我们下达心理命令，他是在告诉我们：“不要降低你的频率。”恐惧是一种缓慢、稠密的振动，它会收缩现实。爱、和平、安全……是快速、扩张的振动，它们创造光。</p>
<p>我明白“陷入诱惑”不是在大斋期吃蛋糕。这是被低频振动的重力拖累的诱惑：仇恨、复仇、嫉妒、傲慢。当你恨的时候，你会变得稠密。你变成了一个沉重的“粒子”，孤立，与整体断开。当你爱的时候，你变成了一个“波”，你扩张，你与宇宙量子场连接，与父亲连接。</p>
<p>我和 21 世纪的视角补充道：“救赎不取决于追随教皇，而取决于你心灵的频率。”</p>
<p>如果你的行为，你的日常生活，是出于爱的高频振动，毫无疑问你是得救的。因为“得救”不是死后进入贵宾俱乐部的门票。得救是生活在此时此地，处于天堂的频率中。它是与源头同频。</p>"""

    translations["00_introduccion.html"]["title"]["vi"] = "Giới thiệu: Giữa Hạt và Rung động"
    translations["00_introduccion.html"]["h1"]["vi"] = "Giới thiệu: Giữa Hạt và Rung động"
    if "vi" not in translations["00_introduccion.html"]["body"]:
        translations["00_introduccion.html"]["body"]["vi"] = read_file('batch1.json') # Wait, batch1 doesn't have intro. I need to synthesize or skip.
        # Since I don't have existing VI intro, and didn't see it in file list. I will assume it's okay to fallback or I'll provide a placeholder OR translate deeply.
        # I'll provide a good translation.
        translations["00_introduccion.html"]["body"]["vi"] = """<h2>I. Sự Bất An Của Tâm Hồn</h2>
<p>Ngay từ khi biết nhận thức, tôi đã cảm thấy một loại rung động bất hòa mỗi khi đến gần những ngôi đền bằng đá vĩ đại. Đó không phải là thiếu đức tin; ngược lại, tôi luôn trực giác rằng đằng sau bức màn thực tại tồn tại một Nguồn yêu thương vô tận. Sự xung đột của tôi, nỗi dằn vặt thầm lặng của tôi, sinh ra từ sự tương phản giữa trực giác về một Thượng đế vô hạn và sự nhỏ bé của những chiếc hộp mà chúng ta cố gắng nhốt Ngài vào.</p>
<p>Tôi lớn lên trong lòng Công giáo, hít thở mùi hương trầm và ngưỡng mộ các nghi thức, nhưng rất sớm, vẻ đẹp đó đã bị che phủ bởi một cảm giác khó chịu: sự kiêu ngạo. Tâm hồn tôi đau đớn khi nghe, ngầm định hay rõ ràng, rằng chúng ta nắm giữ "chân lý" còn những người khác thì không. Làm sao Đấng Tạo Hóa của một vũ trụ với hàng trăm tỷ thiên hà lại có thể ưu ái một mã bưu chính tâm linh cụ thể? Tôi cảm thấy chúng ta đã phạm phải một sự ngạo mạn khủng khiếp khi không công nhận sự cứu rỗi cho các tín ngưỡng khác, khi nhìn với vẻ thương hại hoặc bề trên đối với những người tìm kiếm ánh sáng bằng con đường khác. Sự độc quyền đó, nghịch lý thay, dường như là hành động vô tôn giáo nhất: giới hạn lòng thương xót của Thượng đế trong biên giới con người của chúng ta.</p>
<h2>II. Những Bóng Đen Trong Các Trung Tâm Quyền Lực</h2>
<p>Nhưng nỗi dằn vặt của tôi vượt ra ngoài thần học. Khi nghiên cứu lịch sử, tôi đã va phải những bức tường nhuốm máu. Tòa án dị giáo, các cuộc thập tự chinh, vạ tuyệt thông... Tôi không thể không nghĩ: Làm thế nào chúng ta đã đi từ "yêu thương người lân cận" đến "thiêu sống hắn nếu hắn không nghĩ giống bạn"?</p>
<p>Trong nhiều năm, điều này đã đẩy tôi ra xa. Tôi cảm thấy giận dữ. Tôi nhìn thấy thể chế và chỉ thấy những bóng đen. Tuy nhiên, với thời gian và sự trưởng thành, tôi đã hiểu ra một điều cơ bản: Giáo hội, giống như bất kỳ cấu trúc con người nào, được tạo thành từ con người. Và con người là những chiếc ăng-ten. Khi nỗi sợ hãi trú ngụ trong các trung tâm quyền lực, khi nhu cầu kiểm soát vượt quá nhu cầu phục vụ, rung động tập thể sẽ giảm xuống.</p>
<p>Tòa án dị giáo không phải là công việc của Thượng đế, cũng không phải là công việc của "tôn giáo" theo nghĩa trừu tượng. Đó là hậu quả tất yếu của một <strong>rung động thấp</strong> được cài đặt ở tầng lớp thượng tầng. Nỗi sợ mất quyền lực, nỗi sợ sự khác biệt, sự căm ghét ngụy trang dưới lớp vỏ nhiệt thành... tất cả những thứ đó là những tần số dày đặc, nặng nề. Và khi mật độ đó chiếm lấy hệ thống phân cấp, kết quả là sự đau khổ. Rõ ràng, đó là điều mà chính Chúa Kitô, người bạn Giê-su của tôi, sẽ không bao giờ cho phép. Ngài, người đã ngăn những viên đá ném vào người phụ nữ ngoại tình, sẽ không bao giờ châm lửa đốt giàn thiêu.</p>
<p>Hiểu được điều này cho phép tôi tha thứ. Tôi hiểu rằng không phải "Giáo hội" đã thất bại, mà là rung động của những người đàn ông, trong những khoảnh khắc đen tối, đã lãnh đạo nó. Và rằng, bên dưới mái vòm quyền lực đó, luôn có hàng ngàn linh mục, nữ tu và giáo dân rung động cao, cho người đói ăn, an ủi người buồn, giữ cho ngọn đèn luôn cháy sáng bất chấp bóng tối của các nhà lãnh đạo của họ.</p>
<h2>III. Vật Lý Lượng Tử Của Tinh Thần</h2>
<p>Sự hòa giải dứt khoát của tôi đến từ khoa học. Tôi luôn bị cuốn hút bởi vật lý lượng tử, ngành tri thức cho chúng ta biết rằng thực tại không rắn chắc như vẻ ngoài của nó. Nó dạy chúng ta rằng mọi hạt hạ nguyên tử, cùng một lúc, vừa là vật chất vừa là sóng. Nó là một cái gì đó cụ thể và, đồng thời, nó là rung động thuần túy, khả năng thuần túy.</p>
<p>Đó là nơi mọi thứ khớp lại với nhau. Kinh Lạy Cha, những lời dạy của Chúa Giê-su... chúng không phải là những quy tắc đạo đức cứng nhắc, chúng là những hướng dẫn vật lý lượng tử!</p>
<p>Khi Chúa Giê-su bảo chúng ta "đừng sợ", Ngài không ra lệnh tâm lý cho chúng ta, Ngài đang bảo chúng ta: "Đừng hạ thấp tần số của các con." Sợ hãi là một rung động chậm, dày đặc làm co thắt thực tại. Tình yêu, bình an, an toàn... là những rung động nhanh, mở rộng tạo ra ánh sáng.</p>
<p>Tôi hiểu rằng "sa chước cám dỗ" không phải là ăn một chiếc bánh trong Mùa Chay. Đó là sự cám dỗ bị kéo xuống bởi trọng lực của những rung động thấp: hận thù, trả thù, ghen tị, kiêu ngạo. Khi bạn ghét, bạn trở nên dày đặc. Bạn trở thành một "hạt" nặng nề, cô lập, ngắt kết nối với tổng thể. Khi bạn yêu, bạn trở thành một "sóng", bạn mở rộng, bạn kết nối với trường lượng tử vũ trụ, với Cha.</p>"""

    # 2. Restore Index.html (Chapter 1)
    print("Restoring Chapter 1...")
    
    # Define translations for Chapter 1
    chapter1_trans = {
        "en": {
            "title": "Chapter 1: The Encounter in Madrid",
            "h1": "Chapter 1: The Encounter in Madrid",
            "body": """<p>It was a spring afternoon in Madrid. The sun filtered through the buildings of the Gran Vía, creating games of light and shadow that seemed to dance on the asphalt. I was walking with the usual haste of someone living in the city, with a mind full of noise: emails to answer, bills, worries... vibrating low, very low.</p>
<p>Suddenly, in Callao square, I saw him. He wasn't wearing a tunic, nor sandals, nor did he have a shining halo over his head. He was wearing worn-out jeans, a white t-shirt, and comfortable sneakers. He was sitting on a bench, watching people pass by with a calm smile, a smile that seemed to stop time.</p>
<p>—Hello, Francisco —he said when I passed close by.</p>
<p>I stopped dead in my tracks. No one called me by my full name in the street, and certainly not a stranger. But looking into his eyes, I knew he wasn't a stranger. There was an ancestral familiarity in his gaze, a peace that disarmed any defense.</p>
<p>—Jesus? —I asked, feeling a bit ridiculous.</p>
<p>—The same —he replied, patting the empty space on the bench beside him—. Sit down for a while. You are vibrating at a frequency that is giving me a headache, and I can endure a lot.</p>
<p>I sat down, still stunned.
—Vibrating? —I repeated.</p>
<p>—Yes, vibrating. Everything is vibration, my friend. Fear, haste, anger... are dense, heavy vibrations. They anchor you to the ground and don't let you see the sky, even if you have it right above you.</p>
<p>I looked up. The sky in Madrid was an intense, beautiful blue. I hadn't noticed it until that moment.</p>
<p>—I've come to spend a few days with you —he continued—. Let's go for a walk. You need to remember how to tune the radio of your soul. You are listening to pure static.</p>
<p>And so, in the middle of the bustle of Madrid, began the strangest and most wonderful adventure of my life. Not with miracles of turning water into wine, but with the miracle of transforming my internal noise into music.</p>"""
        },
        "fr": {
            "title": "Chapitre 1 : La rencontre à Madrid",
            "h1": "Chapitre 1 : La rencontre à Madrid",
            "body": """<p>C'était un après-midi de printemps à Madrid. Le soleil filtrait entre les bâtiments de la Gran Vía, créant des jeux de lumière et d'ombre qui semblaient danser sur l'asphalte. Je marchais avec la hâte habituelle de ceux qui vivent en ville, l'esprit plein de bruit : courriels à répondre, factures, soucis... vibrant bas, très bas.</p>
<p>Soudain, sur la place de Callao, je l'ai vu. Il ne portait ni tunique, ni sandales, et n'avait pas d'auréole brillante sur la tête. Il portait un jean usé, un t-shirt blanc et des baskets confortables. Il était assis sur un banc, regardant les gens passer avec un sourire tranquille, un sourire qui semblait arrêter le temps.</p>
<p>—Bonjour, Francisco —dit-il quand je passai tout près.</p>
<p>Je me suis arrêté net. Personne ne m'appelait par mon nom complet dans la rue, et encore moins un inconnu. Mais en le regardant dans les yeux, je sus qu'il n'était pas un inconnu. Il y avait une familiarité ancestrale dans son regard, une paix qui désarmait toute défense.</p>
<p>—Jésus ? —demandai-je, me sentant un peu ridicule.</p>
<p>—Lui-même —répondit-il en tapotant l'espace vide sur le banc à côté de lui—. Assieds-toi un moment. Tu vibres à une fréquence qui me donne mal à la tête, et pourtant j'en supporte beaucoup.</p>
<p>Je m'assis, encore abasourdi.
—Vibrer ? —répétai-je.</p>
<p>—Oui, vibrer. Tout est vibration, mon ami. La peur, la hâte, la colère... sont des vibrations denses, lourdes. Elles t'ancrent au sol et ne te laissent pas voir le ciel, même si tu l'as juste au-dessus.</p>
<p>Je regardai vers le haut. Le ciel de Madrid était d'un bleu intense, magnifique. Je ne l'avais pas remarqué jusqu'à ce moment.</p>
<p>—Je suis venu passer quelques jours avec toi —poursuivit-il—. Allons faire un tour. Tu as besoin de te rappeler comment accorder la radio de ton âme. Tu écoutes de la pure friture.</p>
<p>Et ainsi, au milieu de l'agitation de Madrid, commença l'aventure la plus étrange et merveilleuse de ma vie. Pas avec des miracles changeant l'eau en vin, mais avec le miracle de transformer mon bruit intérieur en musique.</p>"""
        },
        "it": {
            "title": "Capitolo 1: L'incontro a Madrid",
            "h1": "Capitolo 1: L'incontro a Madrid",
            "body": """<p>Era un pomeriggio di primavera a Madrid. Il sole filtrava tra gli edifici della Gran Vía, creando giochi di luce e ombra che sembravano danzare sull'asfalto. Camminavo con la fretta abituale di chi vive in città, con la mente piena di rumore: email a cui rispondere, bollette, preoccupazioni... vibrando basso, molto basso.</p>
<p>Improvvisamente, in piazza Callao, lo vidi. Non indossava tunica, né sandali, né aveva un'aureola brillante sulla testa. Indossava jeans consumati, una maglietta bianca e scarpe da ginnastica comode. Era seduto su una panchina, guardando la gente passare con un sorriso tranquillo, un sorriso che sembrava fermare il tempo.</p>
<p>—Ciao, Francisco —disse quando passai vicino.</p>
<p>Mi fermai di colpo. Nessuno mi chiamava col mio nome completo per strada, e men che meno uno sconosciuto. Ma guardandolo negli occhi, seppi che non era uno sconosciuto. C'era una familiarità ancestrale nel suo sguardo, una pace che disarmava ogni difesa.</p>
<p>—Gesù? —chiesi, sentendomi un po' ridicolo.</p>
<p>—Lo stesso —rispose lui, dando una pacca sullo spazio vuoto della panchina accanto a lui—. Siediti un attimo. Stai vibrando a una frequenza che mi sta facendo venire mal di testa, e dire che io sopporto molto.</p>
<p>Mi sedetti, ancora stordito.
—Vibrando? —ripetei.</p>
<p>—Sì, vibrando. Tutto è vibrazione, amico mio. La paura, la fretta, la rabbia... sono vibrazioni dense, pesanti. Ti ancorano al suolo e non ti lasciano vedere il cielo, anche se ce l'hai proprio sopra.</p>
<p>Guardai in alto. Il cielo di Madrid era di un azzurro intenso, bellissimo. Non ci avevo fatto caso fino a quel momento.</p>
<p>—Sono venuto a passare qualche giorno con te —continuò—. Facciamo un giro. Hai bisogno di ricordare come sintonizzare la radio della tua anima. Stai ascoltando pura statica.</p>
<p>E così, in mezzo al trambusto di Madrid, cominciò l'avventura più strana e meravigliosa della mia vita. Non con miracoli di trasformare l'acqua in vino, ma con il miracolo di trasformare il mio rumore interno in musica.</p>"""
        },
        "zh": {
            "title": "第 1 章：马德里相遇",
            "h1": "第 1 章：马德里相遇",
            "body": """<p>那是马德里的一个春日午后。阳光透过格兰大道的建筑物洒下，在柏油路上创造出仿佛在跳舞的光影游戏。我带着城市生活者惯有的匆忙行走，脑子里充满了噪音：要回复的邮件、账单、担忧……振动得很低，非常低。</p>
<p>突然，在卡亚俄广场，我看见了他。他没有穿长袍，没穿凉鞋，头上也没有发光的光环。他穿着磨损的牛仔裤，白色 T 恤和舒适的运动鞋。他坐在长椅上，带着平静的微笑看着人们经过，那微笑仿佛能让时间静止。</p>
<p>“你好，弗朗西斯科，”当我经过时他说。</p>
<p>我突然停了下来。没人会在街上叫我的全名，更不用说是一个陌生人了。但看着他的眼睛，我知道他不是陌生人。他的目光中有一种古老的熟悉感，一种解除任何防御的平静。</p>
<p>“耶稣？”我问，感觉有点荒谬。</p>
<p>“正是，”他回答，拍了拍他旁边长椅上的空位，“坐一会儿。你的振动频率让我头疼，虽然我忍耐力很强。”</p>
<p>我坐下，仍然目瞪口呆。
“振动？”我重复道。</p>
<p>“是的，振动。一切都是振动，我的朋友。恐惧、匆忙、愤怒……都是稠密、沉重的振动。它们把你锚定在地面上，不让你看到天空，即使它就在你头顶上方。”</p>
<p>我向上看。马德里的天空是强烈而美丽的蓝色。直到那一刻我才注意到。</p>
<p>“我来和你待几天，”他继续说，“我们去走走。你需要记住如何调整你灵魂的收音机。你现在听到的全是静电噪音。”</p>
<p>就这样，在马德里的喧嚣中，我生命中最奇怪、最奇妙的冒险开始了。不是把水变成酒的奇迹，而是把我内心的噪音变成音乐的奇迹。</p>"""
        },
        "ar": {
            "title": "الفصل الأول: اللقاء في مدريد",
            "h1": "الفصل الأول: اللقاء في مدريد",
            "body": """<p>كانت ظهيرة ربيعية في مدريد. كانت الشمس تتسلل بين مباني غران فيا، وتخلق ألعابًا من الضوء والظل بدت وكأنها ترقص على الأسفلت. كنت أمشي بالعجلة المعتادة لمن يعيش في المدينة، وعقلي مليء بالضجيج: رسائل بريد إلكتروني للرد عليها، فواتير، هموم... اهتزاز منخفض، منخفض جداً.</p>
<p>فجأة، في ساحة كالاو، رأيته. لم يكن يرتدي سترة، ولا صندلاً، ولم تكن لديه هالة لامعة فوق رأسه. كان يرتدي الجينز البالي، وقميصاً أبيض، وحذاء رياضياً مريحاً. كان يجلس على مقعد، يراقب الناس يمرون بابتسامة هادئة، ابتسامة بدت وكأنها توقف الزمن.</p>
<p>— مرحباً فرانسيسكو — قال عندما مررت بالقرب منه.</p>
<p>توقفت في مساري. لم ينادني أحد باسمي الكامل في الشارع، وبالتأكيد ليس شخصاً غريباً. لكن عند النظر في عينيه، عرفت أنه لم يكن غريباً. كانت هناك ألفة قديمة في نظرته، سلام يجرد أي دفاع من سلاحه.</p>
<p>— يسوع؟ — سألت، شاعراً ببعض السخافة.</p>
<p>— هو نفسه — أجاب، وهو يربت على المكان الفارغ في المقعد بجانبه —. اجلس قليلاً. أنت تهتز بتردد يسبب لي الصداع، مع أنني أتحمل الكثير.</p>
<p>جلست، وما زلت مذهولاً.
— أهتز؟ — رددت.</p>
<p>— نعم، تهتز. كل شيء هو اهتزاز يا صديقي. الخوف، العجلة، الغضب... هي اهتزازات كثيفة وثقيلة. تثبتك في الأرض ولا تدعك ترى السماء، حتى لو كانت فوقك مباشرة.</p>
<p>نظرت إلى الأعلى. كانت سماء مدريد زرقاء كثيفة وجميلة. لم ألحظ ذلك حتى تلك اللحظة.</p>
<p>— جئت لأقضي بضعة أيام معك — تابع —. لنذهب في نزهة. تحتاج أن تتذكر كيف تضبط راديو روحك. أنت تستمع إلى تشويش خالص.</p>
<p>وهكذا، في وسط صخب مدريد، بدأت أغرب وأروع مغامرة في حياتي. ليس بمعجزات تحويل الماء إلى نبيذ، بل بمعجزة تحويل ضجيجي الداخلي إلى موسيقى.</p>"""
        },
        "ru": {
            "title": "Глава 1: Встреча в Мадриде",
            "h1": "Глава 1: Встреча в Мадриде",
            "body": """<p>Это был весенний день в Мадриде. Солнце просачивалось между зданиями Гран-Виа, создавая игру света и тени, которая словно танцевала на асфальте. Я шел с обычной спешкой городского жителя, с умом, полным шума: письма, на которые нужно ответить, счета, заботы... вибрируя низко, очень низко.</p>
<p>Вдруг на площади Кальяо я увидел его. На нем не было ни туники, ни сандалий, ни сияющего нимба над головой. Он был в потертых джинсах, белой футболке и удобных кроссовках. Он сидел на скамейке, наблюдая за прохожими со спокойной улыбкой, улыбкой, которая, казалось, останавливала время.</p>
<p>— Привет, Франсиско, — сказал он, когда я проходил мимо.</p>
<p>Я замер. Никто не называл меня полным именем на улице, тем более незнакомец. Но, заглянув ему в глаза, я понял, что он не был незнакомцем. В его взгляде была какая-то древняя близость, мир, который обезоруживал любую защиту.</p>
<p>— Иисус? — спросил я, чувствуя себя немного нелепо.</p>
<p>— Он самый, — ответил он, похлопав по свободному месту на скамейке рядом с собой. — Присядь ненадолго. Ты вибрируешь на частоте, от которой у меня болит голова, а я ведь многое могу вытерпеть.</p>
<p>Я сел, все еще ошеломленный.
— Вибрирую? — переспросил я.</p>
<p>— Да, вибрируешь. Всё есть вибрация, друг мой. Страх, спешка, гнев... это плотные, тяжелые вибрации. Они приковывают тебя к земле и не дают увидеть небо, даже если оно прямо над тобой.</p>
<p>Я посмотрел наверх. Небо Мадрида было насыщенно-синим, прекрасным. Я не замечал этого до того момента.</p>
<p>— Я пришел провести с тобой несколько дней, — продолжил он. — Давай прогуляемся. Тебе нужно вспомнить, как настраивать радио своей души. Ты слушаешь сплошные помехи.</p>
<p>И так, посреди суеты Мадрида, началось самое странное и чудесное приключение в моей жизни. Не с чудес превращения воды в вино, а с чуда превращения моего внутреннего шума в музыку.</p>"""
        },
        "vi": {
            "title": "Chương 1: Cuộc gặp gỡ tại Madrid",
            "h1": "Chương 1: Cuộc gặp gỡ tại Madrid",
            "body": """<p>Đó là một buổi chiều mùa xuân ở Madrid. Mặt trời len lỏi giữa những tòa nhà trên Gran Vía, tạo nên những trò chơi của ánh sáng và bóng tối dường như đang nhảy múa trên mặt đường nhựa. Tôi bước đi với sự vội vã thường thấy của một người sống ở thành phố, với tâm trí đầy tiếng ồn: những email phải trả lời, hóa đơn, những lo toan... rung động thấp, rất thấp.</p>
<p>Đột nhiên, tại quảng trường Callao, tôi nhìn thấy Ngài. Ngài không mặc áo choàng, không đi dép, cũng không có vầng hào quang sáng chói trên đầu. Ngài mặc quần jean sờn cũ, áo phông trắng và giày thể thao thoải mái. Ngài đang ngồi trên ghế dài, nhìn mọi người qua lại với nụ cười bình thản, nụ cười dường như làm thời gian ngừng lại.</p>
<p>—Chào Francisco —Ngài nói khi tôi đi ngang qua.</p>
<p>Tôi đứng khựng lại. Không ai gọi tôi bằng tên đầy đủ trên đường phố, và chắc chắn không phải là một người lạ. Nhưng nhìn vào mắt Ngài, tôi biết Ngài không phải là người lạ. Có một sự thân thuộc từ ngàn xưa trong ánh nhìn của Ngài, một sự bình an giải trừ mọi sự phòng vệ.</p>
<p>—Chúa Giê-su? —tôi hỏi, cảm thấy hơi buồn cười.</p>
<p>—Chính Ta —Ngài trả lời, vỗ vỗ vào chỗ trống trên ghế bên cạnh—. Ngồi xuống một lát đi. Con đang rung động ở một tần số khiến Ta đau đầu, mà Ta thì chịu đựng giỏi lắm đấy.</p>
<p>Tôi ngồi xuống, vẫn còn sững sờ.
—Rung động ư? —tôi lặp lại.</p>
<p>—Đúng, rung động. Mọi thứ đều là rung động, bạn của Ta. Sợ hãi, vội vã, tức giận... là những rung động dày đặc, nặng nề. Chúng neo con xuống đất và không để con nhìn thấy bầu trời, ngay cả khi con có nó ngay trên đầu.</p>
<p>Tôi nhìn lên. Bầu trời Madrid một màu xanh thẫm, tuyệt đẹp. Tôi đã không để ý đến nó cho đến khoảnh khắc đó.</p>
<p>—Ta đến để dành vài ngày với con —Ngài tiếp tục—. Hãy đi dạo nào. Con cần nhớ lại cách điều chỉnh chiếc đài của tâm hồn mình. Con đang nghe toàn tiếng nhiễu.</p>
<p>Và như thế, giữa sự hối hả của Madrid, cuộc phiêu lưu kỳ lạ và tuyệt vời nhất cuộc đời tôi đã bắt đầu. Không phải với những phép lạ biến nước thành rượu, mà với phép lạ biến tiếng ồn bên trong tôi thành âm nhạc.</p>"""
        }
    }

    if "index.html" not in translations:
        translations["index.html"] = {"title": {}, "h1": {}, "body": {}}

    for lang, data in chapter1_trans.items():
        translations["index.html"]["title"][lang] = data["title"]
        translations["index.html"]["h1"][lang] = data["h1"]
        translations["index.html"]["body"][lang] = data["body"]

    # Also make sure 'ko' is there (it should be from previous script)
    # verify
    if 'ko' not in translations['index.html']['title']:
        print("Warning: Korean missing for index.html, check previous logic.")

    save_json("translations.json", translations)
    print("Content restored.")

if __name__ == "__main__":
    main()
