"""한국어 copy for the Runout Rank site.

Mirrors locales/en.py exactly: same names, same page order, same markup —
only the strings differ. See locales/en.py for the contract.
"""

from common import (
    FIRST_PUBLISHED, PLAY_URL, UPDATED,
    app_schema, article_schema, breadcrumb, breadcrumb_schema, byline,
    faq_body, faq_schema, locale_by_code, site_schema, store_block,
)

LOCALE = locale_by_code("ko")

UI = dict(
    tagline="안드로이드와 iOS를 위한 절대 당구 실력 측정·훈련 앱",
    author_title="Runout Rank 제작자",

    # --- chrome ---------------------------------------------------------
    skip_link="본문으로 건너뛰기",
    nav_aria="주요 메뉴",
    lang_aria="언어",
    lang_current="언어",
    breadcrumb_label="현재 위치",
    nav_home="홈",
    nav=[
        ("index.html", "홈"),
        ("how-it-works.html", "측정 방식"),
        ("levels.html", "레벨"),
        ("practice.html", "연습"),
        ("fargo-rate-alternative.html", "Fargo Rate 비교"),
        ("runout-pro.html", "Runout Pro"),
        ("faq.html", "자주 묻는 질문"),
    ],

    # --- byline ---------------------------------------------------------
    byline_by="글",
    byline_sep=",",
    byline_published="게시일",
    byline_updated="수정일",
    date_format="{y}년 {m}월 {d}일",
    months=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],

    # --- store badges ---------------------------------------------------
    store_get_it_on="다운로드",
    store_in_review="심사 중",
    store_review_aria="App Store 심사 중",

    # --- footer ---------------------------------------------------------
    footer_blurb="당신이 늘 치는 그 테이블에서 열 판 런아웃 테스트를 치르고 절대 당구 레이팅을 받으세요. "
                 "한 번 앉은 자리에서 0&ndash;100 점수가 나옵니다 &mdash; 리그도, 200경기의 기다림도, "
                 "계정도, 인터넷도 필요 없습니다.",
    footer_col_app="앱",
    footer_col_guides="가이드",
    footer_links_app=[
        ("how-it-works.html", "측정 방식"),
        ("levels.html", "여섯 개의 레벨"),
        ("practice.html", "연습과 훈련 기록"),
        ("runout-pro.html", "Runout Pro"),
    ],
    footer_links_guides=[
        ("fargo-rate-alternative.html", "Fargo Rate 대안"),
        ("pool-rating-without-a-league.html", "리그 없이 받는 레이팅"),
        ("absolute-vs-relative-pool-rating.html", "절대 레이팅과 상대 레이팅"),
        ("pool-skill-level-test.html", "당구 실력 측정 가이드"),
        ("faq.html", "자주 묻는 질문"),
        ("privacy-policy.html", "개인정보 처리방침"),
    ],
    footer_sitemap="사이트맵",
    footer_copyright="&copy; {year} Runout Rank. {author}이(가) 쓰고 만들었습니다.",
    footer_platforms="안드로이드 &amp; iOS &middot; 앱과 마찬가지로 다크 모드 전용",
    footer_disclaimer="Fargo Rate와 FargoRate는 각 소유자의 상표입니다. "
                      "Runout Rank는 독립적인 앱이며 FargoRate, BCA, APA 또는 어떤 리그 운영 주체와도 "
                      "제휴, 보증, 연관 관계가 없습니다. 이 사이트의 비교는 해당 시스템들이 공개한 동작 방식을 "
                      "설명한 것이며, 판단은 읽는 분의 몫으로 남겨 둡니다.",

    # --- social / meta --------------------------------------------------
    og_image_alt="Runout Rank — 당신의 당구 실력, 정말 어느 정도일까요?",

    # --- privacy policy page --------------------------------------------
    privacy_title="개인정보 처리방침 | Runout Rank",
    privacy_description="Runout Rank는 테스트, 레이팅, 연습 기록을 오직 사용자의 기기에만 저장합니다. "
                        "이 방침은 앱이 실제로 사용하는 분석 도구, 데이터가 공유되는 대상, "
                        "그리고 사용자의 권리를 설명합니다.",
    privacy_h1="개인정보 처리방침",
    privacy_breadcrumb="개인정보 처리방침",
    privacy_lead="테스트와 통계는 사용자의 기기에 남습니다. 이 페이지는 앱이 실제로 수집하는 모든 것과 그 이유, "
                 "그리고 사용자가 무엇을 통제할 수 있는지를 설명합니다.",

    # --- 404 ------------------------------------------------------------
    not_found_title="페이지를 찾을 수 없습니다 | Runout Rank",
    not_found_description="해당 페이지는 존재하지 않습니다. Runout Rank 홈으로 돌아가세요.",

    # --- SoftwareApplication schema -------------------------------------
    app_description="Runout Rank는 절대 방식의 당구 실력 측정 앱입니다. 실제 당구대에서 열 판 런아웃 테스트를 "
                    "치르면 한 번의 세션만으로 0-100 레이팅과 Rookie부터 Master까지의 등급을 받고, "
                    "당신을 막고 있는 레벨에서 바로 연습할 수 있습니다. 이 레이팅은 주변 상대가 아니라 고정된 배치를 "
                    "기준으로 측정하므로 리그도, 200경기의 전적도, 상대조차도 필요하지 않습니다. "
                    "모든 데이터는 사용자의 기기에 남습니다.",
    app_features=[
        "절대 레이팅: 주변 상대가 아니라 고정 생성된 배치를 기준으로 측정",
        "열 판 한 세션으로 완전한 0-100 레이팅, 먼저 채워야 할 최소 경기 수 없음",
        "잣대가 절대 바뀌지 않으므로 도시·리그·국가를 옮겨도 그대로 통함",
        "0-100 레이팅과 등급 명칭이 나오는 열 판 레이팅 테스트",
        "Rookie부터 Master까지 여섯 개의 도전 레벨",
        "레벨 제약이 고정되어 있어 같은 레이팅은 어디서나 같은 의미",
        "무한히 무작위 생성되는 연습 배치",
        "즐겨찾기가 있는 훈련 기록",
        "누적 런아웃 성공률, 연속 기록, 레벨별 통계",
        "계정 없이 완전한 오프라인 사용 가능",
    ],
    app_offer="무료 다운로드. 선택 사항인 Runout Pro 구독으로 성장 기록과 CSV 내보내기를 이용할 수 있습니다.",
)

CTA = f"""  <section class="cta band">
    <div class="container">
      <p class="eyebrow">당신의 숫자를 받으세요</p>
      <h2>열 판. 판마다 단 한 번. 정직한 레이팅 하나.</h2>
      <p class="lead" style="max-width:38rem;margin:0 auto 28px">늘 치던 그 테이블에 배치를 그대로 놓으세요.
      앱이 런아웃을 채점하고, 다음에 어느 레벨에서 훈련해야 하는지 알려 줍니다.</p>
      {store_block(UI, centred=True)}
    </div>
  </section>"""


# --------------------------------------------------------------------------
# Page bodies
# --------------------------------------------------------------------------

