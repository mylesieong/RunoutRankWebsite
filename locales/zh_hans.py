"""简体中文文案 / Simplified Chinese copy for the Runout Rank site.

Mirrors locales/en.py exactly: same names, same page order, same markup —
only the strings differ. See locales/en.py for the contract.
"""

from common import (
    FIRST_PUBLISHED, PLAY_URL, UPDATED,
    app_schema, article_schema, breadcrumb, breadcrumb_schema, byline,
    faq_body, faq_schema, locale_by_code, site_schema, store_block,
)

LOCALE = locale_by_code("zh-Hans")

UI = dict(
    tagline="安卓与 iOS 上的绝对台球水平评测与训练应用",
    author_title="Runout Rank 开发者",

    # --- chrome ---------------------------------------------------------
    skip_link="跳到正文",
    nav_aria="主导航",
    lang_aria="语言",
    lang_current="语言",
    breadcrumb_label="面包屑导航",
    nav_home="首页",
    nav=[
        ("index.html", "首页"),
        ("how-it-works.html", "评测原理"),
        ("levels.html", "六个等级"),
        ("practice.html", "练习"),
        ("fargo-rate-alternative.html", "对比 Fargo Rate"),
        ("runout-pro.html", "Runout Pro"),
        ("faq.html", "常见问题"),
    ],

    # --- byline ---------------------------------------------------------
    byline_by="作者",
    byline_sep="，",
    byline_published="发布于",
    byline_updated="更新于",
    date_format="{y} 年 {m} 月 {d} 日",
    months=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],

    # --- store badges ---------------------------------------------------
    store_get_it_on="下载自",
    store_in_review="审核中",
    store_review_aria="App Store 审核中",

    # --- footer ---------------------------------------------------------
    footer_blurb="在你自己的球台上打一轮十桌清台测试，得到一个绝对水平评分。一次坐下就能拿到 0&ndash;100 的数字"
                 "&mdash;&mdash;不用打联赛、不用等 200 局、不用注册账号、不用联网。",
    footer_col_app="应用",
    footer_col_guides="指南",
    footer_links_app=[
        ("how-it-works.html", "评测原理"),
        ("levels.html", "六个等级"),
        ("practice.html", "练习与训练日志"),
        ("runout-pro.html", "Runout Pro"),
    ],
    footer_links_guides=[
        ("fargo-rate-alternative.html", "Fargo Rate 的替代方案"),
        ("pool-rating-without-a-league.html", "不打联赛也能有评分"),
        ("absolute-vs-relative-pool-rating.html", "绝对评分与相对评分"),
        ("pool-skill-level-test.html", "台球水平测试指南"),
        ("faq.html", "常见问题"),
        ("privacy-policy.html", "隐私政策"),
    ],
    footer_sitemap="网站地图",
    footer_copyright="&copy; {year} Runout Rank。由 {author} 撰写并开发。",
    footer_platforms="安卓与 iOS &middot; 与应用一样，只有深色模式",
    footer_disclaimer="Fargo Rate 与 FargoRate 是其各自所有者的商标。"
                      "Runout Rank 是一款独立应用，与 FargoRate、BCA、APA 或任何联赛运营方均无从属、"
                      "认可或关联关系。本网站的对比只是在描述这些系统已公开的运作方式，供读者自行判断。",

    # --- social / meta --------------------------------------------------
    og_image_alt="Runout Rank — 你的台球水平，到底怎么样？",

    # --- privacy policy page --------------------------------------------
    privacy_title="隐私政策 | Runout Rank",
    privacy_description="Runout Rank 只把你的测试、评分和练习记录保存在你自己的设备上。本政策说明应用确实会用到的"
                        "分析服务、数据会与谁共享，以及你享有的权利。",
    privacy_h1="隐私政策",
    privacy_breadcrumb="隐私政策",
    privacy_lead="你的测试和统计数据都留在你自己的设备上。本页说明应用确实会收集什么、为什么收集，"
                 "以及你对这些数据有哪些控制权。",

    # --- 404 ------------------------------------------------------------
    not_found_title="页面未找到 | Runout Rank",
    not_found_description="这个页面不存在。回到 Runout Rank 首页吧。",

    # --- SoftwareApplication schema -------------------------------------
    app_description="Runout Rank 是一款绝对台球水平评分应用。在真实球台上完成一轮十桌清台测试，一次就能拿到 "
                    "0-100 的评分和从 Rookie 到 Master 的等级，然后在那个卡住你的等级上练习。评分衡量的是"
                    "你对固定球型的表现，而不是你和本地对手的胜负，所以不需要联赛、不需要 200 局的战绩，"
                    "甚至不需要对手。所有数据都保存在你的设备上。",
    app_features=[
        "绝对评分：衡量的是固定生成的球型，而不是本地对手",
        "一轮十桌测试即得完整的 0-100 评分，没有必须先打满的最低局数",
        "尺子从不改变，因此评分在不同城市、不同联赛、不同国家之间通用",
        "十桌评级测试，给出 0-100 评分和对应等级称号",
        "从 Rookie 到 Master 六个挑战等级",
        "等级参数固定，所以同一个评分在任何地方含义相同",
        "无穷无尽的随机生成练习球型",
        "带收藏功能的训练日志",
        "终身清台率、连胜纪录与各等级统计",
        "完全离线可用，无需账号",
    ],
    app_offer="免费下载。可选的 Runout Pro 订阅可解锁历史进度与 CSV 导出。",
)

CTA = f"""  <section class="cta band">
    <div class="container">
      <p class="eyebrow">拿到你的数字</p>
      <h2>十桌。每桌一次机会。一个诚实的评分。</h2>
      <p class="lead" style="max-width:38rem;margin:0 auto 28px">在你平时打的那张球台上摆出球型。
      应用会为你的清台打分，并告诉你下一步该在哪个等级上练。</p>
      {store_block(UI, centred=True)}
    </div>
  </section>"""


# --------------------------------------------------------------------------
# Page bodies
# --------------------------------------------------------------------------

