"""Português europeu copy for the Runout Rank site.

Mirrors locales/en.py exactly: same names, same page order, same markup —
only the strings differ. See locales/en.py for the contract.
"""

from common import (
    FIRST_PUBLISHED, PLAY_URL, UPDATED,
    app_schema, article_schema, breadcrumb, breadcrumb_schema, byline,
    faq_body, faq_schema, locale_by_code, site_schema, store_block,
)

LOCALE = locale_by_code("pt-PT")

UI = dict(
    tagline="Aplicação de teste de nível e treino de bilhar com classificação absoluta, para Android e iOS",
    author_title="Criador do Runout Rank",

    # --- chrome ---------------------------------------------------------
    skip_link="Saltar para o conteúdo",
    nav_aria="Principal",
    lang_aria="Idioma",
    lang_current="Idioma",
    breadcrumb_label="Trilho de navegação",
    nav_home="Início",
    nav=[
        ("index.html", "Início"),
        ("how-it-works.html", "Como funciona"),
        ("levels.html", "Níveis"),
        ("practice.html", "Treino"),
        ("fargo-rate-alternative.html", "vs Fargo Rate"),
        ("runout-pro.html", "Runout Pro"),
        ("faq.html", "FAQ"),
    ],

    # --- byline ---------------------------------------------------------
    byline_by="Por",
    byline_sep=",",
    byline_published="Publicado a",
    byline_updated="Atualizado a",
    date_format="{d} de {month} de {y}",
    months=["janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"],

    # --- store badges ---------------------------------------------------
    store_get_it_on="Disponível no",
    store_in_review="Em análise",
    store_review_aria="Em análise para a App Store",

    # --- footer ---------------------------------------------------------
    footer_blurb="Uma classificação de bilhar absoluta, a partir de um teste de dez mesas na sua própria "
                 "mesa. Um número de 0 a 100 numa só sessão &mdash; sem liga, sem esperar 200 jogos, "
                 "sem conta e sem Internet.",
    footer_col_app="A aplicação",
    footer_col_guides="Guias",
    footer_links_app=[
        ("how-it-works.html", "Como funciona"),
        ("levels.html", "Os seis níveis"),
        ("practice.html", "Treino e registo"),
        ("runout-pro.html", "Runout Pro"),
    ],
    footer_links_guides=[
        ("fargo-rate-alternative.html", "Alternativa ao Fargo Rate"),
        ("pool-rating-without-a-league.html", "Uma classificação sem liga"),
        ("absolute-vs-relative-pool-rating.html", "Classificação absoluta e relativa"),
        ("pool-skill-level-test.html", "Guia do teste de nível de bilhar"),
        ("faq.html", "Perguntas frequentes"),
        ("privacy-policy.html", "Política de privacidade"),
    ],
    footer_sitemap="Mapa do site",
    footer_copyright="&copy; {year} Runout Rank. Escrito e desenvolvido por {author}.",
    footer_platforms="Android e iOS &middot; Apenas modo escuro, tal como a aplicação",
    footer_disclaimer="Fargo Rate e FargoRate são marcas registadas dos respetivos titulares. "
                      "O Runout Rank é uma aplicação independente e não está associado, apoiado nem ligado à "
                      "FargoRate, à BCA, à APA ou a qualquer organizador de ligas. As comparações feitas neste "
                      "site descrevem o funcionamento publicado desses sistemas e são apresentadas para que o "
                      "leitor tire as suas próprias conclusões.",

    # --- social / meta --------------------------------------------------
    og_image_alt="Runout Rank — afinal, quão bom é você no bilhar?",

    # --- privacy policy page --------------------------------------------
    privacy_title="Política de privacidade | Runout Rank",
    privacy_description="O Runout Rank guarda os seus testes, classificações e histórico de treino apenas "
                        "no seu dispositivo. Esta política explica que análise a aplicação utiliza, com quem "
                        "os dados são partilhados e quais são os seus direitos.",
    privacy_h1="Política de privacidade",
    privacy_breadcrumb="Política de privacidade",
    privacy_lead="Os seus testes e estatísticas ficam no seu dispositivo. Esta página explica tudo o que a "
                 "aplicação recolhe, porquê, e que controlo tem sobre esses dados.",

    # --- 404 ------------------------------------------------------------
    not_found_title="Página não encontrada | Runout Rank",
    not_found_description="Essa página não existe. Volte à página inicial do Runout Rank.",

    # --- SoftwareApplication schema -------------------------------------
    app_description="O Runout Rank é uma aplicação de classificação absoluta de nível no bilhar. Faça um teste "
                    "de dez mesas numa mesa de bilhar real, obtenha uma classificação de 0 a 100 e um escalão "
                    "de Rookie a Master numa única sessão e treine depois no nível que o trava. A classificação "
                    "mede-o face a disposições fixas em vez de o medir face aos adversários locais, pelo que não "
                    "exige liga, nem um histórico de 200 jogos, nem sequer adversários. Todos os dados ficam no "
                    "seu dispositivo.",
    app_features=[
        "Classificação absoluta: medida face a disposições fixas geradas, não face a adversários locais",
        "Uma classificação completa de 0 a 100 numa sessão de dez mesas, sem número mínimo de jogos a cumprir",
        "Portátil entre cidades, ligas e países, porque a bitola nunca muda",
        "Teste de dez mesas com classificação de 0 a 100 e um escalão com nome",
        "Seis níveis de desafio, de Rookie a Master",
        "Restrições fixas por nível, para que a mesma classificação signifique o mesmo em qualquer lugar",
        "Disposições de treino geradas aleatoriamente, sem fim",
        "Registo de treino com favoritos",
        "Taxa de limpeza de mesa acumulada, séries e estatísticas por nível",
        "Funciona totalmente offline e sem conta",
    ],
    app_offer="Descarregamento gratuito. A subscrição opcional Runout Pro desbloqueia o histórico de progresso e a exportação para CSV.",
)

CTA = f"""  <section class="cta band">
    <div class="container">
      <p class="eyebrow">Fique com o número</p>
      <h2>Dez mesas. Uma tentativa cada. Uma classificação honesta.</h2>
      <p class="lead" style="max-width:38rem;margin:0 auto 28px">Monte as disposições na mesa em que já
      costuma jogar. A aplicação pontua as limpezas de mesa e diz-lhe em que nível treinar a seguir.</p>
      {store_block(UI, centred=True)}
    </div>
  </section>"""


# --------------------------------------------------------------------------
# Page bodies
# --------------------------------------------------------------------------