INDEX = f"""  <section class="hero">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow">절대 당구 레이팅 &middot; 안드로이드 &amp; iOS</p>
        <h1>당신의 당구 레이팅. 200경기 뒤가 아니라 <span class="accent">오늘 밤</span>에.</h1>
        <p class="lead">리그 레이팅은 숫자가 의미를 가지려면 수백 경기가 필요하고, 그렇게 얻은 값조차
        당신이 사는 도시에 마침 누가 있느냐에 좌우됩니다. Runout Rank는 대신 테이블을 기준으로 측정합니다.
        열 개의 배치, 판마다 단 한 번, 한 세션에 0&ndash;100 레이팅.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="{PLAY_URL}">Google Play에서 다운로드</a>
          <a class="btn btn--ghost" href="how-it-works.html">테스트 진행 방식</a>
        </div>
        <p class="hero-note">리그 불필요 &middot; 상대 불필요 &middot; 계정 불필요 &middot; 오프라인 사용 가능</p>
      </div>
      <div class="hero-shot">
        <div class="phone">
          <img src="assets/img/screen-home.png" width="1080" height="2400"
               alt="휴대폰에 표시된 Runout Rank 홈 화면. 열 판 레이팅 테스트를 시작하도록 안내하고 있습니다."
               fetchpriority="high" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <section class="tight band">
    <div class="container">
      <div class="grid grid--4">
        <div><span class="stat">10</span><p class="dim">테스트당 판 수, 판마다 단 한 번</p></div>
        <div><span class="stat">1</span><p class="dim">세션이면 완전한 레이팅, 200경기를 기다릴 필요 없음</p></div>
        <div><span class="stat">0&ndash;100</span><p class="dim">끝나는 즉시 나오는 레이팅과 등급</p></div>
        <div><span class="stat">0</span><p class="dim">필요한 리그, 상대, 계정의 수</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">왜 굳이</p>
        <h2>리그 레이팅은 한 시즌을 요구하고 <span class="accent">그러고도 도시에 따라 움직입니다.</span></h2>
      </div>
      <div class="compare">
        <div class="card pain">
          <h3>200경기를 채워야 비로소 진짜</h3>
          <p>FargoRate는 레이팅이 확립되었다고 보는 최소 기준을 200경기로 둡니다. 즉 내가 어디쯤인지 알기까지
          리그와 한 시즌, 그리고 각종 비용이 먼저 필요하다는 뜻입니다.</p>
          <p><a href="pool-rating-without-a-league.html">리그 없이 받는 레이팅 &rarr;</a></p>
        </div>
        <div class="card pain">
          <h3>당신의 숫자는 사실 우편번호를 말합니다</h3>
          <p>상대 레이팅은 주변 사람들에게 묶여 있으므로, 얇거나 고립된 지역 판은 세계의 나머지와 어긋나게
          흘러갑니다.</p>
          <p><a href="absolute-vs-relative-pool-rating.html">절대와 상대 &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">해법</p>
        <h2>사람을 <span class="accent">테이블</span>에 견주세요. 그 방에 있는 사람들 말고.</h2>
        <p class="lead">각 레벨은 무엇이 그 레벨을 어렵게 만드는지를 정확히 고정합니다 &mdash; 공의 개수,
        프리볼 여부, 공이 얼마나 빽빽하게 놓이는지, 방해구. 그 제약들이 곧 잣대이며, 모두에게 똑같습니다.
        그것을 이겨 내면 숫자가 오릅니다. 그 외에 이 숫자를 움직이는 것은 없습니다.</p>
      </div>
      <div class="grid grid--3">
        <div class="card">
          <h3>상대가 아닌 절대</h3>
          <p>강할 수도 약할 수도 있는 상대 풀이 없으니, 어긋나 흘러갈 대상 자체가 없습니다.</p>
        </div>
        <div class="card">
          <h3>한 시즌이 아니라 한 세션</h3>
          <p>테이블 앞에서 한 시간쯤이면 임시 값이 아니라 진짜 레이팅을 손에 쥐고 끝냅니다.</p>
        </div>
        <div class="card">
          <h3>외울 것이 없음</h3>
          <p>배치는 테스트마다 새로 생성되므로, 당신이 마주하는 것은 언제나 그 레벨이지 답을 이미 외운
          드릴이 아닙니다.</p>
        </div>
      </div>
      <p style="margin-top:28px"><a href="fargo-rate-alternative.html">Fargo Rate와의 전체 비교 &rarr;</a></p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">진행 방식</p>
        <h2>세 단계, 한 자리에서</h2>
      </div>
      <div class="grid grid--3 steps">
        <div class="card step">
          <h3>앱이 그려 주는 대로 배치</h3>
          <p>각 판은 위에서 내려다본 그림이라, 눈앞의 테이블에 똑같이 놓을 수 있습니다.</p>
        </div>
        <div class="card step">
          <h3>딱 한 번 친다</h3>
          <p>런아웃하거나 실패하고, 한 번의 탭으로 기록합니다. 다시 치기도, 건너뛰기도 없습니다.</p>
        </div>
        <div class="card step">
          <h3>레이팅과 계획을 받는다</h3>
          <p>점수, 레이팅, 등급 &mdash; 그리고 당신을 막고 있는 레벨까지. 다음엔 거기서 연습하면 됩니다.</p>
        </div>
      </div>
      <p style="margin-top:28px"><a href="how-it-works.html">전체 설명 읽기 &rarr;</a></p>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-test.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="진행 중인 레이팅 테스트: 10판 중 6판째가 위에서 내려다본 그림으로 표시되고, 천 위에 번호가 매겨진 목적구 네 개와 아래쪽에 런아웃 및 실패 버튼이 있습니다."></div>
        </div>
        <div>
          <p class="eyebrow">테이블</p>
          <h3>한 판은 이렇게 생겼습니다.</h3>
          <p>각 판은 위에서 내려다본 축척 그림이라, 눈앞의 천 위에 그대로 놓고 실제 샷을 칠 수 있습니다.
          한 번의 시도가 끝날 때까지 화면에 남아 있으므로, 공을 건드려 흐트러뜨렸다면 배치를 다시 세울 수
          있습니다.</p>
          <ul class="ticks">
            <li><strong>숫자는 넣어야 하는 순서</strong>입니다 &mdash; 공의 점수가 아닙니다</li>
            <li><strong>방해구</strong>는 흐릿하게, 번호 없이 그려집니다. 길을 막을 뿐 순서에는 없습니다</li>
            <li><strong>수구</strong>는 Advanced부터 등장합니다. 그 아래 레벨에서는 프리볼입니다</li>
          </ul>
        </div>
      </div>

      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-result.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="10판 중 7판 성공, 레이팅 58, League 등급, 그리고 다음에 할 일을 보여 주는 테스트 결과 화면."></div>
        </div>
        <div>
          <p class="eyebrow">결과</p>
          <h3>레이팅, 그리고 당신을 <span class="gold">막고 있는</span> 레벨.</h3>
          <p>10판 중 7판이면 그 레벨을 통과합니다. 점수와 0&ndash;100 레이팅, 등급, 그리고 지난번 대비
          숫자가 얼마나 움직였는지를 받습니다 &mdash; 이어서 지금 당신을 막고 있는 레벨이 나오고,
          거기서의 연습은 탭 한 번 거리입니다.</p>
        </div>
      </div>

      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-progress.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="레이팅, 등급, 누적 지표, 레벨별 상세를 보여 주는 성장 화면."></div>
        </div>
        <div>
          <p class="eyebrow">성장</p>
          <h3>연습이 효과가 있는지 확인하세요.</h3>
          <p>레이팅, 등급, 통과한 레벨, 누적 런아웃 성공률, 최고 연속 기록 &mdash; 영구 무료입니다.
          <a href="runout-pro.html">Runout Pro</a>는 여기에 기록을 더합니다. 모든 테스트를 시간순 그래프로,
          그리고 CSV 내보내기까지.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid grid--3">
        <div class="card">
          <h3>여섯 레벨, 잠긴 곳 없음</h3>
          <p>Rookie부터 Master까지. 어느 레벨에서든 테스트하세요 &mdash; 잘 치는 사람이 맨 아래부터 갈아
          올라갈 이유는 없습니다. <a href="levels.html">레벨 비교하기 &rarr;</a></p>
        </div>
        <div class="card">
          <h3>내 한계선에서 연습</h3>
          <p>당신을 막은 그 레벨에서 무한히 생성되는 배치와, 지금까지 친 모든 판의 기록.
          <a href="practice.html">연습에 대해 더 보기 &rarr;</a></p>
        </div>
        <div class="card">
          <h3>기록은 당신의 것</h3>
          <p>계정도 서버도 없고 오프라인으로 동작합니다. 모든 것이 당신의 기기에 있습니다.
          <a href="privacy-policy.html">개인정보 처리방침 &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

HOW = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "측정 방식")}
      <h1>Runout Rank 레이팅은 어떻게 계산되는가</h1>
      <p class="lead">생성된 열 개의 배치, 판마다 단 한 번의 시도, 그것이 0&ndash;100 레이팅과 등급 명칭으로
      환산됩니다 &mdash; 그리고 다음에 무엇을 해야 하는지에 대한 분명한 지시까지.</p>
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>1. 레벨을 고르고 테스트를 시작합니다</h2>
      <p>레이팅 테스트는 한 레벨에서 치르는 열 판입니다. 레벨은 당신이 고릅니다. 앱이 하나를 제안하지만
      잠긴 레벨은 없으므로, 잘 치는 사람은 Rookie부터 갈아 올라갈 필요 없이 바로 Competitor에서 시작해도
      됩니다. 레이팅을 받아 본 적이 없다면 홈 화면에서 탭 한 번이면 테스트가 시작됩니다 &mdash; 미리
      설정할 것은 없습니다.</p>
      <p>몸을 좀 풀고 싶다면 연습용 배치를 한 판만 생성해 보고 테스트는 나중에 치러도 됩니다.</p>

      <h2>2. 각 배치를 실제 테이블에 놓습니다</h2>
      <p>모든 판은 수구, 목적구, 그리고 방해구가 제자리에 놓인 채 위에서 내려다본 그림으로 그려집니다.
      방해구는 넣는 순서의 일부로 읽히는 일이 없도록 일부러 흐릿하게, 번호 없이 그립니다. 보이는 대로,
      당신이 늘 치던 그 테이블 위에 놓으면 됩니다. 그림은 한 번의 시도가 끝날 때까지 화면에 남아 있으므로
      배치가 흐트러져도 다시 세울 수 있습니다.</p>

      <h2>3. 한 번 치고, 한 번 기록합니다</h2>
      <p>런아웃하거나, 못 하거나. 탭 한 번이면 결과가 기록되고 다음 판으로 넘어갑니다. 상단에는 열 판 중
      몇 번째인지가 항상 표시되고, 판 위쪽의 띠는 이미 친 판들 중 어느 것이 런아웃이었고 어느 것이
      실패였는지를 보여 줍니다.</p>
      <p><strong>판마다 정확히 한 번의 시도. 다시 치기도, 건너뛰기도 없습니다.</strong> 마지막에 나오는
      숫자가 값어치를 갖는 이유가 바로 그 제약입니다.</p>
      <div class="note">중간에 방해를 받았나요? 테스트를 나갔다가 나중에 돌아오세요 &mdash; 멈췄던 바로 그
      판에서 이어집니다. 일부러 그만두려 하면 먼저 확인을 요청하고, 끝내지 못한 회차는 채점할 수 없다는
      점을 알려 줍니다.</div>

      <h2>4. 결과를 읽습니다</h2>
      <p>열 번째 판이 기록되는 순간 다음을 받습니다.</p>
      <ul>
        <li><strong>10점 만점의 점수</strong> &mdash; 열 판 중 몇 판을 런아웃했는지.</li>
        <li><strong>0&ndash;100 레이팅</strong>과 그에 해당하는 <strong>등급</strong>.</li>
        <li><strong>통과 여부.</strong> 10판 중 7판이면 그 레벨을 통과합니다.</li>
        <li><strong>레이팅 변화량</strong> &mdash; 지난 테스트 이후 숫자가 얼마나 움직였는지.</li>
        <li><strong>당신의 한계 레벨</strong> &mdash; 지금 당신을 막고 있는 레벨과, 그에 대해 무엇을 해야
        하는지에 대한 쉬운 설명.</li>
      </ul>
      <p>그 화면에서 한계 레벨의 연습을 시작하는 것은 탭 한 번입니다.</p>

      <h2>배치가 무작위인데 어떻게 점수를 비교할 수 있나</h2>
      <p>모든 테스트는 새로 생성되므로 외울 답도, 미리 연습해 둘 드릴도 없습니다. 두 사람이 똑같은 열 판을
      만나는 일은 없습니다 &mdash; 그럴 필요도 없고요.</p>
      <p>고정된 것은 <strong>레벨</strong>입니다. 공의 개수, 프리볼 여부, 공 사이의 최소 간격, 방해구의
      수는 모두 정의된 상수이며 두 플랫폼의 모든 사용자에게 동일합니다. Level&nbsp;4 테스트는 언제나
      Level&nbsp;4의 질문을 던집니다. 열 판이면 난이도의 기복이 상쇄되기에 충분하고, 그래서 테스트가 한
      판이 아니라 열 판인 것입니다.</p>
      <p>따라서 측정되는 것은 그 레벨의 제약에 맞선 당신이지, 특정한 열 판에 맞선 당신이 아닙니다. 한
      사람의 58점이 다른 사람의 58점과 같은 의미를 갖는 이유가 바로 이것입니다.</p>

      <h2>이 레이팅이 절대적인 이유</h2>
      <p>그 계산 어디에도 상대는 등장하지 않습니다. Fargo Rate 같은 리그 시스템은 <em>상대적</em>입니다
      &mdash; 당신의 숫자가 이미 레이팅을 가진 다른 사람들과의 결과에서 도출되며, 그래서 레이팅이 안정되기까지
      많은 전적이 필요하고, 느슨하게 연결된 지역 판이 네트워크의 나머지에 비해 높거나 낮게 자리 잡을 수 있는
      것입니다. Runout Rank는 대신 고정된 기준과 당신을 비교합니다. 레벨의 제약은 어디서나 같으므로, 이
      레이팅은 첫 테스트부터 어디서나 동일한 측정입니다.</p>
      <p>유일한 지역 변수는 당신의 장비입니다. 포켓을 깎은 형태, 테이블 크기, 천의 빠르기는 런아웃의 난이도를
      바꾸므로, 실제로 치는 그 테이블에서 테스트하고 자신의 숫자를 시간에 따라 비교하세요.</p>
      <p><a href="absolute-vs-relative-pool-rating.html">절대 레이팅과 상대 레이팅 &rarr;</a></p>

      <h2>이 레이팅이 아닌 것</h2>
      <p>이것은 다시 치기 금지 규칙 아래에서, 생성된 배치에 대한 당신의 런아웃 능력을 측정한 값입니다.
      핸디캡 시스템이 아니고, 협회 공인 레이팅도 아니며, 어떤 리그 데이터베이스와도 연동되지 않습니다.
      경기에 핸디를 매길 숫자가 필요하다면 그것이 리그 레이팅의 용도입니다 &mdash;
      <a href="fargo-rate-alternative.html">둘을 비교한 글</a>을 보세요. 이것은 당신이 자신의 테이블에서,
      새 숫자가 필요할 때마다 직접 뽑을 수 있는 정직한 숫자입니다.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="levels.html">여섯 레벨 보기</a>
        <a class="btn btn--ghost" href="fargo-rate-alternative.html">Fargo Rate와 비교</a>
      </div>
    </div>
  </section>

{CTA}
"""

