import json
import os

def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    translations = load_json('translations.json')
    spanish_content = load_json('spanish_content.json')

    print("Adding Korean content...")

    # Define Korean Content
    korean_content = {
        "00_introduccion.html": {
            "title": "서문: 입자와 진동 사이에서",
            "h1": "서문: 입자와 진동 사이에서",
            "body": """<h2>I. 영혼의 불안</h2>
<p>철이 들 무렵부터, 나는 거대한 석조 사원들에 다가갈 때마다 일종의 불협화음을 느꼈습니다. 그것은 신앙심이 부족해서가 아니었습니다. 오히려 현실의 베일 뒤에 마르지 않는 사랑의 원천이 존재한다고 항상 직감하고 있었습니다. 나의 갈등, 나의 조용한 고뇌는 무한한 하느님에 대한 그 직감과 우리가 그분을 가두려 했던 상자들의 작음 사이의 대조에서 비롯되었습니다.</p>
<p>나는 가톨릭의 품에서 자랐고, 향냄새를 맡으며 전례를 감탄했지만, 곧 그 아름다움은 불편한 감정, 즉 오만함에 의해 흐려졌습니다. 우리가 "진리"를 소유하고 있고 다른 이들은 그렇지 않다는 말을 암묵적으로나 명시적으로 듣는 것은 내 영혼을 아프게 했습니다. 천억 개의 은하계를 창조하신 창조주께서 어떻게 특정 영적 우편번호를 선호하실 수 있겠습니까? 나는 우리가 다른 신앙에 대한 구원을 인정하지 않고, 다른 길로 빛을 찾는 이들을 동정하거나 우월감으로 바라보는 것에서 끔찍한 오만을 범하고 있다고 느꼈습니다. 그 배타성은 역설적으로 가장 비종교적인 행위처럼 보였습니다. 하느님의 자비를 우리 인간의 경계로 제한하는 것이니까요.</p>
<h2>II. 권력 중심부의 그림자들</h2>
<p>하지만 나의 고뇌는 신학을 넘어섰습니다. 역사를 공부하면서 나는 피로 얼룩진 벽들을 마주했습니다. 종교재판, 십자군 전쟁, 파문... 나는 생각하지 않을 수 없었습니다: 어떻게 우리는 "네 이웃을 사랑하라"에서 "네 생각과 다르다면 태워 죽여라"로 가게 되었을까?</p>
<p>수년 동안 이것은 나를 멀어지게 했습니다. 나는 분노를 느꼈습니다. 제도를 보았고 오직 그림자만을 보았습니다. 하지만 시간이 지나고 성숙해지면서 나는 근본적인 것을 이해했습니다. 교회는 여느 인간의 구조와 마찬가지로 사람들로 구성되어 있다는 것입니다. 그리고 사람은 안테나입니다. 권력의 중심에 두려움이 자리 잡을 때, 통제의 욕구가 섬김의 욕구를 넘어설 때, 집단의 진동은 낮아집니다.</p>
<p>종교재판은 하느님의 역사가 아니었으며, 추상적인 "종교"의 역사도 아니었습니다. 그것은 상층부에 자리 잡은 <strong>낮은 진동</strong>의 필연적인 결과였습니다. 권력을 잃을 것에 대한 두려움, 다름에 대한 두려움, 열정으로 위장한 증오... 그 모든 것은 밀도가 높고 무거운 주파수입니다. 그리고 그 밀도가 위계질서를 장악할 때, 그 결과는 고통입니다. 분명한 것은, 내 친구 예수님이라면 결코 허용하지 않았을 일이라는 것입니다. 간음한 여인을 향한 돌을 멈추게 하신 그분은 결코 장작더미에 불을 붙이지 않았을 것입니다.</p>
<p>이것을 이해함으로써 나는 용서할 수 있었습니다. 실패한 것은 "교회"가 아니라, 어두운 시기에 교회를 이끌었던 사람들의 진동이었음을 이해했습니다. 그리고 그 권력의 돔 아래에는 항상 굶주린 이에게 먹을 것을 주고, 슬픈 이를 위로하며, 지도자들의 어둠 속에서도 빛을 계속 밝혀온 수천 명의 사제, 수녀, 평신도들이 높은 진동으로 존재했다는 것을요.</p>
<h2>III. 영혼의 양자 물리학</h2>
<p>나의 결정적인 화해는 과학의 손을 잡고 찾아왔습니다. 나는 항상 양자 물리학에 매료되어 있었습니다. 현실이 보이는 것만큼 견고하지 않다는 것을 알려주는 지식의 분야 말이죠. 그것은 모든 아원자 입자가 동시에 물질이자 파동임을 가르쳐 줍니다. 그것은 구체적인 무엇임과 동시에 순수한 진동, 순수한 가능성입니다.</p>
<p>거기서 모든 것이 딱 맞아떨어졌습니다. 주기도문, 예수님의 가르침들... 그것들은 엄격한 도덕 규범이 아니라, 양자 물리학의 지침서였습니다!</p>
<p>예수님께서 "두려워하지 말라"고 하실 때, 심리적인 명령을 내리시는 것이 아닙니다. "너희 주파수를 낮추지 말라"고 말씀하시는 것입니다. 두려움은 느리고 밀도가 높으며 현실을 수축시키는 진동입니다. 사랑, 평화, 안전... 이것들은 빠르고 확장하며 빛을 창조하는 진동입니다.</p>
<p>나는 "시험에 들지 말게" 하는 것이 사순절에 케이크를 먹는 것이 아님을 이해했습니다. 그것은 낮은 진동의 중력에 끌려가는 유혹입니다. 증오, 복수, 질투, 오만 같은 것들이죠. 미워할 때 당신은 밀도가 높아집니다. 무겁고 고립되며 전체와 단절된 "입자"가 됩니다. 사랑할 때 당신은 "파동"이 되어 확장하고, 우주의 양자장과, 아버지와 연결됩니다.</p>
<h2>IV. 루터와의 커피 한 잔</h2>
<p>이 이해의 여정에서, 나는 종종 16세기의 마르틴 루터와 커피를 마시는 상상을 했습니다. 우리는 좋은 친구가 되었을 것 같습니다. 그는 나를 괴롭혔던 바로 그 오만을 보았습니다. 면죄부를 팔고 대리석 대성당을 짓는 데 너무 몰두한 나머지 복음의 진동을 잊어버린, 밀도 높아진 구조를 보았습니다.</p>
<p>루터는 "구원은 로마에 있지 않고 너의 믿음에 있다"고 말할 용기가 있었습니다. 그리고 나는 21세기의 관점에서 덧붙이고 싶습니다: "구원은 교황을 따르는 것에 달려 있는 것이 아니라, 당신 마음의 주파수에 달려 있다."</p>
<p>만약 당신의 행위가, 당신의 일상이 사랑의 높은 진동으로 이루어져 있다면, 당신이 구원받았다는 것에는 의심의 여지가 없습니다. 왜냐하면 "구원받음"은 죽은 후에 VIP 클럽에 들어가는 티켓이 아니기 때문입니다. 구원받음은 여기, 지금, 천국의 주파수 속에서 사는 것입니다. 근원과 동조하는 것입니다.</p>
<p>불교도든, 무신론자든, 기독교인이든 무조건적인 사랑으로 진동한다면, 그들은 같은 주파수에 있습니다. 그들은 "하느님 안에" 있습니다. 그리고 어떤 교서도, 어떤 법령도 그 물리적이고 영적인 현실을 바꿀 수 없습니다. 구원은 관료주의의 문제가 아니라 공명의 문제입니다.</p>
<h2>V. 승리하는 빛</h2>
<p>그래서 나는 이 책을 씁니다. 종교를 공격하기 위해서가 아니라, 그 진동의 본질을 구출하기 위해서입니다. 제도적 오만함에 대해 느꼈던 그 연민을 치유하고, 사랑으로 씁니다. 나는 종교재판의 어둠을 보는 것을 멈추고 신비가들, 이름 없는 성인들, 같은 신앙의 이름으로 너무나 높게 진동하여 세상을 바꾼 선한 사람들의 빛을 바라봅니다.</p>
<p>이 책은 엄한 재판관으로서가 아니라 진동의 스승으로서 예수님과 함께 걷자는 초대장입니다. 마드리드, 라스 로사스, 콜메나레호 사이를 주파수를 잃지 않고 항해하는 법을 가르쳐 주는 친구. 우리가 빛이고, 파동이며, 우리의 유일한 의무는 우리 주변에서 무슨 일이 일어나든 주파수를 높게 유지하는 것임을 반복해서 상기시켜 주는 안내자.</p>
<p>그러니 사랑하는 독자여, 잠시 물려받은 교리, 죄책감, 두려움을 잊으십시오. 모든 것, 절대적으로 모든 것이 음악이라는 가능성에 마음을 여십시오. 그리고 당신의 손에 가장 아름다운 멜로디를 연주할 악기가 들려 있다는 것을요.</p>
<p>"나의 친구 예수 그리스도"에 오신 것을 환영합니다.</p>"""
        },
        "index.html": {
            "title": "제1장: 마드리드에서의 만남",
            "h1": "제1장: 마드리드에서의 만남",
            "body": """<p>마드리드의 어느 봄날 오후였습니다. 태양은 그란 비아의 건물들 사이로 스며들어, 아스팔트 위에서 춤추는 듯한 빛과 그림자의 유희를 만들어내고 있었습니다. 나는 도시에 사는 사람 특유의 서두름으로 걷고 있었고, 머릿속은 소음으로 가득 차 있었습니다. 답장해야 할 이메일, 청구서, 걱정거리들... 낮게, 아주 낮게 진동하고 있었죠.</p>
<p>갑자기 카야오 광장에서 그를 보았습니다. 그는 튜닉을 입지도, 샌들을 신지도 않았으며, 머리 위에 빛나는 후광도 없었습니다. 낡은 청바지에 흰 티셔츠, 편안한 운동화를 신고 있었습니다. 그는 벤치에 앉아 시간을 멈추게 하는 듯한 평온한 미소로 지나가는 사람들을 바라보고 있었습니다.</p>
<p>— 안녕, 프란시스코 — 내가 가까이 지나가자 그가 말했습니다.</p>
<p>나는 제자리에 멈춰 섰습니다. 거리에서 내 전체 이름을 부르는 사람은 없었고, 낯선 사람은 더더욱 아니었습니다. 하지만 그의 눈을 바라보았을 때, 나는 그가 낯선 사람이 아님을 알았습니다. 그의 눈빛에는 태고적부터의 친숙함이 있었고, 어떤 방어기제도 무장 해제시키는 평화가 있었습니다.</p>
<p>— 예수님? — 나는 조금 우스꽝스럽게 느끼며 물었습니다.</p>
<p>— 바로 나야. — 그가 대답하며 옆 벤치의 빈자리를 툭툭 쳤습니다. — 잠시 앉아. 너는 나조차 두통이 올 정도의 주파수로 진동하고 있어. 내가 꽤 잘 참는데도 말이야.</p>
<p>나는 여전히 어안이 벙벙한 채 자리에 앉았습니다.
— 진동이요? — 내가 되물었습니다.</p>
<p>— 그래, 진동. 모든 것은 진동이야, 내 친구여. 두려움, 서두름, 분노... 이것들은 밀도가 높고 무거운 진동들이야. 그것들은 너를 땅에 묶어두고 하늘을 보지 못하게 해. 바로 머리 위에 있는데도 말이지.</p>
<p>나는 위를 올려다보았습니다. 마드리드의 하늘은 강렬하고 아름다운 푸른색이었습니다. 그때까지 전혀 눈치채지 못했었습니다.</p>
<p>— 너와 며칠 보내려고 왔어. — 그가 계속해서 말했습니다. — 한 바퀴 돌자. 너는 영혼의 라디오를 튜닝하는 법을 기억해야 해. 지금은 순전히 잡음만 듣고 있잖아.</p>
<p>그렇게 마드리드의 소음 한가운데서, 내 인생의 가장 기이하고 경이로운 모험이 시작되었습니다. 물을 포도주로 바꾸는 기적이 아니라, 내 내면의 소음을 음악으로 바꾸는 기적과 함께 말이죠.</p>"""
        },
        "02_capitulo.html": {
            "title": "제2장: 라스 로사스 산책",
            "h1": "제2장: 라스 로사스 산책",
            "body": """<p>다음 날, 우리는 중심가에서 조금 벗어나기로 했습니다. 라스 로사스로 갔습니다. 예수님은 교외 지역, 모든 것이 정돈된 것처럼 보이지만 때로는 방탄문 뒤에 혼돈이 숨어 있는 그곳에서 사람들이 어떻게 사는지 보고 싶어 하셨습니다.</p>
<p>우리는 파리 공원을 걷고 있었습니다. 그는 꽃향기를 맡거나 나무껍질을 만지기 위해 멈춰 섰습니다.
— 이것 봐. — 그가 떡갈나무를 가리키며 말했습니다. — 이 나무는 내일 비가 올지 해가 뜰지 걱정하지 않아. 그저 존재할 뿐이야. 자신의 중심에 있어. 생명의 주파수로 진동하고 있지.</p>
<p>— 나무한테는 쉽겠죠. — 내가 대꾸했습니다. — 주택담보대출이 없으니까요.</p>
<p>예수님은 깔깔 웃으셨습니다. 맑고 전염성 있는 웃음이었습니다.
— 주택담보대출... 현대의 거대한 괴물이군. 봐, 프란시스코, 문제는 은행 빚이 아니야. 문제는 네가 미래에 빚을 지고 있다고 생각하는 거야. 너는 아직 존재하지 않는 시간을 너의 불안으로 미리 지불하며 살고 있어.</p>
<p>우리는 잔디밭에 앉았습니다. 개 한 마리가 달려와 그의 손을 핥았습니다. 그는 다정하게 쓰다듬었습니다.
— "우리에게 일용할 양식을 주시고" — 그가 중얼거렸습니다. — 사람들은 내가 음식 이야기만 한다고 생각해. 나는 <em>지금</em> 필요한 에너지에 대해 말하는 거야. 다음 달을 걱정할 때, 너는 오늘의 에너지를 상상의 문제에 써버리는 거야. 진동을 낮추는 거지. 약해지는 거야.</p>
<p>— 그럼 진동은 어떻게 높이나요? — 이해하기 시작한 느낌을 받으며 물었습니다.</p>
<p>— 감사함으로. — 그가 인공 호수를 바라보며 말했습니다. — 감사는 영혼의 엘리베이터야. 이 햇살, 이 공기, 이 순간에 감사하면... 올라가. 부족한 것에 대해 불평하면... 내려가. 이건 기본적인 영적 물리학이야.</p>
<p>라스 로사스에서, 별장들과 고급 차들 사이에서, 나는 진정한 부가 우리가 소유한 것에 있는 것이 아니라, 이미 그곳에, 모두를 위해 무료로 존재하는 것을 즐기는 능력에 있다는 것을 배웠습니다.</p>"""
        },
        "03_capitulo.html": {
            "title": "제3장: 진동과 침묵",
            "h1": "제3장: 진동과 침묵",
            "body": """<p>우리는 산맥 쪽으로 가는 버스를 탔습니다. 풍경이 바뀌며 더 푸르고 더 거칠어졌습니다. 예수님은 첫 소풍을 가는 아이처럼 창밖을 바라보셨습니다.</p>
<p>— 소음. — 그가 갑자기 말했습니다. — 이 세기의 거대한 질병이야. 자동차 소음이 아니라, 스크린의 소음, 알림의 소음, 끊임없는 의견들의 소음 말이야.</p>
<p>우리는 콜메나레호 전의 중간 지점에 도착했습니다. 흙길에 내렸습니다.
— 침묵을 연습하자. — 그가 제안했습니다.</p>
<p>— 입 다물고있는 거요?</p>
<p>— 입만 다무는 게 아니야. 마음을 침묵시켜야 해. 우주의 진동을 들어보길 바라.</p>
<p>우리는 한 시간 동안 침묵 속에 걸었습니다. 처음엔 내 마음이 생각들을 돌리는 세탁기 같았습니다. "나 여기서 예수 그리스도랑 걷으면서 뭐 하는 거지?", "내가 미쳤나?", "엄마한테 전화해야 하는데..." 하지만 점차 내 발걸음의 리듬과 동행자의 평온한 호흡이 나를 진정시켰습니다.</p>
<p>우리는 지평선이 보이는 높은 곳에 멈췄습니다.
— 눈을 감아. — 그가 속삭였습니다. — 느껴봐.</p>
<p>나는 눈을 감았습니다. 그리고 아주 오랜만에 처음으로, 두려움을 느끼지 않았습니다. 부드럽고 따뜻한 웅웅거림 같은 것을 느꼈습니다. 공기가 나를 안아주는 것처럼요.</p>
<p>— 바로 그거야. — 그가 내 느낌을 읽은 듯이 말했습니다. — 그게 높게 진동하는 거야. 사랑의 주파수지. 영화 속의 로맨틱한 사랑이 아니라, 원자들을 결합시키는 그 사랑(Love)이야. 네가 거기에 있을 때, 아무것도 너를 건드릴 수 없어. "악에서 구하시옵소서"는 악한 자들이 존재하지 않게 해달라는 게 아니야. 악이 너에게 닿지 않는 주파수에 있게 해달라는 거지. 악이 너와 공명하지 않는 곳에.</p>
<p>눈을 떴습니다. 세상이 더 밝아 보였습니다.
— 네가 높게 진동하면, 낮은 것은 너를 보지 못해. — 그가 결론지었습니다. — 마치 어둠에게는 네가 보이지 않는 투명인간이 되는 것과 같아.</p>"""
        },
        "04_capitulo.html": {
            "title": "제4장: 콜메나레호와 자연",
            "h1": "제4장: 콜메나레호와 자연",
            "body": """<p>해 질 녘에 콜메나레호에 도착했습니다. 마을은 도시와 시골의 중간쯤 되는 매력을 지니고 있었습니다. 우리는 대학 근처의 넓은 공간이 있고 공기가 다른 곳으로 향했습니다.</p>
<p>— 여기가 더 기분이 좋군. — 예수님이 깊게 숨을 들이마시며 말했습니다. — 자연은 진동의 위대한 스승이야. 자연은 결코 틀리지 않아. 소나무는 떡갈나무가 되려고 하지 않아. 강은 위로 흐르려고 하지 않지.</p>
<p>우리는 암자 근처에 앉았습니다. 하늘은 주황색과 보라색으로 물들고 있었습니다.
— 하늘에 계신 우리 아버지... — 그가 조용히 읊조리기 시작했습니다. — 프란시스코, 하늘이 어디 있는지 아니?</p>
<p>— 저 위에요? — 내가 손가락으로 가리켰습니다.</p>
<p>그는 웃으며 고개를 저었습니다.
— 하늘은 의식 상태야. 모든 것이 괜찮고, 절대적인 평화가 있는 내면의 장소지. "하늘에 계신"이라는 말은 만물의 근원이 그 높은 진동 속에 거한다는 뜻이야. 그리고 너는 거기에 직접 접속할 수 있어. 너는 창조주와 직통 와이파이가 연결되어 있지만, 가끔 비밀번호를 잊어버리지.</p>
<p>— 비밀번호가 뭔데요?</p>
<p>— 항복(내맡김). 있는 그대로의 것과 싸우기를 멈추는 거야. 받아들이는 것. 흐르는 것. 삶에 항복할 때, 너는 거슬러 헤엄치기를 멈추게 돼. 그러면 흐름이 너를 데려가. 그리고 삶의 흐름은 항상 너를 선한 곳으로, 바다로 데려간다.</p>
<p>콜메나레호에서, 첫 별들이 뜨는 아래, 나는 기도한다는 것이 쇼핑 리스트를 만드는 것처럼 무언가를 요구하는 게 아님을 이해했습니다. 기도는 주파수를 맞추는 것이었습니다. 우리가 소음을 만드느라 너무 바빠 듣지 못하더라도 항상 연주되고 있는 음악을 듣기 위해, 다이얼을 다시 올바른 주파수에 맞추는 일이었습니다.</p>"""
        },
        "05_capitulo.html": {
            "title": "제5장: 주기도문 (제1부: 아버지)",
            "h1": "제5장: 주기도문 (제1부: 아버지)",
            "body": """<p>우리는 마드리드로 돌아왔지만, 이번에는 레티로 공원으로 갔습니다. 우리는 수정궁 근처에 앉았습니다.
— 네 아버지에 대해 이야기해보자. — 예수님이 갑자기 말했습니다.</p>
<p>나는 긴장했습니다. 아버지와의 관계가 항상 순탄했던 건 아니었으니까요.
— 왜요?</p>
<p>— 기도가 "우리 아버지"로 시작하니까. 그리고 많은 사람이 거기서 막혀. 만약 육신의 아버지가 엄격했거나, 부재했거나, 비판적이었다면, 그 이미지를 하느님께 투영해. 하느님을 수염 난 아저씨로, 네가 실수하면 벌주려고 감시하는 사람으로 생각하지.</p>
<p>그는 바닥에서 돌을 집어 연못에 던졌습니다. 파문이 퍼져나갔습니다.
— 아람어로 "아버지"라는 단어, <em>Abwoon</em>은 훨씬 더 넓은 의미를 가지고 있어. 그것은 근원, 기원, 생명의 호흡이야. 아저씨가 아니야. 에너지지. 우리 모두가 나온 원래의 진동이야.</p>
<p>— 그럼, 재판관이 아니란 말인가요?</p>
<p>— 당연히 아니지! — 그가 외쳤습니다. — 태양이 꽃들을 심판하니? "너는 꽃을 피우니 빛을 주고, 너는 아니니 어둠 속에 있어라"라고 하니? 태양은 모두를 위해 빛나. 하느님은 무조건적인 사랑이야. 네가 동굴 속에 틀어박힌다면, 네가 어둠 속에 있는 건 태양의 잘못이 아니야. 너의 선택이지.</p>
<p>— 그럼 왜 "우리"인가요?</p>
<p>— "나의" 것이 아니니까. 어떤 종교나 어떤 사람의 사유재산이 아니야. 모두의 것이지. 기독교인, 불교도, 무신론자, 나무, 그리고 개의 것이야. 우리 모두 같은 근원에서 왔어. 그것을 인식하는 것이 높게 진동하는 첫걸음이야: 바로 통일성(Unity). 네가 남들과 분리되어 있다고 보면 진동이 낮아져. 연결되어 있다고 보면 올라가고.</p>"""
        },
        "06_capitulo.html": {
            "title": "제6장: 주기도문 (제2부: 하늘)",
            "h1": "제6장: 주기도문 (제2부: 하늘)",
            "body": """<p>다시 그란 비아를 걸으며, 화려한 광고판과 쇼핑백을 든 사람들 사이에서 예수님은 위를 가리켰습니다.
— "하늘에 계신". 콜메나레호에서 하늘이 의식 상태라고 말했지. 하지만 하나 더 이해했으면 해.</p>
<p>그는 명품 쇼윈도 앞에 멈춰 섰습니다.
— 사람들은 여기서 하늘(천국)을 찾아. — 그가 비싼 시계들을 가리켰습니다. — 이걸 가지면 행복해질 거라고 믿지. 그 직업을 얻으면, 그 연인을 만나면 천국에 닿을 거라고. 하지만 천국은 네가 가는 장소가 아니라, 네가 살아가는(발 딛고 있는) 장소야.</p>
<p>— 교통 체증과 스트레스가 가득한 여기서 어떻게 천국으로부터 살 수 있죠?</p>
<p>— 천국을 땅으로 가져옴으로써. 그게 너의 임무야. "나라가 임하시오며". 이건 죽어서 구름 있는 좋은 곳에 가기를 기다리는 게 아니야. 지금 여기, 이 장소를 사랑과 평화의 진동과 비슷하게 만드는 거지.</p>
<p>— 어려워 보이는데요.</p>
<p>— 내면을 바꾸지 않고 외부 세계를 바꾸려고 하면 어렵지. 네가 평화롭다면, 네가 감사함으로 진동한다면, 너는 네 주변에 작은 천국의 버블을 만드는 거야. 그리고 많은 사람이 그렇게 하면, 버블들이 합쳐져. 그렇게 왕국이 오는 거야. 군대가 아니라, 평온한 마음들로.</p>
<p>그는 나를 빤히 쳐다보았습니다.
— 너는 통로야. 두려움과 원망으로 더러워져 있으면 빛이 통과하지 못해. 네가 깨끗해지면, 높게 진동하면, 하늘이 너를 통해 땅에 닿아. 프란시스코, 너는 다리(bridge)야. 너희 모두가 그래.</p>"""
        },
        "07_capitulo.html": {
            "title": "제7장: 우리에게 일용할 양식",
            "h1": "제7장: 우리에게 일용할 양식",
            "body": """<p>우리는 마요르 광장에서 오징어 샌드위치를 먹고 있었습니다. 예수님은 세상에서 가장 맛있는 음식을 먹는 것처럼 즐거워하셨습니다.
— 이건 신성해. — 입안 가득 문 채 그가 말했습니다.</p>
<p>— 샌드위치가요?</p>
<p>— 영양을 섭취하는 행위가. "오늘 우리에게 일용할 양식을 주시고".</p>
<p>그는 종이 냅킨으로 입을 닦았습니다.
— 사람들은 결핍에 대한 두려움을 안고 살아. 쌓아두고, 저장하고, 잃을까 봐 두려워해. 그건 결핍의 진동이야. "오늘"의 빵을 구할 때, 너는 내일도 있을 것이라고 신뢰하는 거야.</p>
<p>— 하지만 미리 대비해야죠...</p>
<p>— 대비하는 건 좋아. 미래 때문에 괴로워하며 사는 건 생명(Life)에 대한 믿음 부족이야. 참새들을 봐. — 그가 빵 부스러기를 쪼아 먹는 새들을 가리켰습니다. — 창고도 없는데 먹잖아. 생명은 생명을 지탱해.</p>
<p>— 먹을 게 없는 사람들은요?</p>
<p>그의 얼굴이 조금 어두워졌습니다.
— 그건 빵이 부족해서가 아니야. 이기심이 넘쳐서지. 모두가 관대함 속에서 진동한다면, 모두가 우리가 하나임을 이해한다면, 아무도 굶주리지 않을 거야. 문제는 분배지, 공급이 아니야. 우주는 풍요로워. 결핍을 만들어내는 건 인간의 마음이야.</p>
<p>그는 마지막 한 입을 먹었습니다.
— "빵"은 정보, 지식, 사랑이기도 해. 너를 옭아매는 모든 것이지. 오늘 필요한 것을 구해. 오늘 너의 최고의 버전이 되기 위해. 쌓아두고 안전하다고 느끼기 위해 구하지 마. 유일한 진짜 안전은 근원과의 연결뿐이야.</p>"""
        },
        "08_capitulo.html": {
            "title": "제8장: 용서와 빚",
            "h1": "제8장: 용서와 빚",
            "body": """<p>우리는 다시 라스 로사스의 조용한 곳으로 갔습니다. 예수님은 무거운 주제를 이야기하고 싶어 하셨습니다.
— "우리가 우리에게 죄 지은 자를 사하여 준 것 같이 우리 죄를 사하여 주시옵고".</p>
<p>— 그게 어려운 부분이에요. — 내가 인정했습니다. — 상처 준 사람을 용서한다는 게...</p>
<p>— 어려운 이유는 네가 그것을 상대방에게 베푸는 호의라고 생각하기 때문이야. "착한 내가, 나쁜 너를 용서한다." 그건 에고(Ego)야. 그건 소용없어.</p>
<p>— 그럼요?</p>
<p>— 용서는 개인 위생 행위야. 다른 사람에게 던지려고 쥐고 있던 불타는 석탄을 놓는 거야. 화상을 입는 건 너뿐이지.</p>
<p>그는 돌 벤치에 앉았습니다.
— 원한을 품으면 진동이 아주 낮아져. 보이지 않는 사슬로 그 사람과 그 고통스러운 순간에 너를 묶어버려. 날 수 없어. 나아갈 수 없어. 용서는 사슬을 끊는 거야. "나는 너를 놓아주고 나를 놓아준다. 이제 너에게 빚진 것도 없고, 네가 빚진 것도 없다"라고 말하는 거야.</p>
<p>— 만약 그들이 한 짓이 아주 심각하다면요?</p>
<p>— 아픔은 피할 수 없지만, 고통은 선택이야. 네 마음속에서 그 상처를 계속 되새긴다면, 너는 그것을 계속해서 다시 겪는 거야. 지금 너를 아프게 하는 건 상대가 아니라 너 자신이야. "악에서 구하소서"는 용서하지 않음으로써 네가 스스로 만들어내는 악에서 벗어나는 것부터 시작해.</p>
<p>그가 내 어깨에 손을 얹었습니다.
— 용서한다는 건, 그 상처가 더 이상 너에게 닿지 않을 만큼 높게 진동하는 거야. 상대방이 자신의 무의식에서, 자신의 고통에서 행동했음을 이해하는 거야. "그들은 자기가 하는 일을 알지 못하나이다." 남을 해침으로써 자신에게 얼마나 해를 끼치는지 안다면, 그러지 않았을 거야.</p>"""
        },
        "09_capitulo.html": {
            "title": "제9장: 우리를 시험에 들게 하지 마시옵고 (높은 진동)",
            "h1": "제9장: 우리를 시험에 들게 하지 마시옵고 (높은 진동)",
            "body": """<p>우리는 다시 콜메나레호에 있었고, 록로즈(Rockrose)로 둘러싸인 오솔길을 걷고 있었습니다. 들판 냄새가 강렬했습니다.
— 유혹(시험). — 로즈마리 가지를 꺾으며 예수님이 말했습니다. — 뭐라고 생각하니?</p>
<p>— 초콜릿? 쉽게 버는 돈?</p>
<p>— 그런 건 주의를 흩뜨리는 것들이지. 진짜 유혹은 너의 진동을 낮추는 거야. 두려움, 분노, 절망에 빠지려는 유혹이야.</p>
<p>그는 멈춰 서서 내 눈을 보았습니다.
— "우리를 유혹에 빠지지 않게 하시고"는 "내가 높게 진동하며 유지되도록 도와주소서"라는 뜻이야. 왜냐하면 네가 높게 진동할 때 너는 너의 힘(Power) 안에 있기 때문이지. 떨어지면 연결을 잃어.</p>
<p>— 하지만 화가 날 때는 어쩔 수 없잖아요.</p>
<p>— 감정을 느끼는 건 불가피해, 맞아. 하지만 그 감정 속에 살기로 작정하는 건 선택이야. 유혹은 드라마(비극)를 즐기는 거야. 친구에게 전화해서 상사가 얼마나 나쁘게 굴었는지 열 번째 이야기하면서 다시 그 분노를 느끼는 것. 그게 유혹에 빠지는 거야. 고통받는 것을 선택하는 거야, 왜냐하면 그게 널 중요하게, 피해자로 느끼게 해주니까.</p>
<p>— 그럼 어떻게 피하죠?</p>
<p>— 의식(Consciousness)으로. 떨어질 것 같은 느낌이 들 때, 불평이나 비판을 시작하려 할 때, 멈춰. 숨을 쉬어. 네가 누구인지 기억해. 네가 빛이라는 걸 기억해. 그리고 다시 선택해. 감사를 선택해. 희망을 선택해. 사랑을 선택해. 그게 높게 진동하는 거야. 거기서는 유혹이 힘을 못 써.</p>"""
        },
        "10_capitulo.html": {
            "title": "제10장: 다만 악에서 구하시옵소서 (낮은 진동으로부터의 보호)",
            "h1": "제10장: 다만 악에서 구하시옵소서 (낮은 진동으로부터의 보호)",
            "body": """<p>마드리드에서의 마지막 밤, 우리는 도시가 내려다보이는 테라스로 갔습니다. 아래쪽 불빛들이 전기로 된 별들의 바다처럼 깜빡였습니다.
— 다만 악에서 구하시옵소서. — 교통 체증의 혼돈을 바라보며 내가 속삭였습니다.</p>
<p>— 악은 뿔 달린 괴물이 아니야. — 오렌지 주스를 마시며 예수님이 말했습니다. — 악은 단순히 빛의 부재야. 무의식이지. 너무 낮고 빽빽하게 진동해서 고통만 투사할 수 있는 사람들이야.</p>
<p>— 거기서 어떻게 벗어나죠?</p>
<p>— 싸우지 않음으로써. 어둠과 싸우면 너도 어둠으로 얼룩져. 너는 그 위로 올라감으로써 벗어나는 거야.</p>
<p>그는 손짓으로 도시 전체를 가리켰습니다.
— 네가 독수리라고 상상해봐. 땅에 뱀이 있는데 내려가서 싸우면 물릴 수 있어. 하지만 높이 날면 뱀은 너에게 닿지 못해. "악에서 구하시옵소서"는 높이 날 수 있는 날개를 달라는 기도야. 증오, 시기, 두려움의 진동이 너를 건들 수 없는 곳으로.</p>
<p>— 누가 절 공격하러 오면요?</p>
<p>— 네가 순수한 사랑과 절대적인 평화 속에서 진동하고 있다면, 너의 존재만으로도 상대를 무장 해제시킬 수 있어. 아니면 단순히, 삶이 너를 이동시켜 그와 마주치지 않게 할 거야. 동시성이 너를 보호해. 네가 높게 진동하면, 갈등의 레이더에 보이지 않게 돼. 낮게 진동하는 자들은 너를 "보지" 못해, 그들의 주파수에 네가 공명하지 않으니까. 그냥 지나치게 되지.</p>"""
        },
        "11_capitulo.html": {
            "title": "제11장: 나라와 권능과 영광",
            "h1": "제11장: 나라와 권능과 영광",
            "body": """<p>여행이 끝나가고 있었습니다. 우리는 왕궁 앞 오리엔테 광장의 벤치에 앉아 있었습니다.
— 나라와 권능과 영광이 아버지께 있나이다. — 웅장한 건물을 바라보며 예수님이 말했습니다. — 하지만 저 돌과 경비병들의 왕국은 아니야.</p>
<p>— 그럼 어느 왕국이죠?</p>
<p>— 왕국(나라)은 너의 내면의 평화야. 권능은 무슨 일이 있어도 매 순간 너의 진동을 선택할 수 있는 능력이야. 그리고 영광... 영광은 네가 너 자신임의 기쁨이야. 우주의 자녀라는 기쁨.</p>
<p>그는 일어나서 세상을 끌어안듯 팔을 뻗었습니다.
— 밖에서 힘(권력)을 찾지 마. 박수를 구하지 마. 진짜 힘은 조용해. 그것은 결코 혼자가 아니라는, 생명이 너를 지탱하고 있다는 확신이야. 그걸 이해할 때, 네 세포로 느낄 때, 너는 이미 왕국에 있는 거야. 여기, 지금. 마드리드, 라스 로사스, 콜메나레호 사이에서. 네가 깨어 있다면, 왕국은 네가 있는 곳에 있어.</p>
<p>그는 내 영혼을 꿰뚫는 듯한 강렬함으로 나를 보았습니다.
— 이걸 잊지 마, 프란시스코. 너에겐 힘이 있어. 높게 진동하는 데에 그것을 써. 세상의 너의 구석을 밝히는 데 써. 그게 너의 유일한 임무야.</p>"""
        },
        "12_epilogo.html": {
            "title": "에필로그: 마지막 모험과 작별",
            "h1": "에필로그: 마지막 모험과 작별",
            "body": """<p>예수님은 아토차 역에서 작별 인사를 하셨습니다. 기차를 타신다고 했습니다. 아무 곳도 아니면서 동시에 모든 곳으로 가는 기차를요.
— 또 볼 수 있을까요? — 목이 메어 내가 물었습니다.</p>
<p>— 넌 항상 나를 보고 있어. — 그가 미소 지었습니다. — 나는 슈퍼마켓 계산원의 미소 속에 있어. 콜메나레호의 나무를 흔드는 바람 속에. 네 방의 침묵 속에. 하지만 무엇보다, 나는 네 안에 있어. 네가 높게 진동할 때, 사랑할 때, 용서할 때... 거기에 내가 있어. 거기서 우리는 하나야.</p>
<p>그는 나를 꽉 안아주었습니다. 나무 냄새와 신선한 비 냄새가 났습니다.
— 우리를 시험에 들게 하지 마. — 그가 내 귓가에 속삭였습니다. — 주파수를 유지해, 친구. 음악이 계속 들리게 해. 혹시 음이 이탈되더라도, 자책하지 마. 그냥 다시 조율하면 돼.</p>
<p>그는 뒤돌아 군중 속으로 섞여 들어갔습니다. 청바지에 편안한 걸음걸이로, 스마트폰을 보며 뛰는 사람들 사이로 멀어지는 그를 보았습니다. 그리고 아주 잠시, 역의 홀 전체가 황금빛으로 빛나는 것 같았습니다.</p>
<p>거리로 나왔습니다. 마드리드는 여전했습니다. 시끄럽고, 혼란스럽고, 살아있었죠. 하지만 나는 더 이상 예전의 내가 아니었습니다. 깊게 숨을 쉬고, 얼굴에 닿는 햇살을 느끼며 미소 지었습니다. 나는 높게 진동하고 있었습니다. 그리고 무슨 일이 있어도, 모든 것이 괜찮을 것임을 알았습니다.</p>
<p><strong>끝.</strong></p>"""
        },
        "13_apendice_poema.html": {
            "title": "부록: 크리스마스 시",
            "h1": "부록: 크리스마스 시",
            "body": """<p><strong>높은 주파수의 크리스마스</strong></p>
<p>먼 옛날 차가운 지푸라기에서 아기를 찾지 마라,<br />
바람이 흩어버린 캐럴의 메아리 속에서도 찾지 마라.<br />
그란 비아의 네온사인 아래서도 찾지 마라,<br />
영혼이 헐값에 팔리는 그 구석진 곳에서.  </p>
<p>네 가슴 속에 진동하는 침묵 속에서 찾아라,<br />
사랑이 지은 신성한 성전 안에서.<br />
예수님은 왕관도, 금도, 망토도 두르지 않았으니,<br />
낡은 청바지를 입고 너의 눈물을 닦아준다.  </p>
<p>마드리드를 걷는다, 서두름과 소음 사이로,<br />
누구에게도 두려움 주지 않는 영원한 여행자.<br />
카야오에 앉아 너를 보며 미소 짓는다:<br />
"왜 그리 뛰니? 멈춰서 웃어봐."  </p>
<p>"크리스마스는 날짜도, 저녁 식사도, 선물도 아니야,<br />
나쁜 것을 잊을 만큼 높게 진동하는 거야.<br />
구유는 나무나 건초가 아님을 아는 거야,<br />
희망으로 가득 찬 네 자신의 심장이야."  </p>
<p>두려움 속에 진동하면, 분노 속에 진동하면,<br />
아기는 태어나지 않고, 별은 빛나지 않아.<br />
하지만 용서하면, 포용하면, 사랑하면,<br />
네 안에 가장 순수한 불꽃을 켜는 거야.  </p>
<p>우리를 슬픔의 유혹에 빠지게 하지 마시고,<br />
눈을 들어 아름다움을 보게 하소서.<br />
라스 로사스에서 하늘까지, 콜메나레호에서 바다까지,<br />
유일한 임무는 사랑하는 법을 배우는 것.  </p>
<p>바닥에서 진동하는 무게로부터 우리를 구하시고,<br />
날아오를 수 있는 날개를 주소서.<br />
왕국은 지금이고, 영광은 오늘이니,<br />
심장 박동 하나하나에, 너와 함께 내가 있다.  </p>
<p>그러니 축하해라, 친구여, 달력의 날이 아니라,<br />
네 곁에 살아있는 그리스도를.<br />
높게, 아주 높게 진동해라, 세상이 느낄 수 있게,<br />
너의 빛이 거대한 폭풍 속의 등대가 되게 하라.  </p>
<p>이것이 크리스마스다: 지나간 옛이야기가 아니라,<br />
깨어났다는 영원한 기적이다.  </p>"""
        }
    }

    # Updating translations.json
    for filename, k_data in korean_content.items():
        if filename not in translations:
            translations[filename] = {}
        
        # Ensure 'ko' key exists
        if 'title' not in translations[filename]: translations[filename]['title'] = {}
        if 'h1' not in translations[filename]: translations[filename]['h1'] = {}
        if 'body' not in translations[filename]: translations[filename]['body'] = {}

        translations[filename]['title']['ko'] = k_data['title']
        translations[filename]['h1']['ko'] = k_data['h1']
        translations[filename]['body']['ko'] = k_data['body']
        
        # Also ensure 'es' exists for 00 and 01 in translations.json if missing, 
        # though ideally it should be in spanish_content.json.
        # But wait, translate_all_chapters.py uses spanish_content mostly for defaults.
    
    save_json('translations.json', translations)
    
    # Updating spanish_content.json for 00 and 01
    # We need the spanish content for 00 and 01 to be in spanish_content.json
    # so the script doesn't crash when looking for defaults.
    # We extracted them earlier.
    
    # 00_introduccion.html
    spanish_intro_body = """<div class="spanish language">
                    <h1>Introducción: Entre la Partícula y la Vibración</h1>
                    <h2>I. La Inquietud del Alma</h2>
                    <p>Desde que tengo uso de razón, he sentido una especie de vibración disonante cuando me acercaba a los grandes templos de piedra. No era falta de fe; al contrario, siempre he intuido que detrás del velo de la realidad existe una Fuente inagotable de amor. Mi conflicto, mi tormento silencioso, nacía del contraste entre esa intuición de un Dios infinito y la pequeñez de las cajas en las que intentábamos meterlo.</p>
                    <p>Crecí en el seno del catolicismo, respirando el incienso y admirando la liturgia, pero muy pronto, esa belleza se vio empañada por una sensación incómoda: la soberbia. Me dolía en el alma escuchar, implícita o explícitamente, que nosotros teníamos "la verdad" y los demás no. ¿Cómo podía ser que el Creador de un universo de cien mil millones de galaxias tuviera preferencia por un código postal espiritual concreto? Sentía que pecábamos de una arrogancia terrible al no reconocer la salvación para otros credos, al mirar con lástima o superioridad a quien buscaba la luz por otro camino. Esa exclusividad me parecía, paradoxalmente, el acto más irreligioso de todos: limitar la misericordia de Dios a nuestras propias fronteras humanas.</p>
                    <h2>II. Las Sombras en los Centros de Poder</h2>
                    <p>Pero mi tormento iba más allá de la teología. Al estudiar la historia, me topaba con muros manchados de sangre. La Inquisición, las cruzadas, las excomuniones... No podía evitar pensar: ¿Cómo hemos llegado de "ama a tu prójimo" a "quémalo si no piensa como tú"?</p>
                    <p>Durante años, esto me alejó. Sentía rabia. Veía la institución y solo veía las sombras. Sin embargo, con el tiempo y la madurez, entendí algo fundamental: la Iglesia, como cualquier estructura humana, está compuesta de personas. Y las personas somos antenas. Cuando el miedo se instala en los centros de poder, cuando la necesidad de control supera a la necesidad de servir, la vibración colectiva desciende.</p>
                    <p>La Inquisición no fue obra de Dios, ni siquiera fue obra de "la religión" en abstracto. Fue la consecuencia inevitable de una <strong>baja vibración</strong> instalada en la cúpula. El miedo a perder el poder, el miedo a lo diferente, el odio disfrazado de celo... todo eso son frecuencias densas, pesadas. Y cuando esa densidad se apodera de una jerarquía, el resultado es el sufrimiento. Obviamente, es algo que el propio Cristo, mi amigo Jesús, jamás hubiera permitido. Él, que detuvo las piedras contra la adúltera, jamás hubiera encendido una hoguera.</p>
                    <p>Entender esto me permitió perdonar. Entendí que no era "la Iglesia" la que fallaba, sino la vibración de los hombres que, en momentos oscuros, la dirigían. Y que, por debajo de esa cúpula de poder, siempre hubo miles de curas, monjas y laicos vibrando alto, dando de comer al hambriento, consolando al triste, manteniendo encendida la luz a pesar de la oscuridad de sus líderes.</p>
                    <h2>III. La Física Cuántica del Espíritu</h2>
                    <p>Mi reconciliación definitiva llegó de la mano de la ciencia. Siempre me ha fascinado la física cuántica, esa rama del saber que nos dice que la realidad no es tan sólida como parece. Nos enseña que toda partícula subatomicca es, a la vez, materia y onda. Es algo concreto y, al mismo tiempo, es pura vibración, pura posibilidad.</p>
                    <p>Ahí fue donde todo hizo clic. El Padre Nuestro, las enseñanzas de Jesús... no eran normas morales rígidas, ¡eran instrucciones de física cuántica!</p>
                    <p>Cuando Jesús nos dice "no temáis", no nos está dando una orden psicológica, nos está diciendo: "No bajéis vuestra frecuencia". El miedo es una vibración lenta, densa, que contrae la realidad. El amor, la paz, la seguridad... son vibraciones rápidas, expansivas, que crean luz.</p>
                    <p>Entendí que "caer en la tentación" no es comerse un pastel en cuaresma. Es la tentación de dejarse arrastrar por la gravedad de las bajas vibraciones: el odio, la venganza, l'envidia, la soberbia. Cuando odias, te densificas. Te conviertes en "partícula" pesada, aislada, desconectada del todo. Когда amas, te conviertes en "onda", te expandes, te conectas con el campo cuántico universal, con el Padre.</p>
                    <h2>IV. Un Café con Lutero</h2>
                    <p>En este viaje de comprensión, a menudo me he imaginado tomando un café con Martín Lutero en el siglo XVI. Creo que habríamos sido buenos amigos. Él vio esa misma soberbia que a mí me atormentaba. Vio cómo la estructura se había vuelto tan densa, tan preocupada por vender bulas y construir basílicas de mármol, que se había olvidado de la vibración del Evangelio.</p>
                    <p>Lutero tuvo la valentía de decir: "La salvación no está en Roma, está en tu fe". Y yo añadiría, desde mi perspectiva del siglo XXI: "La salvación no depende de seguir al Papa, sino de la frecuencia de tu corazón".</p>
                    <p>Si tus obras, si tu vida diaria, están hechas desde la alta vibración del amor, no cabe duda de que estás salvado. Porque "estar salvado" no es un ticket para entrar en un club VIP después de morir. Estar salvado es vivir, aquí y ahora, en la frecuencia del Paraíso. Es estar en sintonía con la Fuente.</p>
                    <p>Si un budista, un ateo o un cristiano vibran en el amor incondicional, están en la misma frecuencia. Están "en Dios". Y ninguna bula, ningún decreto, puede cambiar esa realidad física y espiritual. La salvación es una cuestión de resonancia, no de burocrazia.</p>
                    <h2>V. La Luz que Prevalece</h2>
                    <p>Por eso escribo este libro. No para atacar a la religión, sino para rescatar su esencia vibracional. Escribo desde el amor, habiendo sanado esa lástima que sentía por la soberbia institucional. He dejado de mirar la oscuridad de la Inquisición para mirar la luz de los místicos, de los santos anónimos, de la gente buena que, en nombre de esa misma fe, ha vibrado tan alto que ha cambiado el mundo.</p>
                    <p>Este libro es una invitación a caminar con Jesús, no como un juez severo, sino como un maestro de vibración. Un amigo que nos enseña a navegar entre Madrid, Las Rozas y Colmenarejo sin perder la sintonía. Un guía que nos recuerda, una y otra vez, que somos luz, que somos onda, y que nuestro único deber es mantener la frecuencia alta, pase lo que pase a nuestro alrededor.</p>
                    <p>Así que, querido lector, olvida por un momento los dogmas, las culpas y los miedos heredados. Abre tu mente a la posibilidad de que todo, absolutamente todo, es música. Y que tú tienes el instrumento en tus manos para tocar la melodía más hermosa.</p>
                    <p>Bienvenido a "Mi amigo Jesucristo".</p>
                </div>"""
    
    # Clean spanish intro body (remove outer div and h1 as the script adds them)
    # The script adds h1 and wraps in div. So we need just the inner HTML from h2 onwards?
    # Actually the script takes 'body' and puts it under h1.
    # Looking at spanish_content.json for other chapters, they start with <p>.
    # So for intro, I should probably strip the first h1 and the wrapper div.
    
    if "00_introduccion.html" not in spanish_content:
        spanish_content["00_introduccion.html"] = {
            "title": "Introducción: Entre la Partícula y la Vibración",
            "h1": "Introducción: Entre la Partícula y la Vibración",
            "body": spanish_intro_body.replace('<div class="spanish language">', '').replace('<h1>Introducción: Entre la Partícula y la Vibración</h1>', '').replace('</div>', '').strip()
        }

    # index.html
    spanish_index_body = """<p>Era una tarde de primavera en Madrid. El sol se filtraba entre los edificios de la Gran Vía,
                        creando juegos de luces y sombras que parecían danzar sobre el asfalto. Yo caminaba con la prisa
                        habitual de quien vive en la ciudad, con la mente llena de ruido: correos por responder,
                        facturas, preocupaciones... vibrando bajo, muy bajo.</p>
                    <p>De repente, en la plaza de Callao, lo vi. No llevaba túnica, ni sandalias, ni tenía un halo
                        brillante sobre la cabeza. Llevaba unos vaqueros desgastados, una camiseta blanca y unas
                        zapatillas cómodas. Estaba sentado en un banco, mirando a la gente pasar con una sonrisa
                        tranquila, una sonrisa que parecía detener el tiempo.</p>
                    <p>—Hola, Francisco —dijo cuando pasé cerca.</p>
                    <p>Me detuve en seco. Nadie me llamaba por mi nombre completo en la calle, y menos un desconocido.
                        Pero al mirarlo a los ojos, supe que no era un desconocido. Había una familiaridad ancestral en
                        su mirada, una paz que desarmaba cualquier defensa.</p>
                    <p>—¿Jesús? —pregunté, sintiéndome un poco ridículo.</p>
                    <p>—El mismo —respondió él, dándome una palmada en el espacio vacío del banco a su lado—. Siéntate
                        un rato. Estás vibrando en una frecuencia que me está dando dolor de cabeza, y eso que yo
                        aguanto mucho.</p>
                    <p>Me senté, todavía aturdido.
                        —¿Vibrando? —repetí.</p>
                    <p>—Sí, vibrando. Todo es vibración, amigo mío. El miedo, la prisa, el enfado... son vibraciones
                        densas, pesadas. Te anclan al suelo y no te dejan ver el cielo, aunque lo tengas encima.</p>
                    <p>Miré hacia arriba. El cielo de Madrid estaba de un azul intenso, precioso. No me había fijado
                        hasta ese momento.</p>
                    <p>—He venido a pasar unos días contigo —continuó—. Vamos a dar una vuelta. Necesitas recordar cómo
                        sintonizar la radio de tu alma. Estás escuchando pura estática.</p>
                    <p>Y así, en medio del bullicio de Madrid, comenzó la aventura más extraña y maravillosa de mi vida.
                        No con milagros de convertir agua en vino, sino con el milagro de transformar mi ruido interno
                        en música.</p>"""
    
    if "index.html" not in spanish_content:
        spanish_content["index.html"] = {
            "title": "Capítulo 1: El Encuentro en Madrid",
            "h1": "Capítulo 1: El Encuentro en Madrid",
            "body": spanish_index_body
        }

    save_json('spanish_content.json', spanish_content)
    print("Updates complete.")

if __name__ == "__main__":
    main()