INDEX = f"""  <section class="hero">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow">绝对台球评分 &middot; 安卓与 iOS</p>
        <h1>你的台球评分。<span class="accent">今晚</span>就有，不用等 200 局。</h1>
        <p class="lead">联赛评分要打上几百场，那个数字才有意义，而且你拿到多少，还取决于你所在的城市恰好有哪些人。
        Runout Rank 换了个衡量对象：球台。十个球型，每个一次机会，一次坐下就得到 0&ndash;100 的评分。</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="{PLAY_URL}">在 Google Play 下载</a>
          <a class="btn btn--ghost" href="how-it-works.html">评测怎么进行</a>
        </div>
        <p class="hero-note">不用联赛 &middot; 不用对手 &middot; 不用账号 &middot; 离线可用</p>
      </div>
      <div class="hero-shot">
        <div class="phone">
          <img src="assets/img/screen-home.png" width="1080" height="2400"
               alt="手机上的 Runout Rank 首页，正提示开始十桌评级测试。"
               fetchpriority="high" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <section class="tight band">
    <div class="container">
      <div class="grid grid--4">
        <div><span class="stat">10</span><p class="dim">每轮测试十桌，每桌一次机会</p></div>
        <div><span class="stat">1</span><p class="dim">一次就拿到完整评分，不必等 200 局</p></div>
        <div><span class="stat">0&ndash;100</span><p class="dim">打完当下就有评分和等级</p></div>
        <div><span class="stat">0</span><p class="dim">不需要联赛、对手和账号</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">为什么要换一种做法</p>
        <h2>联赛评分要花上一整个赛季，<span class="accent">而且还会随你所在的城市浮动。</span></h2>
      </div>
      <div class="compare">
        <div class="card pain">
          <h3>要打满 200 局才算数</h3>
          <p>FargoRate 把 200 局视为评分「确立」的最低门槛。也就是说，你得先加入联赛、打完一个赛季、
          交完各项费用，才能知道自己到底在什么位置。</p>
          <p><a href="pool-rating-without-a-league.html">不打联赛也能有评分 &rarr;</a></p>
        </div>
        <div class="card pain">
          <h3>你的数字描述的是你的邮政编码</h3>
          <p>相对评分锚定在你周围的人身上，所以本地球圈一旦人少或彼此孤立，整体就会相对世界其他地方漂移。</p>
          <p><a href="absolute-vs-relative-pool-rating.html">绝对评分与相对评分 &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">解法</p>
        <h2>衡量球员对<span class="accent">球台</span>的表现，而不是对这屋子里的人。</h2>
        <p class="lead">每个等级都精确规定了难度从何而来&mdash;&mdash;目标球数量、是否自由摆球、
        球堆得有多密、有几颗障碍球。这些限制就是尺子，而且对所有人都一样。战胜它们，数字就上去。
        除此之外没有任何因素能撼动它。</p>
      </div>
      <div class="grid grid--3">
        <div class="card">
          <h3>绝对，而非相对</h3>
          <p>没有强弱不定的对手池，也就没有什么可漂移的。</p>
        </div>
        <div class="card">
          <h3>一次坐下，而非一个赛季</h3>
          <p>在球台前大约一小时，结束时拿到的是真实评分，而不是一个临时占位的数字。</p>
        </div>
        <div class="card">
          <h3>没什么可背的</h3>
          <p>每轮测试的球型都是现场重新生成的，所以你面对的始终是这个等级，而不是某个你早就记住答案的练习。</p>
        </div>
      </div>
      <p style="margin-top:28px"><a href="fargo-rate-alternative.html">与 Fargo Rate 的完整对比 &rarr;</a></p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">怎么进行</p>
        <h2>三步，一次搞定</h2>
      </div>
      <div class="grid grid--3 steps">
        <div class="card step">
          <h3>照着应用画的摆球</h3>
          <p>每个球型都是俯视图，你可以照着在眼前的球台上原样摆好。</p>
        </div>
        <div class="card step">
          <h3>只打一次</h3>
          <p>清台或者失手，然后一键记录。没有重来，也不能跳过。</p>
        </div>
        <div class="card step">
          <h3>拿到评分和下一步计划</h3>
          <p>得分、评分、等级&mdash;&mdash;还有那个正卡住你的等级，供你接着练。</p>
        </div>
      </div>
      <p style="margin-top:28px"><a href="how-it-works.html">阅读完整说明 &rarr;</a></p>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-test.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="进行中的评级测试：第 6 桌（共 10 桌）以俯视图画出，台呢上有四颗编号目标球，下方是「已清台」和「失手」按钮。"></div>
        </div>
        <div>
          <p class="eyebrow">球型</p>
          <h3>一个球型长这样。</h3>
          <p>每个球型都按比例以俯视图画出，你可以照着在眼前的台呢上摆好，然后打真实的球。
          整个过程中球型都留在屏幕上，万一把球碰乱了，你可以照着重新摆。</p>
          <ul class="ticks">
            <li><strong>数字是击球顺序</strong>&mdash;&mdash;不是球的分值</li>
            <li><strong>障碍球</strong>画得暗淡且不带编号：它们挡路，但不在顺序里</li>
            <li><strong>母球</strong>从 Advanced 等级起才会出现。在此之下你都可以自由摆球</li>
          </ul>
        </div>
      </div>

      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-result.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="测试结果页面，显示 10 中 7、评分 58、League 等级，以及接下来该做什么。"></div>
        </div>
        <div>
          <p class="eyebrow">结果</p>
          <h3>一个评分，加上那个<span class="gold">卡住你</span>的等级。</h3>
          <p>十中七即通过一个等级。你会看到得分、0&ndash;100 的评分、你的等级，以及这个数字相比上次移动了多少
          &mdash;&mdash;然后是当前卡住你的等级，一键就能开始在那里练习。</p>
        </div>
      </div>

      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-progress.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="进度页面，显示评分、等级、终身数据以及各等级细分。"></div>
        </div>
        <div>
          <p class="eyebrow">进度</p>
          <h3>看看练习到底有没有用。</h3>
          <p>评分、等级、已通过的等级、终身清台率和最佳连胜&mdash;&mdash;永久免费。
          <a href="runout-pro.html">Runout Pro</a> 再加上历史：每一轮测试随时间绘成曲线，并支持 CSV 导出。</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid grid--3">
        <div class="card">
          <h3>六个等级，全部开放</h3>
          <p>从 Rookie 到 Master。想测哪个都行&mdash;&mdash;高手不必从最低一级慢慢磨上来。
          <a href="levels.html">对比各等级 &rarr;</a></p>
        </div>
        <div class="card">
          <h3>在你的临界点上练</h3>
          <p>在卡住你的那个等级上无限生成球型，并记录你打过的每一桌。
          <a href="practice.html">了解练习功能 &rarr;</a></p>
        </div>
        <div class="card">
          <h3>你的记录只属于你</h3>
          <p>无账号、无服务器、离线可用。一切都存在你的设备上。
          <a href="privacy-policy.html">隐私政策 &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

HOW = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "评测原理")}
      <h1>Runout Rank 的评分是怎么算出来的</h1>
      <p class="lead">十个生成的球型，每个一次机会，换算成 0&ndash;100 的评分和一个等级称号
      &mdash;&mdash;外加一条明确的指示，告诉你接下来该做什么。</p>
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>1. 选一个等级，开始测试</h2>
      <p>一轮评级测试是同一等级下的十个球型。等级由你选：应用会给出建议，但没有任何等级是锁着的，
      所以高手可以直接从 Competitor 开始，而不必从 Rookie 一级级磨上去。如果你从没被评过分，
      从首页一键就能开始测试&mdash;&mdash;不需要先做任何设置。</p>
      <p>如果你想先热热身，也可以先生成单个练习球型，之后再做测试。</p>

      <h2>2. 在真实球台上摆出每一个球型</h2>
      <p>每个球型都以俯视图画出，母球、目标球和障碍球的位置一应俱全。障碍球特意画得暗淡且不带编号，
      这样它们绝不会被误读为击球顺序的一部分。你照着屏幕摆球，就摆在你平时打的那张球台上。
      整个过程中示意图都留在屏幕上，万一把球型碰乱了，你可以照着重新摆好。</p>

      <h2>3. 打一次，记一次</h2>
      <p>清台，或者没清成。一键记录结果并进入下一桌。顶部始终显示你在十桌中的第几桌，
      球型上方的横条则显示已打过的球型中哪些清台、哪些失手。</p>
      <p><strong>每桌恰好一次机会。不能重来，也不能跳过。</strong>正是这条限制，
      才让最后那个数字有意义。</p>
      <div class="note">中途被打断？离开测试，稍后再回来&mdash;&mdash;它会精确地从你停下的那一桌继续。
      若是主动退出，应用会先请你确认，并说明未打完的一轮无法计分。</div>

      <h2>4. 读懂结果</h2>
      <p>第十桌记录完的那一刻，你会得到：</p>
      <ul>
        <li><strong>十中几的得分</strong>&mdash;&mdash;十桌里你清了几桌。</li>
        <li><strong>0&ndash;100 的评分</strong>，以及与之对应的<strong>等级</strong>。</li>
        <li><strong>是否通过。</strong>十中七即通过该等级。</li>
        <li><strong>评分变化</strong>&mdash;&mdash;相比上次测试，这个数字移动了多少。</li>
        <li><strong>你的临界等级</strong>&mdash;&mdash;当前卡住你的那个等级，并用大白话告诉你该怎么办。</li>
      </ul>
      <p>在那个页面上，一键就能开始在临界等级上练习。</p>

      <h2>球型是随机的，为什么分数还能相互比较</h2>
      <p>每轮测试都是重新生成的，所以没有答案可背，也没有可以提前排练的固定练习。
      两个球员永远不会遇到同样的十个球型&mdash;&mdash;而他们也不需要。</p>
      <p>固定不变的是<strong>等级</strong>。目标球数量、是否自由摆球、球与球之间的最小间距、
      障碍球的数量，都是明确定义的常数，在两个平台上对每个人都完全一致。
      一轮 Level&nbsp;4 的测试问的永远是 Level&nbsp;4 的问题。十个球型足以把难度的起伏抹平，
      这也是为什么测试是十桌而不是一桌。</p>
      <p>所以被衡量的，是你对这个等级的限制条件，而不是你对某十个特定球型。
      正因如此，一个人的 58 分和另一个人的 58 分含义相同。</p>

      <h2>为什么这个评分是绝对的</h2>
      <p>整个计算过程中没有任何对手出现。Fargo Rate 这类联赛系统是<em>相对</em>的
      &mdash;&mdash;你的数字来自你与其他已评分球员的胜负结果，这也是为什么它们需要大量战绩
      评分才会稳定下来，以及为什么一个连接稀疏的本地球圈会整体偏高或偏低。
      Runout Rank 则是拿你和一个固定标准做比较。等级的限制条件在任何地方都一样，
      所以从第一轮测试起，这个评分在任何地方都是同一种测量。</p>
      <p>唯一的本地变量是你的器材。袋口的切法、球台尺寸和台呢速度都会改变清台的难度，
      所以请在你实际打球的那张台子上做测试，并把自己不同时期的数字放在一起比较。</p>
      <p><a href="absolute-vs-relative-pool-rating.html">绝对评分与相对评分 &rarr;</a></p>

      <h2>这个评分不是什么</h2>
      <p>它衡量的是你在「不许重来」规则下，对生成球型的清台能力。它不是让分系统，
      不是任何管理机构的官方评分，也不与任何联赛数据库互通。如果你需要一个数字来给比赛让分，
      那正是联赛评分的用途&mdash;&mdash;见<a href="fargo-rate-alternative.html">两者的对比</a>。
      这是一个诚实的数字，你可以在自己的球台上，任何时候想要一个新的就自己测一个。</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="levels.html">查看六个等级</a>
        <a class="btn btn--ghost" href="fargo-rate-alternative.html">与 Fargo Rate 对比</a>
      </div>
    </div>
  </section>

{CTA}
"""

