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
    # Remove H1
    text = re.sub(r'^# .*\n+', '', text)
    # Convert markdown to html
    html = markdown.markdown(text, extensions=['extra'])
    return html

# 1. Prepare Spanish Content for 14, 15, 16, 17
html_14_es = clean_md_for_html(os.path.join(CONTENT_DIR, '14_glosario_cuantico.md'))
html_15_es = clean_md_for_html(os.path.join(CONTENT_DIR, '15_musica_frecuencias.md'))
html_16_es = clean_md_for_html(os.path.join(CONTENT_DIR, '16_sobre_el_autor.md'))
html_17_es = clean_md_for_html(os.path.join(CONTENT_DIR, '17_guia_meditacion.md'))

spanish_content["14_glosario_cuantico.html"] = {
    "title": "Glosario Cuántico y Espiritual",
    "h1": "Glosario Cuántico y Espiritual",
    "body": html_14_es
}

spanish_content["15_musica_frecuencias.html"] = {
    "title": "La Música y las Frecuencias",
    "h1": "La Música y las Frecuencias",
    "body": html_15_es
}

spanish_content["16_sobre_el_autor.html"] = {
    "title": "Sobre el Autor y el Proyecto",
    "h1": "Sobre el Autor y el Proyecto",
    "body": html_16_es
}

spanish_content["17_guia_meditacion.html"] = {
    "title": "Guía de Reflexión y Meditación",
    "h1": "Guía de Reflexión y Meditación",
    "body": html_17_es
}

# ----------------------------------------------------
# CHAPTER 14 TRANSLATIONS (11 LANGUAGES)
# ----------------------------------------------------
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