INDEX = f"""  <section class="hero">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow">Classificação de bilhar absoluta &middot; Android e iOS</p>
        <h1>A sua classificação de bilhar. <span class="accent">Hoje à noite</span>, e não daqui a 200 jogos.</h1>
        <p class="lead">As classificações de liga precisam de centenas de partidas antes de o número
        significar alguma coisa, e o que se obtém depende de quem a sua cidade calha ter. O Runout Rank
        mede-o antes face à mesa: dez disposições, uma tentativa cada, uma classificação de 0 a 100 numa
        só sessão.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="{PLAY_URL}">Disponível no Google Play</a>
          <a class="btn btn--ghost" href="how-it-works.html">Como funciona o teste</a>
        </div>
        <p class="hero-note">Sem liga &middot; Sem adversários &middot; Sem conta &middot; Funciona offline</p>
      </div>
      <div class="hero-shot">
        <div class="phone">
          <img src="assets/img/screen-home.png" width="1080" height="2400"
               alt="Ecrã inicial do Runout Rank num telemóvel, a propor o início do teste de dez mesas."
               fetchpriority="high" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <section class="tight band">
    <div class="container">
      <div class="grid grid--4">
        <div><span class="stat">10</span><p class="dim">mesas por teste, uma tentativa cada</p></div>
        <div><span class="stat">1</span><p class="dim">sessão para uma classificação completa, sem esperar 200 jogos</p></div>
        <div><span class="stat">0&ndash;100</span><p class="dim">classificação e escalão, assim que termina</p></div>
        <div><span class="stat">0</span><p class="dim">ligas, adversários e contas necessários</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Porquê dar-se ao trabalho</p>
        <h2>Uma classificação de liga custa uma época <span class="accent">e continua a mexer com a sua cidade.</span></h2>
      </div>
      <div class="compare">
        <div class="card pain">
          <h3>Só é real ao fim de 200 jogos</h3>
          <p>A FargoRate considera 200 jogos o mínimo para uma classificação estabelecida. Isso significa
          uma liga, uma época e um conjunto de inscrições antes de descobrir onde está.</p>
          <p><a href="pool-rating-without-a-league.html">Uma classificação sem liga &rarr;</a></p>
        </div>
        <div class="card pain">
          <h3>O seu número descreve o seu código postal</h3>
          <p>Uma classificação relativa está ancorada nos jogadores à sua volta, por isso um meio local
          fraco ou isolado desvia-se em relação ao resto do mundo.</p>
          <p><a href="absolute-vs-relative-pool-rating.html">Absoluta e relativa &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">A resposta</p>
        <h2>Medir o jogador face à <span class="accent">mesa</span>, e não face à sala.</h2>
        <p class="lead">Cada nível fixa exatamente aquilo que o torna difícil &mdash; número de bolas,
        bola na mão, o quão juntas ficam as bolas, bloqueadores. Essas restrições são a bitola, e são as
        mesmas para toda a gente. Vença-as e o número sobe. Mais nada o faz mexer.</p>
      </div>
      <div class="grid grid--3">
        <div class="card">
          <h3>Absoluta, não relativa</h3>
          <p>Não há grupo de adversários que possa ser forte ou fraco, nem nada em relação a que se desviar.</p>
        </div>
        <div class="card">
          <h3>Uma sessão, não uma época</h3>
          <p>Cerca de uma hora à mesa, e termina com uma classificação a sério em vez de um valor provisório.</p>
        </div>
        <div class="card">
          <h3>Nada para decorar</h3>
          <p>As disposições são geradas de novo em cada teste, por isso enfrenta sempre o nível e nunca um
          exercício cuja solução já aprendeu.</p>
        </div>
      </div>
      <p style="margin-top:28px"><a href="fargo-rate-alternative.html">A comparação completa com o Fargo Rate &rarr;</a></p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Como funciona</p>
        <h2>Três passos, de uma assentada</h2>
      </div>
      <div class="grid grid--3 steps">
        <div class="card step">
          <h3>Monte o que a aplicação desenha</h3>
          <p>Cada mesa é desenhada vista de cima, para que monte a disposição exata à sua frente.</p>
        </div>
        <div class="card step">
          <h3>Jogue-a uma vez</h3>
          <p>Limpe a mesa ou falhe e registe com um toque. Sem repetições, sem saltar mesas.</p>
        </div>
        <div class="card step">
          <h3>Receba uma classificação e um plano</h3>
          <p>Uma pontuação, uma classificação, o seu escalão &mdash; e o nível que o está a travar, para
          treinar a seguir.</p>
        </div>
      </div>
      <p style="margin-top:28px"><a href="how-it-works.html">Ler a explicação completa &rarr;</a></p>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-test.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Um teste em curso: a mesa 6 de 10 desenhada vista de cima com quatro bolas objeto numeradas sobre o pano, e os botões Limpou e Falhou por baixo."></div>
        </div>
        <div>
          <p class="eyebrow">A mesa</p>
          <h3>É este o aspeto de uma mesa.</h3>
          <p>Cada uma é desenhada vista de cima e à escala, para que a possa montar no pano à sua frente e
          jogar a tacada a sério. Fica no ecrã durante toda a tentativa, por isso pode reconstruir a
          disposição se lhe mexer nas bolas.</p>
          <ul class="ticks">
            <li><strong>Os números são a ordem</strong> pela qual tem de as encaçapar &mdash; não são o valor das bolas</li>
            <li><strong>Os bloqueadores</strong> são desenhados baços e sem número: estão no caminho, não na sequência</li>
            <li><strong>A bola branca</strong> aparece a partir do nível Advanced. Abaixo disso, tem bola na mão</li>
          </ul>
        </div>
      </div>

      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-result.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Ecrã de resultado a mostrar 7 em 10, uma classificação de 58, o escalão League e o que fazer a seguir."></div>
        </div>
        <div>
          <p class="eyebrow">O resultado</p>
          <h3>Uma classificação e o nível que <span class="gold">o trava</span>.</h3>
          <p>Sete em dez passa um nível. Recebe a pontuação, a classificação de 0 a 100, o seu escalão e
          quanto o número se mexeu desde a última vez &mdash; e depois o nível que o está a travar, com o
          treino nesse nível a um toque de distância.</p>
        </div>
      </div>

      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-progress.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Ecrã de progresso a mostrar classificação, escalão, métricas acumuladas e detalhe por nível."></div>
        </div>
        <div>
          <p class="eyebrow">Progresso</p>
          <h3>Ver se o treino está a resultar.</h3>
          <p>Classificação, escalão, nível passado, taxa de limpeza acumulada e melhor série &mdash;
          gratuito, para sempre. O <a href="runout-pro.html">Runout Pro</a> acrescenta o histórico: cada
          teste representado ao longo do tempo e exportação para CSV.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid grid--3">
        <div class="card">
          <h3>Seis níveis, nenhum bloqueado</h3>
          <p>De Rookie a Master. Faça o teste em qualquer um deles &mdash; um bom jogador nunca tem de
          subir a pulso desde o fundo. <a href="levels.html">Comparar os níveis &rarr;</a></p>
        </div>
        <div class="card">
          <h3>Treine no seu limite</h3>
          <p>Disposições geradas sem fim no nível que o travou, com um registo de tudo o que já jogou.
          <a href="practice.html">Mais sobre o treino &rarr;</a></p>
        </div>
        <div class="card">
          <h3>O seu registo continua seu</h3>
          <p>Sem conta, sem servidor, funciona offline. Está tudo no seu dispositivo.
          <a href="privacy-policy.html">Política de privacidade &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

HOW = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Como funciona")}
      <h1>Como funciona a classificação do Runout Rank</h1>
      <p class="lead">Dez mesas geradas, uma tentativa cada, convertidas numa classificação de 0 a 100 e
      num escalão com nome &mdash; e uma instrução clara sobre o que fazer a seguir.</p>
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>1. Escolha um nível e comece o teste</h2>
      <p>Um teste são dez mesas num único nível. O nível é escolhido por si: a aplicação sugere um, mas nada
      está bloqueado, por isso um bom jogador pode começar em Competitor em vez de subir a pulso desde
      Rookie. Se nunca foi classificado, o teste está a um toque do ecrã inicial &mdash; não há nada para
      configurar primeiro.</p>
      <p>Se preferir aquecer, pode gerar antes uma mesa de treino avulsa e fazer o teste mais tarde.</p>

      <h2>2. Monte cada mesa numa mesa a sério</h2>
      <p>Cada mesa é desenhada vista de cima, com a bola branca, as bolas objeto e eventuais bloqueadores no
      sítio. Os bloqueadores são desenhados propositadamente baços e sem número, para que nunca sejam lidos
      como parte da ordem de encaçapamento. Monta o que vê, na mesa em que já joga. A ilustração fica no
      ecrã durante toda a tentativa, por isso pode reconstruir a disposição se lhe mexer.</p>

      <h2>3. Jogue uma vez, registe uma vez</h2>
      <p>Limpou a mesa, ou não. Um toque regista o resultado e leva-o à mesa seguinte. O cabeçalho mostra
      sempre em que mesa vai, de dez, e a faixa por cima da mesa mostra quais das mesas jogadas foram
      limpezas e quais foram falhas.</p>
      <p><strong>Há exatamente uma tentativa por mesa. Sem repetições, sem saltar mesas.</strong> É essa
      restrição a razão inteira de o número final valer alguma coisa.</p>
      <div class="note">Foi interrompido? Saia do teste e volte mais tarde &mdash; ele retoma exatamente na
      mesa em que parou. Sair de propósito pede confirmação primeiro e avisa que uma série incompleta não
      pode ser pontuada.</div>

      <h2>4. Leia o resultado</h2>
      <p>Assim que a décima mesa é registada, recebe:</p>
      <ul>
        <li><strong>Uma pontuação em dez</strong> &mdash; quantas das dez limpou.</li>
        <li><strong>Uma classificação de 0 a 100</strong> e o <strong>escalão</strong> correspondente.</li>
        <li><strong>Passou ou não.</strong> Sete em dez passa o nível.</li>
        <li><strong>A variação da sua classificação</strong> &mdash; quanto o número mexeu desde o último teste.</li>
        <li><strong>O seu nível-limite</strong> &mdash; o nível que o está a travar, com uma explicação em
        linguagem simples sobre o que fazer quanto a isso.</li>
      </ul>
      <p>A partir desse ecrã, treinar no seu nível-limite está a um toque.</p>

      <h2>Porque é que disposições aleatórias dão pontuações comparáveis</h2>
      <p>Cada teste é gerado de novo, por isso não há respostas para decorar nem exercícios que se possam
      ensaiar de antemão. Dois jogadores nunca encontram as mesmas dez mesas &mdash; e não precisam.</p>
      <p>O que está fixo é o <strong>nível</strong>. O número de bolas, se tem bola na mão, o espaçamento
      mínimo entre bolas e o número de bloqueadores são constantes definidas, idênticas para toda a gente
      nas duas plataformas. Um teste de Level&nbsp;4 faz sempre uma pergunta de Level&nbsp;4. Dez mesas
      chegam para a dificuldade se equilibrar, e é por isso que o teste tem dez mesas e não uma.</p>
      <p>Assim, o que está a ser medido é você face às restrições do nível, e não você face a dez mesas em
      particular. É isso que faz com que o 58 de um jogador signifique o mesmo que o 58 de outro.</p>

      <h2>Porque é que a classificação é absoluta</h2>
      <p>Nenhum adversário aparece nesse cálculo. Sistemas de liga como o Fargo Rate são <em>relativos</em>
      &mdash; o seu número resulta de resultados contra outros jogadores classificados, e é por isso que
      precisam de um grande historial de jogos até a classificação assentar, e que um meio local pouco
      ligado pode ficar alto ou baixo face ao resto da rede. O Runout Rank compara-o antes com um padrão
      fixo. As restrições dos níveis são as mesmas em todo o lado, por isso a classificação é a mesma
      medição em todo o lado, logo desde o primeiro teste.</p>
      <p>A única variável local é o seu equipamento. O corte das caçapas, o tamanho da mesa e a rapidez do
      pano mudam a dificuldade de limpar uma mesa, por isso faça o teste na mesa em que joga de facto e
      compare os seus próprios números ao longo do tempo.</p>
      <p><a href="absolute-vs-relative-pool-rating.html">Classificações de bilhar absolutas e relativas &rarr;</a></p>

      <h2>O que a classificação não é</h2>
      <p>É uma medição da sua capacidade de limpar mesas em disposições geradas, feita sob uma regra de não
      repetição. Não é um sistema de handicap, não é a classificação de uma federação e não comunica com
      nenhuma base de dados de ligas. Se precisa de um número para dar handicap num desafio, é para isso que
      serve uma classificação de liga &mdash; veja
      <a href="fargo-rate-alternative.html">como as duas se comparam</a>. Este é um número honesto que pode
      tirar sozinho, na sua própria mesa, sempre que quiser um novo.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="levels.html">Ver os seis níveis</a>
        <a class="btn btn--ghost" href="fargo-rate-alternative.html">Comparado com o Fargo Rate</a>
      </div>
    </div>
  </section>

{CTA}
"""