LEVELS = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "六个等级")}
      <h1>六个等级，从 Rookie 到 Master</h1>
      <p class="lead">难度是一架梯子，不是一根滑杆。每上一阶，你要清的球型都会有某样具体的东西发生变化
      &mdash;&mdash;而且没有任何一阶是锁着的。</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="table-wrap">
        <table>
          <caption class="sr-only">Runout Rank 的六个等级，以及每一阶变化了什么</caption>
          <thead>
            <tr>
              <th scope="col">等级</th>
              <th scope="col">名称</th>
              <th scope="col">目标球</th>
              <th scope="col">自由摆球</th>
              <th scope="col">球间最小间距</th>
              <th scope="col">障碍球</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>1</strong></td><td><strong>Rookie</strong></td><td>2</td><td>是</td><td>8&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>2</strong></td><td><strong>Regular</strong></td><td>3</td><td>是</td><td>6&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>3</strong></td><td><strong>League</strong></td><td>4</td><td>是</td><td>4&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>4</strong></td><td><strong>Competitor</strong></td><td>5</td><td>是</td><td>2.25&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>5</strong></td><td><strong>Advanced</strong></td><td>5</td><td>否</td><td>2.25&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>6</strong></td><td><strong>Master</strong></td><td>5</td><td>否</td><td>2.25&Prime;</td><td>2</td></tr>
          </tbody>
        </table>
      </div>
      <p class="dim" style="margin-top:16px">间距指的是球心到球心的<em>最小</em>距离，所以数字越大，
      球型越分散、越好打。2.25&Prime; 是一个球的直径&mdash;&mdash;这是下限，再小球就会物理重叠了。
      应用内每个等级的卡片上也标着同样的数值。</p>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">读懂这架梯子</p>
        <h2>四个旋钮，每上一阶拧一格</h2>
      </div>
      <div class="grid grid--4">
        <div class="card"><h3>目标球数量</h3><p>Rookie 是两颗，从 Competitor 起升到五颗。每多一颗球，就多一个必须走成的走位决策。</p></div>
        <div class="card"><h3>自由摆球</h3><p>1&ndash;4 级允许你自己摆母球。从 Advanced 起，母球在球型给它的位置上，你只能从拿到的局面开打。</p></div>
        <div class="card"><h3>密集程度</h3><p>球与球之间的最小间隙从 8&Prime; 一路缩到一个球的直径。球挤在一起会挡住角度，也会毁掉走位。</p></div>
        <div class="card"><h3>障碍球</h3><p>只有 Master 会加两颗。它们不属于击球顺序&mdash;&mdash;画得暗淡且不带编号&mdash;&mdash;存在的意义就是挡你的路。</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-levels.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="等级页面，League 等级已展开，显示最佳测试成绩和近期练习清台率。"></div>
        </div>
        <div>
          <p class="eyebrow">每一阶上的战绩</p>
          <h3>每个等级都知道你在它上面打得怎么样</h3>
          <p>展开任意等级，就能看到你在那里的最佳测试成绩、近期练习清台率，以及这个比率是基于多少次尝试算出来的
          &mdash;&mdash;这样你就能分清真正的短板和只是状态不好的一晚。已通过的等级会被标出，
          而你的<span class="gold">临界点</span>&mdash;&mdash;当前卡住你的那个等级&mdash;&mdash;会用金色标示。</p>
          <ul class="ticks ticks--gold">
            <li>可以在任意等级开始评级测试，不限于下一级</li>
            <li>重测已经测过的等级，用来确认或提升成绩</li>
            <li>直接从这架梯子上开始任意等级的自由练习</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