BODY_14 = {
    "es": html_14_es,
    "en": """<p>To enrich your experience and delve deeper into the Master's dialogues, here is a guide to key concepts where quantum science and inner wisdom converge:</p>
<hr />
<h3>1. Abwoon (The Cosmic Origin)</h3>
<p>In the original Aramaic spoken by Jesus, <em>Abwoon</em> does not merely mean a human patriarch, but the <strong>«Cosmic Generator of Light and Breath»</strong>. It represents the omnipresent Source that continuously creates, sustains, and expands the entire fabric of the universe through the vibration of love.</p>
<hr />
<h3>2. The Observer Effect and Faith</h3>
<p>In quantum physics, a particle remains as a wave of infinite possibilities until an observer interacts with it and "collapses" that probability into a tangible physical reality. Jesus taught this very principle when he said: <em>«Whatever you ask for in prayer, believe that you have received it, and it will be yours»</em>. Faith is the conscious observer's certainty that the Light has already manifested the outcome.</p>
<hr />
<h3>3. Quantum Entanglement and Forgiveness</h3>
<p>Quantum entanglement demonstrates that two connected particles continue to influence each other regardless of the distance across space-time. When we harbor resentment toward someone, we remain energetically entangled with the pain of the past. <strong>Forgiveness</strong> is the only quantum tool that severs that dense tie, liberating both souls to vibrate once again in harmony with the present.</p>
<hr />
<h3>4. Vibrational Frequency and the Kingdom of Heaven</h3>
<p>The entire universe is made of energy in constant oscillation. Emotions such as fear, anger, or guilt vibrate at low, dense frequencies (the "gravity" Jesus speaks of). Emotions like gratitude, peace, and unconditional love vibrate at subtle, elevated frequencies. The <strong>Kingdom of Heaven</strong> is not a future geographic location, but the highest frequency of Being: tunable here and now.</p>
<hr />
<h3>5. Heart-Mind Coherence</h3>
<p>When the thoughts of the mind and the emotions of the heart enter harmonic resonance, the electromagnetic field we radiate becomes extraordinarily powerful and protective. This is what the Master defined as <em>«asking in my name»</em>: aligning with the exact frequency of the Presence.</p>""",

    "fr": """<p>Pour enrichir votre expérience et approfondir les dialogues du Maître, voici un guide des concepts clés où la science quantique et la sagesse intérieure se rencontrent :</p>
<hr />
<h3>1. Abwoon (L'Origine Cosmique)</h3>
<p>Dans la langue araméenne originelle parlée par Jésus, <em>Abwoon</em> ne désigne pas simplement un patriarche humain, mais le <strong>« Générateur Cosmique de Lumière et de Souffle »</strong>. Il représente la Source omniprésente qui crée, soutient et expanse continuellement toute la trame de l'univers à travers la vibration de l'amour.</p>
<hr />
<h3>2. L'Effet Observateur et la Foi</h3>
<p>En physique quantique, une particule demeure une onde de possibilités infinies jusqu'à ce qu'un observateur interagisse avec elle et « effondre » cette probabilité en une réalité physique tangible. Jésus a enseigné ce principe même en disant : <em>« Tout ce que vous demandez en priant, croyez que vous l'avez reçu, et cela vous sera accordé »</em>. La foi est la certitude de l'observateur conscient que la Lumière a déjà manifesté le résultat.</p>
<hr />
<h3>3. L'Intrication Quantique et le Pardon</h3>
<p>L'intrication quantique démontre que deux particules connectées continuent de s'influencer mutuellement, quelle que soit la distance dans l'espace-temps. Lorsque nous nourrissons du ressentiment envers quelqu'un, nous restons énergétiquement intriqués dans la douleur du passé. Le <strong>pardon</strong> est le seul outil quantique qui coupe ce lien dense, libérant les deux âmes pour qu'elles vibrent à nouveau en synchronie avec le présent.</p>
<hr />
<h3>4. Fréquence Vibratoire et le Royaume des Cieux</h3>
<p>L'univers tout entier est constitué d'énergie en constante oscillation. Les émotions comme la peur, la colère ou la culpabilité vibrent à des fréquences basses et denses (la « gravité » dont parle Jésus). Les émotions comme la gratitude, la paix et l'amour inconditionnel vibrent à des fréquences subtiles et élevées. Le <strong>Royaume des Cieux</strong> n'est pas un lieu géographique futur, mais la plus haute fréquence de l'Être : syntonisable ici et maintenant.</p>
<hr />
<h3>5. Cohérence Cœur-Esprit</h3>
<p>Lorsque les pensées de l'esprit et les émotions du cœur entrent en résonance harmonique, le champ électromagnétique que nous émettons devient extraordinairement puissant et protecteur. C'est ce que le Maître a défini comme <em>« demander en mon nom »</em> : s'aligner sur la même fréquence de la Présence.</p>""",

    "it": """<p>Per arricchire la tua esperienza e approfondire i dialoghi del Maestro, ecco una guida ai concetti chiave in cui la scienza quantistica e la saggezza interiore si incontrano:</p>
<hr />
<h3>1. Abwoon (L'Origine Cosmica)</h3>
<p>Nell'aramaico originale parlato da Gesù, <em>Abwoon</em> non significa semplicemente un patriarca umano, ma il <strong>«Generatore Cosmico di Luce e Respiro»</strong>. Rappresenta la Fonte onnipresente che crea, sostiene ed espande continuamente l'intera trama dell'universo attraverso la vibrazione dell'amore.</p>
<hr />
<h3>2. L'Effetto Osservatore e la Fede</h3>
<p>Nella fisica quantistica, una particella rimane un'onda di infinite possibilità finché un osservatore non interagisce con essa e «collassa» tale probabilità in una realtà fisica tangibile. Gesù ha insegnato questo stesso principio dicendo: <em>«Tutto quello che chiederete con la preghiera, abbiate fede di averlo già ricevuto e vi sarà accordato»</em>. La fede è la certezza dell'osservatore consapevole che la Luce ha già manifestato il risultato.</p>
<hr />
<h3>3. L'Entanglement Quantistico e il Perdono</h3>
<p>L'entanglement quantistico dimostra che due particelle connesse continuano a influenzarsi a vicenda indipendentemente dalla distanza nello spazio-tempo. Quando serbiamo rancore verso qualcuno, rimaniamo energeticamente legati al dolore del passato. Il <strong>perdono</strong> è l'unico strumento quantistico che recide quel legame denso, liberando entrambe le anime affinché tornino a vibrare in sincronia con il presente.</p>
<hr />
<h3>4. Frequenza Vibratoria e il Regno dei Cieli</h3>
<p>L'intero universo è fatto di energia in costante oscillazione. Emozioni come la paura, la rabbia o il senso di colpa vibrano a frequenze basse e dense (la «gravità» di cui parla Gesù). Emozioni come la gratitudine, la pace e l'amore incondizionato vibrano a frequenze sottili ed elevate. Il <strong>Regno dei Cieli</strong> non è un luogo geografico futuro, ma la frequenza più alta dell'Essere: sintonizzabile qui e ora.</p>
<hr />
<h3>5. Coerenza Cuore-Mente</h3>
<p>Quando i pensieri della mente e le emozioni del cuore entrano in risonanza armonica, il campo elettromagnetico che irradiamo diventa straordinariamente potente e protettivo. È ciò che il Maestro ha definito <em>«chiedere nel mio nome»</em>: allinearsi con la frequenza stessa della Presenza.</p>""",

    "zh": """<p>为了丰富您的阅读体验并深入理解大师的对话，这里提供了一份量子科学与内在智慧相融合的核心概念指南：</p>
<hr />
<h3>1. Abwoon（宇宙之源）</h3>
<p>在耶稣所说的原始亚兰语中，<em>Abwoon</em> 不仅代表一位人类父亲，更意味着<strong>“光与气息的宇宙发生器”</strong>。它代表着通过爱的振动不断创造、维持并扩展整个宇宙织锦的无所不在的源头。</p>
<hr />
<h3>2. 观察者效应与信念</h3>
<p>在量子物理学中，粒子在观察者与其相互作用之前一直作为无限可能性的波而存在，观察使其坍缩为有形的物理现实。耶稣教导了同样的原则：<em>“凡你们祷告祈求的，无论是甚么，只要信是得着的，就必得着”</em>。信念是觉知观察者的确定感，知晓光早已显化了这一结果。</p>
<hr />
<h3>3. 量子纠缠与宽恕</h3>
<p>量子纠缠表明，两个相连的粒子无论在时空中相距多远都会继续相互影响。当我们对某人怀恨在心时，我们在能量上仍与过去的痛苦纠缠在一起。<strong>宽恕</strong>是唯一能够切断这一沉重纽带的量子工具，释放两个灵魂，使其重新与当下同步振动。</p>
<hr />
<h3>4. 振动频率与天国</h3>
<p>整个宇宙由不断振动的能量构成。恐惧、愤怒或内疚等情绪在低沉的频率中振动（耶稣所说的“重力”）。感恩、和平与无条件的爱则在高雅的频率中振动。<strong>天国</strong>不是未来的地理位置，而是“存在”的最高频率：此时此刻即可调谐共振。</p>
<hr />
<h3>5. 心脑合一与共鸣</h3>
<p>当头脑的思想与心灵的情感进入和谐共振时，我们放射出的电磁场变得异常强大并具保护力。这就是大师所定义的<em>“奉我的名祈求”</em>：与“临在”的同一频率完全对齐。</p>""",

    "ar": """<p>لإثراء تجربتك والتعمق في حوارات المعلم، إليك دليلاً للمفاهيم الأساسية التي يلتقي فيها العلم الكمي بالحكمة الباطنية:</p>
<hr />
<h3>1. أبون (Abwoon - المصدر الكوني)</h3>
<p>في اللغة الآرامية الأصلية التي تحدث بها يسوع، لا تعني كلمة <em>Abwoon</em> مجرد أب بشري، بل تعني <strong>«المولد الكوني للنور والنَفَس»</strong>. إنها تمثل المصدر الكلي الوجود الذي يخلق ويغذي ويوسع نسيج الكون باستمرار من خلال اهتزاز الحب.</p>
<hr />
<h3>2. تأثير المراقب والإيمان</h3>
<p>في فيزياء الكم، يظل الجسيم كموجة من الاحتمالات اللانهائية حتى يتفاعل معه مراقب فينهار ذلك الاحتمال إلى حقيقة مادية ملموسة. علّم يسوع هذا المبدأ عينه قائلاً: <em>«كل ما تطلبونه حينما تصلون، فآمنوا أنكم نلتموه، فيكون لكم»</em>. الإيمان هو يقين المراقب الواعي بأن النور قد أظهر النتيجة بالفعل.</p>
<hr />
<h3>3. التشابك الكمي والمغفرة</h3>
<p>يوضح التشابك الكمي أن جسيمين متصلين يستمران في التأثير المتبادل بغض النظر عن المسافة في الزمان والمكان. عندما نحمل ضغينة تجاه شخص ما، فإننا نظل متشابكين طاقياً مع ألم الماضي. إن <strong>المغفرة</strong> هي الأداة الكمية الوحيدة التي تقطع هذا القيد الكثيف، محررةً كلا الروحين لتهتزا مجدداً في تناغم مع الحاضر.</p>
<hr />
<h3>4. التردد الاهتزازي وملكوت السماوات</h3>
<p>الكون بأكمله مصنوع من طاقة في تذبذب مستمر. المشاعر كالفضل والغضب والذنب تهتز بترددات منخفضة وكثيفة («الجاذبية» التي تحدث عنها يسوع). بينما تهتز مشاعر الامتنان والسلام والحب غير المشروط بترددات سامية وعالية. <strong>ملكوت السماوات</strong> ليس موقعاً جغرافياً مستقبلياً، بل هو أعلى تردد للوجود: يمكن ضبطه وتناغمه هنا والآن.</p>
<hr />
<h3>5. التماسك بين القلب والعقل</h3>
<p>عندما تدخل أفكار العقل ومشاعر القلب في رنين متناغم، يصبح الحقل الكهرومغناطيسي الذي نبثه قوياً وواحداً على نحو استثنائي. هذا ما وصفه المعلم بـ <em>«الطلب باسمي»</em>: التناغم مع نفس تردد الحضور الإلهي.</p>""",

    "ru": """<p>Чтобы обогатить ваш опыт и глубже проникнуть в диалоги Учителя, представляем руководство по ключевым понятиям, в которых квантовая наука встречается с внутренней мудростью:</p>
<hr />
<h3>1. Абвун (Abwoon — Космический Источник)</h3>
<p>На арамейском языке, на котором говорил Иисус, <em>Abwoon</em> означает не просто земного отца, а <strong>«Космический Источник Света и Дыхания»</strong>. Это вездесущий Источник, который непрерывно творит, поддерживает и расширяет ткань Вселенной через вибрацию безусловной любви.</p>
<hr />
<h3>2. Эффект наблюдателя и вера</h3>
<p>В квантовой физике частица пребывает в виде волны бесконечных возможностей, пока наблюдатель не вступит с ней во взаимодействие и не «схлопнет» эту вероятность в осязаемую физическую реальность. Иисус учил этому принципу: <em>«Всё, чего ни попросите в молитве с верою, верьте, что получите, — и будет вам»</em>. Вера — это осознанная уверенность наблюдателя в том, что Свет уже явил результат.</p>
<hr />
<h3>3. Квантовая запутанность и прощение</h3>
<p>Квантовая запутанность показывает, что две связанные частицы продолжают влиять друг на друга независимо от расстояния во времени и пространстве. Когда мы храним обиду, мы остаемся энергетически связанными с болью прошлого. <strong>Прощение</strong> — единственный квантовый инструмент, разрывающий эту плотную связь и освобождающий обе души для вибрации в согласии с настоящим.</p>
<hr />
<h3>4. Вибрационная частота и Царство Небесное</h3>
<p>Вся Вселенная состоит из энергии в постоянном колебании. Страх, гнев и чувство вины вибрируют на низких плотных частотах («гравитация», о которой говорил Иисус). Благодарность, мир и любовь вибрируют на высоких тонких частотах. <strong>Царство Небесное</strong> — это не будущее географическое место, а высшая частота Бытия, доступная для настройки здесь и сейчас.</p>
<hr />
<h3>5. Когерентность сердца и разума</h3>
<p>Когда мысли разума и чувства сердца входят в гармонический резонанс, излучаемое нами электромагнитное поле становится невероятно мощным и защитным. Это то, что Учитель называл <em>«просить во имя Мое»</em>: сонастроиться с частотой Божественного Присутствия.</p>""",

    "vi": """<p>Để làm phong phú trải nghiệm của bạn và hiểu sâu hơn về những lời dạy của Thầy, đây là hướng dẫn về các khái niệm cốt lõi nơi khoa học lượng tử và trí tuệ tâm linh hội tụ:</p>
<hr />
<h3>1. Abwoon (Nguồn gốc Vũ trụ)</h3>
<p>Trong ngôn ngữ Aramaic nguyên bản mà Chúa Giê-su sử dụng, <em>Abwoon</em> không chỉ đơn thuần là người cha con người, mà là <strong>«Đấng Tạo Hóa Vũ Trụ của Ánh Sáng và Hơi Thở»</strong>. Ngài đại diện cho Nguồn Hiện Diện Khắp Nơi, Đấng liên tục kiến tạo, nuôi dưỡng và mở rộng vũ trụ thông qua rung động của tình yêu.</p>
<hr />
<h3>2. Hiệu ứng Người quan sát và Đức tin</h3>
<p>Trong vật lý lượng tử, một hạt tồn tại dưới dạng sóng của vô hạn tiềm năng cho đến khi người quan sát tương tác và làm «sụp đổ» xác suất đó thành hiện thực vật lý. Chúa Giê-su dạy nguyên lý này: <em>«Tất cả những gì anh em cầu xin, hãy tin rằng anh em đã nhận được rồi, thì sẽ được như ý»</em>. Đức tin là sự chắc chắn của người quan sát tỉnh thức rằng Ánh Sáng đã biểu hiện kết quả.</p>
<hr />
<h3>3. Vướng víu lượng tử và Sự tha thứ</h3>
<p>Hiện tượng vướng víu lượng tử chứng minh hai hạt kết nối tiếp tục ảnh hưởng lẫn nhau bất kể khoảng cách không-thời gian. Khi ôm giữ oán hận, chúng ta bị trói buộc năng lượng với nỗi đau quá khứ. <strong>Sự tha thứ</strong> là công cụ lượng tử duy nhất cắt đứt sợi dây nặng nề đó, giải phóng cả hai tâm hồn để cùng hòa nhịp với hiện tại.</p>
<hr />
<h3>4. Tần số Rung động và Nước Trời</h3>
<p>Toàn bộ vũ trụ được tạo thành từ năng lượng dao động không ngừng. Nỗi sợ hãi, giận dữ rung động ở tần số thấp và đậm đặc («lực hấp dẫn» mà Chúa Giê-su nhắc đến). Lòng biết ơn, bình an và tình yêu vô điều kiện rung động ở tần số thanh cao. <strong>Nước Trời</strong> không phải là nơi chốn tương lai, mà là tần số cao nhất của Bản Thể: có thể đồng điệu ngay tại đây và lúc này.</p>
<hr />
<h3>5. Sự đồng điệu Tâm - Trí</h3>
<p>Khi suy nghĩ của tâm trí và cảm xúc của trái tim cộng hưởng hài hòa, trường điện từ mà chúng ta phát ra trở nên vô cùng mạnh mẽ và che chở. Đó là điều Thầy dạy khi nói <em>«cầu xin nhân danh Thầy»</em>: hòa làm một với tần số của Sự Hiện Diện.</p>""",

    "ko": """<p>책의 깊은 울림과 예수님의 대화를 더욱 풍성하게 이해할 수 있도록, 양자물리학과 영적 지혜가 만나는 핵심 개념 가이드를 소개합니다:</p>
<hr />
<h3>1. 아브운(Abwoon - 우주의 근원)</h3>
<p>예수님께서 말씀하신 원래의 아람어에서 <em>Abwoon</em>은 단순한 육신의 아버지가 아니라, <strong>«빛과 숨결의 우주적 창조자»</strong>를 뜻합니다. 사랑의 진동을 통해 온 우주의 삼라만상을 끊임없이 창조하고 지탱하며 확장하는 편재하는 근원을 나타냅니다.</p>
<hr />
<h3>2. 관찰자 효과와 믿음</h3>
<p>양자물리학에서 입자는 관찰자가 상호작용하여 그 확률을 유형의 물리적 실체로 «붕괴»시킬 때까지 무한한 가능성의 파동으로 존재합니다. 예수님께서는 <em>«너희가 기도할 때에 무엇이든지 믿고 구하는 것은 다 받으리라»</em>고 말씀하시며 이 원리를 가르치셨습니다. 믿음이란 빛이 이미 결과를 현현했음을 확신하는 깨어 있는 관찰자의 확신입니다.</p>
<hr />
<h3>3. 양자 얽힘과 용서</h3>
<p>양자 얽힘은 연결된 두 입자가 시공간의 거리에 관계없이 서로에게 지속적으로 영향을 미침을 보여줍니다. 타인에 대한 원망을 품고 있을 때, 우리는 과거의 고통과 에너지적으로 얽혀 있게 됩니다. <strong>용서</strong>는 그 무거운 끈을 끊어내어 두 영혼 모두가 다시 현재와 동조하여 진동하도록 해방하는 유일한 양자적 도구입니다.</p>
<hr />
<h3>4. 진동 주파수와 하늘나라</h3>
<p>온 우주는 끊임없이 진동하는 에너지로 이루어져 있습니다. 두려움, 분노, 죄책감은 낮고 둔탁한 주파수(예수님이 말씀하신 «중력»)로 진동합니다. 감사, 평화, 무조건적인 사랑은 미세하고 높은 주파수로 진동합니다. <strong>하늘나라</strong>는 먼 미래의 지리적 장소가 아니라, 지금 여기에서 조율할 수 있는 존재의 가장 높은 진동 상태입니다.</p>
<hr />
<h3>5. 심장과 마음의 일치(코히어런스)</h3>
<p>생각과 가슴의 감정이 조화로운 공명을 이룰 때, 우리가 방출하는 전자기장은 대단히 강력하고 보호적인 힘을 발휘합니다. 이것이 바로 스승께서 <em>«내 이름으로 구하라»</em>고 하신 말씀의 본뜻이며, '참된 현존'의 주파수와 하나 됨을 의미합니다.</p>""",

    "pt": """<p>Para enriquecer a sua experiência e aprofundar os diálogos do Mestre, apresentamos este guia dos conceitos-chave onde a ciência quântica e a sabedoria interior se encontram:</p>
<hr />
<h3>1. Abwoon (A Origem Cósmica)</h3>
<p>No aramaico original falado por Jesus, <em>Abwoon</em> não significa apenas um patriarca humano, mas o <strong>«Gerador Cósmico de Luz e Sopro»</strong>. Representa a Fonte omnipresente que cria, sustenta e expande continuamente todo o tecido do universo através da vibração do amor.</p>
<hr />
<h3>2. O Efeito Observador e a Fé</h3>
<p>Na física quântica, uma partícula permanece como uma onda de infinitas possibilidades até que um observador interaja com ela e «colapse» essa probabilidade numa realidade física tangível. Jesus ensinou este mesmo princípio ao dizer: <em>«Tudo o que pedirdes em oração, crede que o recebereis, e tê-lo-eis»</em>. A fé é a certeza do observador consciente de que a Luz já manifestou o resultado.</p>
<hr />
<h3>3. Entrelaçamento Quântico e o Perdão</h3>
<p>O entrelaçamento quântico demonstra que duas partículas conectadas continuam a influenciar-se mutuamente, independentemente da distância no espaço-tempo. Quando guardamos ressentimento, ficamos energeticamente entrelaçados com a dor do passado. O <strong>perdão</strong> é a única ferramenta quântica que corta esse laço denso, libertando ambas as almas para voltarem a vibrar em sincronia com o presente.</p>
<hr />
<h3>4. Frequência Vibratória e o Reino dos Céus</h3>
<p>O universo inteiro é feito de energia em constante oscilação. Emoções como o medo, a raiva ou a culpa vibram em frequências baixas e densas (a «gravidade» de que Jesus fala). Emoções como a gratidão, a paz e o amor incondicional vibram em frequências subtis e elevadas. O <strong>Reino dos Céus</strong> não é uma localização geográfica futura, mas a frequência mais alta do Ser: sintonizável aqui e agora.</p>
<hr />
<h3>5. Coerência Coração-Mente</h3>
<p>Quando os pensamentos da mente e as emoções do coração entram em ressonância harmónica, o campo eletromagnético que irradiamos torna-se extraordinariamente poderoso e protetor. É o que o Mestre definiu como <em>«pedir em meu nome»</em>: alinhar-se com a frequência da Presença.</p>""",

    "ja": """<p>本書の読書体験をより深め、イエスとの対話をより深く味わうために、量子科学と内なる叡智が融合する重要概念のガイドをお届けします：</p>
<hr />
<h3>1. アブウーン（Abwoon - 宇宙の根源）</h3>
<p>イエスが語った原初のアラム語において、<em>Abwoon</em>は単なる人間の父親を指すのではなく、<strong>「光と息吹の宇宙的生成主」</strong>を意味します。愛の波動を通じて、宇宙全体の織物を絶え間なく創造し、支え、広げ続ける遍在の源（ソース）を表しています。</p>
<hr />
<h3>2. 観察者効果と信仰（信じる力）</h3>
<p>量子力学では、粒子は観察者が働きかけてその確率を有形の物理的現実に「収縮」させるまで、無限の可能性を秘めた波動として存在します。イエスは<em>「祈り求めるものは何でも、すでに受け取ったと信じなさい。そうすれば、その通りになる」</em>と述べ、まさにこの原理を説きました。信仰とは、光がすでに結果を顕現させたと知る、覚醒した観察者の確信です。</p>
<hr />
<h3>3. 量子もつれと許し</h3>
<p>量子もつれは、一度つながった2つの粒子が時空の距離に関係なく相互に影響し続けることを示します。誰かに対して恨みを抱き続けるとき、私たちは過去の苦痛とエネルギー的にもつれ合っています。<strong>「許し」</strong>は、その重い束縛を断ち切り、双方の魂を解き放って再び「今」と同調して振動させる唯一の量子ツールです。</p>
<hr />
<h3>4. 振動周波数（波動）と天国（神の国）</h3>
<p>宇宙全体は絶えず振動するエネルギーで構成されています。恐れ、怒り、罪悪感などの感情は低く重い周波数（イエスの言う「重力」）で振動します。感謝、平安、無条件の愛は精妙で高い周波数で振動します。<strong>天国</strong>とは遠い未来の場所ではなく、「存在」の最も高い波動状態であり、今ここでチューニングできるものです。</p>
<hr />
<h3>5. 心と脳のコヒーレンス（調和共鳴）</h3>
<p>頭の思考と心の感情が調和した共鳴状態に入るとき、私たちが放射する電磁場は並外れて強力で保護的なものになります。これこそがイエスが<em>「私の名によって求めなさい」</em>と説いた真意であり、至高の「臨在（プレゼンス）」の波動と完全に調和することです。</p>"""
}