LEVELS = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Níveis")}
      <h1>Seis níveis, de Rookie a Master</h1>
      <p class="lead">A dificuldade é uma escada, não um cursor. Cada degrau muda algo concreto nas
      disposições que lhe pedem para limpar &mdash; e nenhum deles está bloqueado.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="table-wrap">
        <table>
          <caption class="sr-only">Os seis níveis do Runout Rank e o que muda em cada degrau</caption>
          <thead>
            <tr>
              <th scope="col">Nível</th>
              <th scope="col">Nome</th>
              <th scope="col">Bolas objeto</th>
              <th scope="col">Bola na mão</th>
              <th scope="col">Espaçamento mínimo</th>
              <th scope="col">Bloqueadores</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>1</strong></td><td><strong>Rookie</strong></td><td>2</td><td>Sim</td><td>8&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>2</strong></td><td><strong>Regular</strong></td><td>3</td><td>Sim</td><td>6&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>3</strong></td><td><strong>League</strong></td><td>4</td><td>Sim</td><td>4&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>4</strong></td><td><strong>Competitor</strong></td><td>5</td><td>Sim</td><td>2,25&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>5</strong></td><td><strong>Advanced</strong></td><td>5</td><td>Não</td><td>2,25&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>6</strong></td><td><strong>Master</strong></td><td>5</td><td>Não</td><td>2,25&Prime;</td><td>2</td></tr>
          </tbody>
        </table>
      </div>
      <p class="dim" style="margin-top:16px">O espaçamento é uma distância <em>mínima</em> de centro a centro,
      por isso um número maior significa uma disposição mais aberta e mais tolerante. 2,25&Prime; é o diâmetro
      de uma bola &mdash; o limite abaixo do qual as bolas se sobreporiam fisicamente. Os mesmos valores
      aparecem dentro da aplicação, no cartão de cada nível.</p>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Ler a escada</p>
        <h2>Quatro botões, rodados um degrau de cada vez</h2>
      </div>
      <div class="grid grid--4">
        <div class="card"><h3>Número de bolas</h3><p>Duas bolas em Rookie, subindo para cinco a partir de Competitor. Cada bola a mais é mais uma decisão de posição que tem de sair bem.</p></div>
        <div class="card"><h3>Bola na mão</h3><p>Os níveis 1 a 4 deixam-no colocar a branca. A partir de Advanced, ela fica onde a disposição a puser, e começa com aquilo que lhe é dado.</p></div>
        <div class="card"><h3>Aperto</h3><p>O intervalo mínimo entre bolas encolhe de 8&Prime; até ao diâmetro de uma bola. Bolas muito juntas tapam ângulos e estragam o jogo de posição.</p></div>
        <div class="card"><h3>Bloqueadores</h3><p>Só o Master acrescenta dois. Não fazem parte da ordem de encaçapamento &mdash; são desenhados baços e sem número &mdash; e existem apenas para lhe estarem no caminho.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-levels.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="O ecrã de níveis com o nível League expandido, a mostrar a melhor pontuação de teste e a taxa de treino recente."></div>
        </div>
        <div>
          <p class="eyebrow">A sua posição, degrau a degrau</p>
          <h3>Cada nível sabe como se está a sair nele</h3>
          <p>Expanda qualquer nível para ver a sua melhor pontuação de teste aí, a sua taxa de limpeza no
          treino recente e em quantas tentativas essa taxa assenta &mdash; para distinguir uma fraqueza a
          sério de uma noite má. Os níveis passados ficam assinalados, e o seu
          <span class="gold">limite</span> &mdash; o nível que o está a travar &mdash; é destacado a
          dourado.</p>
          <ul class="ticks ticks--gold">
            <li>Comece um teste em qualquer nível, não apenas no seguinte</li>
            <li>Repita um nível que já testou para confirmar ou melhorar o resultado</li>
            <li>Comece treino livre em qualquer nível diretamente a partir da escada</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

PRACTICE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Treino")}
      <h1>Treino, e um registo de tudo o que já jogou</h1>
      <p class="lead">O teste diz-lhe que nível o trava. O treino é onde faz alguma coisa quanto a isso
      &mdash; um fluxo interminável de disposições geradas exatamente nesse nível.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-practice.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Uma sessão de treino com uma disposição gerada de quatro bolas e a pergunta sobre se limpou a mesa."></div>
        </div>
        <div>
          <p class="eyebrow">Uma sessão</p>
          <h3>Nunca ficar sem material, nunca decorar uma disposição</h3>
          <p>As mesas de treino são geradas a pedido no nível que escolher, e as suas tentativas contam para
          as estatísticas desse nível. A ilustração fica no ecrã durante toda a tentativa, por isso pode
          voltar a montá-la se a disposição se desfizer.</p>
          <ul class="ticks">
            <li>Um toque regista um êxito ou um falhanço, com confirmação de que ficou registado</li>
            <li>Salte uma disposição que não queira jogar, em vez de deixar a sessão parada</li>
            <li>Repita exatamente a mesma disposição para a treinar até a dominar</li>
            <li>Gere a mesa seguinte logo a seguir ao registo &mdash; um ciclo, não uma árvore de menus</li>
            <li>Reabra a última mesa gerada a partir do ecrã inicial depois de fechar a aplicação</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">O registo de treino</p>
        <h2>Um registo completo do trabalho que já fez</h2>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>Todas as mesas que jogou</h3><p>Percorra tudo, com a data, o nível e em quantas tentativas limpou a mesa.</p></div>
        <div class="card"><h3>Favoritos</h3><p>Marque com estrela as disposições que vale a pena repetir e filtre o registo só por favoritos, construindo uma biblioteca pessoal de exercícios.</p></div>
        <div class="card"><h3>Continue a partir de qualquer ponto</h3><p>Escolha qualquer mesa do registo e continue a treinar a partir dela. Voltar a uma disposição antiga é um toque.</p></div>
      </div>
      <p class="dim" style="margin-top:20px">Um registo vazio diz-lhe como o preencher, em vez de lhe mostrar um ecrã em branco.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-progress.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="O ecrã Rank a mostrar a classificação atual, o escalão, as métricas acumuladas e o detalhe por nível."></div>
        </div>
        <div>
          <p class="eyebrow">Onde está &mdash; grátis, sempre</p>
          <h3>Os números que respondem a &ldquo;estou a melhorar?&rdquo;</h3>
          <p>A sua classificação de 0 a 100 e o escalão, o nível mais alto que passou, o seu nível-limite e a
          variação da classificação desde o último teste. Por baixo: tentativas acumuladas, total de limpezas,
          taxa global de limpeza e melhor série, além de uma leitura em linguagem simples do rácio &mdash;
          &ldquo;está a limpar 1 em cada N mesas&rdquo;.</p>
          <p>Repetir o teste no seu nível-limite é um toque a partir do mesmo ecrã.</p>
          <p><a href="runout-pro.html">O que o Runout Pro acrescenta &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