PRACTICE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "练习")}
      <h1>练习，以及你打过的每一桌的记录</h1>
      <p class="lead">测试告诉你哪个等级卡住了你。练习则是你为此做点什么的地方
      &mdash;&mdash;正是那个等级上无穷无尽的生成球型。</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-practice.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="一次练习：生成的四球球型，下方提示询问你是否清台。"></div>
        </div>
        <div>
          <p class="eyebrow">一次练习</p>
          <h3>素材永远用不完，球型永远背不下来</h3>
          <p>练习球型按你选的等级随取随生成，你的尝试也会计入该等级的统计。
          整个过程中示意图都留在屏幕上，球型被碰乱了也能重新摆回来。</p>
          <ul class="ticks">
            <li>一键记录成功或失败，并有确认提示告诉你已记录</li>
            <li>不想打的球型可以跳过，而不必让整次练习卡在那里</li>
            <li>重打完全相同的球型，把它练到彻底吃透</li>
            <li>记录完立刻生成下一桌&mdash;&mdash;这是一个循环，不是一棵菜单树</li>
            <li>关掉应用后，可以从首页重新打开你上次生成的那个球型</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">训练日志</p>
        <h2>你付出过的功夫，有一份完整记录</h2>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>你打过的每一个球型</h3><p>全部可以翻阅，附带日期、等级，以及你在多少次尝试中清了台。</p></div>
        <div class="card"><h3>收藏</h3><p>把值得反复练的球型加星，并把日志筛选到只看收藏，逐步攒出一套属于你自己的练习库。</p></div>
        <div class="card"><h3>从任何地方接着练</h3><p>在日志里挑任意一桌，从它继续训练。重温一个旧球型只需一键。</p></div>
      </div>
      <p class="dim" style="margin-top:20px">空日志不会只给你一个白屏，而是会告诉你怎么把它填满。</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-progress.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Rank 页面，显示当前评分、等级、终身数据以及各等级细分。"></div>
        </div>
        <div>
          <p class="eyebrow">你的位置&mdash;&mdash;永久免费</p>
          <h3>回答「我到底有没有变强？」的那些数字</h3>
          <p>你的 0&ndash;100 评分和等级、你已通过的最高等级、你的临界等级，以及相比上次测试的评分变化。
          下面还有：终身尝试次数、清台总数、总体清台率和最佳连胜，外加一句大白话解读这个比率
          &mdash;&mdash;「你大约每 N 桌清台一次」。</p>
          <p>在同一个页面上，一键就能重测你的临界等级。</p>
          <p><a href="runout-pro.html">Runout Pro 在此之上还提供什么 &rarr;</a></p>
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
      <p class="lead">一条界线，一句话说完：<strong>你现在在哪里，免费；你是怎么走到这里的，属于 Pro。</strong></p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid grid--2">
        <div class="card">
          <p class="eyebrow">永久免费</p>
          <h3>你现在在哪里</h3>
          <ul class="ticks">
            <li>你的 0&ndash;100 评分和等级</li>
            <li>你已通过的等级，以及卡住你的等级</li>
            <li>相比上次测试的评分变化</li>
            <li>各等级细分：最佳测试成绩与近期练习清台率</li>
            <li>终身尝试次数、清台数、清台率与最佳连胜</li>
            <li>不限次数的评级测试，以及所有等级不限量的练习</li>
          </ul>
          <p class="dim">这些都不是试用。不付一分钱，这个应用也完全够用。</p>
        </div>
        <div class="card card--gold">
          <p class="eyebrow eyebrow--gold">Runout Pro</p>
          <h3>你是怎么走到这里的</h3>
          <ul class="ticks ticks--gold">
            <li>你的评分，绘成一条贯穿你做过的每一轮测试的曲线</li>
            <li>各等级的成绩演进&mdash;&mdash;每一轮测试，而不只是最好那次</li>
            <li>清台率随时间的变化，以及你的练习历史</li>
            <li>完整测试日志：每一轮的等级、成绩、日期和评分变化</li>
            <li>全部历史的 CSV 导出</li>
          </ul>
          <p class="dim">按月或按年订阅。你过往的全部历史会立即解锁
          &mdash;&mdash;不必再等一段新的数据收集期。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">这个付费提示怎么表现</p>
        <h2>一张老实的卡片，而不是满页的小锁</h2>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>第一天不推销</h3><p>一个全新的、没有任何测试记录的用户，看不到任何推销。为一样你还想象不出自己会想要的东西设付费墙，纯属噪音。</p></div>
        <div class="card"><h3>预览的是你自己的数据</h3><p>等你攒够了历史、足以解锁某样东西时，你看到的是你自己的进度曲线，只是数值被遮住&mdash;&mdash;而不是一条泛泛的广告。</p></div>
        <div class="card"><h3>一条界线，放在页面底部</h3><p>Rank 页面上只有一张 Pro 卡片。把锁的图标撒得满屏都是，会让每一个免费功能都像是试用样品。</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>计费、恢复购买与取消</h2>
      <ul>
        <li>价格直接取自 App Store 或 Google Play 实时显示，年费的省钱幅度也按其计算，
        所以你看到的就是商店将以你本国货币收取的金额。</li>
        <li>已经买过了？<strong>恢复购买</strong>能在重装后或在第二台设备上把它找回来
        &mdash;&mdash;重装绝不会让你付两次钱。</li>
        <li>随时可在你的 Apple 或 Google 账户中管理或取消。退款和账单问题由商店按其自身条款处理。</li>
        <li>使用条款和<a href="privacy-policy.html">隐私政策</a>在你订阅之前就可以读到，而不是订阅之后。</li>
        <li><strong>Pro 离线照常可用。</strong>球房里信号不好，绝不会把你锁在自己已付费的东西之外。</li>
      </ul>
      <p>支付完全由 Apple 和 Google 处理。Runout Rank 从不接触也不存储你的卡片信息。</p>
    </div>
  </section>

{CTA}
"""

GUIDE_TITLE = "如何测出自己的台球水平（并得到一个可信的数字）"
GUIDE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "台球水平测试")}
      <h1>如何测出自己的台球水平</h1>
      <p class="lead">大多数球员都能告诉你自己赢过谁。很少有人能告诉你自己到底有多强。
      下面就说说，一个值得做的水平测试，和一个你恰好喜欢的练习，差别究竟在哪里。</p>
{byline(UI, FIRST_PUBLISHED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>为什么「我到底有多强」这么难回答</h2>
      <p>比赛结果衡量对手的成分，和衡量你的成分一样多。面对弱阵容的一个好夜晚，
      和面对强阵容的一个坏夜晚，可能给出一模一样的比分。练习无论有没有效果，感觉上都很充实，
      因为你天然会把时间花在自己本来就喜欢的球上。而大多数人跑的练习，
      都是他们以前跑过的&mdash;&mdash;这正是它们越来越容易的原因。</p>
      <p>一个有用的水平测试，必须做到三件随意练习做不到的事。</p>

      <h2>1. 它必须衡量一整项能力，而不是单独一杆</h2>
      <p>打进一颗长距离的直球，只说明你的某一种出杆。清完一整台，则说明了你的球型阅读、走位、
      力度控制、防守判断和心态，而且是按球台要求的顺序逐一说明。这就是为什么清台
      &mdash;&mdash;从头到尾的一整台&mdash;&mdash;才是水平测试正确的计量单位，
      也是为什么 Runout Rank 计的是球型的分，而不是单杆的分。</p>

      <h2>2. 它必须是不可预测的</h2>
      <p>任何一套固定球型，最终都会退化成记忆力测试。当你第十次摆出同一个练习时，
      你衡量的已经不是清台能力，而是你对那个特定球型的答案记得有多牢。
      一个值得反复做的测试，必须自己生成球型，让你面前的局面每次都真正是新的。</p>

      <h2>3. 它的难度必须是被定义的，而不是临场发挥的</h2>
      <p>矛盾就在这里：随机性让测试诚实，但同时也可能让两个分数无法比较。
      如果你的十个球型比我的难，那我们的分数含义就不一样。</p>
      <p>解法是<strong>固定限制条件，而不是固定球型</strong>。精确定义一个难度等级意味着什么
      &mdash;&mdash;多少颗目标球、是否自由摆球、球与球之间的最小间距、几颗障碍球
      &mdash;&mdash;然后在这些规则内自由生成。每个球型都是新的，每个球型难度都相同，
      而连打足够多桌，会把剩下的运气成分抹平。在 Runout Rank 里，这些常数公布在
      <a href="levels.html">等级页面</a>上，并且在安卓和 iOS 上完全一致。</p>
      <p>这才是分数可以带着走的原因：它说的是你在 Level&nbsp;4 十中七，
      而 Level&nbsp;4 对所有人含义相同。</p>

      <h2>让分数诚实的那几条规则</h2>
      <ul>
        <li><strong>每桌一次机会。</strong>三局两胜衡量的是你最好的一天，而不是你的常态。</li>
        <li><strong>不能跳过。</strong>你最想避开的那些球型，恰恰是携带信息量最大的。</li>
        <li><strong>固定的桌数。</strong>十桌足以抹平一次倒霉的走位，又短到能在真实球台前一次打完。</li>
        <li><strong>写明的及格线。</strong>在 Runout Rank 里十中七即通过一个等级。
        开打前就知道标准在哪，本身就是测试的一部分。</li>
        <li><strong>当场记录。</strong>一小时后才补记的结果，是你已经美化过的结果。</li>
      </ul>

      <h2>拿到这个数字之后做什么</h2>
      <p>评分本身只是个谈资。数字只有指向某处才有用，所以一次测试最重要的产出不是分数，
      而是<strong>临界等级</strong>&mdash;&mdash;你还跨不过去的那一阶。练习花在那里才划算，
      因为只有在那个等级上，球型才还在问你一个你答不上来的问题。</p>
      <p>实际的循环是这样的：</p>
      <ol>
        <li>在你自认为能通过的等级上测试。</li>
        <li>如果通过了，就测上一级，直到有一级把你卡住。</li>
        <li>在那个临界等级上练习，并记录每次尝试，让清台率是真实的。</li>
        <li>等清台率有了变化，就重测同一等级。比较评分，别比较感觉。</li>
      </ol>

      <h2>多久重测一次</h2>
      <p>频繁到能让数字跟上现实，又稀疏到每次重测都反映了真正的功夫。
      对大多数每周去球台练两次的球员来说，每两到四周一次差不多合适。
      每次练完就重测，量到的多半是噪音；半年才测一次，则得不到任何可执行的信息。</p>

      <h2>为什么这比苦等联赛评分稳定下来更划算</h2>
      <p>大多数球员被指向的替代方案，是通过打联赛挣来的相对评分，而那需要与其他已评分球员
      积累大量对局，数字才有分量&mdash;&mdash;比如 FargoRate 就把 200 局视为评分确立的最低门槛。
      清台测试一次坐下就能给你答案，因为它衡量的是你对球型，而不是你对这屋子里的人，
      这同时也意味着它不会随本地球圈的强弱而漂移。延伸阅读：</p>
      <ul>
        <li><a href="fargo-rate-alternative.html">不需要 200 场联赛的 Fargo Rate 替代方案</a></li>
        <li><a href="pool-rating-without-a-league.html">不加入联赛，如何拿到台球评分</a></li>
        <li><a href="absolute-vs-relative-pool-rating.html">绝对评分与相对台球评分</a></li>
      </ul>

      <div class="note">上面这一切，Runout Rank 都在你平时打的那张球台上完成：它生成球型、为清台计分、
      把历史留在你的设备上，并点名下一步该练哪个等级。
      <a href="how-it-works.html">看看测试究竟怎么进行 &rarr;</a></div>
    </div>
  </section>

{CTA}
"""