LEVELS = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "레벨")}
      <h1>Rookie부터 Master까지, 여섯 개의 레벨</h1>
      <p class="lead">난이도는 슬라이더가 아니라 사다리입니다. 한 칸 오를 때마다 당신이 런아웃해야 할 배치에서
      무언가 구체적인 것이 바뀝니다 &mdash; 그리고 어느 칸도 잠겨 있지 않습니다.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="table-wrap">
        <table>
          <caption class="sr-only">Runout Rank의 여섯 레벨과 각 단계에서 바뀌는 것</caption>
          <thead>
            <tr>
              <th scope="col">레벨</th>
              <th scope="col">이름</th>
              <th scope="col">목적구</th>
              <th scope="col">프리볼</th>
              <th scope="col">최소 간격</th>
              <th scope="col">방해구</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>1</strong></td><td><strong>Rookie</strong></td><td>2</td><td>있음</td><td>8&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>2</strong></td><td><strong>Regular</strong></td><td>3</td><td>있음</td><td>6&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>3</strong></td><td><strong>League</strong></td><td>4</td><td>있음</td><td>4&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>4</strong></td><td><strong>Competitor</strong></td><td>5</td><td>있음</td><td>2.25&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>5</strong></td><td><strong>Advanced</strong></td><td>5</td><td>없음</td><td>2.25&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>6</strong></td><td><strong>Master</strong></td><td>5</td><td>없음</td><td>2.25&Prime;</td><td>2</td></tr>
          </tbody>
        </table>
      </div>
      <p class="dim" style="margin-top:16px">간격은 공 중심에서 중심까지의 <em>최소</em> 거리이므로, 숫자가
      클수록 더 넓게 퍼진, 더 너그러운 배치입니다. 2.25&Prime;는 공 하나의 지름 &mdash; 그 아래로는 공이
      물리적으로 겹치게 되는 하한선입니다. 같은 수치가 앱 안의 각 레벨 카드에도 표시됩니다.</p>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">사다리 읽기</p>
        <h2>네 개의 다이얼, 한 칸씩 올라갑니다</h2>
      </div>
      <div class="grid grid--4">
        <div class="card"><h3>공의 개수</h3><p>Rookie에서는 두 개, Competitor부터는 다섯 개로 늘어납니다. 공이 하나 늘 때마다 성공시켜야 할 포지션 판단이 하나 더 생깁니다.</p></div>
        <div class="card"><h3>프리볼</h3><p>1&ndash;4 레벨은 수구를 직접 놓게 해 줍니다. Advanced부터는 배치가 정한 자리에 놓이고, 주어진 상황에서 시작해야 합니다.</p></div>
        <div class="card"><h3>밀집도</h3><p>공 사이 최소 간격이 8&Prime;에서 공 지름 하나까지 줄어듭니다. 빽빽한 공은 각을 막고 포지션 플레이를 망칩니다.</p></div>
        <div class="card"><h3>방해구</h3><p>Master에만 두 개가 추가됩니다. 넣는 순서에 포함되지 않고 &mdash; 흐릿하게, 번호 없이 그려지며 &mdash; 오직 당신의 길을 막기 위해 존재합니다.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-levels.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="League 레벨이 펼쳐진 레벨 화면. 최고 테스트 점수와 최근 연습 성공률을 보여 줍니다."></div>
        </div>
        <div>
          <p class="eyebrow">단계별 나의 위치</p>
          <h3>모든 레벨이 당신의 성적을 알고 있습니다</h3>
          <p>어느 레벨이든 펼치면 그곳에서의 최고 테스트 점수, 최근 연습 런아웃 성공률, 그리고 그 성공률이
          몇 번의 시도에 근거한 것인지를 볼 수 있습니다 &mdash; 진짜 약점과 그저 안 풀린 하루를 구분할 수
          있도록 말이죠. 통과한 레벨은 표시되고, 당신의 <span class="gold">한계</span> &mdash; 지금 당신을
          막고 있는 레벨 &mdash; 은 금색으로 강조됩니다.</p>
          <ul class="ticks ticks--gold">
            <li>다음 레벨뿐 아니라 어느 레벨에서든 레이팅 테스트를 시작할 수 있습니다</li>
            <li>이미 테스트한 레벨을 다시 치러 결과를 확인하거나 끌어올릴 수 있습니다</li>
            <li>이 사다리에서 바로 어느 레벨의 자유 연습이든 시작할 수 있습니다</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

PRACTICE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "연습")}
      <h1>연습, 그리고 지금까지 친 모든 판의 기록</h1>
      <p class="lead">테스트는 어느 레벨이 당신을 막는지 알려 줍니다. 연습은 그에 대해 무언가를 하는
      자리입니다 &mdash; 바로 그 레벨에서 끝없이 생성되는 배치들.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-practice.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="생성된 네 개 공 배치와 런아웃 여부를 묻는 안내가 있는 연습 세션."></div>
        </div>
        <div>
          <p class="eyebrow">한 세션</p>
          <h3>소재가 떨어지지 않고, 배치를 외울 일도 없습니다</h3>
          <p>연습용 판은 당신이 고른 레벨에서 필요할 때마다 생성되며, 시도 기록은 그 레벨의 통계에 반영됩니다.
          그림은 한 번의 시도가 끝날 때까지 화면에 남아 있으므로 배치가 흐트러져도 다시 놓을 수 있습니다.</p>
          <ul class="ticks">
            <li>탭 한 번으로 성공 또는 실패를 기록하고, 기록되었다는 확인을 받습니다</li>
            <li>치고 싶지 않은 배치는 세션을 멈춰 세우는 대신 건너뛸 수 있습니다</li>
            <li>완전히 같은 배치를 반복해 자기 것이 될 때까지 파고들 수 있습니다</li>
            <li>기록 직후 바로 다음 판을 생성합니다 &mdash; 메뉴 트리가 아니라 하나의 순환입니다</li>
            <li>앱을 닫은 뒤에도 홈 화면에서 마지막으로 생성한 판을 다시 열 수 있습니다</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">훈련 기록</p>
        <h2>당신이 쏟은 노력의 완전한 기록</h2>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>지금까지 친 모든 판</h3><p>날짜와 레벨, 몇 번의 시도에서 런아웃했는지와 함께 전부 훑어볼 수 있습니다.</p></div>
        <div class="card"><h3>즐겨찾기</h3><p>반복할 가치가 있는 배치에 별을 달고 기록을 즐겨찾기만으로 걸러 보며, 나만의 드릴 라이브러리를 쌓아 가세요.</p></div>
        <div class="card"><h3>어디서든 이어서</h3><p>기록에서 아무 판이나 골라 거기서부터 훈련을 이어 가세요. 예전 배치로 돌아가는 데는 탭 한 번이면 됩니다.</p></div>
      </div>
      <p class="dim" style="margin-top:20px">기록이 비어 있으면 빈 화면을 보여 주는 대신 어떻게 채우면 되는지 알려 줍니다.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-progress.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="현재 레이팅, 등급, 누적 지표, 레벨별 상세를 보여 주는 Rank 화면."></div>
        </div>
        <div>
          <p class="eyebrow">지금 나의 위치 &mdash; 언제나 무료</p>
          <h3>&ldquo;나 좀 늘고 있나?&rdquo;에 답하는 숫자들</h3>
          <p>0&ndash;100 레이팅과 등급, 통과한 가장 높은 레벨, 한계 레벨, 그리고 지난 테스트 대비 레이팅
          변화. 그 아래에는 누적 시도 횟수, 총 런아웃 수, 전체 런아웃 성공률과 최고 연속 기록, 그리고 그
          비율을 쉬운 말로 풀어 준 문장 &mdash; &ldquo;N판마다 한 번꼴로 런아웃하고 있습니다&rdquo;.</p>
          <p>같은 화면에서 한계 레벨을 다시 테스트하는 것도 탭 한 번입니다.</p>
          <p><a href="runout-pro.html">Runout Pro가 여기에 더해 주는 것 &rarr;</a></p>
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
      <p class="lead">경계는 하나, 한 문장이면 충분합니다. <strong>지금 어디에 있는지는 무료, 어떻게 여기까지
      왔는지는 Pro.</strong></p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid grid--2">
        <div class="card">
          <p class="eyebrow">영구 무료</p>
          <h3>지금 어디에 있는가</h3>
          <ul class="ticks">
            <li>0&ndash;100 레이팅과 등급</li>
            <li>통과한 레벨과 당신을 막고 있는 레벨</li>
            <li>지난 테스트 대비 레이팅 변화량</li>
            <li>레벨별 상세: 최고 테스트 점수와 최근 연습 성공률</li>
            <li>누적 시도 횟수, 런아웃 수, 런아웃 성공률, 최고 연속 기록</li>
            <li>모든 레벨에서 무제한 레이팅 테스트와 무제한 연습</li>
          </ul>
          <p class="dim">이 중 어느 것도 체험판이 아닙니다. 돈을 내지 않아도 앱은 충분히 쓸모 있습니다.</p>
        </div>
        <div class="card card--gold">
          <p class="eyebrow eyebrow--gold">Runout Pro</p>
          <h3>어떻게 여기까지 왔는가</h3>
          <ul class="ticks ticks--gold">
            <li>지금까지 치른 모든 테스트에 걸친 레이팅 그래프</li>
            <li>레벨별 점수 추이 &mdash; 최고 기록만이 아니라 모든 테스트</li>
            <li>시간에 따른 런아웃 성공률과 세션 기록</li>
            <li>전체 테스트 로그: 회차별 레벨, 점수, 날짜, 레이팅 변화</li>
            <li>전체 기록의 CSV 내보내기</li>
          </ul>
          <p class="dim">월간 또는 연간으로 구독하세요. 지난 기록 전체가 즉시 열립니다 &mdash; 새로 데이터를
          모으는 기간을 기다릴 필요가 없습니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">구독 권유는 이렇게 동작합니다</p>
        <h2>페이지마다 자물쇠가 아니라, 정직한 카드 하나</h2>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>첫날에는 권유하지 않습니다</h3><p>테스트 기록이 전혀 없는 신규 사용자에게는 어떤 판매 문구도 보여 주지 않습니다. 아직 원할지조차 상상할 수 없는 것에 페이월을 세우는 건 그저 소음입니다.</p></div>
        <div class="card"><h3>미리 보는 건 당신 자신의 데이터</h3><p>무언가를 열 만큼 기록이 쌓이면, 일반적인 광고가 아니라 값이 가려진 당신 자신의 성장 곡선을 보게 됩니다.</p></div>
        <div class="card"><h3>경계는 하나, 화면 맨 아래에</h3><p>Rank 화면에는 Pro 카드가 정확히 하나 있습니다. 자물쇠 아이콘을 화면 곳곳에 뿌리면 모든 무료 기능이 견본처럼 느껴지게 됩니다.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>결제, 복원, 해지</h2>
      <ul>
        <li>가격은 App Store 또는 Google Play에서 실시간으로 가져와 표시되고 연간 절약액도 그에 맞춰
        계산되므로, 보이는 금액이 곧 스토어가 당신의 통화로 청구할 금액입니다.</li>
        <li>이미 구매하셨나요? <strong>구매 복원</strong>으로 재설치 후나 두 번째 기기에서도 되살릴 수
        있습니다 &mdash; 다시 설치한다고 두 번 결제되는 일은 없습니다.</li>
        <li>Apple 또는 Google 계정에서 언제든 관리하거나 해지할 수 있습니다. 환불과 결제 문의는 스토어가
        자체 약관에 따라 처리합니다.</li>
        <li>이용약관과 <a href="privacy-policy.html">개인정보 처리방침</a>은 구독한 뒤가 아니라 구독하기
        전에 읽을 수 있습니다.</li>
        <li><strong>Pro는 오프라인에서도 그대로 동작합니다.</strong> 당구장의 약한 신호 때문에 이미 결제한
        기능에서 막히는 일은 없습니다.</li>
      </ul>
      <p>결제는 전적으로 Apple과 Google이 처리합니다. Runout Rank는 당신의 카드 정보를 보지도, 저장하지도
      않습니다.</p>
    </div>
  </section>