PRO = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Runout Pro")}
      <h1>Runout Pro</h1>
      <p class="lead">Uma fronteira, uma frase: <strong>onde está é grátis, como lá chegou é Pro.</strong></p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid grid--2">
        <div class="card">
          <p class="eyebrow">Grátis, para sempre</p>
          <h3>Onde está</h3>
          <ul class="ticks">
            <li>A sua classificação de 0 a 100 e o escalão</li>
            <li>O nível que passou e o nível que o trava</li>
            <li>Variação da classificação desde o último teste</li>
            <li>Detalhe por nível: melhor pontuação de teste e taxa de treino recente</li>
            <li>Tentativas, limpezas, taxa de limpeza e melhor série acumuladas</li>
            <li>Testes ilimitados e treino ilimitado em todos os níveis</li>
          </ul>
          <p class="dim">Nada disto é uma versão de avaliação. A aplicação é plenamente útil sem pagar.</p>
        </div>
        <div class="card card--gold">
          <p class="eyebrow eyebrow--gold">Runout Pro</p>
          <h3>Como cá chegou</h3>
          <ul class="ticks ticks--gold">
            <li>A sua classificação representada ao longo de todos os testes que alguma vez fez</li>
            <li>Evolução da pontuação em cada nível &mdash; todos os testes, não apenas o melhor</li>
            <li>Taxa de limpeza ao longo do tempo e o histórico das suas sessões</li>
            <li>Um registo de testes completo: nível, pontuação, data e variação de classificação de cada série</li>
            <li>Exportação para CSV de todo o seu histórico</li>
          </ul>
          <p class="dim">Subscreva mensalmente ou anualmente. Todo o seu histórico passado é desbloqueado de
          imediato &mdash; não há novo período de recolha à espera.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Como se comporta a proposta de subscrição</p>
        <h2>Um cartão honesto, e não cadeados por toda a página</h2>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>Nada de venda no primeiro dia</h3><p>A um jogador novo, sem histórico de testes, não é mostrada qualquer proposta comercial. Uma barreira de pagamento por algo que ainda não imagina querer é apenas ruído.</p></div>
        <div class="card"><h3>Uma pré-visualização dos seus dados</h3><p>Assim que tiver histórico suficiente para desbloquear algo, vê a sua própria curva de progresso com os valores ocultos &mdash; e não um anúncio genérico.</p></div>
        <div class="card"><h3>Uma fronteira, no fundo</h3><p>O ecrã Rank tem exatamente um cartão Pro. Espalhar ícones de cadeado por um ecrã faz com que cada funcionalidade gratuita pareça uma amostra.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Faturação, restauro e cancelamento</h2>
      <ul>
        <li>Os preços são mostrados em direto a partir da App Store ou do Google Play, com a poupança anual
        calculada com base neles, por isso o que vê é o que a sua loja vai cobrar na sua moeda.</li>
        <li>Já o comprou? <strong>Restaurar compra</strong> traz tudo de volta depois de uma reinstalação ou
        num segundo dispositivo &mdash; reinstalar nunca lhe custa duas vezes.</li>
        <li>Faça a gestão ou cancele quando quiser na sua conta Apple ou Google. Reembolsos e questões de
        faturação são tratados pela loja, segundo os termos dela.</li>
        <li>Os Termos de Utilização e a <a href="privacy-policy.html">política de privacidade</a> podem ser
        lidos antes de subscrever, e não depois.</li>
        <li><strong>O Pro continua a funcionar offline.</strong> Uma má rede num salão de bilhar nunca o
        deixa de fora daquilo que pagou.</li>
      </ul>
      <p>Os pagamentos são processados inteiramente pela Apple e pela Google. O Runout Rank nunca vê nem
      guarda os dados do seu cartão.</p>
    </div>
  </section>

{CTA}
"""

GUIDE_TITLE = "Como testar o seu nível de bilhar (e obter um número em que possa confiar)"
GUIDE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Teste de nível de bilhar")}
      <h1>Como testar o seu nível de bilhar</h1>
      <p class="lead">Quase todos os jogadores sabem dizer a quem ganham. Muito poucos sabem dizer quão bons
      são. Eis o que separa um teste de nível que vale a pena fazer de um exercício de que calha gostar.</p>
{byline(UI, FIRST_PUBLISHED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Porque é tão difícil responder a &ldquo;quão bom sou?&rdquo;</h2>
      <p>Os resultados das partidas medem tanto os seus adversários como o medem a si. Uma boa noite contra
      um lote fraco e uma má noite contra um lote forte podem dar resultados idênticos. O treino parece
      produtivo quer esteja a resultar quer não, porque naturalmente o gasta em tacadas de que já gosta. E os
      exercícios que a maioria dos jogadores faz são aqueles que já fez antes &mdash; o que é exatamente a
      razão de se tornarem mais fáceis.</p>
      <p>Um teste de nível útil tem de fazer três coisas que o treino informal não faz.</p>

      <h2>1. Tem de medir uma competência inteira, não uma tacada isolada</h2>
      <p>Encaçapar uma bola longa a direito diz-lhe algo sobre um gesto. Limpar uma mesa diz-lhe algo sobre
      leitura de padrões, jogo de posição, controlo de força, critério defensivo e nervos, pela ordem em que
      a mesa os exige. É por isso que a limpeza de mesa &mdash; a mesa inteira, do princípio ao fim &mdash; é
      a unidade de medida certa para um teste de nível, e é por isso que o Runout Rank pontua mesas em vez de
      tacadas.</p>

      <h2>2. Tem de ser imprevisível</h2>
      <p>Qualquer conjunto fixo de disposições degenera num teste de memória. À décima vez que monta o mesmo
      exercício, já não está a medir capacidade de limpar mesas, está a medir o quão bem se lembra da solução
      daquela mesa em concreto. Um teste que valha a pena repetir tem de gerar as suas disposições, para que
      o padrão à sua frente seja genuinamente novo de cada vez.</p>

      <h2>3. A dificuldade tem de ser definida, não improvisada</h2>
      <p>Eis a tensão: a aleatoriedade torna um teste honesto e, ao mesmo tempo, ameaça tornar duas pontuações
      incomparáveis. Se as suas dez mesas foram mais difíceis do que as minhas, as nossas pontuações
      significam coisas diferentes.</p>
      <p>A solução é <strong>fixar as restrições em vez das disposições</strong>. Definir com precisão o que
      significa um nível de dificuldade &mdash; quantas bolas objeto, se há bola na mão, o espaçamento mínimo
      entre bolas, quantos bloqueadores &mdash; e gerar livremente dentro dessas regras. Todas as disposições
      são novas, todas têm a mesma dificuldade, e mesas suficientes seguidas equilibram a sorte que reste. No
      Runout Rank, essas constantes estão publicadas na <a href="levels.html">página dos níveis</a> e são
      idênticas em Android e iOS.</p>
      <p>É isso que torna uma pontuação portátil: diz que limpou sete em dez no Level&nbsp;4, e o
      Level&nbsp;4 significa o mesmo para toda a gente.</p>

      <h2>As regras que tornam uma pontuação honesta</h2>
      <ul>
        <li><strong>Uma tentativa por mesa.</strong> À melhor de três mede o seu melhor dia, não o seu
        nível habitual.</li>
        <li><strong>Não saltar mesas.</strong> As disposições que preferia evitar são precisamente as que
        carregam a informação.</li>
        <li><strong>Um número fixo de mesas.</strong> Dez chega para equilibrar um mau ressalto e é curto o
        bastante para terminar numa só ida à mesa.</li>
        <li><strong>Uma marca de aprovação declarada.</strong> Sete em dez passa um nível no Runout Rank.
        Saber a fasquia antes de começar faz parte do teste.</li>
        <li><strong>Registar de imediato.</strong> Um resultado que anota uma hora depois é um resultado que
        já embelezou.</li>
      </ul>

      <h2>O que fazer com o número</h2>
      <p>Uma classificação por si só é curiosidade. O número só é útil se apontar para algum lado, e é por
      isso que o resultado importante de um teste não é a pontuação mas o
      <strong>nível-limite</strong> &mdash; o degrau que ainda não consegue passar. É aí que o treino
      compensa, porque é o único nível em que as disposições ainda lhe fazem uma pergunta a que não sabe
      responder.</p>
      <p>O ciclo prático é assim:</p>
      <ol>
        <li>Faça o teste num nível que ache que consegue passar.</li>
        <li>Se passar, teste o nível acima até que um o trave.</li>
        <li>Treine nesse nível-limite, registando as tentativas para que a taxa de limpeza seja real.</li>
        <li>Repita o teste no mesmo nível quando a taxa se mexer. Compare classificações, não sensações.</li>
      </ol>

      <h2>Com que frequência repetir o teste</h2>
      <p>Com frequência suficiente para o número acompanhar a realidade, e com espaçamento suficiente para
      cada repetição refletir trabalho a sério. Para a maioria dos jogadores que fazem duas idas à mesa por
      semana, de duas em duas a quatro semanas é o adequado. Repetir o teste depois de cada sessão mede
      sobretudo ruído; repeti-lo duas vezes por ano não lhe diz nada sobre o qual possa agir.</p>

      <h2>Porque é que isto é melhor do que esperar que uma classificação de liga assente</h2>
      <p>A alternativa para que a maioria dos jogadores é encaminhada é uma classificação relativa obtida
      jogando na liga, que precisa de um grande historial de jogos contra outros jogadores classificados para
      significar muito &mdash; a FargoRate, por exemplo, considera 200 jogos o mínimo para uma classificação
      estabelecida. Um teste de limpeza de mesa dá-lhe a resposta numa só ida à mesa porque o mede face às
      disposições e não face à sala, o que também significa que não oscila com a força do meio onde joga.
      Leitura adicional:</p>
      <ul>
        <li><a href="fargo-rate-alternative.html">Uma alternativa ao Fargo Rate que não exige 200 jogos de liga</a></li>
        <li><a href="pool-rating-without-a-league.html">Como obter uma classificação de bilhar sem entrar numa liga</a></li>
        <li><a href="absolute-vs-relative-pool-rating.html">Classificações de bilhar absolutas e relativas</a></li>
      </ul>

      <div class="note">O Runout Rank faz tudo isto na mesa em que já joga: gera as disposições, pontua as
      limpezas, guarda o histórico no seu dispositivo e indica o nível em que deve treinar a seguir.
      <a href="how-it-works.html">Veja exatamente como funciona o teste &rarr;</a></div>
    </div>
  </section>

{CTA}
"""