# --------------------------------------------------------------------------
# Positioning pages: the two pain points a relative league rating leaves open
# --------------------------------------------------------------------------

FARGO_DISCLAIMER = """      <p class="disclaimer">Runout Rank 是独立的，与 FargoRate 没有从属、认可或关联关系。
      本页关于 Fargo Rate 的一切说法，均取自
      <a href="https://www.fargorate.com/" rel="nofollow">FargoRate 自己公开发布的资料</a>，
      并已尽我们所能公允地描述；它是一套好系统，本页谈的只是它的设计适合与不适合哪一类球员。</p>"""

FARGO_ALT_TITLE = "不需要 200 场联赛的 Fargo Rate 替代方案"
FARGO_ALT = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Fargo Rate 的替代方案")}
      <h1>给永远打不满 200 场联赛的球员的 Fargo Rate 替代方案</h1>
      <p class="lead">Fargo Rate 是台球界最好的相对评分系统。但「相对」这一点，恰恰就是它难挣、
      又对你住在哪里敏感的原因。下面说说绝对评分的做法有何不同，以及这两者你到底想要哪一个。</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>先把该给的肯定给足</h2>
      <p>Fargo Rate 把业余爱好者和世界冠军放到了同一把尺子上，也让台球让分从比拼名气变成了可以用数字争论的事。
      如果你每周都和其他已评分球员打联赛，它很好用，本页不会假装不是这样。请继续用它。</p>
      <p>本页要谈的问题更窄：<strong>如果你不是那类球员，你该怎么办？</strong>
      如果你独自练球、和朋友随便打打、经常出差，或者只是想知道自己有多强而不想为此报名打一整个赛季，
      那么相对评分有两个结构性问题&mdash;&mdash;是结构性的，不是 bug。</p>

      <h2>痛点一：不满 200 局，这个数字就不算数</h2>
      <p>FargoRate 把你的对局历史规模称为<em>robustness（稳健度）</em>，并明确说明 200 局
      是它认定一个评分「已确立」的最低门槛。在这条线以下，你的官方评分是你实际表现和一个
      <em>starter rating（初始评分）</em>&mdash;&mdash;也就是一个初步猜测&mdash;&mdash;的混合，
      随着你逼近 200 局，猜测的权重逐渐减小。</p>
      <p>算一算 200 场计分对局对一个普通人意味着什么。它意味着要找到一个向该系统报送成绩的联赛、
      交它的费用、每周同一个晚上都有空，并且打完大半个乃至一两个赛季
      &mdash;&mdash;之后应用里那个数字才是对你的测量，而不是一个加权的意见。
      一个只想为「我到底有多强」求一个诚实答案的球员，得先买下一年的承诺才能拿到它。</p>
      <p>而且这条路没法抄近道，因为根本没有近道可抄：
      在你打出足够多、对手又是系统已经认识的人的结果之前，一个相对系统是真的无从知道你的任何情况。</p>
      <p><a href="pool-rating-without-a-league.html">不加入联赛，如何拿到台球评分 &rarr;</a></p>

      <h2>痛点二：你的评分有一部分描述的是你的城市</h2>
      <p>相对评分是从「谁赢了谁」算出来的。这意味着，你的数字有多稳，取决于把你本地球员
      和世界其他已评分球员连接起来的那条对局链条有多粗。链条粗的地方&mdash;&mdash;大城市、
      强势的巡回赛圈子、会出门打公开赛的球员&mdash;&mdash;评分对得很齐。链条细的地方，
      一个本地群体可能会稳定在一个与别处的同样数字并不相符的水平上。</p>
      <p>这不是外人的抱怨。FargoRate 自己的文章就把两个几乎彼此隔离、其中一组相对另一组评分偏高的情况，
      描述为一个特别棘手的问题&mdash;&mdash;而它只能靠长时间的大量交叉对局慢慢自我修正。
      它对「可靠评分」的定义同样指出，对手评分已确立的对局权重更高。</p>
      <p>所以，如果你所在的区域高手扎堆、或者和更大的网络几乎不连通、又或者刚刚接入这套系统，
      那么你带着的那个数字，在说你之外，也在说你的周遭。换个地方，它可能就不是在老家时的那个意思了。</p>
      <p><a href="absolute-vs-relative-pool-rating.html">绝对评分与相对评分详解 &rarr;</a></p>

      <h2>绝对评分改成怎么做</h2>
      <p>Runout Rank 把对手从测量里彻底拿掉了。它不问你赢了谁，
      而是在球台上摆出一个定义好的球型，然后问你能不能把它清掉。</p>
      <p>你在同一等级下打十个生成的球型，每个一次机会，不能重来也不能跳过，
      并把每一桌记为清台或失手。十个答案换成一个得分、一个 0&ndash;100 的评分，
      以及一个从 Rookie 到 Master 的等级。十中七即通过该等级。
      整件事在你平时打的那张球台上大约花一小时。</p>
      <p>因为球型就是尺子，而尺子从不改变，所以无论屋里还有谁，这个数字含义相同；
      明年和今年也含义相同。它从第一次坐下就挣到了，而不是攒了一个赛季才有。</p>

      <h2>并排对比</h2>
      <div class="table-wrap">
        <table>
          <caption class="sr-only">相对联赛评分与 Runout Rank 绝对评分的对比</caption>
          <thead>
            <tr>
              <th scope="col"></th>
              <th scope="col">相对评分（Fargo Rate 及同类）</th>
              <th scope="col">Runout Rank</th>
            </tr>
          </thead>
          <tbody>
            <tr><th scope="row">衡量什么</th><td>与其他已评分球员的胜负结果</td><td>对固定生成球型的清台表现</td></tr>
            <tr><th scope="row">多久之后才有意义</th><td>200 局才算评分确立；在此之下会混入一个初始评分</td><td>一轮十桌测试，大约一小时</td></tr>
            <tr><th scope="row">你需要什么</th><td>一个会报送成绩的联赛或计分赛事、对手、费用、固定档期</td><td>一张球台和一部手机</td></tr>
            <tr><th scope="row">本地球圈的影响</th><td>确实存在：连通性和你的对手池强弱都会影响数字</td><td>没有：不涉及任何对手</td></tr>
            <tr><th scope="row">可携带性</th><td>在网络内部可通用；连接稀疏的区域会漂移</td><td>安卓和 iOS 上，各地等级参数完全相同</td></tr>
            <tr><th scope="row">适合用来</th><td>比赛让分、赛事分组、联赛参赛资格</td><td>了解自己的水准，以及下一步该练什么</td></tr>
            <tr><th scope="row">不适合用来</th><td>第一天就回答「我到底有多强」</td><td>与他人比赛时让分&mdash;&mdash;它不是让分系统</td></tr>
            <tr><th scope="row">费用与账号</th><td>联赛会员资格；一个线上档案</td><td>免费应用，无需账号，完全离线可用</td></tr>
          </tbody>
        </table>
      </div>

      <h2>把 Runout Rank 不是什么讲清楚</h2>
      <p>它不能取代联赛评分来让分，也不会让你在赛事中拿到种子位。没有任何管理机构承认它。
      它对自己的变量也很坦白：你打的是自己的器材，所以一张袋口紧、台呢慢的球台，
      读数会和酒吧小台不一样。请在你实际比赛的那张台子上做测试，并且拿同类条件的数字逐段比较。</p>
      <p>它给你的，是相对系统没法便宜地给你的东西：今天就有的、来自你自己击球的、
      不依赖任何其他人的真实数字。</p>

      <h2>显而易见的答案：两个都用</h2>
      <p>它们衡量的是不同的东西，彼此并不冲突。如果你打联赛，就留着 Fargo Rate 用于比赛，
      并在赛间用 Runout Rank 告诉你自己哪一部分落后了&mdash;&mdash;清台测试会点名卡住你的等级，
      并直接把针对它的练习递到你手上，这是一个基于比赛结果的评分做不到的。
      如果你不打联赛，Runout Rank 就是那个你真正能拥有的数字。</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="how-it-works.html">看看测试怎么进行</a>
        <a class="btn btn--ghost" href="pool-rating-without-a-league.html">不打联赛也拿到评分</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

