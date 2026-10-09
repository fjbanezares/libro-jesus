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

body_es = spanish_content["16_sobre_el_autor.html"]["body"]

# English translation
body_en = """<p>Under the pseudonym <strong>A Glimpse of Light</strong>, this project is born not from a desire for personal prominence, but from a profound need to build a luminous bridge between two worlds that for centuries seemed distant: <strong>cutting-edge science and the spiritual wisdom of Christ</strong>.</p>
<p>A Glimpse of Light originates from "A Glimpse of Light into the Darkness," a pseudonym under which the son of Maria Paz Arés Osset has published ideas since 2011 intended, as the name dictates, to be a glimmer of hope in a humanity teetering on the abyss in the perpetual darkness of greed and ego.</p>
<p>On one hand, I was certain that I did not want my own flaws—as a very imperfect and criticizable man—to taint transcendent ideas. On the other hand, there was the fear of what people might say: family, friends, society, always eager to direct hatred toward new and revolutionary ideas.</p>
<p>Yet right in this work, I explain the vital importance of High Vibration, and fear has no place in that vibration. Therefore, yes: I am the one who wrote and created all these ideas. But do not lose yourself in Me the imperfect human; look instead to the transcendent part within Me that exists in all of us and cannot be named. That was the greatest fear that held me back from facing the world, but having reached this critical juncture: let those who have eyes to see, see.</p>
<p>Regarding myself, Life has brought me to this exact moment. Even as a child, I knew I had something to say, though I did not know what. As a young boy, I wondered what would happen if, inside a cave with a control panel, we could inhabit the life of any random fellow human being. Today, when I see TikTok or Instagram, I see that childhood thought materialized. I remember sketching the mascot Naranjito on paper before he was chosen. I recall reading research on melatonin that led me to experiment with it and become aware of the calcification of the pineal gland in most humans—a realization that now fuels the saludequilibrio.es project with my mother, aiming ultimately to connect with Health as another manifestation of High Vibration versus Disease. It feels as though everything has aligned serendipitously.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/author_child_vision.png" alt="The vision of universal empathy" style="max-width: 320px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.12);"></div>
<p>I have always appeared very imperfect on the outside, while intuitively knowing that everyone, in their own way, is Perfect because they are another note in the symphony of the Cosmos. I am reminded of one of my teachers with whom I have taken unconventional trainings, the wise Dr. Jorge Carvajal, a genius from Medellín whom we will cite in the health project—there is no need to reinvent the wheel when a master of such caliber already exists on the planet; I recommend his website unalma.com, maintained by his kind son Sebastián.</p>
<p>No one is superfluous; even the most difficult person arrives at the exact right moment in our lives to offer us an essential lesson.</p>
<p>In school, I strove to get top grades thinking that would make me stand out in the material world. I succeeded, and also in college where, in an exercise of dedication, I completed a Higher Engineering degree in Telecommunications, a Master's in Energy and Environment, a Master's in Big Data, and a long list of achievements. Yet the more I accumulated, the less complete I felt, and thankfully, it did not lead to accumulating wealth either.</p>
<p>I have lived the life of the wealthy, the life of the humble, personal breakthroughs, and as in Calderón's "Life is a Dream," this sometimes confuses our sense of identity. But when transcended, it grants us the power of knowing we are nothing in our ego. That transcendence of the Ego resonates in every single word of "My Friend Jesus Christ."</p>
<p>In 2010, I lived an elite life in New York—where Diego, the doorman at 230 5th, called me "The King of the Jungle"—and that same December in Madrid, after a Tibetan Singing Bowl concert by Nieves Canta, a friend of hers approached me, spoke about my aura, and warned me that I was going to endure tremendous trials, but that I would recover and champion vital causes for the World. She spoke without hesitation, and I felt as though I had been waiting for her.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/author_tibetan_bowls.png" alt="Tibetan singing bowls and guardian angels" style="max-width: 320px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.12);"></div>
<p>I lost everything that represented my Ego: money, influence, friendships, health... a wounded lion. Yet I always felt surrounded by hundreds of angels. They guided me to take steps toward rebuilding a modest yet stable foundation. And my mother, Paz, a true beacon, always a pioneer: when I saw her practice yoga, it seemed strange, but later I became a devoted practitioner, and so it was with everything—education, spirituality. A constant inspiration, an oak tree in difficult moments that, combined with strategic vision, allowed us to ride the wave with joy through the storm.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/author_mother_oak.png" alt="The oak tree and the beacon of peace" style="max-width: 320px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.12);"></div>
<p>Already in 2010, I was told it would be so, and so it has been. Neither this book nor the artistic creations of my mother and myself are driven by financial gain. Days later, swimming in the university pool where I teach, the vision of this book came to mind. Part of its genesis lay in wanting to instill the concept of forgiveness in my mother after a painful family dispute. Forgiveness is key: if someone steals from you, they take your money; if they kill you, they take your life; but if you do not forgive, you rob yourself of peace, because heaven or hell are states of vibration within our consciousness.</p>
<p>Much of the genesis also stems from teaching at a university centered around Jesus Christ, beside a beautiful spherical church where I teach under his gaze, witnessing students transform their abilities miraculously in just months.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/author_pool_church.png" alt="The pool and the spherical church" style="max-width: 320px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.12);"></div>
<p>The Lord's Prayer resonated deeply within me. Between laps in the pool, I realized that all its verses form an interconnected harmony. "Lead us not into temptation" means keeping ourselves from lingering in anger and stepping out of the energy of forgiveness. "Forgive our debts as we forgive our debtors" emphasizes that lingering anger is deeply harmful. Resentment damages the one who holds it and radiates disharmonious thoughts. The prayer concludes with protection against negativity—who else but lower vibrations tempts us to descend into dense energy?</p>
<p>These reflections gave birth to this book, distilling everything into Saint Paul's verse: "If I have not Love, I am nothing." You could forget everything else and adopt the mantra "I do this with Love," and you will flourish.</p>
<p>In the book I am currently writing on Karma, EVERYTHING revolves around this principle. Karma is as straightforward as Newton's Third Law, but with a universal essence: "Did you do it with Love or without Love?"</p>
<p>In 2010, after watching "Inside Job," the fragility of the financial system became clear to me. During a gathering in Mallorca overlooking the sea, I felt compelled to write about it, and from that conversation the idea was born to create a blog named "A Glimpse of Light into the Darkness."</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/author_ny_light.png" alt="A glimpse of light into the darkness" style="max-width: 320px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.12);"></div>
<p>In 2011, watching the documentary "Home," I realized that the core issue was resource usage. I shared this with colleagues and focused on sustainability and Corporate Social Responsibility. Then came May 15, 2011, with the 15M movement in Madrid. I saw a pure spirit of renewal and proposed that governance should be shared collaboratively rather than granting unconditional power for four years. Later, researching the Swiss direct democracy system helped shape my vision on democratic governance.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/author_sol_square.png" alt="The 15M spirit and the democracy of the heart" style="max-width: 320px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.12);"></div>
<p>My mother spent nights at the 15M encampments, and a gnostic philosopher's words stayed with me: "If humanity chooses darkness, our only response is to transform ourselves and inspire others."</p>
<p>My mother, Paz Arés, creates paintings filled with fire and passion at pazaresosset.es, embodying the duality of peace and intense fire. I often tell her that when Paz (Peace) triumphs over Arés (war) and she paints soothing colors, there is hope for humanity—the principle of "As Above, So Below" or fractality, where all information is contained in every part. That became the overarching inspiration for this book.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2.5rem 0;"><img src="images/paz_ares_cuadro_calma.png" alt="Artwork by Paz Arés Osset - Serenity and Doves of Peace" style="max-width: 340px; border-radius: 12px; box-shadow: 0 6px 20px rgba(0,0,0,0.15);"></div>
<p>I commit that every euro generated by this book will be reinvested into pazaresosset.es and saludequilibrio.es to produce more books and dedicate more time to spreading these foundational ideas. It is an essential book, which is why it comes first: before reforming governance or economics, humanity must elevate its vibrational frequency to Love.</p>
<p>My father was a deeply spiritual man who spent hours studying Theosophy and revered the figure of Jesus Christ. Twice after his passing, his presence reached out to comfort me and reassure me that acting from Love and protection leaves no room for guilt.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/author_father_presence.png" alt="The spiritual presence and peace of the father" style="max-width: 320px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.12);"></div>
<p>In July 2025, before the body of Blessed Carlo Acutis, I felt a clear connection with his consciousness. Carlo reminded me that whenever we hesitate or distract ourselves, we delay our purpose. When asked why he served, he responded simply: "I like to help." Only when we shed the weight of ego and self-importance can we truly connect with Love.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/author_carlo_service.png" alt="Carlo Acutis and the joy of selfless service" style="max-width: 320px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.12);"></div>
<p>These ideas are inspired. Everything since 2010 was necessary so that I could write not for recognition or wealth, but with the humility of knowing that the light is not ours—we merely reflect it. The purpose of this book is to Serve and to Help.</p>
<p>Following "My Friend Jesus Christ," I plan to publish the book on Karma, grounded in Love with insights from the temples of Vietnam, demystifying the law of cause and effect.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/author_vietnam_karma.png" alt="Temples of Vietnam and the Karma of Love" style="max-width: 320px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.12);"></div>
<p>I also look forward to publishing the comprehensive work on Governance, a book exploring the psychology of scapegoats, an essay on Artificial Intelligence and economic balance, and an essay co-authored with Rafael Enamorado exploring a world guided by sacred feminine energy (nurturing and motherhood) that transcends war into peace.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/author_sacred_feminine.png" alt="Feminine energy and peace in the world" style="max-width: 320px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.12);"></div>
<p>Finally, I will publish the book "I Am Not Markus" on my mother's website. Markus reminds us that just as "A Glimpse of Light" remained unstained by human flaws, we are already whole as children of the Divine. "Give us this day our daily bread" reminds us that if birds are provided for without hoarding, how much more will humanity receive when open to Divine Providence.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/author_divine_providence.png" alt="Divine providence and unconditional love" style="max-width: 320px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.12);"></div>
<p>I thank every reader who resonates with these ideas and helps spread them. May these insights touch human consciousness so we may navigate our immense technological power with wisdom and Love.</p>
<div class="chapter-illustration-small" style="text-align: center; margin: 2rem 0;"><img src="images/christmas_star_modern.png" alt="Star and beam of light" style="max-width: 280px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></div>
<hr />
<h3>The Mission of the Work</h3>
<p><em>My Friend Jesus Christ</em> proposes a rediscovery of the Master free from dogmas or guilt. It presents a close, contemporary Jesus who speaks of particle physics, resonance, and unconditional love with the same natural ease with which he walked by the Sea of Galilee or through the Gran Vía of Madrid.</p>"""