{CTA}
"""

GUIDE_TITLE = "내 당구 실력을 측정하는 법 (그리고 믿을 수 있는 숫자를 얻는 법)"
GUIDE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "당구 실력 측정")}
      <h1>내 당구 실력을 측정하는 법</h1>
      <p class="lead">대부분의 사람은 자기가 누구를 이기는지는 말할 수 있습니다. 자기가 얼마나 잘 치는지를
      말할 수 있는 사람은 아주 드뭅니다. 해볼 만한 실력 측정과 그저 마음에 드는 드릴을 가르는 것이
      무엇인지 정리했습니다.</p>
{byline(UI, FIRST_PUBLISHED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>&ldquo;나는 얼마나 잘 치나?&rdquo;가 답하기 어려운 이유</h2>
      <p>경기 결과는 당신을 측정하는 만큼이나 상대를 측정합니다. 약한 상대들을 만난 좋은 밤과 강한 상대들을
      만난 나쁜 밤이 똑같은 스코어를 만들어 낼 수 있습니다. 연습은 효과가 있든 없든 생산적으로 느껴지는데,
      자연히 원래 좋아하던 샷에 시간을 쓰기 때문입니다. 그리고 대부분이 돌리는 드릴은 이미 해 본 드릴입니다
      &mdash; 그게 바로 그것들이 점점 쉬워지는 이유입니다.</p>
      <p>쓸모 있는 실력 측정은 여느 연습이 하지 못하는 세 가지를 해내야 합니다.</p>

      <h2>1. 한 샷이 아니라 능력 전체를 측정해야 합니다</h2>
      <p>먼 직구 하나를 넣는 건 당신의 스트로크 하나에 대해 말해 줍니다. 한 테이블을 다 치우는 건 배치
      읽기, 포지션 플레이, 힘 조절, 수비 판단, 그리고 배짱에 대해, 그것도 테이블이 요구하는 순서대로 말해
      줍니다. 그래서 런아웃 &mdash; 처음부터 끝까지 테이블 전체 &mdash; 이 실력 측정의 올바른 단위이고,
      Runout Rank가 샷이 아니라 판을 채점하는 이유입니다.</p>

      <h2>2. 예측할 수 없어야 합니다</h2>
      <p>고정된 배치 묶음은 결국 기억력 시험으로 변질됩니다. 같은 드릴을 열 번째 놓는 순간 당신이 측정하는
      건 런아웃 능력이 아니라 그 특정 판의 답을 얼마나 잘 기억하는지입니다. 반복할 가치가 있는 측정은
      배치를 스스로 생성해서, 눈앞의 상황이 매번 진짜로 새롭게 만들어야 합니다.</p>

      <h2>3. 난이도는 즉흥이 아니라 정의되어야 합니다</h2>
      <p>여기에 긴장이 있습니다. 무작위성은 측정을 정직하게 만들지만, 동시에 두 점수를 비교 불가능하게
      만들 위험이 있습니다. 당신의 열 판이 제 열 판보다 어려웠다면 우리 점수는 다른 뜻을 갖습니다.</p>
      <p>해법은 <strong>배치가 아니라 제약을 고정하는 것</strong>입니다. 난이도 레벨이 무엇을 뜻하는지
      정확히 정의하고 &mdash; 목적구 몇 개, 프리볼 여부, 공 사이 최소 간격, 방해구 몇 개 &mdash; 그 규칙
      안에서는 자유롭게 생성하는 것이죠. 배치는 매번 새롭고, 배치마다 난이도는 같으며, 충분한 판수를
      연달아 치르면 남은 운은 상쇄됩니다. Runout Rank에서는 그 상수들이
      <a href="levels.html">레벨 페이지</a>에 공개되어 있으며 안드로이드와 iOS에서 동일합니다.</p>
      <p>점수가 어디서나 통하게 되는 건 그래서입니다. 그 점수는 당신이 Level&nbsp;4에서 10판 중 7판을
      쳤다고 말하고, Level&nbsp;4는 모두에게 같은 의미이니까요.</p>

      <h2>점수를 정직하게 만드는 규칙들</h2>
      <ul>
        <li><strong>판마다 한 번의 시도.</strong> 3판 2선승제는 당신의 평소가 아니라 가장 좋은 날을
        측정합니다.</li>
        <li><strong>건너뛰기 없음.</strong> 피하고 싶은 배치야말로 정보를 품고 있는 배치입니다.</li>
        <li><strong>정해진 판수.</strong> 열 판이면 운 나쁜 한 번을 상쇄하기에 충분하고, 실제 테이블에서
        한 자리에 끝낼 만큼 짧습니다.</li>
        <li><strong>명시된 합격선.</strong> Runout Rank에서는 10판 중 7판이면 레벨 통과입니다. 시작 전에
        기준을 아는 것도 측정의 일부입니다.</li>
        <li><strong>즉시 기록.</strong> 한 시간 뒤에 적는 결과는 이미 당신이 미화한 결과입니다.</li>
      </ul>

      <h2>그 숫자로 무엇을 할 것인가</h2>
      <p>레이팅 그 자체는 잡담거리입니다. 숫자는 어딘가를 가리킬 때만 쓸모가 있고, 그래서 측정의 중요한
      결과물은 점수가 아니라 <strong>한계 레벨</strong> &mdash; 아직 통과하지 못하는 그 칸입니다. 연습이
      값어치를 하는 곳이 거기입니다. 배치가 아직 당신이 답하지 못하는 질문을 던지는 유일한 레벨이기
      때문입니다.</p>
      <p>실제 순환은 이렇습니다.</p>
      <ol>
        <li>통과할 수 있을 것 같은 레벨에서 테스트합니다.</li>
        <li>통과하면 한 레벨 위를 테스트하고, 어느 레벨이 당신을 막을 때까지 올라갑니다.</li>
        <li>그 한계 레벨에서 연습하되, 런아웃 성공률이 실제 값이 되도록 시도를 모두 기록합니다.</li>
        <li>성공률이 움직이면 같은 레벨을 다시 테스트합니다. 느낌이 아니라 레이팅을 비교하세요.</li>
      </ol>

      <h2>얼마나 자주 다시 측정할까</h2>
      <p>숫자가 현실을 따라올 만큼은 자주, 그리고 매번의 재측정이 실제 노력을 반영할 만큼은 드물게.
      일주일에 두어 번 테이블에 서는 대부분의 사람에게는 2주에서 4주에 한 번이 적당합니다. 세션마다 다시
      측정하면 대개 잡음을 재는 것이고, 반년에 한 번이면 행동으로 옮길 정보를 아무것도 얻지 못합니다.</p>

      <h2>리그 레이팅이 안정되기를 기다리는 것보다 나은 이유</h2>
      <p>대부분의 사람이 안내받는 대안은 리그 경기로 쌓는 상대 레이팅인데, 그것이 의미를 가지려면 이미
      레이팅을 가진 사람들과의 방대한 전적이 필요합니다 &mdash; 예컨대 FargoRate는 레이팅이 확립되었다고
      보는 최소 기준을 200경기로 둡니다. 런아웃 측정은 한 자리에서 답을 줍니다. 그 방에 있는 사람들이
      아니라 배치를 기준으로 당신을 재기 때문이고, 그래서 지역 판의 강약에 따라 흔들리지도 않습니다.
      더 읽어 보기:</p>
      <ul>
        <li><a href="fargo-rate-alternative.html">200경기의 리그가 필요 없는 Fargo Rate 대안</a></li>
        <li><a href="pool-rating-without-a-league.html">리그에 가입하지 않고 당구 레이팅을 받는 법</a></li>
        <li><a href="absolute-vs-relative-pool-rating.html">절대 레이팅과 상대 당구 레이팅</a></li>
      </ul>

      <div class="note">Runout Rank는 이 모든 것을 당신이 늘 치던 그 테이블 위에서 해냅니다. 배치를
      생성하고, 런아웃을 채점하고, 기록을 당신의 기기에 보관하고, 다음에 훈련할 레벨을 짚어 줍니다.
      <a href="how-it-works.html">테스트가 정확히 어떻게 진행되는지 보기 &rarr;</a></div>
    </div>
  </section>

{CTA}
"""