NO_LEAGUE_TITLE = "不加入联赛，如何拿到台球评分"
NO_LEAGUE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "不打联赛也能有评分")}
      <h1>不加入联赛，如何拿到台球评分</h1>
      <p class="lead">每一套成熟的评分系统都收同一笔门票钱：与其他已评分球员打上数百场。
      如果那不是你的生活，你并非无法被评分&mdash;&mdash;你只是需要一种衡量球台、
      而不是衡量这屋子里的人的评分。</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>为什么休闲球员最后一个数字都没有</h2>
      <p>常见的建议是：加入一个向评分系统报送成绩的联赛，打一个赛季，你的评分就会稳定下来。
      这建议本身没错，但对很多球员来说它同时也是不可能的。它要求每周固定一个晚上、
      要交会员费、要有一个运营报送制联赛的场地，还要有足够多本身也已评分的对手。</p>
      <p>然后还有数量问题。FargoRate 把 200 局视为称一个评分「已确立」的最低稳健度；
      在此之下，你看到的有一部分是系统给你安排的初始评分，而不是你打出来的。
      对大多数联赛球员来说，200 场计分对局是一个赛季甚至更久，而对其他所有人来说则是幻想。</p>
      <p>所以对休闲球员来说，诚实的结论是：挣一个相对评分所要付出的力气，
      大过了知道这个评分的价值。多数人于是悄悄放弃，回到从「我在俱乐部赢过谁」来猜测的老路上。</p>

      <h2>你真正想弄清楚的是什么</h2>
      <p>把系统这层皮剥掉，底下通常是三个问题：</p>
      <ul>
        <li><strong>我在什么位置？</strong>我是个像样的俱乐部球员，还是比自己想的强，或者更弱？</li>
        <li><strong>我在进步吗？</strong>不是「今晚感觉不错」&mdash;&mdash;而是那条曲线在动吗？</li>
        <li><strong>我该练什么？</strong>究竟是哪一块在拖其余部分的后腿？</li>
      </ul>
      <p>这三个问题没有一个需要对手。它们需要的是一项固定、可重复、难到会失败的任务，
      以及一份你多久能完成一次的记录。</p>

      <h2>能回答它们的那个测试</h2>
      <p>清台是正确的计量单位：清完一整台会按球台要求的顺序，考验球型阅读、走位、力度控制和心态，
      而单纯的进球练习做不到这一点。把它定成同一难度等级下的十个球型，每个一次机会，
      不能重来也不能跳过，你就把一次练习变成了一次测量。</p>
      <p>这正是 Runout Rank 做的事。应用以俯视图画出每个球型，你在自己的球台上摆好，打一次，
      然后点「清台」或「失手」。结束时你会得到十中几的得分、0&ndash;100 的评分、
      一个从 Rookie 到 Master 的等级、是否通过该等级，以及当前卡住你的等级。
      整个过程大约一小时，而且不需要场子里有别人。</p>
      <p>球型每轮测试都重新生成，所以没什么可背；而等级的限制条件&mdash;&mdash;目标球数量、
      是否自由摆球、间距、障碍球&mdash;&mdash;是固定常数，在安卓和 iOS 上对每个球员都一样。
      每次都是新球型，每次都是同样的难度。</p>

      <h2>给独自练球者的一套实用流程</h2>
      <ol>
        <li><strong>在你自认为能通过的等级上测试。</strong>没有任何等级是锁着的，
        所以从你觉得自己该在的位置开始，而不是从最低一级开始。</li>
        <li><strong>一直往上测，直到某一级把你卡住。</strong>十中七即通过；
        当你做不到七桌时，你就找到了自己的临界点。</li>
        <li><strong>在临界等级上练习，</strong>并记录每一次尝试，让清台率成为事实而不是印象。</li>
        <li><strong>等清台率有变化，就重测那个等级。</strong>每两到四周一次适合大多数球员
        &mdash;&mdash;频繁到能跟上真实的功夫，又稀疏到你量的不是噪音。</li>
        <li><strong>比较评分，别比较感觉。</strong>结果页面上的评分变化，才是整件事的重点。</li>
      </ol>

      <h2>这要花你什么</h2>
      <p>一小时、一张你订得到的球台，除此之外别无所需。应用免费下载，不用注册账号，
      完全离线可用，而你的历史留在应用位于你自己设备上的私有存储里。
      Runout Pro 是可选的，加的是历史：你的评分贯穿每一轮测试绘成曲线、各等级的演进，
      以及 CSV 导出。「你在什么位置」这件事永久免费。</p>

      <h2>如果你确实打联赛</h2>
      <p>那就留着你的联赛评分&mdash;&mdash;它是给比赛让分的正确工具，本文并不是要取代它。
      把清台测试和它并用，因为一个基于比赛结果的评分只会告诉你水准在哪一档，
      却不会告诉你哪一部分落后了。参见
      <a href="fargo-rate-alternative.html">与 Fargo Rate 的完整对比</a>。</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="how-it-works.html">测试怎么进行</a>
        <a class="btn btn--ghost" href="levels.html">查看六个等级</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