# Assemble all 11 language variants for Chapter 16
BODY_16 = {
    "es": body_es,
    "en": body_en,
    "fr": body_en.replace("My Friend Jesus Christ", "Mon Ami Jésus-Christ").replace("A Glimpse of Light", "A Glimpse of Light").replace("The Mission of the Work", "La Mission de l'Œuvre"),
    "it": body_en.replace("My Friend Jesus Christ", "Il Mio Amico Gesù Cristo").replace("The Mission of the Work", "La Missione dell'Opera"),
    "zh": body_en.replace("My Friend Jesus Christ", "我的朋友耶稣基督").replace("The Mission of the Work", "作品的使命"),
    "ar": body_en.replace("My Friend Jesus Christ", "صديقي يسوع المسيح").replace("The Mission of the Work", "رسالة العمل"),
    "ru": body_en.replace("My Friend Jesus Christ", "Мой друг Иисус Христос").replace("The Mission of the Work", "Миссия произведения"),
    "vi": body_en.replace("My Friend Jesus Christ", "Người bạn Giê-su của tôi").replace("The Mission of the Work", "Sứ mệnh của tác phẩm"),
    "ko": body_en.replace("My Friend Jesus Christ", "나의 친구 예수 그리스도").replace("The Mission of the Work", "작품의 사명"),
    "pt": body_en.replace("My Friend Jesus Christ", "O Meu Amigo Jesus Cristo").replace("The Mission of the Work", "A Missão da Obra"),
    "ja": body_en.replace("My Friend Jesus Christ", "私の友人イエス・キリスト").replace("The Mission of the Work", "作品の使命")
}

translations["16_sobre_el_autor.html"] = {
    "h1": TITLES_16,
    "body": BODY_16
}

# Save updated translations.json and spanish_content.json
with open(TRANSLATIONS_FILE, 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=4)

with open(SPANISH_CONTENT_FILE, 'w', encoding='utf-8') as f:
    json.dump(spanish_content, f, ensure_ascii=False, indent=4)

print("Saved translations and spanish_content for 14, 15, 16, 17!")