# --------------------------------------------------------------------------
# Positioning pages: the two pain points a relative league rating leaves open
# --------------------------------------------------------------------------

FARGO_DISCLAIMER = """      <p class="disclaimer">Runout Rank는 독립적인 앱이며 FargoRate와 제휴, 보증, 연관 관계가
      없습니다. 이 페이지에서 Fargo Rate에 대해 말한 내용은 모두
      <a href="https://www.fargorate.com/" rel="nofollow">FargoRate가 직접 공개한 자료</a>에서 가져왔고
      저희가 아는 한 가장 공정하게 서술했습니다. 좋은 시스템이며, 이 페이지는 그 설계가 특정한 유형의
      사용자에게 맞는 지점과 맞지 않는 지점에 관한 이야기일 뿐입니다.</p>"""

FARGO_ALT_TITLE = "200경기의 리그가 필요 없는 Fargo Rate 대안"
FARGO_ALT = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Fargo Rate 대안")}
      <h1>리그 200경기를 결코 치르지 않을 사람들을 위한 Fargo Rate 대안</h1>
      <p class="lead">Fargo Rate는 당구가 가진 최고의 상대 레이팅입니다. 하지만 바로 그 &lsquo;상대적&rsquo;
      이라는 점이 그것을 얻기 더디게 만들고, 사는 곳에 민감하게 만듭니다. 절대 레이팅은 무엇을 다르게 하는지,
      그리고 둘 중 당신에게 정말 필요한 쪽은 어느 것인지 이야기합니다.</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>먼저, 마땅한 인정부터</h2>
      <p>Fargo Rate는 아마추어와 세계 챔피언을 하나의 척도 위에 올려놓았고, 당구의 핸디캡을 평판이 아니라
      숫자로 다툴 수 있는 것으로 만들었습니다. 매주 레이팅을 가진 상대와 리그 경기를 치른다면 그것은 잘
      작동하며, 이 페이지는 그렇지 않은 척하지 않을 겁니다. 계속 쓰세요.</p>
      <p>이 페이지가 다루는 질문은 더 좁습니다. <strong>당신이 그런 사람이 아니라면 어떻게 해야
      할까요?</strong> 혼자 연습하거나, 친구들과 가볍게 치거나, 자주 이동하거나, 또는 그저 한 시즌의 경기에
      등록하지 않고도 자기가 얼마나 잘 치는지 알고 싶을 뿐이라면, 상대 레이팅에는 구조적인 문제가 둘
      있습니다 &mdash; 버그가 아니라 구조입니다.</p>

      <h2>첫 번째 통점: 200경기 전까지 그 숫자는 진짜가 아닙니다</h2>
      <p>FargoRate는 전적의 규모를 <em>robustness(견고성)</em>라 부르며, 견고성 200경기가 레이팅을
      &ldquo;확립되었다&rdquo;고 볼 수 있는 최소 기준이라고 분명히 밝힙니다. 그 아래에서는 공식 레이팅이
      실제 성적과 <em>starter rating(초기 레이팅)</em> &mdash; 즉 최초의 추정치 &mdash; 의 혼합이며,
      200에 가까워질수록 추정치의 영향력이 줄어듭니다.</p>
      <p>보통 사람에게 200경기가 무엇을 요구하는지 따져 보죠. 그 시스템에 성적을 보고하는 리그를 찾고,
      회비를 내고, 매주 같은 저녁을 비우고, 한두 시즌의 대부분을 치러야 한다는 뜻입니다 &mdash; 그래야
      비로소 앱 속 숫자가 가중 평균된 의견이 아니라 당신에 대한 측정이 됩니다. &ldquo;나는 얼마나 잘
      치나?&rdquo;에 대한 정직한 답 하나를 원하는 사람이 그것을 얻으려고 1년치 헌신을 사야 하는 셈입니다.</p>
      <p>그리고 지름길은 없습니다. 지름길로 줄일 것 자체가 없기 때문입니다. 상대 시스템은 이미 아는 사람들을
      상대로 충분한 결과를 만들어 내기 전까지는 당신에 대해 정말로 아무것도 알 수 없습니다.</p>
      <p><a href="pool-rating-without-a-league.html">리그에 가입하지 않고 당구 레이팅을 받는 법 &rarr;</a></p>

      <h2>두 번째 통점: 당신의 레이팅은 당신의 도시를 일부 설명합니다</h2>
      <p>상대 레이팅은 누가 누구를 이겼는지로 계산됩니다. 즉 당신의 숫자는 당신 동네 사람들을 레이팅된 세계의
      나머지와 잇는 경기의 사슬만큼만 단단히 고정됩니다. 그 사슬이 두꺼운 곳 &mdash; 큰 도시, 강한 투어
      씬, 오픈 대회를 찾아다니는 사람들 &mdash; 에서는 레이팅이 잘 맞아떨어집니다. 사슬이 얇은 곳에서는
      한 지역 집단이 다른 곳의 같은 숫자와 맞지 않는 수준에 자리 잡을 수 있습니다.</p>
      <p>이건 외부인의 불평이 아닙니다. FargoRate 자신의 글도, 거의 고립된 두 집단 중 한쪽이 다른 쪽에 비해
      너무 높게 매겨지는 상황을 특히 골치 아픈 문제로 서술합니다 &mdash; 오랜 시간에 걸친 많은 교차 경기로만
      스스로 교정되는 문제라고요. 신뢰할 수 있는 레이팅에 대한 그들의 정의 역시, 레이팅이 확립된 상대와의
      경기에 더 큰 비중이 실린다고 짚습니다.</p>
      <p>그러니 당신의 지역에 강자가 빽빽하거나, 더 넓은 네트워크와 거의 이어져 있지 않거나, 그 시스템에
      이제 막 들어왔다면, 당신이 지니고 다니는 숫자는 당신에 대해서만이 아니라 당신의 주변에 대해서도 무언가를
      말하고 있는 것입니다. 다른 곳으로 옮기면 그 숫자는 고향에서의 의미와 달라질 수 있습니다.</p>
      <p><a href="absolute-vs-relative-pool-rating.html">절대 레이팅과 상대 레이팅 자세히 보기 &rarr;</a></p>

      <h2>절대 레이팅은 대신 무엇을 하는가</h2>
      <p>Runout Rank는 측정에서 상대를 통째로 걷어냅니다. 누구를 이겼는지 묻는 대신, 정의된 배치를 테이블에
      올려놓고 이것을 다 칠 수 있느냐고 묻습니다.</p>
      <p>한 레벨에서 생성된 열 판을 치고, 판마다 단 한 번, 다시 치기도 건너뛰기도 없이, 각 판을 런아웃 또는
      실패로 기록합니다. 열 개의 답이 점수와 0&ndash;100 레이팅, 그리고 Rookie부터 Master까지의 등급이 됩니다.
      10판 중 7판이면 그 레벨 통과입니다. 늘 치던 그 테이블에서 전부 한 시간쯤 걸립니다.</p>
      <p>배치가 곧 잣대이고 그 잣대는 절대 바뀌지 않으므로, 그 방에 누가 있든 숫자의 의미는 같고, 내년에도
      올해와 같습니다. 한 시즌에 걸쳐 쌓는 것이 아니라 첫 세션에 벌어들이는 숫자입니다.</p>

      <h2>나란히 놓고 보기</h2>
      <div class="table-wrap">
        <table>
          <caption class="sr-only">상대 리그 레이팅과 Runout Rank 절대 레이팅의 비교</caption>
          <thead>
            <tr>
              <th scope="col"></th>
              <th scope="col">상대 레이팅 (Fargo Rate 및 유사 시스템)</th>
              <th scope="col">Runout Rank</th>
            </tr>
          </thead>
          <tbody>
            <tr><th scope="row">무엇을 측정하나</th><td>레이팅을 가진 다른 사람들과의 경기 결과</td><td>고정 생성된 배치에 대한 런아웃</td></tr>
            <tr><th scope="row">의미를 갖기까지</th><td>확립된 레이팅까지 200경기, 그 아래에서는 초기 레이팅이 섞임</td><td>열 판 테스트 한 번, 약 한 시간</td></tr>
            <tr><th scope="row">필요한 것</th><td>성적을 보고하는 리그나 공인 대회, 상대, 참가비, 고정된 일정</td><td>당구대 하나와 휴대폰 하나</td></tr>
            <tr><th scope="row">지역 판의 영향</th><td>실재함: 연결성과 상대 풀의 강약이 숫자에 영향을 줌</td><td>없음: 상대가 개입하지 않음</td></tr>
            <tr><th scope="row">이식성</th><td>네트워크 안에서는 통용되나, 느슨하게 연결된 지역은 어긋날 수 있음</td><td>안드로이드와 iOS 어디서나 동일한 레벨 제약</td></tr>
            <tr><th scope="row">이럴 때 좋음</th><td>경기 핸디캡, 대회 대진, 리그 참가 자격</td><td>내 수준과 다음에 무엇을 연습할지 파악</td></tr>
            <tr><th scope="row">이럴 땐 부적합</th><td>첫날에 &ldquo;나는 얼마나 잘 치나?&rdquo;에 답하기</td><td>다른 사람과의 경기에 핸디를 매기기 &mdash; 핸디캡 시스템이 아님</td></tr>
            <tr><th scope="row">비용과 계정</th><td>리그 회원 자격, 온라인 프로필</td><td>무료 앱, 계정 없음, 완전한 오프라인 동작</td></tr>
          </tbody>
        </table>
      </div>

      <h2>Runout Rank가 아닌 것을 분명히 해 둡니다</h2>
      <p>핸디캡 용도로 리그 레이팅을 대체하지 않고, 대회 시드를 받게 해 주지도 않습니다. 어떤 협회도 이를
      공인하지 않습니다. 자신의 변수에 대해서도 솔직합니다. 당신은 자기 장비로 치고 있으므로, 포켓이 좁고
      천이 느린 테이블은 바 박스와 다르게 읽힐 것입니다. 실제로 경기하는 그 테이블에서 테스트하고, 같은
      조건끼리 시간에 따라 비교하세요.</p>
      <p>이것이 주는 것은 상대 시스템이 값싸게 줄 수 없는 것입니다. 오늘 당장, 당신 자신의 플레이에서 나온,
      다른 누구에게도 기대지 않는 진짜 숫자 말입니다.</p>

      <h2>당연한 답: 둘 다 쓰세요</h2>
      <p>둘은 서로 다른 것을 측정하며 충돌하지 않습니다. 리그를 뛴다면 경기용으로는 Fargo Rate를 유지하고,
      그 사이사이에 Runout Rank로 자기 게임의 어느 부분이 뒤처졌는지 확인하세요 &mdash; 런아웃 측정은
      당신을 막는 레벨을 짚어 주고 그 레벨의 연습을 바로 건네주는데, 경기 결과 기반 레이팅은 그럴 수
      없습니다. 리그를 뛰지 않는다면, Runout Rank가 당신이 실제로 가질 수 있는 숫자입니다.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="how-it-works.html">테스트가 어떻게 진행되는지 보기</a>
        <a class="btn btn--ghost" href="pool-rating-without-a-league.html">리그 없이 레이팅 받기</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