ABSOLUTE_TITLE = "绝对评分与相对台球评分：为什么你的城市会改变你的数字"
ABSOLUTE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "绝对评分与相对评分")}
      <h1>绝对评分与相对台球评分</h1>
      <p class="lead">两个水平完全相同的球员，一个在强势城市、一个在冷清城市，
      可以连着好几年带着不同的相对评分。这不是算法的缺陷&mdash;&mdash;这就是「相对」的含义。
      下面说清楚两者的区别，以及每一种评分各自适合做什么。</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>什么是相对评分</h2>
      <p>相对评分&mdash;&mdash;Elo、Glicko、Fargo Rate 以及这一族的其他成员
      &mdash;&mdash;没有绝对标准这个概念。它只知道结果：你赢了他们，他们赢了别人。
      从足够大的一张结果之网里，系统找出最能解释这些胜负的那组数字。
      从来没有人被直接测量过；每一个评分都是它在其他评分构成的网络中的一个位置。</p>
      <p>这是个优雅的设计，在网络足够稠密时效果好得惊人。但它同时带来两个后果，
      再高明的数学也去不掉。</p>

      <h2>后果一：它需要大量对局</h2>
      <p>一个结果只是一比特证据，而一比特非常少。所以系统需要数量，才能把你和运气分开
      &mdash;&mdash;这正是 FargoRate 采用稳健度指标、并把 200 局视为称一个评分已确立的最低门槛的原因，
      在你达到之前，它会把一个初始评分混进这个数字里。在你用对局付清这笔钱之前，
      你的评分有一部分是关于你的猜测。</p>

      <h2>后果二：它锚定在你的邻居身上</h2>
      <p>因为每个评分都是相对其他评分定义的，一群球员只有在有足够多的对局把他们和世界其他地方连起来时，
      才会和外界对得齐。连接稀薄的地方&mdash;&mdash;孤立的区域、新成立的联赛、
      球员很少出门打公开赛的圈子&mdash;&mdash;整个群体可能会稳定在一个与别处同样数字并不相符的水平上。
      FargoRate 就把这种情况&mdash;&mdash;两个几乎隔离的群体，其中一组相对另一组评分偏高
      &mdash;&mdash;描述为一个棘手的问题，并且正是出于同样的原因指出，与已确立评分的对手交手权重更高。</p>
      <p>对球员来说的实际版本是：如果你的城市高手云集，或者和更大的已评分人群几乎不连通，
      那么你的数字有一部分是在陈述你的周遭。两个水平相同但身处不同球圈的球员，读数未必相同，
      而他们除了多打一些和外来者的对局之外，对此无能为力。</p>

      <h2>什么是绝对评分</h2>
      <p>绝对评分衡量的是对一个固定标准的表现，而不是对人的表现。高尔夫差点就是这样对标准杆运作的。
      田径就是这样对秒表运作的。秒表不在乎赛道上还有谁，马尼拉的 10.4 秒和曼彻斯特的 10.4 秒是一回事。</p>
      <p>台球传统上没有这样的东西，因为台球缺一个显而易见的秒表。Runout Rank 提供了等价物：
      一套定义好的球型，加上一个问题&mdash;&mdash;你能把它清掉吗？同一等级下十个球型，
      每个一次机会，不能重来也不能跳过。得出的数字完全由你自己对这些球型的结果算出。</p>
      <p>所以不存在强弱不定的对手池，没有什么可漂移的，也没有一个「测量才有效」的最低对局数。
      第一次打完你就有了评分，而且它在任何地方含义相同。</p>

      <h2>固定标准如何避免变成记忆力测试</h2>
      <p>一个明显的反驳：一套固定球型，在你打过几次之后就不再衡量技术了，
      因为那时你是在回忆解法，而不是在找解法。</p>
      <p>Runout Rank 靠固定<em>难度</em>而不是固定球型来避开这一点。一个等级是一组公开的常数
      &mdash;&mdash;目标球数量、是否自由摆球、最小间距、障碍球&mdash;&mdash;
      而球型每次都在这些规则内重新生成。你永远不会见到同一个球型两次，
      而每一个球型问的都是同一个问题。连打十个，会把剩下的运气成分抹平。</p>

      <h2>绝对评分做不到什么</h2>
      <p>它不是让分系统，也不该被当成让分系统用。相对评分存在的意义，
      是预测两个特定的人之间的一场比赛，而它在这件事上远胜于任何绝对测量
      &mdash;&mdash;因为它本来就是用比赛结果搭起来的。</p>
      <p>绝对评分也有它自己需要老实交代的变量：器材。袋口的切法、球台尺寸和台呢速度
      都会改变清台的难度，所以在一张九尺紧袋台上做的测试，和在酒吧小台上做的是两种不同的测量。
      固定你的条件，在你比赛用的那张台子上做测试，并把自己不同时期的数字放在一起比较。</p>

      <h2>你到底想要哪一个？</h2>
      <div class="compare" style="margin:24px 0">
        <div class="card">
          <h3>这些时候用相对评分</h3>
          <ul class="ticks">
            <li>你需要一个让分数字来打比赛或分组</li>
            <li>你的联赛或赛事要求必须有</li>
            <li>你本来就打足够多的计分对局，能让它保持稳健</li>
          </ul>
        </div>
        <div class="card card--gold">
          <h3>这些时候用绝对评分</h3>
          <ul class="ticks ticks--gold">
            <li>你想知道自己在什么位置，而不想先打一个赛季</li>
            <li>你独自练球、经常出差，或在不同球圈之间流动</li>
            <li>你想知道<em>该练什么</em>，而不只是自己排第几</li>
          </ul>
        </div>
      </div>
      <p>它们回答的是不同的问题，一个认真的球员完全可以两个都带着。</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="fargo-rate-alternative.html">与 Fargo Rate 对比</a>
        <a class="btn btn--ghost" href="how-it-works.html">评分是怎么算出来的</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

FAQ_ITEMS = [
    ("使用 Runout Rank 需要一张真实的球台吗？",
     "需要。Runout Rank 不是一款台球游戏&mdash;&mdash;它是真实球台的伴侣。应用以俯视图画出每个球型，"
     "你在眼前的台呢上摆好、打完，然后记录结果。"),
    ("需要账号或者网络连接吗？",
     "都不需要。没有什么要注册，也没有什么要登录，应用完全可以离线使用。你的测试、尝试、收藏和统计数据，"
     "只存在应用位于你自己设备上的私有存储里。"),
    ("评分是怎么算出来的？",
     "你在同一等级下打十个生成的球型，每个一次机会。十中几的得分会换算成 0&ndash;100 的评分和一个等级称号，"
     "十中七即通过该等级。结果还会显示你的评分相比上次测试移动了多少。"),
    ("既然测试是随机的，两个分数怎么比较？",
     "因为固定的是等级，不是球型。每个等级都规定了目标球数量、是否自由摆球、球与球之间的最小间距"
     "和障碍球数量，这些常数对两个平台上的每个球员都完全一致。球型是在这些规则内重新生成的，"
     "而连打十桌会把运气抹平&mdash;&mdash;所以 Level 4 的十中七，无论是谁打出来的，含义都相同。"),
    ("打砸了的球型可以重打吗？",
     "评级测试中不行&mdash;&mdash;每桌一次机会，不能重来也不能跳过，正是这一点让分数有意义。"
     "在自由练习里，同一个球型你想重打多少次都可以。"),
    ("测试中途被打断了会怎样？",
     "测试会精确地从你停下的那一桌继续。若是主动退出，应用会先请你确认，"
     "并说明未打完的一轮无法计分。"),
    ("我必须从 Level 1 开始吗？",
     "不必。没有任何等级是锁着的。六个等级里你想测哪个都行，已经测过的等级也可以重测。"),
    ("我的「临界等级」是什么？",
     "就是当前卡住你的那个等级&mdash;&mdash;你还跨不过去的最高一阶。它是最值得练的等级，"
     "结果页面和 Rank 页面都能让你一键直接进入。"),
    ("Runout Pro 多少钱，又多提供什么？",
     "Runout Pro 是可选的按月或按年订阅，价格由你所在商店以你本国货币定价。它加的是历史："
     "你的评分贯穿每一轮测试绘成曲线、各等级的成绩演进、清台率随时间的变化、完整测试日志，"
     "以及 CSV 导出。所有告诉你「此刻你在什么位置」的东西都保持免费。"),
    ("应用更新后我的历史记录安全吗？",
     "安全。你已有的测试、尝试和收藏会在应用更新之间保留。由于数据是本地的，"
     "卸载应用或清除其数据确实会把它们删掉。"),
    ("这和 Fargo Rate 有什么不同？",
     "Fargo Rate 是相对评分：它从你与其他已评分球员的结果中推算你的数字，"
     "这就是为什么 FargoRate 把 200 局视为评分确立的最低稳健度，"
     "也是为什么一个连接稀疏的本地球圈会相对整个网络漂移。Runout Rank 是绝对的"
     "&mdash;&mdash;它衡量你对固定生成球型的表现，所以一轮十桌就给你完整评分，"
     "而且没有任何对手池会影响它。它不是让分系统，也不能在比赛让分上取代联赛评分。"),
    ("我的 Runout Rank 评分要打多少局才有意义？",
     "十桌&mdash;&mdash;一轮测试，大约一小时。没有资格期，也没有临时评分阶段，"
     "因为这个评分是从你对既定球型的清台表现算出来的，而不是从你与其他球员的对战历史算出来的。"),
    ("我住在哪里会影响我的评分吗？",
     "不会。每个等级的限制条件在任何地方都是同样的常数，而且没有任何对手进入计算。"
     "唯一的本地变量是你的器材：袋口切法、球台尺寸和台呢速度都会改变清台的难度，"
     "所以请在你实际打球的那张台子上做测试，并把自己不同时期的数字放在一起比较。"),
    ("我可以同时用 Runout Rank 和联赛评分吗？",
     "可以，而且如果你打联赛，这才是明智的做法。联赛评分留着给比赛让分，"
     "清台测试则用来找出哪个等级卡住了你、并在那里练习"
     "&mdash;&mdash;这是一个基于比赛结果的评分给不了你的东西。"),
    ("Runout Rank 在安卓和 iOS 上一样吗？",
     "一样。等级定义、球型生成器和评分算法都是在两个平台上运行的同一份共享代码，"
     "所以你用什么手机对评分没有任何影响。"),
]