translations["14_glosario_cuantico.html"] = {
    "h1": TITLES_14,
    "body": BODY_14
}

# ----------------------------------------------------
# CHAPTER 15 TRANSLATIONS (11 LANGUAGES)
# ----------------------------------------------------
BODY_15 = {
    "es": html_15_es,
    "en": """<p>The experience of <em>My Friend Jesus Christ</em> does not end with the written words: it was conceived from the beginning as a <strong>multisensory and vibrational work</strong>, where sound acts as a direct vehicle for inner tuning.</p>
<hr />
<h3>The Musical Creation of Maria Paz Arés Osset</h3>
<p>Every chapter of the book resonates with musical compositions and sound frequencies crafted by <strong>Maria Paz Arés Osset</strong>. These melodies are designed to accompany the mind and heart into a state of deep relaxation, coherence, and openness.</p>
<p>Listening to these musical pieces:</p>
<ul>
<li><strong>Brainwave activity gently slows down</strong> into alpha and theta states, fostering introspection and peace.</li>
<li><strong>Tensions and dense emotional burdens</strong> accumulated in daily life dissolve.</li>
<li><strong>The message of the text is integrated</strong> at a subconscious and cellular level through the universal language of sound.</li>
</ul>
<hr />
<h3>How to Experience the Sound Journey</h3>
<p>We invite you to listen to the album while reading each chapter or during your daily meditation and silence:</p>
<ol>
<li><strong>On Spotify</strong>: Search for the official tracks of the album and immerse yourself in its uplifting atmospheres.</li>
<li><strong>On the Official Website</strong>: Visit <a href="https://pazaresosset.es">pazaresosset.es</a> to access new releases, visual artwork, and additional content from the artist.</li>
</ol>
<blockquote>
<p><em>«Music is the voice of the soul that reminds matter of its origin of pure Light.»</em></p>
</blockquote>""",

    "fr": """<p>L'expérience de <em>Mon Ami Jésus-Christ</em> ne s'arrête pas aux mots écrits : elle a été conçue dès son origine comme une <strong>œuvre multisensorielle et vibratoire</strong>, où le son agit comme un véhicule direct d'harmonisation intérieure.</p>
<hr />
<h3>La Création Musicale de Maria Paz Arés Osset</h3>
<p>Chaque chapitre du livre résonne avec des compositions musicales et des fréquences sonores créées par <strong>Maria Paz Arés Osset</strong>. Ces mélodies sont conçues pour accompagner l'esprit et le cœur dans un état de relaxation profonde, de cohérence et d'ouverture.</p>
<p>En écoutant ces pièces musicales :</p>
<ul>
<li><strong>Le rythme cérébral ralentit</strong> vers les états alpha et thêta, facilitant l'introspection et la paix.</li>
<li><strong>Les tensions et les charges émotionnelles denses</strong> accumulées au quotidien se dissolvent.</li>
<li><strong>Le message du texte s'intègre</strong> au niveau subconscient et cellulaire à travers le langage universel du son.</li>
</ul>
<hr />
<h3>Comment Vivre l'Expérience Sonore</h3>
<p>Nous vous invitons à écouter l'album pendant votre lecture de chaque chapitre ou lors de vos moments quotidiens de méditation et de silence :</p>
<ol>
<li><strong>Sur Spotify</strong> : Recherchez les morceaux officiels de l'album et plongez dans ses atmosphères enveloppantes.</li>
<li><strong>Sur le Site Officiel</strong> : Visitez <a href="https://pazaresosset.es">pazaresosset.es</a> pour découvrir les nouveautés, l'art visuel et les contenus additionnels de l'artiste.</li>
</ol>
<blockquote>
<p><em>« La musique est la voix de l'âme qui rappelle à la matière son origine de pure Lumière. »</em></p>
</blockquote>""",

    "it": """<p>L'esperienza di <em>Il Mio Amico Gesù Cristo</em> non si esaurisce nelle parole scritte: è stata concepita fin dalle origini come un'<strong>opera multisensoriale e vibratoria</strong>, in cui il suono funge da veicolo diretto per la sintonizzazione interiore.</p>
<hr />
<h3>La Creazione Musicale di Maria Paz Arés Osset</h3>
<p>Ogni capitolo del libro risuona con composizioni musicali e frequenze sonore create da <strong>Maria Paz Arés Osset</strong>. Queste melodie sono studiate per accompagnare la mente e il cuore in uno stato di profondo rilassamento, coerenza e apertura.</p>
<p>Ascoltando questi brani musicali:</p>
<ul>
<li><strong>Il ritmo cerebrale rallenta</strong> verso stati alfa e theta, facilitando l'introspezione e la quiete.</li>
<li><strong>Si sciolgono le tensioni</strong> e i carichi emotivi densi accumulati nella quotidianità.</li>
<li><strong>Il messaggio del testo si integra</strong> a livello subconscio e cellulare attraverso il linguaggio universale del suono.</li>
</ul>
<hr />
<h3>Come Vivere l'Esperienza Sonora</h3>
<p>Ti invitiamo ad ascoltare l'album durante la lettura di ciascun capitolo o nei tuoi momenti quotidiani di meditazione e silenzio:</p>
<ol>
<li><strong>Su Spotify</strong>: Cerca le tracce ufficiali dell'album e immergiti nelle sue atmosfere avvolgenti.</li>
<li><strong>Sul Sito Ufficiale</strong>: Visita <a href="https://pazaresosset.es">pazaresosset.es</a> per accedere a tutte le novità, all'arte visiva e ai contenuti aggiuntivi dell'autrice.</li>
</ol>
<blockquote>
<p><em>«La musica è la voce dell'anima che ricorda alla materia la sua origine di pura Luce.»</em></p>
</blockquote>""",

    "zh": """<p>《我的朋友耶稣基督》的体验并不仅限于文字：它自构思之初便是一部<strong>多感官与高振动的艺术作品</strong>，声音在此成为直接引导内在调谐的载体。</p>
<hr />
<h3>Maria Paz Arés Osset 的音乐创作</h3>
<p>本书的每一章节都与 <strong>Maria Paz Arés Osset</strong> 创作的音乐和声音频率产生共鸣。这些旋律旨在引导身心进入深度放松、谐振与敞开的境界。</p>
<p>聆听这些音乐作品：</p>
<ul>
<li><strong>脑电波减缓</strong>进入阿尔法（Alpha）与西塔（Theta）状态，带来内省与宁静。</li>
<li><strong>日常积累的压力与沉重情绪负担得以消融</strong>。</li>
<li><strong>书中的信息通过声音这一宇宙通用语言</strong>在潜意识与细胞层面深度整合。</li>
</ul>
<hr />
<h3>如何体验声音之旅</h3>
<p>诚邀您在阅读每一章节或日常冥想静心时聆听该专辑：</p>
<ol>
<li><strong>在 Spotify 上</strong>：搜索专辑官方曲目，沉浸于其深邃空灵的氛围中。</li>
<li><strong>在官方网站上</strong>：访问 <a href="https://pazaresosset.es">pazaresosset.es</a> 获取最新动态、视觉艺术作品及更多精彩内容。</li>
</ol>
<blockquote>
<p><em>“音乐是灵魂的声音，提醒物质其源自纯粹之光的本质。”</em></p>
</blockquote>""",

    "ar": """<p>لا تنتهي تجربة <em>صديقي يسوع المسيح</em> عند الكلمات المكتوبة: بل صُممت منذ بدايتها كـ <strong>عمل متعدد الحواس والاهتزازات</strong>، حيث يعمل الصوت كناقل مباشر للتناغم الداخلي.</p>
<hr />
<h3>الإبداع الموسيقي لـ Maria Paz Arés Osset</h3>
<p>يتردد صدى كل فصل في الكتاب مع مؤلفات موسيقية وترددات صوتية أبدعتها <strong>Maria Paz Arés Osset</strong>. صُممت هذه الألحان لمرافقة العقل والقلب نحو حالة من الاسترخاء العميق والتناغم والانفتاح.</p>
<p>عند الاستماع إلى هذه المقطوعات الموسيقية:</p>
<ul>
<li><strong>يتباطأ إيقاع الدماغ</strong> نحو موجات ألفا وثيتا، مما يسهل التأمل والسلام الباطني.</li>
<li><strong>تتلاشى التوترات</strong> والأحمال العاطفية الثقيلة المتراكمة في الحياة اليومية.</li>
<li><strong>تترسخ رسالة النص</strong> في العقل الباطن وعلى المستوى الخلوي من خلال لغة الصوت العالمية.</li>
</ul>
<hr />
<h3>كيفية عيش التجربة الصوتية</h3>
<p>ندعوك للاستماع إلى الألبوم أثناء قراءة كل فصل أو خلال لحظات التأمل والصمت اليومية:</p>
<ol>
<li><strong>على Spotify</strong>: ابحث عن المقطوعات الرسمية للألبوم وانغمس في أجوائه الساحرة.</li>
<li><strong>على الموقع الرسمي</strong>: تفضل بزيارة <a href="https://pazaresosset.es">pazaresosset.es</a> للاطلاع على الأعمال الفنية والمحتوى الإضافي للفنانة.</li>
</ol>
<blockquote>
<p><em>«الموسيقى هي صوت الروح الذي يذكّر المادة بأصلها المكون من نور خالص.»</em></p>
</blockquote>""",

    "ru": """<p>Опыт книги <em>«Мой друг Иисус Христос»</em> не ограничивается печатным текстом: с самого начала она задумывалась как <strong>многосенсорное вибрационное произведение</strong>, в котором звук служит прямым проводником внутренней сонастройки.</p>
<hr />
<h3>Музыкальное творчество Марии Пас Арес Оссет</h3>
<p>Каждая глава книги резонирует с музыкальными композициями и звуковыми частотами, созданными <strong>Марией Пас Арес Оссет (Maria Paz Arés Osset)</strong>. Эти мелодии созданы для того, чтобы погрузить ум и сердце в состояние глубокого расслабления, когерентности и открытости.</p>
<p>При прослушивании этих произведений:</p>
<ul>
<li><strong>Мозговая активность замедляется</strong>, переходя в альфа- и тета-состояния, способствуя умиротворению.</li>
<li><strong>Растворяются напряжения</strong> и тяжелые эмоциональные блоки, накопленные в повседневной суете.</li>
<li><strong>Смысл текста интегрируется</strong> на подсознательном и клеточном уровнях через универсальный язык звука.</li>
</ul>
<hr />
<h3>Как погрузиться в звуковой опыт</h3>
<p>Приглашаем вас слушать альбом во время чтения каждой главы или в минуты ежедневного безмолвия и медитации:</p>
<ol>
<li><strong>На Spotify</strong>: Найдите официальные треки альбома и погрузитесь в их возвышающую атмосферу.</li>
<li><strong>На официальном сайте</strong>: Посетите <a href="https://pazaresosset.es">pazaresosset.es</a>, чтобы увидеть художественные работы и дополнительные материалы автора.</li>
</ol>
<blockquote>
<p><em>«Музыка — это голос души, напоминающий материи о её происхождении из чистого Света.»</em></p>
</blockquote>""",

    "vi": """<p>Trải nghiệm của <em>Người bạn Giê-su của tôi</em> không dừng lại ở những dòng chữ: tác phẩm được tạo ra như một <strong>tuyệt tác đa giác quan và rung động</strong>, nơi âm thanh đóng vai trò là nhịp cầu trực tiếp dẫn lối cho sự hòa hợp nội tâm.</p>
<hr />
<h3>Sáng tác âm nhạc của Maria Paz Arés Osset</h3>
<p>Mỗi chương sách đều hòa quyện với những bản nhạc và tần số âm thanh do <strong>Maria Paz Arés Osset</strong> sáng tác. Những giai điệu này được thiết kế để dẫn dắt tâm trí và trái tim vào trạng thái thư thái sâu sắc, kết nối và rộng mở.</p>
<p>Khi lắng nghe những giai điệu này:</p>
<ul>
<li><strong>Nhịp sóng não chậm lại</strong> chuyển sang trạng thái Alpha và Theta, giúp đạt tới sự bình an sâu sắc.</li>
<li><strong>Mọi căng thẳng</strong> và gánh nặng cảm xúc tích tụ hàng ngày tan biến.</li>
<li><strong>Thông điệp của cuốn sách được thẩm thấu</strong> vào tiềm thức và tế bào qua ngôn ngữ âm thanh vũ trụ.</li>
</ul>
<hr />
<h3>Cách trải nghiệm hành trình âm thanh</h3>
<p>Trân trọng mời bạn lắng nghe album trong khi đọc từng chương hoặc trong những phút giây tĩnh lặng mỗi ngày:</p>
<ol>
<li><strong>Trên Spotify</strong>: Tìm kiếm các bản nhạc chính thức của album và đắm mình trong không gian âm nhạc thiêng liêng.</li>
<li><strong>Trên Website chính thức</strong>: Truy cập <a href="https://pazaresosset.es">pazaresosset.es</a> để thưởng thức các tác phẩm hội họa và nội dung độc quyền từ nghệ sĩ.</li>
</ol>
<blockquote>
<p><em>«Âm nhạc là tiếng nói của tâm hồn, nhắc nhở vật chất về nguồn cội Ánh Sáng thuần khiết.»</em></p>
</blockquote>""",

    "ko": """<p><em>«나의 친구 예수 그리스도»</em>의 체험은 활자에만 머물지 않습니다. 이 책은 기획 단계부터 소리가 내면의 주파수를 조율하는 직접적인 통로가 되는 <strong>다감각적·진동적 예술 작품</strong>으로 창작되었습니다.</p>
<hr />
<h3>마리아 파스 아레스 오셋(Maria Paz Arés Osset)의 음악 창작</h3>
<p>책의 각 장은 <strong>Maria Paz Arés Osset</strong>이 작곡한 음악과 음파 주파수와 깊이 공명합니다. 이 선율들은 마음과 가슴을 깊은 이완과 조화, 열림의 상태로 안내하도록 설계되었습니다.</p>
<p>이 음악을 감상할 때:</p>
<ul>
<li><strong>뇌파가 알파파와 세타파 상태로 안정</strong>되어 깊은 성찰과 평온을 누릴 수 있습니다.</li>
<li><strong>일상에서 쌓인 긴장감과 무거운 감정의 잔재</strong>가 씻은 듯이 사라집니다.</li>
<li><strong>소리라는 우주 공용어를 통해</strong> 책의 메시지가 잠재의식과 세포 수준에서 통합됩니다.</li>
</ul>
<hr />
<h3>음악 여정을 즐기는 방법</h3>
<p>각 장을 읽을 때나 매일의 묵상 및 침묵의 시간에 이 앨범을 함께 감상하시기를 권합니다:</p>
<ol>
<li><strong>Spotify에서</strong>: 앨범의 공식 트랙을 검색하여 영혼을 감싸는 평온한 분위기에 젖어보세요.</li>
<li><strong>공식 웹사이트에서</strong>: <a href="https://pazaresosset.es">pazaresosset.es</a>를 방문하여 작가의 최신 소식과 시각 예술 작품을 만나보세요.</li>
</ol>
<blockquote>
<p><em>«음악은 물질에게 그것이 순수한 빛에서 비롯되었음을 일깨워주는 영혼의 목소리이다.»</em></p>
</blockquote>""",

    "pt": """<p>A experiência de <em>O Meu Amigo Jesus Cristo</em> não se limita às palavras escritas: foi concebida desde a sua génese como uma <strong>obra multissensorial e vibratória</strong>, onde o som atua como um veículo direto de sintonização interior.</p>
<hr />
<h3>A Criação Musical de Maria Paz Arés Osset</h3>
<p>Cada capítulo do livro ressoa com composições musicais e frequências sonoras criadas por <strong>Maria Paz Arés Osset</strong>. Estas melodias foram criadas para conduzir a mente e o coração a um estado de relaxamento profundo, coerência e abertura.</p>
<p>Ao escutar estas peças musicais:</p>
<ul>
<li><strong>O ritmo cerebral abranda</strong> para estados alfa e theta, facilitando a introspeção e a paz.</li>
<li><strong>Dissolvem-se as tensões</strong> e as cargas emocionais densas acumuladas no quotidiano.</li>
<li><strong>A mensagem do texto é integrada</strong> a nível subconsciente e celular através da linguagem universal do som.</li>
</ul>
<hr />
<h3>Como Viver a Experiência Sonora</h3>
<p>Convidamo-lo a escutar o álbum enquanto lê cada capítulo ou durante os seus momentos diários de meditação e silêncio:</p>
<ol>
<li><strong>No Spotify</strong>: Procure as faixas oficiais do álbum e mergulhe nas suas atmosferas envolventes.</li>
<li><strong>No Site Oficial</strong>: Visite <a href="https://pazaresosset.es">pazaresosset.es</a> para aceder a todas as novidades, arte visual e conteúdos adicionais da autora.</li>
</ol>
<blockquote>
<p><em>«A música é a voz da alma que recorda à matéria a sua origem de pura Luz.»</em></p>
</blockquote>""",

    "ja": """<p>『私の友人イエス・キリスト』の体験は、活字にとどまりません。本書は当初より、音が内なる波長を調和させる直接の乗り物となる<strong>多感覚的・波動的アート作品</strong>として構想されました。</p>
<hr />
<h3>マリア・パス・アレス・オセットによる音楽創造</h3>
<p>本書の各章は、<strong>Maria Paz Arés Osset</strong>が創り出した楽曲や周波数と響き合っています。これらのメロディは、心と脳を深いリラクゼーション、コヒーレンス、そして受容の状態へと導くように設計されています。</p>
<p>これらの楽曲を聴くことで：</p>
<ul>
<li><strong>脳波がアルファ波やシータ波へと穏やかに低下</strong>し、深い内省と静寂がもたらされます。</li>
<li><strong>日々の生活で蓄積された緊張や重たい感情</strong>が優しく溶きほぐされます。</li>
<li><strong>音という宇宙共通の言語を通じて</strong>、メッセージが潜在意識と細胞レベルに浸透します。</li>
</ul>
<hr />
<h3>サウンド体験の楽しみ方</h3>
<p>各章を読み進める際や、日々の瞑想と静寂の時間にぜひアルバムをお聴きください：</p>
<ol>
<li><strong>Spotifyで聴く</strong>：アルバムの公式トラックを検索し、包み込むような美しいサウンドスケープに浸ってください。</li>
<li><strong>公式サイトを訪れる</strong>：<a href="https://pazaresosset.es">pazaresosset.es</a> にアクセスして、著者の絵画作品や最新コンテンツをご覧ください。</li>
</ol>
<blockquote>
<p><em>「音楽とは、物質に対して自らが純粋な光から生まれたことを思い起こさせる魂の声である。」</em></p>
</blockquote>"""
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

translations["15_musica_frecuencias.html"] = {
    "h1": TITLES_15,
    "body": BODY_15
}

# ----------------------------------------------------
# CHAPTER 17 TRANSLATIONS (11 LANGUAGES)
# ----------------------------------------------------
BODY_17 = {
    "es": html_17_es,
    "en": """<p>To ground the teachings of the book into a living experience in your daily life, here is a simple three-step practice for quantum alignment:</p>
<hr />
<h3>1. The Observer's Pause (Conscious Silence)</h3>
<ul>
<li>Find a quiet moment at the beginning or end of your day.</li>
<li>Close your eyes and take three slow, deep breaths, breathing in tranquility and releasing any worry.</li>
<li>Become the neutral «observer» of your thoughts without judgment. Remember: you are not the mental noise; you are the conscious space in which the noise arises.</li>
</ul>
<hr />
<h3>2. Frequency Realignment (The Breath of Abwoon)</h3>
<ul>
<li>Gently bring your focus to the center of your chest (heart coherence).</li>
<li>Recall a genuine feeling of gratitude, appreciation, or sincere love.</li>
<li>Feel how this emotion instantly elevates your vibrational state and dissolves heaviness and fear.</li>
</ul>
<hr />
<h3>3. Inquiries for Your Inner Journal</h3>
<p>Take a few minutes to reflect or write in your notebook:</p>
<ol>
<li><em>In what everyday situations do I feel my vibration dropping, and how can I choose to respond with love?</em></li>
<li><em>Is there a bond from the past that I am ready to dissolve through conscious forgiveness today?</em></li>
<li><em>How can I be a living reflection of Light and Presence for those around me?</em></li>
</ol>
<hr />
<blockquote>
<p><em>«Peace is not the absence of movement in the outer world, but the unshakable presence of Light within you.»</em></p>
</blockquote>""",

    "fr": """<p>Pour ancrer les enseignements du livre dans votre quotidien, voici une pratique simple d'alignement quantique en trois étapes :</p>
<hr />
<h3>1. La Pause de l'Observateur (Silence Conscient)</h3>
<ul>
<li>Trouvez un moment de calme au début ou à la fin de votre journée.</li>
<li>Fermez les yeux et prenez trois respirations lentes et profondes, en inspirant la paix et en expirant toute inquiétude.</li>
<li>Devenez l'« observateur » neutre de vos pensées sans les juger. Souvenez-vous : vous n'êtes pas le bruit mental, vous êtes l'espace conscient dans lequel le bruit apparaît.</li>
</ul>
<hr />
<h3>2. Le Réalignement de Fréquence (Le Souffle d'Abwoon)</h3>
<ul>
<li>Portez doucement votre attention au centre de votre poitrine (cohérence cardiaque).</li>
<li>Évoquez un sentiment authentique de gratitude, d'appréciation ou d'amour sincère.</li>
<li>Ressentez comment cette émotion élève instantanément votre état vibratoire et dissout la lourdeur et la peur.</li>
</ul>
<hr />
<h3>3. Questions pour votre Journal Intérieur</h3>
<p>Prenez quelques minutes pour méditer ou écrire :</p>
<ol>
<li><em>Dans quelles situations quotidiennes ma fréquence a-t-elle tendance à baisser, et comment puis-je choisir de répondre avec amour ?</em></li>
<li><em>Y a-t-il un lien du passé que je suis prêt à dissoudre par le pardon conscient aujourd'hui ?</em></li>
<li><em>Comment puis-je être un reflet vivant de Lumière et de Présence pour ceux qui m'entourent ?</em></li>
</ol>
<hr />
<blockquote>
<p><em>« La paix n'est pas l'absence de mouvement dans le monde extérieur, mais la présence inébranlable de la Lumière en vous. »</em></p>
</blockquote>""",

    "it": """<p>Per radicare gli insegnamenti del libro nella vita di tutti i giorni, ecco una semplice pratica di allineamento quantistico in tre passi:</p>
<hr />
<h3>1. La Pausa dell'Osservatore (Silenzio Consapevole)</h3>
<ul>
<li>Trova un momento di quiete all'inizio o alla fine della giornata.</li>
<li>Chiudi gli occhi e fai tre respiri lenti e profondi, inspirando calma ed espirando ogni preoccupazione.</li>
<li>Diventa l'«osservatore» neutrale dei tuoi pensieri senza giudicarli. Ricorda: tu non sei il rumore mentale, sei lo spazio cosciente in cui il rumore accade.</li>
</ul>
<hr />
<h3>2. Il Riallineamento di Frequenza (Il Respiro di Abwoon)</h3>
<ul>
<li>Porta dolcemente l'attenzione al centro del petto (coerenza cardiaca).</li>
<li>Evoca un ricordo o un sentimento genuino di gratitudine, apprezzamento o amore sincero.</li>
<li>Senti come questa emozione innalza all'istante il tuo stato vibrazionale e dissolve ogni pesantezza o timore.</li>
</ul>
<hr />
<h3>3. Domande per il tuo Quaderno Interiore</h3>
<p>Dedica qualche minuto a riflettere o a scrivere:</p>
<ol>
<li><em>In quali situazioni quotidiane sento calare la mia frequenza, e come posso scegliere di rispondere con amore?</em></li>
<li><em>C'è un legame del passato che sono pronto a sciogliere oggi attraverso il perdono consapevole?</em></li>
<li><em>Come posso essere un riflesso vivente di Luce e Presenza per chi mi circonda?</em></li>
</ol>
<hr />
<blockquote>
<p><em>«La pace non è l'assenza di movimento nel mondo esterno, ma l'incrollabile presenza della Luce dentro di te.»</em></p>
</blockquote>""",

    "zh": """<p>为了将书中的教导转化为日常生活中的鲜活体验，建议您进行以下三步量子对齐练习：</p>
<hr />
<h3>1. 观察者之静（觉知静默）</h3>
<ul>
<li>在清晨或夜晚寻找一段静谧时光。</li>
<li>闭上双眼，做三次深长缓慢的呼吸，吸入宁静，呼出所有担忧。</li>
<li>成为不加评判的“观察者”。请记住：您不是大脑的杂念，您是杂念升起并消逝的觉知空间。</li>
</ul>
<hr />
<h3>2. 频率重新校准（Abwoon 的气息）</h3>
<ul>
<li>将注意力轻轻移至胸部中央（心脑共振区）。</li>
<li>唤起一份真诚的感激、赞赏或由衷的爱。</li>
<li>感受这种情感如何瞬间提升您的振动状态，消融所有的沉重与恐惧。</li>
</ul>
<hr />
<h3>3. 内省日志反思问题</h3>
<p>花几分钟静心思考或在笔记本上写下：</p>
<ol>
<li><em>在日常生活的哪些情境中我的振动频率容易下降，我又该如何选择以爱回应？</em></li>
<li><em>今天我是否准备好通过有意识的宽恕，切断来自过去的沉重纽带？</em></li>
<li><em>我该如何成为身边人眼中鲜活的光与临在的映照？</em></li>
</ol>
<hr />
<blockquote>
<p><em>“和平并非外在世界的止步不前，而是你内在光芒的坚不可摧。”</em></p>
</blockquote>""",

    "ar": """<p>لترسيخ تعاليم الكتاب وتحويلها إلى تجربة حية في يومك، نقترح عليك هذا التمرين البسيط للمحاذاة الكمية في ثلاث خطوات:</p>
<hr />
<h3>1. وقفة المراقب (الصمت الواعي)</h3>
<ul>
<li>ابحث عن لحظة هدوء في بداية اليوم أو نهايته.</li>
<li>أغمض عينيك وخذ ثلاثة أنفاس عميقة وبطيئة، مستنشقاً السكينة وطارداً أي قلق.</li>
<li>كن «المراقب» المحايد لأفكارك دون إطلاق أحكام. تذكر أنك لست الضجيج العقلي؛ بل أنت الفضاء الواعي الذي يحدث فيه هذا الضجيج.</li>
</ul>
<hr />
<h3>2. إعادة ضبط التردد (نَفَس أبون)</h3>
<ul>
<li>وجّه انتباهك برفق إلى مركز صدرك (تماسك القلب).</li>
<li>استحضر شعوراً حقيقياً بالامتنان أو التقدير أو الحب الصادق.</li>
<li>اشعر كيف يرفع هذا الشعور حالتك الاهتزازية على الفور ويبدد مشاعر الثقل والخوف.</li>
</ul>
<hr />
<h3>3. أسئلة لدفتر تأملاتك الداخلي</h3>
<p>خصص بضع دقائق للتفكير أو الكتابة:</p>
<ol>
<li><em>في أي مواقف يومية أشعر بانخفاض ترددي الاهتزازي، وكيف يمكنني أن أختار الاستجابة بمحبة؟</em></li>
<li><em>هل هناك أي رابط من الماضي أنا مستعد لتحريره اليوم من خلال المغفرة الواعية؟</em></li>
<li><em>كيف يمكنني أن أكون انعكاساً حياً للنور والحضور لمن حولي؟</em></li>
</ol>
<hr />
<blockquote>
<p><em>«السلام ليس غياب الحركة في العالم الخارجي، بل هو الحضور الراسخ للنور في داخلك.»</em></p>
</blockquote>""",

    "ru": """<p>Чтобы воплотить учения книги в живой повседневный опыт, предлагаем простую трехшаговую практику квантовой сонастройки:</p>
<hr />
<h3>1. Пауза наблюдателя (Осознанное безмолвие)</h3>
<ul>
<li>Найдите несколько минут тишины в начале или в конце дня.</li>
<li>Закройте глаза и сделайте три медленных глубоких вдоха, впуская покой и отпуская тревоги.</li>
<li>Станьте нейтральным «наблюдателем» своих мыслей без осуждения. Помните: вы не ментальный шум, вы — пространство сознания, в котором этот шум возникает.</li>
</ul>
<hr />
<h3>2. Перенастройка частоты (Дыхание Абвуна)</h3>
<ul>
<li>Мягко направьте внимание в центр груди (сердечная когерентность).</li>
<li>Вызовите искреннее чувство благодарности, признательности или любви.</li>
<li>Почувствуйте, как это чувство мгновенно повышает вашу вибрацию и растворяет страх и тяжесть.</li>
</ul>
<hr />
<h3>3. Вопросы для внутреннего дневника</h3>
<p>Уделите несколько минут размышлению или записи:</p>
<ol>
<li><em>В каких повседневных ситуациях моя частота падает, и как я могу ответить любовью?</em></li>
<li><em>Есть ли связь из прошлого, которую я готов отпустить сегодня через осознанное прощение?</em></li>
<li><em>Как я могу быть живым отражением Света и Присутствия для окружающих?</em></li>
</ol>
<hr />
<blockquote>
<p><em>«Мир — это не отсутствие движения во внешнем мире, а непоколебимое присутствие Света внутри вас.»</em></p>
</blockquote>""",

    "vi": """<p>Để biến những lời dạy thành trải nghiệm sống động trong cuộc sống hàng ngày, chúng tôi gợi ý bài thực hành lượng tử ba bước đơn giản này:</p>
<hr />
<h3>1. Khoảng lặng của Người quan sát (Tĩnh lặng Tỉnh thức)</h3>
<ul>
<li>Tìm một khoảnh khắc yên tĩnh vào đầu hoặc cuối ngày.</li>
<li>Nhắm mắt lại và hít thở sâu, chậm rãi ba lần, hít vào sự bình an và thở ra mọi lo âu.</li>
<li>Trở thành «người quan sát» vô tư đối với suy nghĩ mà không phán xét. Bạn không phải là dòng suy nghĩ ồn ào; bạn là không gian nhận biết nơi những suy nghĩ đó diễn ra.</li>
</ul>
<hr />
<h3>2. Điều chỉnh lại Tần số (Hơi thở Abwoon)</h3>
<ul>
<li>Nhẹ nhàng đưa sự chú ý vào giữa lồng ngực (sự đồng điệu của trái tim).</li>
<li>Gợi lại cảm giác chân thành về lòng biết ơn, trân trọng hoặc tình yêu thương.</li>
<li>Cảm nhận cảm xúc này nâng cao trạng thái rung động của bạn ngay lập tức, xua tan mọi nặng nề và sợ hãi.</li>
</ul>
<hr />
<h3>3. Câu hỏi cho Nhật ký Nội tâm</h3>
<p>Dành vài phút suy ngẫm hoặc viết vào sổ:</p>
<ol>
<li><em>Trong những tình huống nào tần số của tôi bị giảm sút, và tôi có thể chọn đáp lại bằng tình yêu như thế nào?</em></li>
<li><em>Có mối ràng buộc quá khứ nào tôi đã sẵn sàng buông bỏ bằng sự tha thứ tỉnh thức hôm nay không?</em></li>
<li><em>Làm thế nào để tôi trở thành hiện thân sống động của Ánh Sáng và Sự Hiện Diện cho những người xung quanh?</em></li>
</ol>
<hr />
<blockquote>
<p><em>«Bình an không phải là sự thiếu vắng chuyển động ở thế giới bên ngoài, mà là sự hiện diện bất biến của Ánh Sáng bên trong bạn.»</em></p>
</blockquote>""",

    "ko": """<p>책의 가르침을 일상에서 살아 숨 쉬는 생생한 체험으로 만들기 위해, 3단계 양자 정렬 명상법을 권합니다:</p>
<hr />
<h3>1. 관찰자의 멈춤 (의식적 침묵)</h3>
<ul>
<li>하루의 시작이나 끝에 고요한 시간을 마련합니다.</li>
<li>눈을 감고 세 번의 깊고 느린 호흡을 하며, 평온을 들이마시고 모든 근심을 내보냅니다.</li>
<li>판단 없이 생각의 중립적인 «관찰자»가 됩니다. 기억하세요: 당신은 생각의 소음이 아니라, 그 소음이 일어나는 고요한 의식의 공간입니다.</li>
</ul>
<hr />
<h3>2. 주파수 재조율 (아브운의 숨결)</h3>
<ul>
<li>가슴 정중앙으로 부드럽게 의식을 집중합니다(심장 코히어런스).</li>
<li>진심 어린 감사, 존중, 또는 순수한 사랑의 감정을 떠올립니다.</li>
<li>이 감정이 어떻게 순식간에 진동 상태를 끌어올리고 무거운 두려움을 녹여내는지 느껴보세요.</li>
</ul>
<hr />
<h3>3. 내면 일기를 위한 성찰 질문</h3>
<p>잠시 시간을 내어 다음 질문을 성찰하거나 기록해 봅니다:</p>
<ol>
<li><em>나의 진동 주파수가 낮아지는 일상의 순간은 언제이며, 어떻게 사랑으로 반응할 수 있을까요?</em></li>
<li><em>오늘 의식적인 용서를 통해 끊어낼 준비가 된 과거의 얽힘이 있나요?</em></li>
<li><em>내 주변 사람들에게 어떻게 빛과 현존의 살아있는 통로가 될 수 있을까요?</em></li>
</ol>
<hr />
<blockquote>
<p><em>«평화란 외부 세계의 움직임이 멈추는 것이 아니라, 당신 내면에 빛이 흔들림 없이 현존하는 것입니다.»</em></p>
</blockquote>""",

    "pt": """<p>Para ancorar os ensinamentos do livro numa experiência viva no seu dia a dia, sugerimos esta prática simples de alinhamento quântico em três passos:</p>
<hr />
<h3>1. A Pausa do Observador (Silêncio Consciente)</h3>
<ul>
<li>Encontre um momento de tranquilidade no início ou no fim do dia.</li>
<li>Feche os olhos e respire fundo e devagar três vezes, inspirando serenidade e libertando qualquer preocupação.</li>
<li>Torne-se o «observador» neutro dos seus pensamentos, sem julgamentos. Lembre-se: você não é o ruído mental; é o espaço consciente no qual o ruído acontece.</li>
</ul>
<hr />
<h3>2. O Realinhamento de Frequência (O Sopro de Abwoon)</h3>
<ul>
<li>Leve suavemente a sua atenção para o centro do peito (coerência cardíaca).</li>
<li>Evoque um sentimento genuíno de gratidão, apreço ou amor sincero.</li>
<li>Sinta como essa emoção eleva instantaneamente o seu estado vibracional e dissolve o medo e a sensação de peso.</li>
</ul>
<hr />
<h3>3. Perguntas para o seu Caderno Interior</h3>
<p>Dedique alguns minutos para refletir ou escrever no seu diário:</p>
<ol>
<li><em>Em que situações do dia a dia sinto que a minha frequência baixa, e como posso escolher responder com amor?</em></li>
<li><em>Existe algum laço do passado que eu esteja pronto para dissolver através do perdão consciente hoje?</em></li>
<li><em>Como posso ser um reflexo vivo de Luz e Presença para as pessoas ao meu redor?</em></li>
</ol>
<hr />
<blockquote>
<p><em>«A paz não é a ausência de movimento no mundo exterior, mas a presença inabalável da Luz no seu interior.»</em></p>
</blockquote>""",

    "ja": """<p>本書の教えを日々の生活の中で生き生きと実践するために、3つのステップで行う量子アライメント（調和）のワークをおすすめします：</p>
<hr />
<h3>1. 観察者の静止（自覚的な静寂）</h3>
<ul>
<li>一日の始まりや終わりに、静かな時間を見つけます。</li>
<li>目を閉じ、ゆっくりと深呼吸を3回行い、平穏を吸い込み、すべての不安を吐き出します。</li>
<li>判断を下さずに、自らの思考のニュートラルな「観察者」になります。思い出してください：あなたは頭の中の雑音ではなく、その雑音が現れては消える静寂の空間そのものです。</li>
</ul>
<hr />
<h3>2. 周波数の再調整（アブウーンの息吹）</h3>
<ul>
<li>意識を優しく胸の中央（心臓のコヒーレンス領域）に向けます。</li>
<li>心からの感謝、慈しみ、あるいは純粋な愛の感情を思い起こします。</li>
<li>その感情が一瞬であなたの波動を高め、重苦しさや恐れを溶かしていくのを感じてください。</li>
</ul>
<hr />
<h3>3. 内なるジャーナルのための問いかけ</h3>
<p>数分間静かに内省し、ノートに書き留めてみましょう：</p>
<ol>
<li><em>日常のどんな場面で自分の波動が下がりがちでしょうか。どのように愛を持って応答することを選べるでしょうか？</em></li>
<li><em>今日、意識的な許しを通じて解き放つ準備ができている過去の執着はありますか？</em></li>
<li><em>周囲の人々にとって、どのようにして光と至高の存在（プレゼンス）の生きた鏡になれるでしょうか？</em></li>
</ol>
<hr />
<blockquote>
<p><em>「平和とは外の世界の動きが止むことではなく、あなたの内側に光が揺るぎなく存在することである。」</em></p>
</blockquote>"""
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

translations["17_guia_meditacion.html"] = {
    "h1": TITLES_17,
    "body": BODY_17
}

print("14, 15, 17 prepared.")