# --------------------------------------------------------------------------
# Positioning pages: the two pain points a relative league rating leaves open
# --------------------------------------------------------------------------

FARGO_DISCLAIMER = """      <p class="disclaimer">O Runout Rank é independente e não está associado, apoiado nem
      ligado à FargoRate. Tudo o que aqui se diz sobre o Fargo Rate provém do
      <a href="https://www.fargorate.com/" rel="nofollow">material publicado pela própria FargoRate</a>
      e é descrito da forma mais justa que sabemos; é um bom sistema, e esta página trata apenas de onde o
      seu desenho serve, e não serve, um determinado tipo de jogador.</p>"""

FARGO_ALT_TITLE = "Uma alternativa ao Fargo Rate que não exige 200 jogos de liga"
FARGO_ALT = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Alternativa ao Fargo Rate")}
      <h1>Uma alternativa ao Fargo Rate para quem nunca vai jogar 200 jogos de liga</h1>
      <p class="lead">O Fargo Rate é a melhor classificação relativa que o bilhar tem. Mas é precisamente o
      facto de ser relativa que a torna lenta de conquistar e sensível ao sítio onde vive. Eis o que uma
      classificação absoluta faz de diferente, e qual das duas quer realmente.</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Primeiro, o mérito devido</h2>
      <p>O Fargo Rate pôs amadores e campeões do mundo numa mesma escala e transformou o handicap no bilhar
      em algo que se discute com números em vez de reputações. Se joga partidas de liga todas as semanas
      contra outros jogadores classificados, funciona, e esta página não vai fingir o contrário. Fique com
      ele.</p>
      <p>A questão de que esta página trata é mais estreita: <strong>o que faz se não for esse
      jogador?</strong> Se treina sozinho, joga por gosto com amigos, viaja, ou simplesmente quer saber quão
      bom é sem se inscrever numa época inteira de partidas, uma classificação relativa tem dois problemas
      estruturais &mdash; e são estruturais, não são defeitos.</p>

      <h2>Ponto sensível um: o número só é real ao fim de 200 jogos</h2>
      <p>A FargoRate chama <em>robustez</em> à dimensão do seu historial de jogos e afirma claramente que uma
      robustez de 200 jogos é o mínimo para considerar uma classificação
      &ldquo;estabelecida&rdquo;. Abaixo desse limiar, a sua classificação oficial é uma mistura do seu
      desempenho real com uma <em>classificação inicial</em> &mdash; um palpite de partida &mdash; em que o
      palpite vai perdendo influência à medida que se aproxima dos 200.</p>
      <p>Faça as contas ao que 200 jogos classificados custam a uma pessoa normal. Significa encontrar uma
      liga que reporte ao sistema, pagar as respetivas inscrições, ter a mesma noite livre todas as semanas e
      jogar a maior parte de uma época ou duas &mdash; antes de o número na aplicação ser uma medição sua em
      vez de uma opinião ponderada. Um jogador que queira uma única resposta honesta a &ldquo;quão bom
      sou?&rdquo; tem de comprar um ano de compromisso para a obter.</p>
      <p>E não há atalho possível, porque não há nada para encurtar: um sistema relativo genuinamente não
      pode saber nada sobre si enquanto não gerar resultados suficientes contra pessoas que ele já conhece.</p>
      <p><a href="pool-rating-without-a-league.html">Como obter uma classificação de bilhar sem entrar numa liga &rarr;</a></p>

      <h2>Ponto sensível dois: a sua classificação descreve em parte a sua cidade</h2>
      <p>Uma classificação relativa é calculada a partir de quem ganhou a quem. Isso significa que o seu
      número só está tão ancorado quanto a cadeia de jogos que liga os jogadores da sua zona ao resto do
      mundo classificado. Onde essa cadeia é espessa &mdash; grandes cidades, circuitos fortes, jogadores que
      viajam para provas abertas &mdash; as classificações alinham bem. Onde é ténue, um grupo local pode
      assentar num nível que não corresponde aos mesmos números noutro sítio.</p>
      <p>Esta não é uma queixa de quem está de fora. Os próprios textos da FargoRate descrevem dois grupos de
      jogadores quase isolados, um classificado alto demais em relação ao outro, como um problema
      particularmente espinhoso &mdash; que só se corrige com muitos jogos cruzados ao longo de muito tempo.
      A sua definição de classificação fiável nota igualmente que jogos contra adversários com classificação
      estabelecida contam mais.</p>
      <p>Assim, se a sua região está cheia de jogadores fortes, ou mal ligada à rede mais alargada, ou é nova
      no sistema, o número que carrega está a dizer-lhe algo sobre o que o rodeia, além de dizer algo sobre
      si. Mude-se para outro sítio e ele pode deixar de significar o que significava em casa.</p>
      <p><a href="absolute-vs-relative-pool-rating.html">Classificações absolutas e relativas, explicadas &rarr;</a></p>

      <h2>O que uma classificação absoluta faz em vez disso</h2>
      <p>O Runout Rank retira por completo os adversários da medição. Em vez de perguntar a quem ganhou, põe
      uma disposição definida na mesa e pergunta se consegue limpá-la.</p>
      <p>Joga dez mesas geradas num único nível, uma tentativa cada, sem repetições nem saltar mesas, e
      regista cada uma como limpeza ou falha. Dez respostas tornam-se uma pontuação, uma classificação de 0 a
      100 e um escalão de Rookie a Master. Sete em dez passa o nível. Tudo isto leva cerca de uma hora na
      mesa em que já joga.</p>
      <p>Como as disposições são a bitola e a bitola nunca muda, o número significa o mesmo esteja quem
      estiver na sala, e significa o mesmo no próximo ano e neste. É conquistado logo na primeira sessão, e
      não acumulado ao longo de uma época.</p>

      <h2>Lado a lado</h2>
      <div class="table-wrap">
        <table>
          <caption class="sr-only">Classificações de liga relativas comparadas com a classificação absoluta do Runout Rank</caption>
          <thead>
            <tr>
              <th scope="col"></th>
              <th scope="col">Classificação relativa (Fargo Rate e afins)</th>
              <th scope="col">Runout Rank</th>
            </tr>
          </thead>
          <tbody>
            <tr><th scope="row">O que mede</th><td>Resultados contra outros jogadores classificados</td><td>Limpezas de mesa em disposições fixas geradas</td></tr>
            <tr><th scope="row">Até significar algo</th><td>200 jogos para uma classificação estabelecida; abaixo disso é misturada uma classificação inicial</td><td>Um teste de dez mesas, cerca de uma hora</td></tr>
            <tr><th scope="row">O que precisa</th><td>Uma liga que reporte ou provas classificadas, adversários, inscrições, um horário</td><td>Uma mesa de bilhar e um telemóvel</td></tr>
            <tr><th scope="row">Efeito do meio local</th><td>Real: a ligação e a força do grupo de jogadores influenciam o número</td><td>Nenhum: não entram adversários</td></tr>
            <tr><th scope="row">Portabilidade</th><td>Viaja dentro da rede; regiões mal ligadas podem desviar-se</td><td>As mesmas restrições de nível em todo o lado, em Android e iOS</td></tr>
            <tr><th scope="row">Boa para</th><td>Dar handicap em desafios, quadros de torneio, elegibilidade em ligas</td><td>Saber o seu próprio nível e o que treinar a seguir</td></tr>
            <tr><th scope="row">Não serve para</th><td>Responder a &ldquo;quão bom sou?&rdquo; logo no primeiro dia</td><td>Dar handicap num desafio contra outra pessoa &mdash; não é um sistema de handicap</td></tr>
            <tr><th scope="row">Custo e conta</th><td>Filiação na liga; um perfil online</td><td>Aplicação gratuita, sem conta, funciona totalmente offline</td></tr>
          </tbody>
        </table>
      </div>

      <h2>Que fique claro o que o Runout Rank não é</h2>
      <p>Não substitui uma classificação de liga para dar handicap, e não o vai colocar como cabeça de série
      num torneio. Nenhuma federação o reconhece. É também honesto quanto à sua própria variável: está a
      jogar no seu equipamento, por isso uma mesa de caçapas apertadas e pano lento dará uma leitura
      diferente de uma mesa de bar. Faça o teste na mesa em que compete de facto e compare o que é
      comparável ao longo do tempo.</p>
      <p>O que lhe dá é aquilo que um sistema relativo não lhe pode dar barato: um número a sério hoje, a
      partir do seu próprio jogo, que não depende de mais ninguém.</p>

      <h2>A resposta óbvia: use os dois</h2>
      <p>Medem coisas diferentes e não estão em conflito. Se joga na liga, guarde o Fargo Rate para as
      partidas e use o Runout Rank entre elas para saber que parte do seu jogo está atrasada &mdash; um teste
      de limpeza de mesa nomeia o nível que o trava e põe-lhe treino nesse nível na mão, coisa que uma
      classificação por resultados não consegue fazer. Se não joga na liga, o Runout Rank é o número que pode
      realmente ter.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="how-it-works.html">Ver como funciona o teste</a>
        <a class="btn btn--ghost" href="pool-rating-without-a-league.html">Obter uma classificação sem liga</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