FAQ_BODY_ITEMS = faq_body(FAQ_ITEMS)
FAQ_SCHEMA = faq_schema(FAQ_ITEMS)

FAQ = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "常见问题")}
      <h1>常见问题</h1>
      <p class="lead">测试、评分、等级、订阅，以及你的数据。</p>
    </div>
  </section>

  <section>
    <div class="container" style="max-width:52rem">
{FAQ_BODY_ITEMS}
      <p style="margin-top:28px">还是不清楚这个数字是怎么来的？
      <a href="how-it-works.html">看看评分的原理 &rarr;</a></p>
    </div>
  </section>

{CTA}
"""

NOT_FOUND = """  <section class="page-head">
    <div class="container">
      <h1>这一桌还没摆上</h1>
      <p class="lead">你要找的页面不存在。这里是回去的路。</p>
      <div class="btn-row" style="margin-bottom:40px">
        <a class="btn btn--primary" href="index.html">回到首页</a>
        <a class="btn btn--ghost" href="how-it-works.html">评测怎么进行</a>
      </div>
    </div>
  </section>
"""


PAGES = [
    dict(slug="index.html",
         title="Runout Rank — 安卓与 iOS 上的绝对台球水平评测",
         description="一次坐下就拿到真实的台球评分，不用打满 200 场联赛。Runout Rank 衡量的是你对十个"
                     "生成球型的表现，而不是你和本地对手的胜负，所以这个 0–100 的数字在每一座城市"
                     "含义相同。不用联赛、不用账号、离线可用。",
         body=INDEX,
         schema=[app_schema(LOCALE, UI), site_schema(LOCALE, UI)],
         keywords="绝对台球评分, Fargo Rate 替代, 台球水平测试, 桌球评分应用, 不打联赛的台球评分, "
                  "清台测试, 台球训练应用, 台球等级测试"),

    dict(slug="how-it-works.html",
         title="Runout Rank 评分的原理 — 十桌，每桌一次机会",
         description="同一等级下十个随机生成的球型，每个一次机会，换算成 0–100 的绝对台球评分和一个等级。"
                     "每轮球型全新，等级参数固定，所以这个数字在每一座城市含义相同。",
         body=HOW,
         schema=[breadcrumb_schema(LOCALE, UI, "评测原理", "how-it-works.html")]),

    dict(slug="levels.html",
         title="六个等级 — 从 Rookie 到 Master | Runout Rank",
         description="Rookie、Regular、League、Competitor、Advanced、Master。这架梯子每一阶变化了什么"
                     "——球数、自由摆球、密集程度和障碍球——以及为什么没有一阶是锁着的。",
         body=LEVELS,
         schema=[breadcrumb_schema(LOCALE, UI, "六个等级", "levels.html")]),

    dict(slug="practice.html",
         title="台球练习与一份记得住的训练日志 | Runout Rank",
         description="在你选择的等级上无穷生成练习球型，一键记录，可重打可跳过，可收藏，"
                     "并保留你打过的每一桌的完整训练日志。",
         body=PRACTICE,
         schema=[breadcrumb_schema(LOCALE, UI, "练习", "practice.html")]),

    dict(slug="fargo-rate-alternative.html",
         dated=True,
         title=FARGO_ALT_TITLE + " | Runout Rank",
         description="Fargo Rate 要打满 200 局评分才算确立，而相对评分锚定在你周围的人身上。"
                     "Runout Rank 是一轮十桌就得出的绝对台球评分——两者公允地并排对比。",
         body=FARGO_ALT,
         schema=[article_schema(LOCALE, UI,
             FARGO_ALT_TITLE,
             "为什么相对联赛评分要 200 局才能确立、又会随本地球员池浮动，绝对清台评分改成怎么做，"
             "以及这两者你到底想要哪一个。",
             "fargo-rate-alternative.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "Fargo Rate 的替代方案", "fargo-rate-alternative.html")],
         published=UPDATED,
         keywords="Fargo Rate 替代, Fargo 评分替代方案, 台球评分应用, 绝对台球评分, "
                  "Fargo Rate 200 局, Fargo 评分确立, Fargo Rate 准确度"),

    dict(slug="pool-rating-without-a-league.html",
         dated=True,
         title=NO_LEAGUE_TITLE + " | Runout Rank",
         description="每一套联赛评分都要求先打上数百场对局，数字才算数。这里讲的是一个休闲或独自练球的球员，"
                     "如何在自己的球台上、一次坐下就拿到诚实的 0–100 台球评分。",
         body=NO_LEAGUE,
         schema=[article_schema(LOCALE, UI,
             NO_LEAGUE_TITLE,
             "休闲球员或独自练球的人，如何不加入联赛、不打满 200 场计分对局，"
             "就在一次坐下之内拿到诚实的台球评分。",
             "pool-rating-without-a-league.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "不打联赛也能有评分", "pool-rating-without-a-league.html")],
         published=UPDATED,
         keywords="不打联赛的台球评分, 怎么拿到台球评分, 休闲台球评分, 独自练球评分, "
                  "台球水平评定, 桌球技术评分"),

    dict(slug="absolute-vs-relative-pool-rating.html",
         dated=True,
         title=ABSOLUTE_TITLE + " | Runout Rank",
         description="Elo、Glicko 和 Fargo Rate 都是相对的：每个评分都是它在一张评分网络中的位置，"
                     "所以对局数量和本地连通性都会起作用。绝对台球评分改成衡量什么，两者各自适合做什么。",
         body=ABSOLUTE,
         schema=[article_schema(LOCALE, UI,
             ABSOLUTE_TITLE,
             "为什么相对台球评分取决于你周围的人，绝对评分改成衡量什么，以及哪一种回答哪一个问题。",
             "absolute-vs-relative-pool-rating.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "绝对评分与相对评分", "absolute-vs-relative-pool-rating.html")],
         published=UPDATED,
         keywords="绝对评分与相对台球评分, 相对评分系统, Elo 台球评分, "
                  "Fargo 评分地区差异, 台球评分原理"),

    dict(slug="runout-pro.html",
         title="Runout Pro — 完整评分历史与 CSV 导出 | Runout Rank",
         description="你现在在哪里，永久免费。Runout Pro 加的是你怎么走到这里的：评分贯穿每一轮测试的曲线、"
                     "各等级的演进、完整测试日志与 CSV 导出。",
         body=PRO,
         schema=[breadcrumb_schema(LOCALE, UI, "Runout Pro", "runout-pro.html")]),

    dict(slug="pool-skill-level-test.html",
         dated=True,
         title=GUIDE_TITLE,
         description="一个值得做的台球水平测试，和一个你恰好喜欢的练习，区别在哪里：完整清台、"
                     "不可预测的球型、被定义的难度、每桌一次机会，以及拿到那个数字之后该做什么。",
         body=GUIDE,
         schema=[article_schema(LOCALE, UI,
             GUIDE_TITLE,
             "一个值得做的台球水平测试，和一个你恰好喜欢的练习，区别究竟在哪里。",
             "pool-skill-level-test.html", FIRST_PUBLISHED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "台球水平测试", "pool-skill-level-test.html")],
         keywords="怎么测台球水平, 台球水平测试, 桌球水平评估, 清台练习, 台球评分系统"),

    dict(slug="faq.html",
         title="Runout Rank 常见问题 — 测试、评分、等级与你的数据",
         description="需要真实球台吗？需要联赛吗？评分怎么算，和 Fargo Rate 有什么不同，"
                     "Runout Pro 又多提供什么？这里是常见问题的答案。",
         body=FAQ,
         schema=[FAQ_SCHEMA, breadcrumb_schema(LOCALE, UI, "常见问题", "faq.html")]),
]
