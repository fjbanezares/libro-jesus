import json
import os
import re

# Source files
TRANSLATIONS_FILE = '/Users/fjbanezares/libro sobre mi amigo Jesucristo/translations.json'
SPANISH_CONTENT_FILE = '/Users/fjbanezares/libro sobre mi amigo Jesucristo/spanish_content.json'

def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    print("Loading existing data...")
    translations = load_json(TRANSLATIONS_FILE)
    spanish_content = load_json(SPANISH_CONTENT_FILE)
    
    # Portugues translations mapping
    pt_translations = {
        "00_introduccion.html": {
            "title": "Introdução: Entre a Partícula e a Vibração",
            "h1": "Introdução: Entre a Partícula e a Vibração",
            "body": """<h2>I. A Inquietação da Alma</h2>
<p>Desde que me lembro, senti uma espécie de vibração dissonante sempre que me aproximava dos grandes templos de pedra. Não era falta de fé; pelo contrário, sempre intuí que por trás do véu da realidade existe uma Fonte inesgotável de amor. O meu conflito, o meu tormento silencioso, nascia do contraste entre essa intuição de um Deus infinito e a pequenez das caixas em que tentávamos encaixá-Lo.</p>
<p>Cresci no seio do catolicismo, respirando o incenso e admirando a liturgia, mas muito cedo essa beleza foi toldada por uma sensação desconfortável: o orgulho. Doía-me na alma ouvir, implícita ou explicitamente, que nós tínhamos "a verdade" e os outros não. Como poderia ser que o Criador de um universo de cem biliões de galáxias tivesse preferência por um código postal espiritual específico? Sentia que éramos culpados de uma arrogância terrível ao não reconhecer a salvação para outros credos, ao olhar com pena ou superioridade para aqueles que buscavam a luz por outro caminho. Essa exclusividade parecia-me, paradoxalmente, o ato mais irreligioso de todos: limitar a misericórdia de Deus às nossas próprias fronteiras humanas.</p>
<h2>II. As Sombras nos Centros de Poder</h2>
<p>Mas o meu tormento ia além da teologia. Ao estudar história, deparei-me com paredes manchadas de sangue. A Inquisição, as cruzadas, as excomunhões... Não conseguia deixar de pensar: Como passámos de "amai o próximo" para "queimai-o se não pensar como vós"?</p>
<p>Durante anos, isto afastou-me. Senti raiva. Via a instituição e só via as sombras. No entanto, com o tempo e a maturidade, compreendi algo fundamental: a Igreja, como qualquer estrutura humana, é composta por pessoas. E as pessoas são antenas. Quando o medo se instala nos centros de poder, quando a necessidade de controlo excede a necessidade de servir, a vibração coletiva desce.</p>
<p>A Inquisição não foi obra de Deus, nem sequer foi obra da "religião" em abstrato. Foi a consequência inevitável de uma <strong>baixa vibração</strong> instalada no topo. O medo de perder o poder, o medo do diferente, o ódio disfarçado de zelo... tudo isso são frequências densas e pesadas. E quando essa densidade toma conta de uma hierarquia, o resultado é sofrimento. Obviamente, é algo que o próprio Cristo, o meu amigo Jesus, nunca teria permitido. Ele, que parou as pedras contra a adúltera, nunca teria acendido uma fogueira.</p>
<p>Compreender isto permitiu-me perdoar. Compreendi que não foi "a Igreja" que falhou, mas a vibração dos homens que, em momentos sombrios, a lideraram. E que, abaixo dessa cúpula de poder, sempre houve milhares de padres, freiras e leigos a vibrar alto, a alimentar os famintos, a confortar os tristes, a manter a luz acesa apesar da escuridão dos seus líderes.</p>
<h2>III. A Física Quântica do Espírito</h2>
<p>A minha reconciliação definitiva veio da ciência. Sempre fui fascinado pela física quântica, esse ramo do conhecimento que nos diz que a realidade não é tão sólida como parece. Ensina-nos que cada partícula subatómica é, ao mesmo tempo, matéria e onda. É algo concreto e, ao mesmo tempo, é pura vibração, pura possibilidade.</p>
<p>Foi aí que tudo fez sentido. O Pai Nosso, os ensinamentos de Jesus... não eram regras morais rígidas, eram instruções de física quântica!</p>
<p>Quando Jesus nos diz "não temais", não nos está a dar uma ordem psicológica, está a dizer-nos: "Não baixem a vossa frequência." O medo é uma vibração lenta e densa que contrai a realidade. O amor, a paz, a segurança... são vibrações rápidas e expansivas que criam luz.</p>
<p>Compreendi que "cair em tentação" não é comer um bolo durante a Quaresma. É a tentação de ser arrastado pela gravidade das baixas vibrações: ódio, vingança, inveja, orgulho. Quando odeias, tornas-te denso. Tornas-te uma "partícula" pesada, isolada, desconectada do todo. Quando amas, tornas-te uma "onda", expandes-te, conectas-te com o campo quântico universal, com o Pai.</p>
<p>E acrescentaria, da minha perspetiva do século XXI: "A salvação não depende de seguir o Papa, mas da frequência do teu coração."</p>
<p>Se as tuas obras, se a tua vida diária, são feitas a partir da alta vibração do amor, não há dúvida de que estás salvo. Porque "ser salvo" não é um bilhete para entrar num clube VIP depois de morrer. Ser salvo é viver, aqui e agora, na frequência do Paraíso. É estar em sintonia com a Fonte.</p>"""
        },
        "index.html": {
            "title": "Capítulo 1: O Encontro em Madrid",
            "h1": "Capítulo 1: O Encontro em Madrid",
            "body": """<p>Era uma tarde de primavera em Madrid. O sol filtrava-se por entre os edifícios da Gran Vía, criando jogos de luz e sombra que pareciam dançar no asfalto. Eu caminhava com a pressa habitual de quem vive na cidade, com a mente cheia de ruído: e-mails para responder, contas, preocupações... vibrando baixo, muito baixo.</p>
<p>De repente, na praça de Callao, vi-o. Não usava túnica, nem sandálias, nem tinha um halo brilhante sobre a cabeça. Usava uns jeans gastos, uma t-shirt branca e uns ténis confortáveis. Estava sentado num banco, a observar as pessoas a passar com um sorriso tranquilo, um sorriso que parecia parar o tempo.</p>
<p>—Olá, Francisco —disse ele quando passei perto.</p>
<p>Parei de repente. Ninguém me chamava pelo meu nome completo na rua, e muito menos um desconhecido. Mas ao olhar nos seus olhos, soube que não era um desconhecido. Havia uma familiaridade ancestral no seu olhar, uma paz que desarmava qualquer defesa.</p>
<p>—Jesus? —perguntei, sentindo-me um pouco ridículo.</p>
<p>—O próprio —respondeu ele, dando uma palmada no espaço vazio do banco ao seu lado—. Senta-te um pouco. Estás a vibrar numa frequência que me está a dar dor de cabeça, e olha que eu aguento muito.</p>
<p>Sentei-me, ainda atordoado.
—Vibrar? —repeti.</p>
<p>—Sim, vibrar. Tudo é vibração, meu amigo. O medo, a pressa, a raiva... são vibrações densas, pesadas. Ancoram-te ao chão e não te deixam ver o céu, mesmo que o tenhas mesmo por cima.</p>
<p>Olhei para cima. O céu de Madrid estava de um azul intenso, lindo. Não tinha reparado até àquele momento.</p>
<p>—Vim passar uns dias contigo —continuou—. Vamos dar uma volta. Precisas de te lembrar de como sintonizar o rádio da tua alma. Estás a ouvir pura estática.</p>
<p>E assim, no meio da confusão de Madrid, começou a aventura mais estranha e maravilhosa da minha vida. Não com milagres de transformar água em vinho, mas com o milagre de transformar o meu ruído interno em música.</p>"""
        },
        "02_capitulo.html": {
            "title": "Capítulo 2: Passeio por Las Rozas",
            "h1": "Capítulo 2: Passeio por Las Rozas",
            "body": """<p>No dia seguinte, levei Jesus a Las Rozas. Pensei que ele gostaria de ver algo mais verde, menos caótico. Fomos ao parque Paris.</p>
<p>—Isto é melhor —disse ele, vendo os patos no lago—. Mas continuas tenso. O que te preocupa?</p>
<p>—O trabalho, o futuro... sinto que não chego a tudo.</p>
<p>Jesus riu-se. Um riso fresco, como água.</p>
<p>—Essa é a armadilha do tempo linear. Pensas que a felicidade está em algum lugar do futuro: 'quando tiver aquele emprego', 'quando me reformar', 'quando pagar a casa'. Mas a vida acontece Agora. A vibração só existe no presente.</p>
<p>Apontou para um miúdo que corria atrás de uma bola, totalmente absorto na sua brincadeira.</p>
<p>—Vês aquele miúdo? Ele está no Reino. Não está preocupado com o jogo de amanhã. Está a vibrar com a alegria do momento. 'Só quem for como crianças entrará no Reino dos Céus'. Não me referia a ser ingénuo. Referia-me a viver o presente sem o peso do passado nem a ansiedade do futuro.</p>
<p>Caminhámos até ao centro comercial. Era irónico passear com Jesus entre montras de moda.</p>
<p>—Não te incomoda o consumismo? —perguntei.</p>
<p>—As coisas não são más —respondeu—. O mau é o apego. Se a tua felicidade depende de comprar essa camisa, és escravo da camisa. Se vibras em gratidão pelo que tens, és livre. Podes ter a camisa ou não ter, e a tua paz é a mesma.</p>"""
        },
        "03_capitulo.html": {
            "title": "Capítulo 3: A Vibração e o Silêncio",
            "h1": "Capítulo 3: A Vibração e o Silêncio",
            "body": """<p>Apanhámos o autocarro em direção à serra. A paisagem ia mudando, tornando-se mais verde, mais selvagem. Jesus olhava pela janela como uma criança na sua primeira excursão.</p>
<p>—O ruído —disse de repente—. É a grande doença deste século. Não o ruído dos carros, mas o ruído dos ecrãs, das notificações, das opiniões constantes.</p>
<p>Chegámos a um ponto intermédio antes de Colmenarejo. Descemos num caminho de terra.
—Vamos praticar o silêncio —propôs.</p>
<p>—Ficar calados?</p>
<p>—Não apenas fechar a boca. Calar a mente. Quero que escutes a vibração do universo.</p>
<p>Caminhámos em silêncio durante uma hora. No início, a minha mente era uma máquina de lavar a centrifugar pensamentos: 'O que estou aqui a fazer a caminhar com Jesus Cristo?', 'Terei enlouquecido?', 'Tenho de ligar à minha mãe...'. Mas, pouco a pouco, o ritmo dos meus passos e a respiração tranquila do meu companheiro foram-me acalmando.</p>
<p>Parámos num ponto alto de onde se via o horizonte.
—Fecha os olhos —sussurrou-me—. Sente.</p>
<p>Fi-lo. E pela primeira vez em muito tempo, não senti medo. Senti uma espécie de zumbido suave, quente. Como se o ar me abraçasse.</p>
<p>—É isso —disse ele, como se pudesse ler o meu sentimento—. Isso é vibrar alto. É a frequência do Amor. Não o amor romântico dos filmes, mas o Amor que mantém os átomos unidos. Quando estás aí, nada te pode tocar. 'Livrai-nos do mal' não é pedir que os maus não existam. É pedir para estar numa frequência onde a maldade não te alcance, onde não ressoe contigo.</p>
<p>Abri os olhos. O mundo parecia mais brilhante.
—Se vibras alto, o baixo não te vê —concluiu—. É como se fosses invisível para a escuridão.</p>"""
        },
        "04_capitulo.html": {
            "title": "Capítulo 4: Colmenarejo e a Natureza",
            "h1": "Capítulo 4: Colmenarejo e a Natureza",
            "body": """<p>Chegámos a Colmenarejo ao pôr do sol. A vila tinha aquele encanto do que está a meio caminho entre a cidade e o campo. Fomos para a zona da Universidade, onde há grandes espaços abertos e respira-se outro ar.</p>
<p>—Sente-se melhor aqui —disse Jesus, respirando fundo—. A natureza é a grande mestra da vibração. Ela nunca se engana. Um pinheiro não tenta ser uma azinheira. Um rio não tenta correr para cima.</p>
<p>Sentámo-nos perto da ermida. O céu tingia-se de laranja e violeta.
—Pai Nosso que estais nos céus... —começou a recitar baixinho—. Sabes onde fica o céu, Francisco?</p>
<p>—Lá em cima? —apontei.</p>
<p>Ele abanou a cabeça a sorrir.
—O céu é um estado de consciência. É aquele lugar interior onde tudo está bem, onde há paz absoluta. 'Que estais nos céus' significa que a Fonte de tudo reside nessa alta vibração. E tu tens acesso direto lá. Tens wifi direto com o Criador, mas às vezes esqueces-te da palavra-passe.</p>
<p>—Qual é a palavra-passe?</p>
<p>—A entrega. Parar de lutar contra o que é. Aceitar. Fluir. Quando te entregas à vida, paras de nadar contra a corrente. E então, a corrente leva-te. E a corrente da vida leva-te sempre para o bem, para o mar.</p>
<p>Em Colmenarejo, sob as primeiras estrelas, compreendi que rezar não era pedir coisas como quem faz a lista de compras. Rezar era sintonizar. Era voltar a pôr o mostrador na frequência correta para escutar a música que toca sempre, embora nós estejamos demasiado ocupados a fazer barulho para a ouvir.</p>"""
        },
        "05_capitulo.html": {
            "title": "Capítulo 5: O Pai Nosso (Parte 1: Pai)",
            "h1": "Capítulo 5: O Pai Nosso (Parte 1: Pai)",
            "body": """<p>Voltámos a Madrid, mas desta vez fomos ao Retiro. Sentámo-nos perto do Palácio de Cristal.
—Falemos do teu pai —disse Jesus de repente.</p>
<p>Fiquei tenso. A minha relação com o meu pai nem sempre tinha sido fácil.
—Porquê?</p>
<p>—Porque a oração começa com 'Pai Nosso'. E muita gente fica presa aí. Se o teu pai terreno foi duro, ou ausente, ou crítico, projetas essa imagem em Deus. Acreditas que Deus é um senhor com uma barba que te vigia para te castigar se errares.</p>
<p>Pegou numa pedra do chão e atirou-a para o lago. As ondas expandiram-se.
—A palavra 'Pai' em aramaico, <em>Abwoon</em>, tem um significado muito mais amplo. É a Fonte, a Origem, o Sopro da Vida. Não é um senhor. É uma Energia. É a vibração original de onde todos saímos.</p>
<p>—Portanto, não é um juiz?</p>
<p>—Claro que não! —exclamou—. O sol julga as flores? Diz-lhes 'tu sim floresces, dou-te luz; tu não, ficas no escuro'? O sol brilha para todas. Deus é Amor incondicional. Se te fechas numa gruta, não é culpa do sol que estejas no escuro. É a tua escolha.</p>
<p>—E porquê 'Nosso'?</p>
<p>—Porque não é 'Meu'. Não é propriedade privada de nenhuma religião, nem de nenhuma pessoa. É de todos. Do cristão, do budista, do ateu, da árvore e do cão. Todos vimos da mesma Fonte. Reconhecer isso é o primeiro passo para vibrar alto: a Unidade. Se te vês separado ou</p>"""
        },
        "06_capitulo.html": {
            "title": "Capítulo 6: O Pai Nosso (Parte 2: Céu)",
            "h1": "Capítulo 6: O Pai Nosso (Parte 2: Céu)",
            "body": """<p>Continuámos pelo Retiro, observando os barcos no lago.</p>
<p>—Já te disse que o Céu é um estado de consciência —prosseguiu Jesus—. 'Santificado seja o Vosso nome'. Em aramaico, santificar significa limpar, esvaziar para criar espaço.</p>
<p>—Esvaziar o quê?</p>
<p>—A mente. Para que a alta vibração entre, tens de esvaziar o lixo. Não podes encher um copo que já está cheio de vinagre com vinho. Se a tua mente está cheia de juízos, queixas e medo, onde é que Deus vai entrar? Santificar o Nome é criar um espaço de silêncio e pureza dentro de ti para que a vibração original possa ressoar.</p>
<p>Uma mulher passou a correr, a olhar para o relógio, visivelmente stressada. Jesus olhou para ela com compaixão.</p>
<p>—'Venha a nós o Vosso reino' —recitou—. Muita gente pensa que é esperar que o mundo se arranje por magia. Mas o Reino é agora. É decidir, a cada instante, vibrar na paz. Quando tu estás em paz no meio do caos, estás a trazer o Reino à Terra. Tu és a antena.</p>
<p>—Isso soa a muita responsabilidade.</p>
<p>—É a única responsabilidade que tens! Não vieste salvar o mundo. Vieste salvar a tua própria vibração. E ao fazê-lo, iluminas o mundo. Uma lâmpada não se preocupa em iluminar a sala inteira. Só se preocupa em estar ligada à corrente. O resto acontece sozinho.</p>"""
        },
         "07_capitulo.html": {
            "title": "Capítulo 7: O Pão de Cada Dia",
            "h1": "Capítulo 7: O Pão de Cada Dia",
            "body": """<p>Comíamos uma sandes de lulas perto da Plaza Mayor. Jesus desfrutava de cada dentada como se fosse um manjar.</p>
<p>—'O pão nosso de cada dia nos dai hoje' —disse, limpando um pouco de maionese—. As pessoas pedem para ganhar a lotaria, para ter segurança para os próximos trinta anos. Mas a oração diz 'de cada dia'.</p>
<p>—Viver o dia a dia?</p>
<p>—Viver o momento. A confiança é viver sabendo que hoje terás o que precisas. Se guardas pão para um mês porque tens medo de não ter amanhã, o pão ganha bolor. O 'maná' no deserto apodrecia se o guardassem. A energia tem de fluir.</p>
<p>—É difícil não preocupar com o futuro tal como as coisas estão.</p>
<p>—A preocupação é usar a tua imaginação para criar coisas que não queres. É rezar pelo que não queres. 'Seja feita a Vossa vontade' é deixar de querer controlar como é que as coisas te devem chegar. O Universo é infinitamente criativo. Talvez o que precises não venha na forma que esperas, mas virá.</p>
<p>Deu a última dentada.</p>
<p>—Vontade não é resignação. Vontade é alinhamento. É dizer: 'Universo, que a minha vibração se alinhe com o fluxo da vida'. Quando nadas a favor da corrente, chegas mais longe e cansas-te menos.</p>"""
        },
        "08_capitulo.html": {
            "title": "Capítulo 8: Perdão e Dívidas",
            "h1": "Capítulo 8: Perdão e Dívidas",
            "body": """<p>Atravessando a ponte de Segóvia, falámos do tema mais difícil.</p>
<p>—'Perdoai as nossas ofensas, assim como nós perdoamos a quem nos tem ofendido'. Isto não é uma troca comercial —esclareceu—. Não é 'eu perdoo para que Tu me perdoes'.</p>
<p>—Então?</p>
<p>—É uma lei física. Não podes receber o que não dás, porque ao não dar, bloqueias o fluxo. O rancor é um tampão no cano. Se guardas rancor a alguém, estás a fechar a tua própria torneira de amor. Deus quer dar-te tudo, mas se tens o punho fechado para bater em alguém, não podes ter a mão aberta para receber.</p>
<p>—Às vezes é impossível perdoar certas coisas.</p>
<p>—Perdoar não é dizer 'o que fizeste foi bom'. Perdoar é dizer 'não vou deixar que o que fizeste baixe a minha vibração'. É cortar a corda elástica que te une ao agressor. Enquanto odeias, estás atado a ele. Quando perdoas, soltas-te. Ficas livre. O perdão é o maior ato de egoísmo inteligente que existe: fá-lo por ti, para seres livre, para voltares a vibrar alto.</p>"""
        },
        "09_capitulo.html": {
            "title": "Capítulo 9: Não nos deixeis cair em tentação (Vibrar Alto)",
            "h1": "Capítulo 9: Não nos deixeis cair em tentação (Vibrar Alto)",
            "body": """<p>Estávamos a ver o pôr do sol no Templo de Debod.
—A tentação... —murmurou Jesus—. Não é sobre maçãs, nem sobre sexo, nem sobre chocolate.</p>
<p>—Não?</p>
<p>—A única tentação real é a de te esqueceres de quem és. A tentação de acreditar que és pequeno, que estás sozinho, que és vítima. A tentação de baixar a tua frequência.</p>
<p>Olhou-me fixamente.
—Sempre que te queixas, cais em tentação. Sempre que criticas, cais em tentação. Sempre que sentes inveja, cais na armadilha da densidade. 'Não nos deixeis cair em tentação' significa: ajuda-nos a manter o foco na Luz, para que a escuridão não nos confunda.</p>
<p>—É difícil manter o foco quando tudo corre mal.</p>
<p>—É aí que é mais importante! Qualquer um vibra alto quando está na praia. O mestre demonstra-se na tempestade. Quando tudo corre mal, se conseguires parar, respirar e dizer 'isto também passará, eu escolho a paz', então venceste o mundo. Transformaste o chumbo em ouro. Essa é a verdadeira alquimia.</p>"""
        },
        "10_capitulo.html": {
            "title": "Capítulo 10: Livrai-nos do mal (Proteção de Baixas Vibrações)",
            "h1": "Capítulo 10: Livrai-nos do mal (Proteção de Baixas Vibrações)",
            "body": """<p>—E o mal? —perguntei enquanto voltávamos—. Ele existe?</p>
<p>—Existe a ausência de luz. Existe a inconsciência. As pessoas que fazem mal estão profundamente adormecidas, desconectadas da Fonte. Não são monstros, são almas perdidas na névoa do medo.</p>
<p>—'Mas livrai-nos do mal'...</p>
<p>—Sí. Livra-nos da ignorância. Livra-nos de acreditar que o medo é real. Protege-nos das baixas vibrações, não porque tenham poder sobre nós, mas para não nos enredarmos nelas. Esvazia-nos.</p>
<p>Parou e pôs-me a mão no ombro.
—Não há nada a temer, Francisco. A luz dissolve a escuridão sem lutar. Acaso acendes uma lâmpada e a luz tem de lutar à espadeirada contra a sombra? Não. A luz brilha e a sombra simplesmente desaparece. Sê tu a luz. Não lutes contra o mal. Simplesmente brilha.</p>"""
        },
        "11_capitulo.html": {
            "title": "Capítulo 11: O Reino, o Poder e a Glória",
            "h1": "Capítulo 11: O Reino, o Poder e a Glória",
            "body": """<p>No último dia, caminhámos pela Gran Vía de noite. As luzes da cidade brilhavam.</p>
<p>—Porque Vosso é o Reino, o Poder e a Glória —disse eu.</p>
<p>—Para sempre —acrescentou Jesus—. Isto é o reconhecimento final. É saber que, aconteça o que acontecer no filme da tua vida, o ecrã está intacto. O Reino é a tua verdadeira natureza. O Poder é a energia do Amor que cria mundos. A Glória é a beleza de tudo o que existe.</p>
<p>—Parece um final feliz.</p>
<p>—É que não há final. A vida é eterna. Mudas de fato, mudas de cenário, mas o Ator, o Espirito, é sempre o mesmo. Tu és eterno, Francisco. Nada real pode ser ameaçado. Nada irreal existe. Nisso reside a paz de Deus.</p>"""
        },
        "12_epilogo.html": {
            "title": "Epílogo: Aventuras Finais e Despedida",
            "h1": "Epílogo: Aventuras Finais e Despedida",
            "body": """<p>Chegámos ao local onde nos tínhamos encontrado, em Callao.</p>
<p>—Tenho de ir —disse ele—. Tenho vibrações para elevar noutros sítios.</p>
<p>—Vou sentir a tua falta —confessei. As lágrimas picavam-me os olhos.</p>
<p>—Aí estás tu de novo a cair na ilusão da separação —sorriu e abraçou-me. Foi um abraço que senti em todas as células do meu corpo—. Como podes sentir falta de algo que está dentro de ti? Eu estou no teu coração. Sempre que amas, aí estou eu. Sempre que perdoas, aí estou eu. Sempre que sorris a um estranho, somos nós os dois.</p>
<p>Afastou-se um pouco, mas a sua luz parecia ficar.</p>
<p>—Lembra-te: Vibra Alto. Não deixes que o ruído do mundo apague a tua música. És um instrumento de Deus. Toca forte, toca bonito.</p>
<p>E tal como apareceu, misturou-se com a multidão. Perdi-o de vista entre um grupo de turistas e um casal que discutia. Mas já não importava. Olhei para o céu noturno de Madrid, respirei fundo e senti a música. O ruído tinha desaparecido. Só restava a canção.</p>"""
        },
        "13_apendice_poema.html": {
             "title": "Apêndice: Poema de Natal",
             "h1": "Apêndice: Poema de Natal",
             "body": """<p><strong>Natal de Alta Frequência</strong></p>
<p>Não procures o Menino na palha fria de um tempo remoto,<br />
nem no eco de uma canção de natal que o vento quebrou.<br />
Não o procures na Gran Vía, sob luzes de néon,<br />
onde a alma se vende barata em cada esquina. </p>
<p>Procura-o no silêncio que vibra no teu peito,<br />
no templo sagrado que o Amor fez.<br />
Porque Jesus não usa coroa, nem ouro, nem manto,<br />
usa jeans gastos e seca o teu pranto. </p>
<p>Caminha por Madrid, entre pressas e ruído,<br />
um viajante eterno, por ninguém temido.<br />
Senta-se em Callao, olha-te e sorri:<br />
"Por que corres tanto? Pára e ri." </p>
<p>"O Natal não é data, nem ceia, nem presente,<br />
é vibrar tão alto que esqueces o que é mau.<br />
É saber que o presépio não é madeira nem feno,<br />
é o teu próprio coração, de esperança cheio." </p>
<p>Se vibras no medo, se vibras na ira,<br />
o Menino não nasce, a estrela não brilha.<br />
Mas se perdoas, se abraças, se amas,<br />
acendes em ti as mais puras chamas. </p>
<p>Não nos deixeis cair na tentação da tristeza,<br />
levanta a vista, contempla a beleza.<br />
De Las Rozas ao céu, de Colmenarejo ao mar,<br />
a única missão é aprender a Amar. </p>
<p>Livrai-nos do peso de vibrar no chão,<br />
e dai-nos as asas para levantar voo.<br />
Porque o Reino é agora, a Glória é hoje,<br />
e em cada batida, contigo eu estou. </p>
<p>Por isso celebra, amigo, não o dia marcado,<br />
mas o Cristo vivo que tens ao lado.<br />
Vibra alto, muito alto, que o mundo o sinta,<br />
que a tua luz seja o farol na grande tempestade. </p>
<p>Este é o Natal: não um conto passado,<br />
mas o milagre eterno de ter despertado. </p>"""
        }
    }

    print("Adding Portuguese content...")
    for filename, content in pt_translations.items():
        if filename not in translations:
            translations[filename] = {"title": {}, "h1": {}, "body": {}}
        
        translations[filename]["title"]["pt"] = content["title"]
        translations[filename]["h1"]["pt"] = content["h1"]
        translations[filename]["body"]["pt"] = content["body"]

    save_json(TRANSLATIONS_FILE, translations)
    print("Portuguese content added successfully.")

if __name__ == "__main__":
    main()