NO_LEAGUE_TITLE = "Como obter uma classificação de bilhar sem entrar numa liga"
NO_LEAGUE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Uma classificação sem liga")}
      <h1>Como obter uma classificação de bilhar sem entrar numa liga</h1>
      <p class="lead">Todos os sistemas de classificação estabelecidos pedem a mesma entrada: centenas de
      partidas contra outros jogadores classificados. Se essa não é a sua vida, não é que não possa ser
      classificado &mdash; só precisa de uma classificação que meça a mesa em vez de medir a sala.</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Porque é que os jogadores ocasionais acabam sem número nenhum</h2>
      <p>O conselho habitual é: entre numa liga que reporte a um sistema de classificação, jogue uma época e
      a sua classificação assentará. É um bom conselho e, para muitos jogadores, é também impossível. Exige
      uma noite fixa todas as semanas, quotas, um espaço que organize uma liga que reporte, e adversários
      suficientes que estejam eles próprios classificados.</p>
      <p>Depois há o volume. A FargoRate considera 200 jogos a robustez mínima para chamar estabelecida a uma
      classificação; abaixo disso, parte do que está a ver é a classificação inicial que o sistema lhe
      atribuiu e não aquilo que fez. Duzentos jogos classificados são uma época ou mais para a maioria dos
      jogadores de liga, e uma fantasia para todos os outros.</p>
      <p>Por isso, a posição honesta para um jogador ocasional é esta: o esforço de conquistar uma
      classificação relativa é maior do que o valor de a conhecer. A maioria das pessoas desiste em silêncio
      e volta a adivinhar a partir de quem consegue ganhar no clube.</p>

      <h2>O que quer mesmo descobrir</h2>
      <p>Tirando os sistemas do caminho, por baixo há normalmente três perguntas:</p>
      <ul>
        <li><strong>Onde estou?</strong> Sou um jogador de clube razoável, ou melhor do que penso, ou pior?</li>
        <li><strong>Estou a melhorar?</strong> Não &ldquo;senti-me bem esta noite&rdquo; &mdash; a curva está
        a mexer?</li>
        <li><strong>O que devo treinar?</strong> Que parte do jogo está mesmo a travar o resto?</li>
      </ul>
      <p>Nenhuma destas três perguntas exige um adversário. Exigem uma tarefa fixa e repetível, difícil o
      bastante para se falhar, e um registo de quantas vezes a completa.</p>

      <h2>O teste que lhes responde</h2>
      <p>A limpeza de mesa é a unidade certa: limpar uma mesa exercita leitura de padrões, posição, controlo
      de força e nervos pela ordem em que a mesa os exige, coisa que um exercício de encaçapamento isolado não
      faz. Faça disso dez mesas num único nível de dificuldade, uma tentativa cada, sem repetições nem saltar
      mesas, e passa a ter uma medição em vez de uma sessão de treino.</p>
      <p>É isso que o Runout Rank faz. A aplicação desenha cada disposição vista de cima, monta-a na sua
      própria mesa, joga-a uma vez e toca em limpou ou falhou. No fim recebe uma pontuação em dez, uma
      classificação de 0 a 100, um escalão de Rookie a Master, se passou o nível, e o nível que o está a
      travar. Leva cerca de uma hora e não precisa de mais ninguém no edifício.</p>
      <p>As disposições são geradas de novo em cada teste, por isso não há nada para decorar, enquanto as
      restrições do nível &mdash; número de bolas, bola na mão, espaçamento, bloqueadores &mdash; são
      constantes fixas, iguais para todos os jogadores em Android e iOS. Mesas novas de cada vez, a mesma
      dificuldade de cada vez.</p>

      <h2>Uma rotina prática para quem joga sozinho</h2>
      <ol>
        <li><strong>Faça o teste no nível que acha que consegue passar.</strong> Nada está bloqueado, por isso
        comece onde acha que pertence e não no fundo.</li>
        <li><strong>Suba até um nível o travar.</strong> Sete em dez passa um nível; quando não consegue fazer
        sete, encontrou o seu limite.</li>
        <li><strong>Treine no nível-limite,</strong> registando cada tentativa para que a taxa de limpeza seja
        um facto e não uma impressão.</li>
        <li><strong>Repita o teste nesse nível quando a taxa se mexer.</strong> De duas em duas a quatro
        semanas serve a maioria dos jogadores &mdash; com frequência suficiente para acompanhar trabalho a
        sério, e espaçado o bastante para não estar a medir ruído.</li>
        <li><strong>Compare classificações, não sensações.</strong> A variação da classificação no ecrã de
        resultado é o essencial de tudo isto.</li>
      </ol>

      <h2>O que lhe custa</h2>
      <p>Uma hora, uma mesa que consiga reservar, e mais nada. A aplicação é gratuita, não há conta para
      criar, funciona inteiramente offline e o seu histórico fica no armazenamento privado da aplicação, no
      seu próprio dispositivo. O Runout Pro é opcional e acrescenta o histórico: a sua classificação
      representada ao longo de todos os testes, a evolução por nível e a exportação para CSV. Saber onde está
      é gratuito para sempre.</p>

      <h2>Se joga mesmo na liga</h2>
      <p>Então guarde a sua classificação de liga &mdash; é a ferramenta certa para dar handicap em partidas,
      e isto não a substitui. Use um teste de limpeza de mesa a par dela, porque uma classificação por
      resultados diz-lhe o nível em que está sem lhe dizer que parte do seu jogo está atrasada. Veja
      <a href="fargo-rate-alternative.html">a comparação completa com o Fargo Rate</a>.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="how-it-works.html">Como funciona o teste</a>
        <a class="btn btn--ghost" href="levels.html">Ver os seis níveis</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