NO_LEAGUE_TITLE = "리그에 가입하지 않고 당구 레이팅을 받는 법"
NO_LEAGUE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "리그 없이 받는 레이팅")}
      <h1>리그에 가입하지 않고 당구 레이팅을 받는 법</h1>
      <p class="lead">자리 잡은 레이팅 시스템은 모두 같은 입장료를 요구합니다. 레이팅을 가진 상대와의 수백
      경기 말이죠. 그게 당신의 삶이 아니라면, 당신이 레이팅 불가능한 게 아닙니다 &mdash; 그 방에 있는
      사람들이 아니라 테이블을 재는 레이팅이 필요할 뿐입니다.</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>가볍게 치는 사람들이 결국 숫자 하나 없이 남는 이유</h2>
      <p>흔한 조언은 이렇습니다. 레이팅 시스템에 성적을 보고하는 리그에 들어가 한 시즌을 뛰면 레이팅이
      안정된다고요. 타당한 조언이고, 많은 사람에게는 동시에 불가능한 조언입니다. 매주 고정된 저녁, 회비,
      보고제 리그를 운영하는 장소, 그리고 그들 자신도 레이팅을 가진 충분한 수의 상대를 요구하니까요.</p>
      <p>그다음은 물량 문제입니다. FargoRate는 레이팅을 확립되었다고 부르기 위한 최소 견고성을 200경기로
      둡니다. 그 아래에서 당신이 보는 것의 일부는 당신이 해낸 것이 아니라 시스템이 배정한 초기 레이팅입니다.
      200번의 공인 경기는 대부분의 리그 선수에게 한 시즌 이상이고, 나머지 모두에게는 공상입니다.</p>
      <p>그러니 가볍게 치는 사람에게 정직한 결론은 이렇습니다. 상대 레이팅을 벌어들이는 수고가 그것을 아는
      가치보다 큽니다. 대부분은 조용히 포기하고, 동네에서 누구를 이기는지로 짐작하던 자리로 돌아갑니다.</p>

      <h2>당신이 정말로 알아내려는 것</h2>
      <p>시스템을 걷어내고 나면 그 밑에는 대개 세 가지 질문이 있습니다.</p>
      <ul>
        <li><strong>나는 어디쯤인가?</strong> 나는 괜찮은 동호인인가, 생각보다 잘 치는가, 아니면 더 못
        치는가?</li>
        <li><strong>나는 늘고 있는가?</strong> &ldquo;오늘 밤 느낌이 좋았다&rdquo;가 아니라 &mdash; 곡선이
        움직이고 있는가?</li>
        <li><strong>무엇을 연습해야 하는가?</strong> 실제로 나머지를 붙잡고 있는 건 게임의 어느 부분인가?</li>
      </ul>
      <p>이 세 질문 중 어느 것도 상대를 필요로 하지 않습니다. 필요한 건 실패할 만큼 어려운, 고정되고 반복
      가능한 과제와, 그것을 얼마나 자주 완수하는지에 대한 기록입니다.</p>

      <h2>그에 답하는 측정</h2>
      <p>런아웃이 올바른 단위입니다. 테이블을 치우는 일은 배치 읽기, 포지션, 힘 조절, 배짱을 테이블이
      요구하는 순서대로 쓰게 하는데, 단순한 포팅 드릴은 그러지 못합니다. 이것을 한 난이도 레벨에서 열 판,
      판마다 한 번, 다시 치기와 건너뛰기 없이로 만들면, 연습이 아니라 측정을 갖게 됩니다.</p>
      <p>Runout Rank가 하는 일이 바로 그것입니다. 앱이 각 배치를 위에서 내려다본 그림으로 그려 주면, 당신은
      자기 테이블에 그대로 놓고 한 번 친 뒤 런아웃 또는 실패를 탭합니다. 끝나면 10점 만점의 점수,
      0&ndash;100 레이팅, Rookie부터 Master까지의 등급, 그 레벨의 통과 여부, 그리고 지금 당신을 막고 있는
      레벨을 받습니다. 한 시간쯤 걸리고, 건물 안에 다른 사람이 있을 필요가 없습니다.</p>
      <p>배치는 테스트마다 새로 생성되므로 외울 것이 없고, 레벨의 제약 &mdash; 공의 개수, 프리볼, 간격,
      방해구 &mdash; 은 안드로이드와 iOS의 모든 사용자에게 같은 고정 상수입니다. 매번 새로운 판, 매번 같은
      난이도.</p>

      <h2>혼자 치는 사람을 위한 실전 루틴</h2>
      <ol>
        <li><strong>통과할 수 있을 것 같은 레벨에서 테스트하세요.</strong> 잠긴 레벨은 없으니, 맨 아래가
        아니라 자신이 있어야 할 것 같은 곳에서 시작하면 됩니다.</li>
        <li><strong>어느 레벨이 당신을 막을 때까지 올라가세요.</strong> 10판 중 7판이면 통과이고, 일곱 판을
        못 채우는 순간 당신의 한계를 찾은 것입니다.</li>
        <li><strong>그 한계 레벨에서 연습하되,</strong> 런아웃 성공률이 인상이 아니라 사실이 되도록 모든
        시도를 기록하세요.</li>
        <li><strong>성공률이 움직이면 그 레벨을 다시 테스트하세요.</strong> 2주에서 4주에 한 번이 대부분의
        사람에게 맞습니다 &mdash; 실제 노력을 따라갈 만큼 자주, 잡음을 재지 않을 만큼 드물게.</li>
        <li><strong>느낌이 아니라 레이팅을 비교하세요.</strong> 결과 화면의 레이팅 변화량이 이 모든 것의
        핵심입니다.</li>
      </ol>

      <h2>비용은 얼마인가</h2>
      <p>한 시간, 예약할 수 있는 테이블 하나, 그 외에는 없습니다. 앱은 무료로 받을 수 있고, 만들 계정도
      없으며, 완전히 오프라인으로 동작하고, 기록은 당신 기기의 앱 전용 저장소에 남습니다. Runout Pro는
      선택 사항이며 기록을 더해 줍니다. 모든 테스트에 걸친 레이팅 그래프, 레벨별 추이, CSV 내보내기 말이죠.
      지금 어디에 있는지는 영구 무료입니다.</p>

      <h2>리그를 뛴다면</h2>
      <p>그렇다면 리그 레이팅은 그대로 두세요 &mdash; 경기 핸디캡에는 그것이 올바른 도구이고, 이 글은 그
      대체품이 아닙니다. 런아웃 측정을 그 옆에 함께 쓰세요. 경기 결과 기반 레이팅은 당신이 어느 수준인지는
      알려 주지만 게임의 어느 부분이 뒤처졌는지는 알려 주지 않으니까요.
      <a href="fargo-rate-alternative.html">Fargo Rate와의 전체 비교</a>를 보세요.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="how-it-works.html">테스트 진행 방식</a>
        <a class="btn btn--ghost" href="levels.html">여섯 레벨 보기</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