ABSOLUTE_TITLE = "Classificações de bilhar absolutas e relativas: porque é que a sua cidade muda o seu número"
ABSOLUTE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Classificação absoluta e relativa")}
      <h1>Classificações de bilhar absolutas e relativas</h1>
      <p class="lead">Dois jogadores de capacidade idêntica, um numa cidade forte e outro numa cidade
      calma, podem carregar classificações relativas diferentes durante anos. Isso não é um defeito das
      contas &mdash; é o que &ldquo;relativa&rdquo; quer dizer. Eis a diferença, e para que serve cada tipo
      de classificação.</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>O que é uma classificação relativa</h2>
      <p>Uma classificação relativa &mdash; Elo, Glicko, Fargo Rate e o resto da família &mdash; não tem
      noção de padrão absoluto. Só conhece resultados: você ganhou-lhes, eles ganharam a outros. A partir de
      uma teia suficientemente grande desses resultados, o sistema encontra o conjunto de números que melhor
      explica os desfechos. Ninguém é alguma vez medido diretamente; cada classificação é uma posição numa
      rede de outras classificações.</p>
      <p>É um desenho elegante e funciona notavelmente bem quando a rede é densa. Também traz duas
      consequências que nenhuma matemática engenhosa elimina.</p>

      <h2>Consequência um: precisa de muitos jogos</h2>
      <p>Um resultado é um bit de prova, e um bit é muito pouco. Por isso o sistema precisa de volume antes de
      o conseguir separar da sorte &mdash; e é por isso que a FargoRate usa uma medida de robustez e considera
      200 jogos o mínimo para chamar estabelecida a uma classificação, misturando uma classificação inicial no
      número até lá chegar. Enquanto não tiver pago esse preço em jogos, a sua classificação é em parte um
      palpite sobre si.</p>

      <h2>Consequência dois: está ancorada nos seus vizinhos</h2>
      <p>Como cada classificação é definida face a outras classificações, um grupo de jogadores só alinha
      corretamente com o resto do mundo se houver jogos suficientes a ligá-lo a ele. Onde essa ligação é ténue
      &mdash; uma região isolada, uma liga nova, um meio cujos jogadores raramente vão a provas abertas
      &mdash; o grupo pode assentar num nível que não corresponde aos mesmos números noutro sítio. A FargoRate
      descreve exatamente este caso, dois grupos quase isolados com um classificado alto demais em relação ao
      outro, como um problema espinhoso, e nota que jogos contra adversários estabelecidos valem mais
      precisamente por essa razão.</p>
      <p>A versão prática para um jogador: se a sua cidade está cheia de jogadores fortes, ou mal ligada à
      população classificada mais alargada, o seu número é em parte uma afirmação sobre o que o rodeia. Dois
      jogadores do mesmo nível em meios diferentes não têm de dar leituras iguais, e nenhum deles pode fazer
      nada quanto a isso a não ser jogar mais contra gente de fora.</p>

      <h2>O que é uma classificação absoluta</h2>
      <p>Uma classificação absoluta mede o desempenho face a um padrão fixo em vez de o medir face a pessoas.
      Os handicaps do golfe funcionam assim, face ao par. O atletismo funciona assim, face ao cronómetro. Um
      cronómetro não quer saber quem mais está na corrida, e 10,4 segundos em Manila são 10,4 segundos em
      Manchester.</p>
      <p>O bilhar tradicionalmente não teve nada disso, porque lhe falta um cronómetro óbvio. O Runout Rank
      fornece o equivalente: um conjunto de disposições definidas e uma pergunta &mdash; consegue limpar
      isto? Dez mesas num nível, uma tentativa cada, sem repetições nem saltar mesas. O número que sai é
      calculado inteiramente a partir dos seus próprios resultados face às disposições.</p>
      <p>Assim, não há grupo de adversários que possa ser forte ou fraco, não há nada em relação a que se
      desviar, e não há número mínimo de jogos antes de a medição ser válida. Tem a sua classificação no fim
      da primeira sessão, e ela significa o mesmo em qualquer lugar.</p>

      <h2>Como é que um padrão fixo evita tornar-se um teste de memória</h2>
      <p>A objeção óbvia: um conjunto fixo de disposições deixa de medir competência assim que o joga umas
      quantas vezes, porque passa a recordar soluções em vez de as encontrar.</p>
      <p>O Runout Rank evita isso fixando a <em>dificuldade</em> em vez das mesas. Um nível é um conjunto de
      constantes publicadas &mdash; número de bolas objeto, bola na mão ou não, espaçamento mínimo,
      bloqueadores &mdash; e as disposições são geradas de novo dentro dessas regras de cada vez. Nunca vê a
      mesma mesa duas vezes, e todas as mesas fazem a mesma pergunta. Dez seguidas equilibram a sorte que
      reste.</p>

      <h2>O que uma classificação absoluta não consegue fazer</h2>
      <p>Não é um sistema de handicap e não deve ser usada como tal. Uma classificação relativa existe para
      prever um desafio entre duas pessoas concretas, e é muito melhor nisso do que qualquer medida absoluta
      &mdash; porque são os desfechos das partidas que a constroem.</p>
      <p>Uma classificação absoluta tem também a sua própria variável a manter honesta: o equipamento. O corte
      das caçapas, o tamanho da mesa e a rapidez do pano mudam todos a dificuldade de limpar uma mesa, por
      isso uma classificação tirada numa mesa de nove pés com caçapas apertadas é uma medição diferente de
      uma tirada numa mesa de bar. Fixe as suas condições, faça o teste na mesa em que compete e compare os
      seus próprios números ao longo do tempo.</p>

      <h2>Qual delas quer?</h2>
      <div class="compare" style="margin:24px 0">
        <div class="card">
          <h3>Use uma classificação relativa quando</h3>
          <ul class="ticks">
            <li>Precisa de um handicap para um desafio ou um quadro</li>
            <li>A sua liga ou torneio o exige</li>
            <li>Já joga jogos classificados que cheguem para a manter robusta</li>
          </ul>
        </div>
        <div class="card card--gold">
          <h3>Use uma classificação absoluta quando</h3>
          <ul class="ticks ticks--gold">
            <li>Quer saber onde está sem jogar primeiro uma época</li>
            <li>Treina sozinho, viaja ou muda de meio</li>
            <li>Quer saber <em>o que treinar</em>, e não apenas como se classifica</li>
          </ul>
        </div>
      </div>
      <p>Respondem a perguntas diferentes, e um jogador sério pode perfeitamente ter as duas.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="fargo-rate-alternative.html">Comparado com o Fargo Rate</a>
        <a class="btn btn--ghost" href="how-it-works.html">Como é calculada a classificação</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

FAQ_ITEMS = [
    ("Preciso de uma mesa de bilhar a sério para usar o Runout Rank?",
     "Sim. O Runout Rank não é um jogo de bilhar &mdash; é um companheiro para uma mesa a sério. A aplicação "
     "desenha cada disposição vista de cima, monta-a no pano à sua frente, joga-a e regista o que aconteceu."),
    ("Preciso de conta ou de ligação à Internet?",
     "Não, nem uma coisa nem outra. Não há nada para registar nem nada onde iniciar sessão, e a aplicação "
     "funciona totalmente offline. Os seus testes, tentativas, favoritos e estatísticas ficam apenas no "
     "armazenamento privado da aplicação, no seu próprio dispositivo."),
    ("Como é calculada a classificação?",
     "Joga dez mesas geradas num único nível, uma tentativa cada. A pontuação em dez é convertida numa "
     "classificação de 0 a 100 com um escalão com nome, e sete em dez passa o nível. O resultado mostra "
     "também quanto a sua classificação mexeu desde o último teste."),
    ("Se os testes são aleatórios, como podem duas pontuações ser comparadas?",
     "Porque o que está fixo é o nível e não as mesas. Cada nível define o número de bolas objeto, se tem "
     "bola na mão, o espaçamento mínimo entre bolas e o número de bloqueadores, e essas constantes são "
     "idênticas para todos os jogadores nas duas plataformas. As disposições são geradas de novo dentro "
     "dessas regras, e dez mesas seguidas equilibram a sorte &mdash; por isso sete em dez no Level 4 "
     "significa o mesmo, seja quem for a consegui-lo."),
    ("Posso repetir uma mesa que joguei mal?",
     "Não durante um teste &mdash; uma tentativa por mesa, sem repetições nem saltar mesas, e é isso que faz "
     "a pontuação significar alguma coisa. No treino livre pode repetir a mesma disposição as vezes que "
     "quiser."),
    ("O que acontece se for interrompido a meio de um teste?",
     "O teste retoma exatamente na mesa em que parou. Sair de propósito pede-lhe confirmação primeiro e "
     "explica que uma série incompleta não pode ser pontuada."),
    ("Tenho de começar no Level 1?",
     "Não. Nada está bloqueado. Pode fazer um teste em qualquer um dos seis níveis e repetir qualquer nível "
     "que já tenha testado."),
    ("O que é o meu &ldquo;nível-limite&rdquo;?",
     "É o nível que o está a travar &mdash; o mais alto que ainda não consegue passar. É o nível em que vale "
     "a pena treinar, e tanto o ecrã de resultado como o ecrã Rank o deixam saltar diretamente para lá."),
    ("Quanto custa o Runout Pro e o que acrescenta?",
     "O Runout Pro é uma subscrição opcional mensal ou anual, com preço definido pela sua loja na sua própria "
     "moeda. Acrescenta o histórico: a sua classificação representada ao longo de todos os testes, a evolução "
     "da pontuação por nível, a taxa de limpeza ao longo do tempo, o registo de testes completo e a exportação "
     "para CSV. Tudo o que lhe diz onde está neste momento continua gratuito."),
    ("O meu histórico está seguro quando a aplicação é atualizada?",
     "Sim. Os seus testes, tentativas e favoritos são preservados nas atualizações da aplicação. Como os dados "
     "são locais, desinstalar a aplicação ou limpar os seus dados apaga-os."),
    ("Em que é que isto é diferente do Fargo Rate?",
     "O Fargo Rate é uma classificação relativa: calcula o seu número a partir de resultados contra outros "
     "jogadores classificados, e é por isso que a FargoRate considera 200 jogos a robustez mínima para uma "
     "classificação estabelecida, e que um meio local mal ligado se pode desviar do resto da rede. O Runout "
     "Rank é absoluto &mdash; mede-o face a disposições fixas geradas, por isso uma sessão de dez mesas dá-lhe "
     "uma classificação completa e nenhum grupo de adversários a influencia. Não é um sistema de handicap e "
     "não substitui uma classificação de liga para dar handicap em partidas."),
    ("De quantos jogos preciso para a minha classificação Runout Rank significar alguma coisa?",
     "Dez mesas &mdash; um teste, cerca de uma hora. Não há período de qualificação nem fase provisória, "
     "porque a classificação é calculada a partir das suas limpezas de mesa em disposições definidas e não a "
     "partir de um historial de resultados contra outros jogadores."),
    ("O sítio onde vivo afeta a minha classificação?",
     "Não. As restrições de cada nível são as mesmas constantes em todo o lado, e nenhum adversário entra no "
     "cálculo. A única variável local é o seu equipamento: o corte das caçapas, o tamanho da mesa e a rapidez "
     "do pano mudam a dificuldade de limpar uma mesa, por isso faça o teste na mesa em que joga de facto e "
     "compare os seus próprios números ao longo do tempo."),
    ("Posso usar o Runout Rank e uma classificação de liga em conjunto?",
     "Sim, e é isso que faz sentido se joga na liga. Guarde a classificação de liga para dar handicap em "
     "partidas e use o teste de limpeza de mesa para descobrir que nível o trava e treinar aí &mdash; algo "
     "que uma classificação por resultados não lhe consegue dizer."),
    ("O Runout Rank é igual em Android e iOS?",
     "Sim. As definições dos níveis, o gerador e a matemática da classificação são código partilhado a correr "
     "nas duas plataformas, por isso o telemóvel que tem não tem qualquer efeito na sua classificação."),
]

FAQ_BODY_ITEMS = faq_body(FAQ_ITEMS)
FAQ_SCHEMA = faq_schema(FAQ_ITEMS)

FAQ = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Perguntas frequentes")}
      <h1>Perguntas frequentes</h1>
      <p class="lead">O teste, a classificação, os níveis, a subscrição e os seus dados.</p>
    </div>
  </section>

  <section>
    <div class="container" style="max-width:52rem">
{FAQ_BODY_ITEMS}
      <p style="margin-top:28px">Ainda com dúvidas sobre como o número é produzido?
      <a href="how-it-works.html">Leia como funciona a classificação &rarr;</a></p>
    </div>
  </section>

{CTA}
"""

NOT_FOUND = """  <section class="page-head">
    <div class="container">
      <h1>Essa mesa não está montada</h1>
      <p class="lead">A página que procurava não existe. Aqui fica o caminho de volta.</p>
      <div class="btn-row" style="margin-bottom:40px">
        <a class="btn btn--primary" href="index.html">Voltar à página inicial</a>
        <a class="btn btn--ghost" href="how-it-works.html">Como funciona o teste</a>
      </div>
    </div>
  </section>
"""


PAGES = [
    dict(slug="index.html",
         title="Runout Rank — Um teste de nível de bilhar absoluto para Android e iOS",
         description="Obtenha uma classificação de bilhar a sério numa só sessão, e não em 200 jogos de liga. "
                     "O Runout Rank mede-o face a dez disposições geradas em vez de o medir face aos "
                     "adversários locais, por isso o número de 0 a 100 significa o mesmo em todas as cidades. "
                     "Sem liga, sem conta, funciona offline.",
         body=INDEX,
         schema=[app_schema(LOCALE, UI), site_schema(LOCALE, UI)],
         keywords="classificação de bilhar absoluta, alternativa ao fargo rate, teste de nível de bilhar, "
                  "aplicação de classificação de bilhar, classificação de bilhar sem liga, teste de limpeza "
                  "de mesa, aplicação de treino de bilhar"),

    dict(slug="how-it-works.html",
         title="Como funciona a classificação do Runout Rank — dez mesas, uma tentativa cada",
         description="Dez mesas geradas aleatoriamente num único nível, uma tentativa cada, convertidas numa "
                     "classificação de bilhar absoluta de 0 a 100 e num escalão. Disposições novas em cada "
                     "teste, restrições de nível fixas, para que o número signifique o mesmo em todas as "
                     "cidades.",
         body=HOW,
         schema=[breadcrumb_schema(LOCALE, UI, "Como funciona", "how-it-works.html")]),

    dict(slug="levels.html",
         title="Os seis níveis — de Rookie a Master | Runout Rank",
         description="Rookie, Regular, League, Competitor, Advanced, Master. O que muda em cada degrau da "
                     "escada — número de bolas, bola na mão, aperto e bloqueadores — e porque é que nenhum "
                     "está bloqueado.",
         body=LEVELS,
         schema=[breadcrumb_schema(LOCALE, UI, "Níveis", "levels.html")]),

    dict(slug="practice.html",
         title="Sessões de treino de bilhar e um registo que não esquece | Runout Rank",
         description="Disposições de treino geradas aleatoriamente sem fim, no nível que escolher, registo "
                     "com um toque, repetir e saltar, favoritos, e um registo completo de todas as mesas que "
                     "já jogou.",
         body=PRACTICE,
         schema=[breadcrumb_schema(LOCALE, UI, "Treino", "practice.html")]),

    dict(slug="fargo-rate-alternative.html",
         dated=True,
         title=FARGO_ALT_TITLE + " | Runout Rank",
         description="O Fargo Rate precisa de 200 jogos até uma classificação estar estabelecida, e uma "
                     "classificação relativa está ancorada nos jogadores à sua volta. O Runout Rank é uma "
                     "classificação de bilhar absoluta a partir de uma sessão de dez mesas — comparados lado "
                     "a lado, com justiça.",
         body=FARGO_ALT,
         schema=[article_schema(LOCALE, UI,
             FARGO_ALT_TITLE,
             "Porque é que uma classificação de liga relativa leva 200 jogos a estabelecer-se e oscila com o "
             "grupo de jogadores da sua zona, o que faz em vez disso uma classificação absoluta de limpeza de "
             "mesa, e qual das duas quer.",
             "fargo-rate-alternative.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "Alternativa ao Fargo Rate", "fargo-rate-alternative.html")],
         published=UPDATED,
         keywords="alternativa ao fargo rate, alternativa à classificação fargo, aplicação de classificação "
                  "de bilhar, classificação de bilhar absoluta, fargo rate 200 jogos, classificação fargo "
                  "estabelecida, precisão do fargo rate"),

    dict(slug="pool-rating-without-a-league.html",
         dated=True,
         title=NO_LEAGUE_TITLE + " | Runout Rank",
         description="Todas as classificações de liga pedem centenas de partidas contra jogadores "
                     "classificados antes de o número ser real. Eis como um jogador ocasional ou solitário "
                     "obtém uma classificação de bilhar honesta de 0 a 100 numa só sessão, na sua própria "
                     "mesa.",
         body=NO_LEAGUE,
         schema=[article_schema(LOCALE, UI,
             NO_LEAGUE_TITLE,
             "Como um jogador ocasional ou solitário pode obter uma classificação de bilhar honesta numa só "
             "sessão, sem entrar numa liga nem jogar 200 jogos classificados.",
             "pool-rating-without-a-league.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "Uma classificação sem liga", "pool-rating-without-a-league.html")],
         published=UPDATED,
         keywords="classificação de bilhar sem liga, como obter uma classificação de bilhar, classificação "
                  "para jogador de bilhar ocasional, classificação de treino de bilhar a solo, ser "
                  "classificado no bilhar, avaliação de nível no bilhar"),

    dict(slug="absolute-vs-relative-pool-rating.html",
         dated=True,
         title=ABSOLUTE_TITLE + " | Runout Rank",
         description="Elo, Glicko e Fargo Rate são relativos: cada classificação é uma posição numa rede de "
                     "outras classificações, por isso tanto o volume como a ligação local contam. O que mede "
                     "em vez disso uma classificação de bilhar absoluta, e para que serve cada uma.",
         body=ABSOLUTE,
         schema=[article_schema(LOCALE, UI,
             ABSOLUTE_TITLE,
             "Porque é que as classificações de bilhar relativas dependem dos jogadores à sua volta, o que "
             "mede em vez disso uma classificação absoluta, e qual delas responde a que pergunta.",
             "absolute-vs-relative-pool-rating.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "Classificação absoluta e relativa", "absolute-vs-relative-pool-rating.html")],
         published=UPDATED,
         keywords="classificação de bilhar absoluta e relativa, sistema de classificação relativa, "
                  "classificação elo bilhar, diferenças regionais na classificação fargo, classificação de "
                  "bilhar explicada"),

    dict(slug="runout-pro.html",
         title="Runout Pro — todo o seu histórico de classificação e exportação para CSV | Runout Rank",
         description="Saber onde está é gratuito, para sempre. O Runout Pro acrescenta como lá chegou: a "
                     "classificação representada em todos os testes, a evolução por nível, o registo de testes "
                     "completo e a exportação para CSV.",
         body=PRO,
         schema=[breadcrumb_schema(LOCALE, UI, "Runout Pro", "runout-pro.html")]),

    dict(slug="pool-skill-level-test.html",
         dated=True,
         title=GUIDE_TITLE,
         description="O que separa um teste de nível de bilhar que vale a pena fazer de um exercício de que "
                     "calha gostar: limpezas de mesa inteiras, disposições imprevisíveis, dificuldade "
                     "definida, uma tentativa por mesa, e o que fazer com o número.",
         body=GUIDE,
         schema=[article_schema(LOCALE, UI,
             GUIDE_TITLE,
             "O que separa um teste de nível de bilhar que vale a pena fazer de um exercício de que calha "
             "gostar.",
             "pool-skill-level-test.html", FIRST_PUBLISHED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "Teste de nível de bilhar", "pool-skill-level-test.html")],
         keywords="como testar o nível de bilhar, teste de nível de bilhar, avaliação de competência no "
                  "bilhar, exercício de limpeza de mesa, sistema de classificação de bilhar"),

    dict(slug="faq.html",
         title="Perguntas frequentes do Runout Rank — o teste, a classificação, os níveis e os seus dados",
         description="É preciso uma mesa a sério? Uma liga? Como é calculada a classificação, em que difere "
                     "do Fargo Rate, e o que acrescenta o Runout Pro? Respostas às perguntas mais comuns.",
         body=FAQ,
         schema=[FAQ_SCHEMA, breadcrumb_schema(LOCALE, UI, "Perguntas frequentes", "faq.html")]),
]