ABSOLUTE_TITLE = "절대 레이팅과 상대 당구 레이팅: 사는 도시가 당신의 숫자를 바꾸는 이유"
ABSOLUTE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "절대 레이팅과 상대 레이팅")}
      <h1>절대 레이팅과 상대 당구 레이팅</h1>
      <p class="lead">실력이 똑같은 두 사람이, 한 명은 강한 도시에 한 명은 조용한 도시에 있다는 이유로 몇
      년씩 다른 상대 레이팅을 지니고 다닐 수 있습니다. 그건 계산의 결함이 아니라 &mdash;
      &lsquo;상대적&rsquo;이라는 말의 뜻 그대로입니다. 그 차이가 무엇이고 각각의 레이팅이 무엇에 좋은지
      정리했습니다.</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>상대 레이팅이란 무엇인가</h2>
      <p>상대 레이팅 &mdash; Elo, Glicko, Fargo Rate와 그 일가 &mdash; 에는 절대 기준이라는 개념이
      없습니다. 그것이 아는 것은 결과뿐입니다. 당신이 그들을 이겼고, 그들은 또 누군가를 이겼다는 식이죠.
      그런 결과가 충분히 큰 그물을 이루면, 시스템은 그 승패를 가장 잘 설명하는 숫자들의 조합을 찾아냅니다.
      누구도 직접 측정되지 않습니다. 모든 레이팅은 다른 레이팅들로 이루어진 네트워크 속의 한 위치입니다.</p>
      <p>우아한 설계이고 네트워크가 촘촘할 때는 놀라울 만큼 잘 작동합니다. 동시에 아무리 영리한 수학으로도
      없앨 수 없는 두 가지 결과를 함께 가져옵니다.</p>

      <h2>결과 하나: 많은 경기가 필요합니다</h2>
      <p>결과 하나는 증거 1비트이고, 1비트는 매우 적습니다. 그래서 시스템은 당신을 운에서 떼어내기 위해
      물량을 필요로 합니다 &mdash; FargoRate가 견고성 지표를 쓰고 레이팅을 확립되었다고 부르는 최소 기준을
      200경기로 두며, 그때까지는 초기 레이팅을 숫자에 섞는 이유가 이것입니다. 그 값을 경기로 치르기
      전까지, 당신의 레이팅은 일부는 당신에 대한 추측입니다.</p>

      <h2>결과 둘: 이웃에 묶여 있습니다</h2>
      <p>모든 레이팅이 다른 레이팅에 견주어 정의되므로, 한 무리의 사람들은 그들을 세계와 잇는 경기가 충분할
      때에만 나머지와 올바르게 정렬됩니다. 그 연결이 얇은 곳 &mdash; 고립된 지역, 신생 리그, 오픈 대회에
      거의 나가지 않는 씬 &mdash; 에서는 집단 전체가 다른 곳의 같은 숫자와 맞지 않는 수준에 자리 잡을 수
      있습니다. FargoRate는 정확히 이 경우, 즉 거의 고립된 두 집단 중 한쪽이 다른 쪽에 비해 너무 높게
      매겨진 상황을 골치 아픈 문제로 서술하고, 바로 그 이유로 레이팅이 확립된 상대와의 경기가 더 큰 값을
      갖는다고 짚습니다.</p>
      <p>사용자 입장의 실용적 번역은 이렇습니다. 당신의 도시에 강자가 가득하거나 더 넓은 레이팅 인구와
      거의 이어져 있지 않다면, 당신의 숫자는 일부 당신의 주변에 대한 진술입니다. 서로 다른 씬에 있는 같은
      수준의 두 사람이 같은 값으로 읽힐 이유가 없고, 둘 다 외부 사람들과 더 많이 치는 것 말고는 달리 할
      수 있는 일이 없습니다.</p>

      <h2>절대 레이팅이란 무엇인가</h2>
      <p>절대 레이팅은 사람이 아니라 고정된 기준에 견주어 수행을 측정합니다. 골프 핸디캡은 파를 기준으로 그렇게
      작동합니다. 육상은 시계를 기준으로 그렇게 작동합니다. 스톱워치는 트랙에 누가 더 있는지 상관하지 않고,
      마닐라의 10.4초는 맨체스터의 10.4초입니다.</p>
      <p>당구에는 전통적으로 그런 것이 없었습니다. 명백한 시계가 없기 때문이죠. Runout Rank가 그 등가물을
      제공합니다. 정의된 배치 한 세트와 하나의 질문 &mdash; 이걸 다 칠 수 있습니까? 한 레벨에서 열 판,
      판마다 한 번, 다시 치기와 건너뛰기 없이. 거기서 나오는 숫자는 전적으로 그 배치들에 대한 당신 자신의
      결과로 계산됩니다.</p>
      <p>그러니 강하거나 약할 상대 풀도 없고, 어긋나 흘러갈 대상도 없으며, 측정이 유효해지기까지 필요한
      최소 경기 수도 없습니다. 첫 세션이 끝나면 레이팅이 손에 있고, 그것은 어디서나 같은 의미입니다.</p>

      <h2>고정된 기준이 기억력 시험이 되지 않는 이유</h2>
      <p>당연한 반론이 있습니다. 고정된 배치 묶음은 몇 번 쳐 보고 나면 실력을 측정하기를 멈춘다는 것이죠.
      그때부터는 해법을 찾는 게 아니라 떠올리는 것이니까요.</p>
      <p>Runout Rank는 판이 아니라 <em>난이도</em>를 고정하는 방식으로 그것을 피합니다. 레벨은 공개된
      상수들의 묶음이고 &mdash; 목적구 개수, 프리볼 여부, 최소 간격, 방해구 &mdash; 배치는 매번 그 규칙
      안에서 새로 생성됩니다. 같은 판을 두 번 보는 일은 없고, 모든 판이 같은 질문을 던집니다. 열 판을 연달아
      치면 남은 운은 상쇄됩니다.</p>

      <h2>절대 레이팅이 할 수 없는 것</h2>
      <p>그것은 핸디캡 시스템이 아니며 그렇게 써서도 안 됩니다. 상대 레이팅은 특정한 두 사람 사이의 경기를
      예측하기 위해 존재하고, 그 일에 있어서는 어떤 절대적 측정보다도 훨씬 낫습니다 &mdash; 경기 결과가
      바로 그것을 이루는 재료이기 때문입니다.</p>
      <p>절대 레이팅에도 정직하게 다뤄야 할 자기만의 변수가 있습니다. 장비 말입니다. 포켓을 깎은 형태,
      테이블 크기, 천의 빠르기가 모두 런아웃의 난이도를 바꾸므로, 포켓이 좁은 9피트 테이블에서 받은 레이팅은
      바 박스에서 받은 것과 다른 측정입니다. 조건을 고정하고, 실제로 경기하는 테이블에서 테스트하고, 자신의
      숫자를 시간에 따라 비교하세요.</p>

      <h2>당신에게 필요한 쪽은?</h2>
      <div class="compare" style="margin:24px 0">
        <div class="card">
          <h3>이럴 때 상대 레이팅을</h3>
          <ul class="ticks">
            <li>경기나 대진을 위한 핸디캡이 필요할 때</li>
            <li>리그나 대회가 그것을 요구할 때</li>
            <li>이미 견고성을 유지할 만큼 공인 경기를 충분히 치르고 있을 때</li>
          </ul>
        </div>
        <div class="card card--gold">
          <h3>이럴 때 절대 레이팅을</h3>
          <ul class="ticks ticks--gold">
            <li>한 시즌을 먼저 치르지 않고 지금 내 위치를 알고 싶을 때</li>
            <li>혼자 연습하거나, 자주 이동하거나, 씬을 옮겨 다닐 때</li>
            <li>순위만이 아니라 <em>무엇을 연습할지</em>를 알고 싶을 때</li>
          </ul>
        </div>
      </div>
      <p>둘은 서로 다른 질문에 답하며, 진지한 사람이라면 둘 다 지니고 다녀도 전혀 이상하지 않습니다.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="fargo-rate-alternative.html">Fargo Rate와 비교</a>
        <a class="btn btn--ghost" href="how-it-works.html">레이팅 계산 방식</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

FAQ_ITEMS = [
    ("Runout Rank를 쓰려면 실제 당구대가 필요한가요?",
     "필요합니다. Runout Rank는 당구 게임이 아니라 &mdash; 실제 테이블의 동반자입니다. 앱이 각 배치를 위에서 "
     "내려다본 그림으로 그려 주면, 눈앞의 천 위에 그대로 놓고 쳐 본 뒤 결과를 기록하면 됩니다."),
    ("계정이나 인터넷 연결이 필요한가요?",
     "둘 다 필요 없습니다. 가입할 것도 로그인할 것도 없고, 앱은 완전히 오프라인으로 동작합니다. 테스트, 시도, "
     "즐겨찾기, 통계는 오직 사용자 기기의 앱 전용 저장소에만 남습니다."),
    ("레이팅은 어떻게 계산되나요?",
     "한 레벨에서 생성된 열 판을 판마다 한 번씩 칩니다. 10점 만점의 점수가 0&ndash;100 레이팅과 등급 명칭으로 "
     "환산되며, 10판 중 7판이면 그 레벨을 통과합니다. 결과에는 지난 테스트 이후 레이팅이 얼마나 움직였는지도 "
     "함께 표시됩니다."),
    ("테스트가 무작위라면 두 점수를 어떻게 비교하나요?",
     "고정된 것은 판이 아니라 레벨이기 때문입니다. 각 레벨은 목적구 개수, 프리볼 여부, 공 사이 최소 간격, "
     "방해구 수를 정의하며, 그 상수들은 두 플랫폼의 모든 사용자에게 동일합니다. 배치는 그 규칙 안에서 새로 "
     "생성되고, 열 판을 연달아 치면 운이 상쇄됩니다 &mdash; 그래서 Level 4에서의 10판 중 7판은 누가 해내든 "
     "같은 의미입니다."),
    ("잘못 친 판을 다시 칠 수 있나요?",
     "레이팅 테스트 중에는 안 됩니다 &mdash; 판마다 한 번, 다시 치기도 건너뛰기도 없으며, 바로 그 점이 점수에 "
     "의미를 부여합니다. 자유 연습에서는 같은 배치를 원하는 만큼 반복해서 칠 수 있습니다."),
    ("테스트 도중에 방해를 받으면 어떻게 되나요?",
     "테스트는 멈췄던 바로 그 판에서 이어집니다. 일부러 그만두려 하면 먼저 확인을 요청하고, 끝내지 못한 회차는 "
     "채점할 수 없다는 점을 설명해 줍니다."),
    ("Level 1부터 시작해야 하나요?",
     "아닙니다. 잠긴 것은 없습니다. 여섯 레벨 중 어디서든 레이팅 테스트를 치를 수 있고, 이미 테스트한 레벨도 "
     "다시 치를 수 있습니다."),
    ("&ldquo;한계 레벨&rdquo;이 무엇인가요?",
     "지금 당신을 막고 있는 레벨 &mdash; 아직 통과하지 못하는 가장 높은 레벨입니다. 연습할 가치가 있는 레벨이며, "
     "결과 화면과 Rank 화면 모두에서 바로 그곳으로 건너뛸 수 있습니다."),
    ("Runout Pro는 얼마이고 무엇이 추가되나요?",
     "Runout Pro는 선택 사항인 월간 또는 연간 구독이며, 가격은 스토어가 사용자의 통화로 책정합니다. 추가되는 "
     "것은 기록입니다. 모든 테스트에 걸친 레이팅 그래프, 레벨별 점수 추이, 시간에 따른 런아웃 성공률, 전체 "
     "테스트 로그, 그리고 CSV 내보내기. 지금 어디에 있는지를 알려 주는 것들은 모두 무료로 남습니다."),
    ("앱을 업데이트해도 기록이 안전한가요?",
     "안전합니다. 기존 테스트, 시도, 즐겨찾기는 앱 업데이트 사이에 그대로 보존됩니다. 데이터가 기기에 있으므로 "
     "앱을 삭제하거나 앱 데이터를 지우면 함께 사라집니다."),
    ("Fargo Rate와 무엇이 다른가요?",
     "Fargo Rate는 상대 레이팅입니다. 레이팅을 가진 다른 사람들과의 결과로 숫자를 산출하며, 그래서 FargoRate가 "
     "확립된 레이팅의 최소 견고성을 200경기로 두고, 느슨하게 연결된 지역 판이 네트워크의 나머지와 어긋날 수 있는 "
     "것입니다. Runout Rank는 절대적입니다 &mdash; 고정 생성된 배치를 기준으로 측정하므로 열 판 한 세션이면 "
     "완전한 레이팅이 나오고, 어떤 상대 풀도 여기에 영향을 주지 않습니다. 핸디캡 시스템이 아니며, 경기 핸디캡 "
     "용도로 리그 레이팅을 대체하지 않습니다."),
    ("Runout Rank 레이팅이 의미를 가지려면 몇 경기가 필요한가요?",
     "열 판 &mdash; 테스트 한 번, 약 한 시간입니다. 자격 기간도 잠정 단계도 없습니다. 이 레이팅은 다른 사람들과의 "
     "전적이 아니라, 정의된 배치에 대한 당신의 런아웃으로 계산되기 때문입니다."),
    ("사는 곳이 레이팅에 영향을 주나요?",
     "주지 않습니다. 모든 레벨의 제약은 어디서나 동일한 상수이고, 계산에 상대가 개입하지 않습니다. 유일한 지역 "
     "변수는 장비입니다. 포켓을 깎은 형태, 테이블 크기, 천의 빠르기가 런아웃의 난이도를 바꾸므로, 실제로 치는 "
     "그 테이블에서 테스트하고 자신의 숫자를 시간에 따라 비교하세요."),
    ("Runout Rank와 리그 레이팅을 함께 쓸 수 있나요?",
     "가능하고, 리그를 뛴다면 그게 현명한 방법입니다. 경기 핸디캡에는 리그 레이팅을 그대로 쓰고, 런아웃 측정은 "
     "어느 레벨이 당신을 막고 있는지 찾아 거기서 연습하는 데 쓰세요 &mdash; 경기 결과 기반 레이팅이 알려 줄 수 "
     "없는 부분입니다."),
    ("Runout Rank는 안드로이드와 iOS에서 동일한가요?",
     "동일합니다. 레벨 정의, 생성기, 레이팅 계산은 두 플랫폼에서 함께 돌아가는 공유 코드이므로, 어떤 휴대폰을 "
     "쓰든 레이팅에는 아무 영향이 없습니다."),
]

FAQ_BODY_ITEMS = faq_body(FAQ_ITEMS)
FAQ_SCHEMA = faq_schema(FAQ_ITEMS)

FAQ = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "자주 묻는 질문")}
      <h1>자주 묻는 질문</h1>
      <p class="lead">테스트, 레이팅, 레벨, 구독, 그리고 사용자의 데이터.</p>
    </div>
  </section>

  <section>
    <div class="container" style="max-width:52rem">
{FAQ_BODY_ITEMS}
      <p style="margin-top:28px">그 숫자가 어떻게 만들어지는지 아직 헷갈리시나요?
      <a href="how-it-works.html">레이팅의 원리 읽기 &rarr;</a></p>
    </div>
  </section>

{CTA}
"""

NOT_FOUND = """  <section class="page-head">
    <div class="container">
      <h1>그 판은 아직 놓이지 않았습니다</h1>
      <p class="lead">찾으시는 페이지는 존재하지 않습니다. 돌아가는 길은 여기입니다.</p>
      <div class="btn-row" style="margin-bottom:40px">
        <a class="btn btn--primary" href="index.html">홈으로 돌아가기</a>
        <a class="btn btn--ghost" href="how-it-works.html">테스트 진행 방식</a>
      </div>
    </div>
  </section>
"""


PAGES = [
    dict(slug="index.html",
         title="Runout Rank — 안드로이드와 iOS를 위한 절대 당구 실력 측정",
         description="200경기의 리그가 아니라 한 세션으로 진짜 당구 레이팅을 받으세요. Runout Rank는 주변 "
                     "상대가 아니라 생성된 열 개의 배치를 기준으로 측정하므로, 0–100 숫자가 어느 도시에서나 "
                     "같은 의미를 갖습니다. 리그도 계정도 필요 없고 오프라인으로 동작합니다.",
         body=INDEX,
         schema=[app_schema(LOCALE, UI), site_schema(LOCALE, UI)],
         keywords="절대 당구 레이팅, Fargo Rate 대안, 당구 실력 측정, 당구 레이팅 앱, 리그 없는 당구 레이팅, "
                  "런아웃 테스트, 당구 훈련 앱, 포켓볼 실력 측정"),

    dict(slug="how-it-works.html",
         title="Runout Rank 레이팅의 원리 — 열 판, 판마다 한 번",
         description="한 레벨에서 무작위로 생성된 열 판을 판마다 한 번씩 쳐서 0–100 절대 당구 레이팅과 등급으로 "
                     "환산합니다. 테스트마다 새로운 배치, 고정된 레벨 제약 덕분에 그 숫자는 어느 도시에서나 같은 "
                     "의미를 갖습니다.",
         body=HOW,
         schema=[breadcrumb_schema(LOCALE, UI, "측정 방식", "how-it-works.html")]),

    dict(slug="levels.html",
         title="여섯 개의 레벨 — Rookie부터 Master까지 | Runout Rank",
         description="Rookie, Regular, League, Competitor, Advanced, Master. 사다리의 각 칸에서 무엇이 "
                     "바뀌는지 — 공의 개수, 프리볼, 밀집도, 방해구 — 그리고 왜 어느 칸도 잠겨 있지 않은지.",
         body=LEVELS,
         schema=[breadcrumb_schema(LOCALE, UI, "레벨", "levels.html")]),

    dict(slug="practice.html",
         title="당구 연습과 기억하는 훈련 기록 | Runout Rank",
         description="원하는 레벨에서 무한히 무작위 생성되는 연습 배치, 탭 한 번의 기록, 다시 치기와 건너뛰기, "
                     "즐겨찾기, 그리고 지금까지 친 모든 판의 완전한 훈련 기록.",
         body=PRACTICE,
         schema=[breadcrumb_schema(LOCALE, UI, "연습", "practice.html")]),

    dict(slug="fargo-rate-alternative.html",
         dated=True,
         title=FARGO_ALT_TITLE + " | Runout Rank",
         description="Fargo Rate는 레이팅이 확립되기까지 200경기가 필요하고, 상대 레이팅은 주변 사람들에게 묶여 "
                     "있습니다. Runout Rank는 열 판 한 세션으로 나오는 절대 당구 레이팅입니다 — 두 방식을 "
                     "공정하게 나란히 비교합니다.",
         body=FARGO_ALT,
         schema=[article_schema(LOCALE, UI,
             FARGO_ALT_TITLE,
             "상대 리그 레이팅이 확립되기까지 200경기가 걸리고 지역 상대 풀에 따라 흔들리는 이유, 절대 런아웃 "
             "레이팅은 대신 무엇을 하는지, 그리고 둘 중 어느 것이 필요한지.",
             "fargo-rate-alternative.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "Fargo Rate 대안", "fargo-rate-alternative.html")],
         published=UPDATED,
         keywords="Fargo Rate 대안, 파고 레이팅 대안, 당구 레이팅 앱, 절대 당구 레이팅, "
                  "Fargo Rate 200경기, 확립된 파고 레이팅, Fargo Rate 정확도"),

    dict(slug="pool-rating-without-a-league.html",
         dated=True,
         title=NO_LEAGUE_TITLE + " | Runout Rank",
         description="모든 리그 레이팅은 숫자가 진짜가 되기 전에 레이팅을 가진 상대와의 수백 경기를 요구합니다. "
                     "가볍게 치거나 혼자 치는 사람이 자기 테이블에서 한 세션 만에 정직한 0–100 당구 레이팅을 "
                     "받는 방법입니다.",
         body=NO_LEAGUE,
         schema=[article_schema(LOCALE, UI,
             NO_LEAGUE_TITLE,
             "가볍게 치거나 혼자 치는 사람이 리그에 가입하거나 200번의 공인 경기를 치르지 않고도 한 세션 만에 "
             "정직한 당구 레이팅을 받는 방법.",
             "pool-rating-without-a-league.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "리그 없이 받는 레이팅", "pool-rating-without-a-league.html")],
         published=UPDATED,
         keywords="리그 없는 당구 레이팅, 당구 레이팅 받는 법, 동호인 당구 레이팅, 혼자 하는 당구 연습 레이팅, "
                  "당구 실력 등급, 포켓볼 실력 평가"),

    dict(slug="absolute-vs-relative-pool-rating.html",
         dated=True,
         title=ABSOLUTE_TITLE + " | Runout Rank",
         description="Elo, Glicko, Fargo Rate는 모두 상대적입니다. 각 레이팅이 다른 레이팅들로 이루어진 네트워크 "
                     "속 한 위치이므로 경기 수와 지역 연결성이 모두 영향을 줍니다. 절대 당구 레이팅은 대신 무엇을 "
                     "측정하고, 각각은 무엇에 좋은지 살펴봅니다.",
         body=ABSOLUTE,
         schema=[article_schema(LOCALE, UI,
             ABSOLUTE_TITLE,
             "상대 당구 레이팅이 주변 사람들에게 좌우되는 이유, 절대 레이팅은 대신 무엇을 측정하는지, 그리고 어느 "
             "쪽이 어떤 질문에 답하는지.",
             "absolute-vs-relative-pool-rating.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "절대 레이팅과 상대 레이팅", "absolute-vs-relative-pool-rating.html")],
         published=UPDATED,
         keywords="절대 레이팅과 상대 당구 레이팅, 상대 레이팅 시스템, 당구 Elo 레이팅, "
                  "지역별 파고 레이팅 차이, 당구 레이팅 설명"),

    dict(slug="runout-pro.html",
         title="Runout Pro — 전체 레이팅 기록과 CSV 내보내기 | Runout Rank",
         description="지금 어디에 있는지는 영구 무료입니다. Runout Pro는 어떻게 여기까지 왔는지를 더해 줍니다. "
                     "모든 테스트에 걸친 레이팅 그래프, 레벨별 추이, 전체 테스트 로그, CSV 내보내기까지.",
         body=PRO,
         schema=[breadcrumb_schema(LOCALE, UI, "Runout Pro", "runout-pro.html")]),

    dict(slug="pool-skill-level-test.html",
         dated=True,
         title=GUIDE_TITLE,
         description="해볼 만한 당구 실력 측정과 그저 마음에 드는 드릴을 가르는 것: 완전한 런아웃, 예측할 수 없는 "
                     "배치, 정의된 난이도, 판마다 한 번의 시도, 그리고 그 숫자로 무엇을 할 것인가.",
         body=GUIDE,
         schema=[article_schema(LOCALE, UI,
             GUIDE_TITLE,
             "해볼 만한 당구 실력 측정과 그저 마음에 드는 드릴을 가르는 것은 무엇인가.",
             "pool-skill-level-test.html", FIRST_PUBLISHED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "당구 실력 측정", "pool-skill-level-test.html")],
         keywords="당구 실력 측정 방법, 당구 실력 테스트, 포켓볼 실력 평가, 런아웃 드릴, 당구 레이팅 시스템"),

    dict(slug="faq.html",
         title="Runout Rank 자주 묻는 질문 — 테스트, 레이팅, 레벨, 그리고 데이터",
         description="실제 당구대가 필요한가요? 리그는요? 레이팅은 어떻게 계산되고 Fargo Rate와 무엇이 다르며 "
                     "Runout Pro는 무엇을 더해 주나요? 자주 나오는 질문에 답합니다.",
         body=FAQ,
         schema=[FAQ_SCHEMA, breadcrumb_schema(LOCALE, UI, "자주 묻는 질문", "faq.html")]),
]
