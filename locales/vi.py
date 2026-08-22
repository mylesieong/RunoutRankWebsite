"""Tiếng Việt copy for the Runout Rank site.

Mirrors locales/en.py exactly: same names, same page order, same markup —
only the strings differ. See locales/en.py for the contract.
"""

from common import (
    FIRST_PUBLISHED, PLAY_URL, UPDATED,
    app_schema, article_schema, breadcrumb, breadcrumb_schema, byline,
    faq_body, faq_schema, locale_by_code, site_schema, store_block,
)

LOCALE = locale_by_code("vi")

UI = dict(
    tagline="Ứng dụng kiểm tra và luyện tập trình độ bi-a tuyệt đối cho Android và iOS",
    author_title="Người tạo ra Runout Rank",

    # --- chrome ---------------------------------------------------------
    skip_link="Bỏ qua, vào nội dung chính",
    nav_aria="Điều hướng chính",
    lang_aria="Ngôn ngữ",
    lang_current="Ngôn ngữ",
    breadcrumb_label="Đường dẫn phân cấp",
    nav_home="Trang chủ",
    nav=[
        ("index.html", "Trang chủ"),
        ("how-it-works.html", "Cách hoạt động"),
        ("levels.html", "Các cấp độ"),
        ("practice.html", "Luyện tập"),
        ("fargo-rate-alternative.html", "So với Fargo Rate"),
        ("runout-pro.html", "Runout Pro"),
        ("faq.html", "Hỏi đáp"),
    ],

    # --- byline ---------------------------------------------------------
    byline_by="Tác giả:",
    byline_sep=",",
    byline_published="Đăng ngày",
    byline_updated="Cập nhật",
    date_format="{d} {month} {y}",
    months=["tháng 1", "tháng 2", "tháng 3", "tháng 4", "tháng 5", "tháng 6",
            "tháng 7", "tháng 8", "tháng 9", "tháng 10", "tháng 11", "tháng 12"],

    # --- store badges ---------------------------------------------------
    store_get_it_on="Tải trên",
    store_in_review="Đang duyệt",
    store_review_aria="Đang chờ duyệt trên App Store",

    # --- footer ---------------------------------------------------------
    footer_blurb="Một chỉ số bi-a tuyệt đối, có được từ bài kiểm tra dọn bàn mười ván ngay trên bàn của bạn. "
                 "Một con số 0&ndash;100 chỉ trong một buổi &mdash; không cần giải đấu, không phải chờ 200 ván, "
                 "không cần tài khoản, không cần Internet.",
    footer_col_app="Ứng dụng",
    footer_col_guides="Bài hướng dẫn",
    footer_links_app=[
        ("how-it-works.html", "Cách hoạt động"),
        ("levels.html", "Sáu cấp độ"),
        ("practice.html", "Luyện tập &amp; nhật ký"),
        ("runout-pro.html", "Runout Pro"),
    ],
    footer_links_guides=[
        ("fargo-rate-alternative.html", "Giải pháp thay thế Fargo Rate"),
        ("pool-rating-without-a-league.html", "Có chỉ số mà không cần giải đấu"),
        ("absolute-vs-relative-pool-rating.html", "Chỉ số tuyệt đối và tương đối"),
        ("pool-skill-level-test.html", "Hướng dẫn kiểm tra trình độ bi-a"),
        ("faq.html", "Hỏi đáp"),
        ("privacy-policy.html", "Chính sách quyền riêng tư"),
    ],
    footer_sitemap="Sơ đồ trang",
    footer_copyright="&copy; {year} Runout Rank. Do {author} viết và xây dựng.",
    footer_platforms="Android &amp; iOS &middot; Chỉ có chế độ tối, giống như ứng dụng",
    footer_disclaimer="Fargo Rate và FargoRate là thương hiệu của chủ sở hữu tương ứng. "
                      "Runout Rank là một ứng dụng độc lập, không trực thuộc, không được chứng thực bởi và "
                      "không có liên hệ nào với FargoRate, BCA, APA hay bất kỳ đơn vị tổ chức giải đấu nào. "
                      "Các so sánh trên trang này mô tả cách vận hành đã được công bố của những hệ thống đó, "
                      "và được đưa ra để bạn đọc tự đánh giá.",

    # --- social / meta --------------------------------------------------
    og_image_alt="Runout Rank — trình độ bi-a thật sự của bạn tới đâu?",

    # --- privacy policy page --------------------------------------------
    privacy_title="Chính sách quyền riêng tư | Runout Rank",
    privacy_description="Runout Rank chỉ lưu các bài kiểm tra, chỉ số và lịch sử luyện tập của bạn trên "
                        "thiết bị của chính bạn. Chính sách này giải thích phần phân tích mà ứng dụng có "
                        "sử dụng, dữ liệu được chia sẻ với ai, và bạn có những quyền gì.",
    privacy_h1="Chính sách quyền riêng tư",
    privacy_breadcrumb="Chính sách quyền riêng tư",
    privacy_lead="Các bài kiểm tra và số liệu thống kê của bạn nằm lại trên thiết bị của bạn. Trang này "
                 "giải thích mọi thứ ứng dụng thực sự thu thập, vì sao, và bạn kiểm soát được những gì.",

    # --- 404 ------------------------------------------------------------
    not_found_title="Không tìm thấy trang | Runout Rank",
    not_found_description="Trang đó không tồn tại. Hãy quay lại trang chủ Runout Rank.",

    # --- SoftwareApplication schema -------------------------------------
    app_description="Runout Rank là ứng dụng chấm điểm trình độ bi-a tuyệt đối. Hãy thực hiện bài kiểm tra "
                    "dọn bàn mười ván trên một bàn bi-a thật, nhận chỉ số 0-100 cùng một hạng từ Rookie đến "
                    "Master chỉ trong một buổi, rồi luyện tập ở đúng cấp độ đang chặn bạn lại. Chỉ số này đo "
                    "bạn với những thế bi cố định chứ không phải với các đối thủ quanh bạn, nên nó không cần "
                    "giải đấu, không cần lịch sử 200 ván và thậm chí không cần đối thủ nào. Toàn bộ dữ liệu "
                    "nằm trên thiết bị của bạn.",
    app_features=[
        "Chỉ số tuyệt đối: đo với các thế bi cố định được tạo ra, không phải với đối thủ quanh bạn",
        "Chỉ số 0-100 đầy đủ chỉ từ một buổi mười ván, không có số ván tối thiểu phải hoàn thành trước",
        "Mang đi được giữa các thành phố, giải đấu và quốc gia vì thước đo không bao giờ thay đổi",
        "Bài kiểm tra mười ván cho ra chỉ số 0-100 và một hạng có tên gọi",
        "Sáu cấp độ thử thách từ Rookie đến Master",
        "Ràng buộc của mỗi cấp độ là cố định, nên cùng một chỉ số mang cùng một ý nghĩa ở mọi nơi",
        "Vô số thế bi luyện tập được tạo ngẫu nhiên",
        "Nhật ký luyện tập có mục yêu thích",
        "Tỷ lệ dọn bàn trọn đời, chuỗi thắng và thống kê theo từng cấp độ",
        "Hoạt động hoàn toàn ngoại tuyến, không cần tài khoản",
    ],
    app_offer="Miễn phí tải về. Gói đăng ký Runout Pro tùy chọn mở khóa lịch sử tiến bộ và xuất file CSV.",
)

CTA = f"""  <section class="cta band">
    <div class="container">
      <p class="eyebrow">Nhận con số của bạn</p>
      <h2>Mười ván. Mỗi ván một lần. Một chỉ số trung thực.</h2>
      <p class="lead" style="max-width:38rem;margin:0 auto 28px">Hãy sắp các thế bi lên chính chiếc bàn
      bạn vẫn chơi. Ứng dụng chấm điểm các lượt dọn bàn và cho bạn biết nên luyện ở cấp độ nào tiếp theo.</p>
      {store_block(UI, centred=True)}
    </div>
  </section>"""


# --------------------------------------------------------------------------
# Page bodies
# --------------------------------------------------------------------------

INDEX = f"""  <section class="hero">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow">Chỉ số bi-a tuyệt đối &middot; Android &amp; iOS</p>
        <h1>Chỉ số bi-a của bạn. <span class="accent">Tối nay</span>, chứ không phải sau 200 ván.</h1>
        <p class="lead">Chỉ số của giải đấu cần hàng trăm trận thì con số mới có ý nghĩa, và kết quả bạn
        nhận được còn phụ thuộc vào việc thành phố của bạn tình cờ có những ai. Runout Rank đo bạn với
        chính chiếc bàn: mười thế bi, mỗi thế một lần, một chỉ số 0&ndash;100 chỉ trong một buổi.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="{PLAY_URL}">Tải trên Google Play</a>
          <a class="btn btn--ghost" href="how-it-works.html">Bài kiểm tra diễn ra thế nào</a>
        </div>
        <p class="hero-note">Không cần giải đấu &middot; Không cần đối thủ &middot; Không cần tài khoản &middot; Chạy ngoại tuyến</p>
      </div>
      <div class="hero-shot">
        <div class="phone">
          <img src="assets/img/screen-home.png" width="1080" height="2400"
               alt="Màn hình chính của Runout Rank trên điện thoại, mời bạn bắt đầu bài kiểm tra mười ván."
               fetchpriority="high" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <section class="tight band">
    <div class="container">
      <div class="grid grid--4">
        <div><span class="stat">10</span><p class="dim">ván mỗi bài kiểm tra, mỗi ván một lần</p></div>
        <div><span class="stat">1</span><p class="dim">buổi là có chỉ số đầy đủ, không phải chờ 200 ván</p></div>
        <div><span class="stat">0&ndash;100</span><p class="dim">chỉ số và hạng, ngay khi bạn kết thúc</p></div>
        <div><span class="stat">0</span><p class="dim">giải đấu, đối thủ và tài khoản cần có</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Vì sao phải bận tâm</p>
        <h2>Chỉ số giải đấu tốn cả một mùa <span class="accent">mà vẫn dao động theo thành phố của bạn.</span></h2>
      </div>
      <div class="compare">
        <div class="card pain">
          <h3>Phải 200 ván nó mới là thật</h3>
          <p>FargoRate xem 200 ván là mức tối thiểu để một chỉ số được coi là đã xác lập. Nghĩa là một giải
          đấu, một mùa giải và một loạt khoản phí, trước khi bạn biết mình đang đứng ở đâu.</p>
          <p><a href="pool-rating-without-a-league.html">Có chỉ số mà không cần giải đấu &rarr;</a></p>
        </div>
        <div class="card pain">
          <h3>Con số của bạn mô tả nơi bạn sống</h3>
          <p>Chỉ số tương đối được neo vào những người quanh bạn, nên một cộng đồng bi-a địa phương mỏng
          hoặc biệt lập sẽ trôi dạt so với phần còn lại của thế giới.</p>
          <p><a href="absolute-vs-relative-pool-rating.html">Tuyệt đối và tương đối &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Lời giải</p>
        <h2>Đo người chơi với <span class="accent">chiếc bàn</span>, chứ không phải với căn phòng.</h2>
        <p class="lead">Mỗi cấp độ ấn định chính xác điều gì làm nên độ khó &mdash; số bi, có được đặt bi
        cái tự do hay không, các bi nằm sát nhau đến mức nào, bi cản. Những ràng buộc đó chính là thước đo,
        và chúng giống nhau với tất cả mọi người. Vượt qua chúng thì con số đi lên. Không gì khác làm nó
        thay đổi.</p>
      </div>
      <div class="grid grid--3">
        <div class="card">
          <h3>Tuyệt đối, không phải tương đối</h3>
          <p>Không có nhóm đối thủ mạnh hay yếu, và cũng chẳng có gì để trôi dạt theo.</p>
        </div>
        <div class="card">
          <h3>Một buổi, không phải một mùa</h3>
          <p>Khoảng một giờ bên bàn bi-a, và bạn kết thúc với một chỉ số thật chứ không phải con số tạm.</p>
        </div>
        <div class="card">
          <h3>Không có gì để học thuộc</h3>
          <p>Thế bi được tạo mới cho mỗi bài kiểm tra, nên thứ bạn đối mặt luôn là cấp độ đó, chứ không
          phải một bài tập mà bạn đã thuộc lòng đáp án.</p>
        </div>
      </div>
      <p style="margin-top:28px"><a href="fargo-rate-alternative.html">So sánh đầy đủ với Fargo Rate &rarr;</a></p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Cách hoạt động</p>
        <h2>Ba bước, một lần ngồi xuống</h2>
      </div>
      <div class="grid grid--3 steps">
        <div class="card step">
          <h3>Sắp bi đúng như ứng dụng vẽ</h3>
          <p>Mỗi thế bi được vẽ từ trên xuống, để bạn sắp đúng y như vậy ngay trước mặt mình.</p>
        </div>
        <div class="card step">
          <h3>Chơi đúng một lần</h3>
          <p>Dọn sạch bàn hoặc trượt, rồi ghi lại bằng một chạm. Không đánh lại, không bỏ qua.</p>
        </div>
        <div class="card step">
          <h3>Nhận chỉ số và một kế hoạch</h3>
          <p>Điểm số, chỉ số, hạng của bạn &mdash; và cấp độ đang chặn bạn lại, để luyện tiếp.</p>
        </div>
      </div>
      <p style="margin-top:28px"><a href="how-it-works.html">Đọc giải thích đầy đủ &rarr;</a></p>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-test.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Một bài kiểm tra đang diễn ra: ván 6 trên 10 được vẽ từ trên xuống với bốn bi mục tiêu có đánh số trên mặt nỉ, cùng các nút Đã dọn sạch và Trượt ở bên dưới."></div>
        </div>
        <div>
          <p class="eyebrow">Thế bi</p>
          <h3>Một thế bi trông như thế này.</h3>
          <p>Mỗi thế bi được vẽ từ trên xuống, đúng tỷ lệ, để bạn sắp lại trên mặt nỉ ngay trước mặt và
          chơi cú đánh thật. Nó nằm trên màn hình suốt lượt chơi, nên bạn có thể dựng lại thế bi nếu lỡ
          làm xô lệch.</p>
          <ul class="ticks">
            <li><strong>Các con số là thứ tự</strong> bạn phải đưa bi vào lỗ &mdash; không phải điểm của bi</li>
            <li><strong>Bi cản</strong> được vẽ xỉn màu và không đánh số: chúng chắn đường, chứ không nằm trong thứ tự</li>
            <li><strong>Bi cái</strong> xuất hiện từ cấp Advanced trở lên. Dưới mức đó bạn được đặt bi cái tự do</li>
          </ul>
        </div>
      </div>

      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-result.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Màn hình kết quả hiển thị 7 trên 10, chỉ số 58, hạng League, và việc cần làm tiếp theo."></div>
        </div>
        <div>
          <p class="eyebrow">Kết quả</p>
          <h3>Một chỉ số, và cấp độ đang <span class="gold">chặn bạn lại</span>.</h3>
          <p>Bảy trên mười là vượt qua một cấp độ. Bạn nhận được điểm số, chỉ số 0&ndash;100, hạng của mình
          và con số đã dịch chuyển bao nhiêu so với lần trước &mdash; rồi đến cấp độ hiện đang chặn bạn,
          với phần luyện tập ở đó chỉ cách một chạm.</p>
        </div>
      </div>

      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-progress.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Màn hình tiến độ hiển thị chỉ số, hạng, số liệu trọn đời và phân tích theo từng cấp độ."></div>
        </div>
        <div>
          <p class="eyebrow">Tiến độ</p>
          <h3>Xem việc luyện tập có hiệu quả không.</h3>
          <p>Chỉ số, hạng, cấp độ đã vượt qua, tỷ lệ dọn bàn trọn đời và chuỗi thắng tốt nhất &mdash; miễn
          phí, vĩnh viễn. <a href="runout-pro.html">Runout Pro</a> bổ sung phần lịch sử: mọi bài kiểm tra
          vẽ thành đồ thị theo thời gian và xuất file CSV.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid grid--3">
        <div class="card">
          <h3>Sáu cấp độ, không khóa cấp nào</h3>
          <p>Từ Rookie đến Master. Kiểm tra ở bất kỳ cấp nào &mdash; người chơi giỏi không phải cày từ đáy
          lên. <a href="levels.html">So sánh các cấp độ &rarr;</a></p>
        </div>
        <div class="card">
          <h3>Luyện ngay tại giới hạn của bạn</h3>
          <p>Vô số thế bi được tạo ra ở đúng cấp độ đang chặn bạn, kèm nhật ký mọi ván bạn đã chơi.
          <a href="practice.html">Tìm hiểu về luyện tập &rarr;</a></p>
        </div>
        <div class="card">
          <h3>Dữ liệu của bạn vẫn là của bạn</h3>
          <p>Không tài khoản, không máy chủ, chạy ngoại tuyến. Mọi thứ nằm trên thiết bị của bạn.
          <a href="privacy-policy.html">Chính sách quyền riêng tư &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

HOW = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Cách hoạt động")}
      <h1>Chỉ số Runout Rank được tính như thế nào</h1>
      <p class="lead">Mười thế bi được tạo ra, mỗi thế một lần chơi, quy thành chỉ số 0&ndash;100 và một
      hạng có tên gọi &mdash; kèm một chỉ dẫn rõ ràng về việc cần làm tiếp theo.</p>
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>1. Chọn một cấp độ và bắt đầu bài kiểm tra</h2>
      <p>Một bài kiểm tra là mười ván ở cùng một cấp độ. Bạn chọn cấp độ: ứng dụng có gợi ý, nhưng không
      cấp nào bị khóa cả, nên một người chơi giỏi có thể bắt đầu ngay ở Competitor thay vì cày dần từ
      Rookie. Nếu bạn chưa từng được chấm điểm, bài kiểm tra chỉ cách màn hình chính một chạm &mdash;
      không có gì phải thiết lập trước.</p>
      <p>Nếu muốn khởi động trước, bạn có thể tạo một thế bi luyện tập đơn lẻ và làm bài kiểm tra sau.</p>

      <h2>2. Sắp từng thế bi lên bàn thật</h2>
      <p>Mỗi thế bi được vẽ từ trên xuống với bi cái, các bi mục tiêu và mọi bi cản đúng vị trí. Bi cản
      được vẽ cố ý xỉn màu và không đánh số để chúng không bao giờ bị hiểu nhầm là một phần của thứ tự
      đưa bi vào lỗ. Bạn sắp đúng những gì nhìn thấy, trên chính chiếc bàn bạn vẫn chơi. Hình minh họa
      nằm trên màn hình suốt lượt chơi, nên bạn có thể dựng lại thế bi nếu làm xô lệch.</p>

      <h2>3. Chơi một lần, ghi lại một lần</h2>
      <p>Dọn sạch bàn, hoặc không. Một chạm ghi lại kết quả và đưa bạn sang ván kế tiếp. Phần đầu màn hình
      luôn cho biết bạn đang ở ván thứ mấy trên mười, còn dải phía trên thế bi cho thấy trong những ván đã
      chơi, ván nào dọn sạch và ván nào trượt.</p>
      <p><strong>Mỗi ván đúng một lần chơi. Không đánh lại, không bỏ qua.</strong> Chính ràng buộc đó là
      toàn bộ lý do khiến con số cuối cùng có giá trị.</p>
      <div class="note">Bị gián đoạn? Cứ rời bài kiểm tra rồi quay lại sau &mdash; nó tiếp tục đúng ở ván
      bạn đã dừng. Nếu bạn chủ động thoát, ứng dụng sẽ hỏi xác nhận trước, và cho bạn biết rằng một lượt
      chơi dở dang thì không thể chấm điểm.</div>

      <h2>4. Đọc kết quả</h2>
      <p>Ngay khi ván thứ mười được ghi lại, bạn nhận được:</p>
      <ul>
        <li><strong>Điểm số trên mười</strong> &mdash; bạn đã dọn sạch bao nhiêu trong mười ván.</li>
        <li><strong>Chỉ số 0&ndash;100</strong> và <strong>hạng</strong> tương ứng.</li>
        <li><strong>Vượt qua hay chưa.</strong> Bảy trên mười là vượt qua cấp độ.</li>
        <li><strong>Mức thay đổi chỉ số</strong> &mdash; con số đã dịch chuyển bao nhiêu so với lần trước.</li>
        <li><strong>Cấp độ giới hạn của bạn</strong> &mdash; cấp đang chặn bạn lại, kèm giải thích dễ hiểu
        về việc nên làm gì với nó.</li>
      </ul>
      <p>Từ màn hình đó, luyện tập ở cấp độ giới hạn chỉ cách một chạm.</p>

      <h2>Vì sao thế bi ngẫu nhiên vẫn cho ra điểm số so sánh được</h2>
      <p>Mỗi bài kiểm tra đều được tạo mới, nên không có đáp án nào để học thuộc và không có bài tập nào
      để tập dượt trước. Hai người chơi không bao giờ gặp cùng mười thế bi &mdash; và họ cũng không cần.</p>
      <p>Thứ cố định là <strong>cấp độ</strong>. Số bi, có được đặt bi cái tự do hay không, khoảng cách tối
      thiểu giữa các bi và số bi cản đều là hằng số đã định nghĩa, giống hệt nhau với mọi người trên cả hai
      nền tảng. Một bài kiểm tra Level&nbsp;4 luôn đặt ra câu hỏi của Level&nbsp;4. Mười ván là đủ để độ khó
      được san đều, và đó là lý do bài kiểm tra có mười ván chứ không phải một.</p>
      <p>Vậy nên thứ được đo là bạn với các ràng buộc của cấp độ, chứ không phải bạn với mười thế bi cụ thể.
      Đó là điều khiến con số 58 của người này mang cùng ý nghĩa với 58 của người khác.</p>

      <h2>Vì sao chỉ số này là tuyệt đối</h2>
      <p>Không có đối thủ nào xuất hiện trong phép tính đó. Các hệ thống giải đấu như Fargo Rate là
      <em>tương đối</em> &mdash; con số của bạn được suy ra từ kết quả đối đầu với những người chơi đã có
      chỉ số, và đó là lý do chúng cần một lịch sử thi đấu lớn thì chỉ số mới ổn định, cũng như lý do một
      cộng đồng địa phương kết nối lỏng lẻo có thể nằm cao hoặc thấp so với phần còn lại của mạng lưới.
      Runout Rank thay vào đó so bạn với một chuẩn cố định. Ràng buộc của mỗi cấp độ giống nhau ở mọi nơi,
      nên chỉ số là cùng một phép đo ở mọi nơi, ngay từ bài kiểm tra đầu tiên.</p>
      <p>Biến số địa phương duy nhất là thiết bị của bạn. Kiểu cắt lỗ, kích thước bàn và tốc độ mặt nỉ đều
      làm thay đổi độ khó của một lượt dọn bàn, nên hãy làm bài kiểm tra trên chính chiếc bàn bạn vẫn chơi
      và so sánh các con số của riêng bạn theo thời gian.</p>
      <p><a href="absolute-vs-relative-pool-rating.html">Chỉ số bi-a tuyệt đối và tương đối &rarr;</a></p>

      <h2>Chỉ số này không phải là gì</h2>
      <p>Nó là phép đo khả năng dọn bàn của bạn trên các thế bi được tạo ra, dưới quy tắc không đánh lại.
      Nó không phải hệ thống chấp điểm, không phải chỉ số của một liên đoàn, và nó không kết nối với bất kỳ
      cơ sở dữ liệu giải đấu nào. Nếu bạn cần một con số để chấp trong trận đấu, đó là việc của chỉ số giải
      đấu &mdash; xem <a href="fargo-rate-alternative.html">so sánh giữa hai bên</a>. Đây là một con số trung
      thực mà bạn có thể tự lấy, trên bàn của chính mình, bất cứ khi nào bạn muốn một con số mới.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="levels.html">Xem sáu cấp độ</a>
        <a class="btn btn--ghost" href="fargo-rate-alternative.html">So sánh với Fargo Rate</a>
      </div>
    </div>
  </section>

{CTA}
"""

LEVELS = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Các cấp độ")}
      <h1>Sáu cấp độ, từ Rookie đến Master</h1>
      <p class="lead">Độ khó là một chiếc thang, không phải một thanh trượt. Mỗi bậc thay đổi một điều cụ
      thể trong các thế bi bạn phải dọn &mdash; và không bậc nào bị khóa.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="table-wrap">
        <table>
          <caption class="sr-only">Sáu cấp độ Runout Rank và điều thay đổi ở mỗi bậc</caption>
          <thead>
            <tr>
              <th scope="col">Cấp</th>
              <th scope="col">Tên</th>
              <th scope="col">Bi mục tiêu</th>
              <th scope="col">Đặt bi cái tự do</th>
              <th scope="col">Khoảng cách tối thiểu</th>
              <th scope="col">Bi cản</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>1</strong></td><td><strong>Rookie</strong></td><td>2</td><td>Có</td><td>8&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>2</strong></td><td><strong>Regular</strong></td><td>3</td><td>Có</td><td>6&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>3</strong></td><td><strong>League</strong></td><td>4</td><td>Có</td><td>4&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>4</strong></td><td><strong>Competitor</strong></td><td>5</td><td>Có</td><td>2.25&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>5</strong></td><td><strong>Advanced</strong></td><td>5</td><td>Không</td><td>2.25&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>6</strong></td><td><strong>Master</strong></td><td>5</td><td>Không</td><td>2.25&Prime;</td><td>2</td></tr>
          </tbody>
        </table>
      </div>
      <p class="dim" style="margin-top:16px">Khoảng cách ở đây là khoảng cách <em>tối thiểu</em> giữa hai tâm
      bi, nên số càng lớn thì thế bi càng trải rộng và càng dễ chơi. 2.25&Prime; là đường kính một viên bi
      &mdash; mức sàn, dưới mức đó các bi sẽ chồng lên nhau. Cùng những con số này cũng hiển thị trong ứng
      dụng trên thẻ của từng cấp độ.</p>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Đọc chiếc thang</p>
        <h2>Bốn núm vặn, mỗi bậc vặn lên một nấc</h2>
      </div>
      <div class="grid grid--4">
        <div class="card"><h3>Số bi</h3><p>Hai bi ở Rookie, tăng lên năm từ Competitor trở lên. Mỗi bi thêm vào là một quyết định chạy bi nữa phải thực hiện trót lọt.</p></div>
        <div class="card"><h3>Đặt bi cái tự do</h3><p>Cấp 1&ndash;4 cho bạn tự đặt bi cái. Từ Advanced, bi cái nằm ở nơi thế bi đặt nó, và bạn bắt đầu từ những gì được trao.</p></div>
        <div class="card"><h3>Độ sát nhau</h3><p>Khoảng hở tối thiểu giữa các bi thu từ 8&Prime; xuống còn đúng một đường kính bi. Bi nằm sát nhau chắn góc và phá hỏng việc chạy bi.</p></div>
        <div class="card"><h3>Bi cản</h3><p>Chỉ riêng Master thêm hai viên. Chúng không thuộc thứ tự đưa bi vào lỗ &mdash; được vẽ xỉn màu và không đánh số &mdash; và tồn tại chỉ để chắn đường bạn.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-levels.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Màn hình các cấp độ với cấp League đang mở rộng, hiển thị điểm kiểm tra tốt nhất và tỷ lệ luyện tập gần đây."></div>
        </div>
        <div>
          <p class="eyebrow">Vị trí của bạn ở từng bậc</p>
          <h3>Mỗi cấp độ đều biết bạn đang làm tốt đến đâu trên nó</h3>
          <p>Mở rộng bất kỳ cấp độ nào để xem điểm kiểm tra tốt nhất của bạn ở đó, tỷ lệ dọn bàn khi luyện
          tập gần đây, và tỷ lệ ấy dựa trên bao nhiêu lượt thử &mdash; để bạn phân biệt được một điểm yếu
          thật sự với một buổi tối tệ. Các cấp đã vượt qua được đánh dấu, còn
          <span class="gold">giới hạn</span> của bạn &mdash; cấp độ hiện đang chặn bạn lại &mdash; được
          làm nổi bằng màu vàng.</p>
          <ul class="ticks ticks--gold">
            <li>Bắt đầu bài kiểm tra ở bất kỳ cấp nào, không chỉ cấp kế tiếp</li>
            <li>Kiểm tra lại một cấp đã làm để xác nhận hoặc cải thiện kết quả</li>
            <li>Bắt đầu luyện tập tự do ở bất kỳ cấp nào ngay từ chiếc thang này</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

PRACTICE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Luyện tập")}
      <h1>Luyện tập, và nhật ký mọi ván bạn đã chơi</h1>
      <p class="lead">Bài kiểm tra cho bạn biết cấp độ nào đang chặn bạn. Luyện tập là nơi bạn làm gì đó
      với điều ấy &mdash; một dòng thế bi bất tận được tạo ra ở đúng cấp độ đó.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-practice.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Một buổi luyện tập với thế bi bốn viên được tạo ra và câu hỏi bạn có dọn sạch bàn hay không."></div>
        </div>
        <div>
          <p class="eyebrow">Một buổi luyện</p>
          <h3>Không bao giờ hết bài, không bao giờ thuộc lòng thế bi</h3>
          <p>Thế bi luyện tập được tạo theo yêu cầu ở bất kỳ cấp độ nào bạn chọn, và các lượt thử của bạn
          được tính vào thống kê của cấp độ đó. Hình minh họa nằm trên màn hình suốt lượt chơi, nên bạn có
          thể sắp lại nếu thế bi bị xô lệch.</p>
          <ul class="ticks">
            <li>Một chạm ghi lại thành công hay thất bại, kèm xác nhận rằng nó đã được lưu</li>
            <li>Bỏ qua thế bi bạn không muốn chơi, thay vì để cả buổi luyện bị treo lại</li>
            <li>Chơi lại đúng thế bi đó để tập cho tới khi bạn làm chủ nó</li>
            <li>Tạo ván tiếp theo ngay sau khi ghi lại &mdash; một vòng lặp, không phải một cây menu</li>
            <li>Mở lại thế bi cuối cùng bạn đã tạo từ màn hình chính sau khi đóng ứng dụng</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Nhật ký luyện tập</p>
        <h2>Một bản ghi đầy đủ về công sức bạn đã bỏ ra</h2>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>Mọi ván bạn đã chơi</h3><p>Xem lại tất cả, kèm ngày tháng, cấp độ, và bạn đã dọn sạch trong bao nhiêu lượt thử.</p></div>
        <div class="card"><h3>Mục yêu thích</h3><p>Gắn sao cho những thế bi đáng lặp lại và lọc nhật ký chỉ xem mục yêu thích, dần dựng nên một thư viện bài tập của riêng bạn.</p></div>
        <div class="card"><h3>Tiếp tục từ bất cứ đâu</h3><p>Chọn bất kỳ ván nào trong nhật ký và luyện tiếp từ đó. Quay lại một thế bi cũ chỉ cần một chạm.</p></div>
      </div>
      <p class="dim" style="margin-top:20px">Nhật ký trống sẽ hướng dẫn bạn cách lấp đầy nó, thay vì chỉ hiện một màn hình trắng.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-progress.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Màn hình Rank hiển thị chỉ số hiện tại, hạng, số liệu trọn đời và phân tích theo từng cấp độ."></div>
        </div>
        <div>
          <p class="eyebrow">Bạn đang ở đâu &mdash; miễn phí, luôn luôn</p>
          <h3>Những con số trả lời câu &ldquo;mình có đang khá lên không?&rdquo;</h3>
          <p>Chỉ số 0&ndash;100 và hạng của bạn, cấp độ cao nhất bạn đã vượt qua, cấp độ giới hạn của bạn,
          và mức thay đổi chỉ số so với bài kiểm tra trước. Bên dưới: tổng số lượt thử trọn đời, tổng số lần
          dọn sạch bàn, tỷ lệ dọn bàn chung và chuỗi thắng tốt nhất, kèm một cách diễn đạt dễ hiểu của tỷ lệ
          đó &mdash; &ldquo;bạn dọn sạch được 1 trong mỗi N ván&rdquo;.</p>
          <p>Kiểm tra lại ở cấp độ giới hạn chỉ cách một chạm ngay trên cùng màn hình.</p>
          <p><a href="runout-pro.html">Runout Pro bổ sung thêm gì &rarr;</a></p>
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
      <p class="lead">Một ranh giới, một câu: <strong>bạn đang ở đâu thì miễn phí, bạn đến đó bằng cách nào
      thì thuộc về Pro.</strong></p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid grid--2">
        <div class="card">
          <p class="eyebrow">Miễn phí, vĩnh viễn</p>
          <h3>Bạn đang ở đâu</h3>
          <ul class="ticks">
            <li>Chỉ số 0&ndash;100 và hạng của bạn</li>
            <li>Cấp độ bạn đã vượt qua và cấp độ đang chặn bạn</li>
            <li>Mức thay đổi chỉ số so với bài kiểm tra trước</li>
            <li>Phân tích theo cấp độ: điểm kiểm tra tốt nhất và tỷ lệ luyện tập gần đây</li>
            <li>Lượt thử, số lần dọn bàn, tỷ lệ dọn bàn và chuỗi thắng tốt nhất trọn đời</li>
            <li>Không giới hạn số bài kiểm tra và không giới hạn luyện tập ở mọi cấp độ</li>
          </ul>
          <p class="dim">Đây không phải bản dùng thử. Ứng dụng hoàn toàn hữu ích mà không cần trả tiền.</p>
        </div>
        <div class="card card--gold">
          <p class="eyebrow eyebrow--gold">Runout Pro</p>
          <h3>Bạn đã đến đây bằng cách nào</h3>
          <ul class="ticks ticks--gold">
            <li>Chỉ số của bạn vẽ thành đồ thị qua mọi bài kiểm tra bạn từng làm</li>
            <li>Diễn tiến điểm số ở từng cấp độ &mdash; mọi bài kiểm tra, không chỉ lần tốt nhất</li>
            <li>Tỷ lệ dọn bàn theo thời gian, và lịch sử các buổi luyện của bạn</li>
            <li>Nhật ký kiểm tra đầy đủ: cấp độ, điểm số, ngày và mức thay đổi chỉ số của từng lượt</li>
            <li>Xuất toàn bộ lịch sử ra file CSV</li>
          </ul>
          <p class="dim">Đăng ký theo tháng hoặc theo năm. Toàn bộ lịch sử trong quá khứ của bạn mở khóa
          ngay lập tức &mdash; không phải chờ một giai đoạn thu thập dữ liệu mới nào cả.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Lời mời nâng cấp cư xử ra sao</p>
        <h2>Một tấm thẻ trung thực, không phải ổ khóa rải khắp trang</h2>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>Ngày đầu không chào mời</h3><p>Một người chơi hoàn toàn mới, chưa có lịch sử kiểm tra nào, sẽ không thấy bất kỳ lời chào mời nào. Một bức tường trả phí cho thứ bạn còn chưa hình dung ra mình muốn thì chỉ là tiếng ồn.</p></div>
        <div class="card"><h3>Xem trước dữ liệu của chính bạn</h3><p>Khi bạn đã có đủ lịch sử để mở khóa điều gì đó, bạn thấy đường cong tiến bộ của chính mình với các giá trị bị làm mờ &mdash; chứ không phải một mẩu quảng cáo chung chung.</p></div>
        <div class="card"><h3>Một ranh giới, đặt ở cuối trang</h3><p>Màn hình Rank có đúng một thẻ Pro. Rải biểu tượng ổ khóa khắp màn hình sẽ khiến mọi tính năng miễn phí đều có cảm giác như hàng mẫu.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Thanh toán, khôi phục và hủy</h2>
      <ul>
        <li>Giá được hiển thị trực tiếp từ App Store hoặc Google Play, và mức tiết kiệm của gói năm được tính
        dựa trên đó, nên những gì bạn thấy đúng là số tiền cửa hàng sẽ thu bằng đơn vị tiền tệ của bạn.</li>
        <li>Đã mua rồi? <strong>Khôi phục giao dịch</strong> sẽ lấy lại nó sau khi cài lại hoặc trên thiết bị
        thứ hai &mdash; cài lại không bao giờ khiến bạn trả tiền hai lần.</li>
        <li>Quản lý hoặc hủy bất cứ lúc nào trong tài khoản Apple hoặc Google của bạn. Việc hoàn tiền và các
        thắc mắc về thanh toán do cửa hàng xử lý theo điều khoản của chính họ.</li>
        <li>Điều khoản sử dụng và <a href="privacy-policy.html">chính sách quyền riêng tư</a> có thể đọc được
        trước khi bạn đăng ký, chứ không phải sau đó.</li>
        <li><strong>Pro vẫn hoạt động ngoại tuyến.</strong> Sóng yếu trong một câu lạc bộ bi-a không bao giờ
        khóa bạn khỏi thứ bạn đã trả tiền.</li>
      </ul>
      <p>Việc thanh toán hoàn toàn do Apple và Google xử lý. Runout Rank không bao giờ nhìn thấy hay lưu trữ
      thông tin thẻ của bạn.</p>
    </div>
  </section>

{CTA}
"""

GUIDE_TITLE = "Cách kiểm tra trình độ bi-a của bạn (và có một con số đáng tin)"
GUIDE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Kiểm tra trình độ bi-a")}
      <h1>Cách kiểm tra trình độ bi-a của bạn</h1>
      <p class="lead">Hầu hết người chơi đều có thể kể ra họ thắng được ai. Rất ít người nói được mình giỏi
      đến đâu. Đây là điều phân biệt một bài kiểm tra trình độ đáng làm với một bài tập mà bạn tình cờ
      thích.</p>
{byline(UI, FIRST_PUBLISHED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Vì sao &ldquo;mình giỏi đến đâu?&rdquo; lại khó trả lời đến thế</h2>
      <p>Kết quả trận đấu đo đối thủ của bạn nhiều ngang với đo chính bạn. Một buổi tối hay trước dàn đối thủ
      yếu và một buổi tối dở trước dàn đối thủ mạnh có thể cho ra tỷ số giống hệt nhau. Việc luyện tập tạo
      cảm giác hiệu quả bất kể nó có hiệu quả hay không, bởi bạn tự nhiên dành thời gian cho những cú đánh
      mình vốn đã thích. Còn những bài tập mà đa số người chơi thực hiện lại chính là những bài họ đã làm
      trước đó &mdash; và đó đúng là lý do chúng ngày càng dễ.</p>
      <p>Một bài kiểm tra trình độ hữu ích phải làm được ba điều mà luyện tập tùy hứng không làm được.</p>

      <h2>1. Nó phải đo trọn một kỹ năng, không phải một cú đánh đơn lẻ</h2>
      <p>Đưa được một viên bi xanh xa và thẳng vào lỗ chỉ nói lên một đường cơ. Dọn sạch cả bàn thì nói lên
      khả năng đọc thế bi, chạy bi, kiểm soát lực, phán đoán phòng thủ và bản lĩnh, theo đúng thứ tự mà chiếc
      bàn đòi hỏi. Đó là lý do lượt dọn bàn &mdash; trọn một bàn, từ đầu đến cuối &mdash; mới là đơn vị đo
      đúng cho một bài kiểm tra trình độ, và là lý do Runout Rank chấm điểm theo ván chứ không theo cú đánh.</p>

      <h2>2. Nó phải khó đoán</h2>
      <p>Bất kỳ bộ thế bi cố định nào rồi cũng thoái hóa thành bài kiểm tra trí nhớ. Lần thứ mười bạn sắp lại
      cùng một bài tập, thứ bạn đo không còn là khả năng dọn bàn nữa, mà là bạn nhớ đáp án cho đúng thế bi đó
      tốt đến mức nào. Một bài kiểm tra đáng làm đi làm lại phải tự tạo ra thế bi của nó, để cục diện trước
      mặt bạn thực sự mới mỗi lần.</p>

      <h2>3. Độ khó của nó phải được định nghĩa, chứ không phải ứng biến</h2>
      <p>Mâu thuẫn nằm ở đây: tính ngẫu nhiên làm bài kiểm tra trung thực, nhưng đồng thời cũng có nguy cơ
      khiến hai điểm số không so sánh được với nhau. Nếu mười thế bi của bạn khó hơn của tôi, điểm số của
      chúng ta mang ý nghĩa khác nhau.</p>
      <p>Cách khắc phục là <strong>cố định các ràng buộc thay vì cố định thế bi</strong>. Hãy định nghĩa
      chính xác một cấp độ khó nghĩa là gì &mdash; bao nhiêu bi mục tiêu, có được đặt bi cái tự do không,
      khoảng cách tối thiểu giữa các bi, bao nhiêu bi cản &mdash; rồi tạo thế bi tự do bên trong những quy
      tắc ấy. Mọi thế bi đều mới, mọi thế bi đều cùng độ khó, và đủ nhiều ván liên tiếp sẽ san đều phần may
      rủi còn lại. Trong Runout Rank, các hằng số đó được công bố trên
      <a href="levels.html">trang các cấp độ</a> và giống hệt nhau trên Android lẫn iOS.</p>
      <p>Đó là điều khiến một điểm số mang đi được: nó nói rằng bạn dọn sạch bảy trên mười ở Level&nbsp;4,
      và Level&nbsp;4 mang cùng ý nghĩa với tất cả mọi người.</p>

      <h2>Những quy tắc làm nên một điểm số trung thực</h2>
      <ul>
        <li><strong>Mỗi ván một lần chơi.</strong> Chơi ba lấy hai đo ngày tốt nhất của bạn, không phải mặt
        bằng của bạn.</li>
        <li><strong>Không bỏ qua.</strong> Những thế bi bạn muốn né nhất chính là những thế mang nhiều thông
        tin nhất.</li>
        <li><strong>Số ván cố định.</strong> Mười là đủ để san đều một cú xui, và đủ ngắn để hoàn thành trong
        một buổi bên bàn bi-a thật.</li>
        <li><strong>Một mức đạt được nêu rõ.</strong> Bảy trên mười là vượt qua một cấp độ trong Runout Rank.
        Biết trước ngưỡng trước khi bắt đầu cũng là một phần của bài kiểm tra.</li>
        <li><strong>Ghi lại ngay lập tức.</strong> Một kết quả bạn ghi lại sau đó một tiếng là một kết quả bạn
        đã tô hồng rồi.</li>
      </ul>

      <h2>Làm gì với con số đó</h2>
      <p>Một chỉ số tự thân nó chỉ là chuyện phiếm. Con số chỉ hữu ích khi nó chỉ về đâu đó, và vì vậy sản
      phẩm quan trọng của một bài kiểm tra không phải điểm số mà là <strong>cấp độ giới hạn</strong>
      &mdash; bậc thang bạn chưa vượt được. Đó là nơi luyện tập sinh lời, vì đó là cấp độ duy nhất mà các
      thế bi vẫn đang đặt cho bạn một câu hỏi bạn chưa trả lời được.</p>
      <p>Vòng lặp thực tế trông như thế này:</p>
      <ol>
        <li>Kiểm tra ở cấp độ bạn nghĩ mình vượt qua được.</li>
        <li>Nếu vượt qua, hãy kiểm tra cấp trên cho tới khi có một cấp chặn bạn lại.</li>
        <li>Luyện tập ở cấp độ giới hạn đó, ghi lại từng lượt thử để tỷ lệ dọn bàn là thật.</li>
        <li>Kiểm tra lại chính cấp độ đó khi tỷ lệ đã dịch chuyển. Hãy so sánh chỉ số, đừng so sánh cảm giác.</li>
      </ol>

      <h2>Bao lâu nên kiểm tra lại</h2>
      <p>Đủ thường xuyên để con số bám sát thực tế, và đủ thưa để mỗi lần kiểm tra lại phản ánh công sức thật.
      Với đa số người chơi có vài buổi bên bàn mỗi tuần, hai đến bốn tuần một lần là hợp lý. Kiểm tra lại sau
      mỗi buổi thì phần lớn là đo nhiễu; kiểm tra hai lần một năm thì chẳng cho bạn điều gì để hành động.</p>

      <h2>Vì sao cách này hơn việc ngồi chờ một chỉ số giải đấu ổn định</h2>
      <p>Phương án mà đa số người chơi được chỉ tới là một chỉ số tương đối kiếm được qua thi đấu giải, và nó
      cần một lịch sử lớn các ván đấu với những người đã có chỉ số thì mới có nhiều ý nghĩa &mdash; FargoRate
      chẳng hạn, xem 200 ván là mức tối thiểu để một chỉ số được coi là đã xác lập. Một bài kiểm tra dọn bàn
      cho bạn câu trả lời trong một buổi, bởi nó đo bạn với các thế bi chứ không phải với căn phòng, điều này
      cũng có nghĩa là nó không dao động theo sức mạnh của cộng đồng bi-a nơi bạn ở. Đọc thêm:</p>
      <ul>
        <li><a href="fargo-rate-alternative.html">Giải pháp thay thế Fargo Rate không cần 200 ván đấu giải</a></li>
        <li><a href="pool-rating-without-a-league.html">Cách có chỉ số bi-a mà không cần tham gia giải đấu</a></li>
        <li><a href="absolute-vs-relative-pool-rating.html">Chỉ số bi-a tuyệt đối và tương đối</a></li>
      </ul>

      <div class="note">Runout Rank làm tất cả những điều trên ngay trên chiếc bàn bạn vẫn chơi: nó tạo ra
      các thế bi, chấm điểm các lượt dọn bàn, giữ lịch sử trên thiết bị của bạn, và gọi tên cấp độ cần luyện
      tiếp theo. <a href="how-it-works.html">Xem chính xác bài kiểm tra hoạt động thế nào &rarr;</a></div>
    </div>
  </section>

{CTA}
"""

# --------------------------------------------------------------------------
# Positioning pages: the two pain points a relative league rating leaves open
# --------------------------------------------------------------------------

FARGO_DISCLAIMER = """      <p class="disclaimer">Runout Rank là ứng dụng độc lập, không trực thuộc, không được
      chứng thực bởi và không có liên hệ nào với FargoRate. Mọi điều nói ở đây về Fargo Rate đều lấy từ
      <a href="https://www.fargorate.com/" rel="nofollow">tài liệu do chính FargoRate công bố</a>
      và được mô tả công bằng hết mức chúng tôi có thể; đó là một hệ thống tốt, và trang này chỉ bàn về việc
      thiết kế của nó phù hợp và không phù hợp với kiểu người chơi nào.</p>"""

FARGO_ALT_TITLE = "Giải pháp thay thế Fargo Rate không cần 200 ván đấu giải"
FARGO_ALT = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Giải pháp thay thế Fargo Rate")}
      <h1>Giải pháp thay thế Fargo Rate cho những người sẽ không bao giờ chơi 200 ván đấu giải</h1>
      <p class="lead">Fargo Rate là hệ thống chỉ số tương đối tốt nhất mà bi-a có được. Nhưng chính tính
      tương đối là thứ khiến nó chậm kiếm được và nhạy cảm với nơi bạn sống. Đây là những gì một chỉ số tuyệt
      đối làm khác đi, và bạn thực sự muốn cái nào trong hai cái đó.</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Trước hết, ghi nhận điều đáng ghi nhận</h2>
      <p>Fargo Rate đã đặt người chơi nghiệp dư và nhà vô địch thế giới lên cùng một thang đo, và biến việc
      chấp điểm trong bi-a thành thứ có thể tranh luận bằng con số thay vì bằng tiếng tăm. Nếu bạn chơi các
      trận đấu giải hằng tuần với những người đã có chỉ số, nó hoạt động tốt, và trang này sẽ không giả vờ
      ngược lại. Hãy giữ lấy nó.</p>
      <p>Câu hỏi mà trang này bàn tới hẹp hơn: <strong>bạn làm gì nếu bạn không phải người chơi kiểu đó?</strong>
      Nếu bạn luyện tập một mình, chơi vui với bạn bè, hay đi lại nhiều, hoặc đơn giản là muốn biết mình giỏi
      đến đâu mà không phải đăng ký cả một mùa thi đấu, thì một chỉ số tương đối có hai vấn đề mang tính cấu
      trúc &mdash; và chúng là cấu trúc, không phải lỗi.</p>

      <h2>Điểm đau thứ nhất: con số chưa là thật cho tới 200 ván</h2>
      <p>FargoRate gọi quy mô lịch sử thi đấu của bạn là <em>robustness</em> (độ vững), và nói rõ rằng độ vững
      200 ván là mức tối thiểu để nó coi một chỉ số là &ldquo;đã xác lập&rdquo;. Dưới ngưỡng đó, chỉ số chính
      thức của bạn là hỗn hợp giữa thành tích thực tế và một <em>starter rating</em> &mdash; một phỏng đoán
      ban đầu &mdash; với phần phỏng đoán mất dần ảnh hưởng khi bạn tiến gần tới mốc 200.</p>
      <p>Hãy tính xem 200 ván có tính điểm tốn của một người bình thường những gì. Nó có nghĩa là tìm được một
      giải đấu có báo cáo về hệ thống, đóng các khoản phí của giải, rảnh vào cùng một buổi tối mỗi tuần, và
      chơi hết phần lớn một hoặc hai mùa giải &mdash; trước khi con số trong ứng dụng là một phép đo về bạn
      chứ không phải một ý kiến có trọng số. Một người chơi chỉ muốn một câu trả lời trung thực cho
      &ldquo;mình giỏi đến đâu?&rdquo; lại phải mua trọn một năm cam kết mới có được nó.</p>
      <p>Và không có cách nào đi tắt, bởi chẳng có gì để đi tắt cả: một hệ thống tương đối thực sự không thể
      biết gì về bạn cho tới khi bạn tạo ra đủ kết quả trước những người mà nó đã biết.</p>
      <p><a href="pool-rating-without-a-league.html">Cách có chỉ số bi-a mà không cần tham gia giải đấu &rarr;</a></p>

      <h2>Điểm đau thứ hai: chỉ số của bạn một phần mô tả thành phố của bạn</h2>
      <p>Một chỉ số tương đối được tính từ chuyện ai thắng ai. Nghĩa là con số của bạn chỉ được neo chắc bằng
      đúng chuỗi các ván đấu nối những người chơi địa phương của bạn với phần còn lại của thế giới đã có chỉ
      số. Nơi chuỗi đó dày &mdash; các thành phố lớn, những cộng đồng thi đấu mạnh, những người chơi hay đi
      đánh giải mở &mdash; chỉ số khớp nhau rất tốt. Nơi nó mỏng, một nhóm địa phương có thể ổn định ở một
      mức không tương ứng với chính những con số đó ở nơi khác.</p>
      <p>Đây không phải lời phàn nàn của người ngoài. Chính các bài viết của FargoRate mô tả trường hợp hai
      nhóm người chơi gần như biệt lập, một nhóm được chấm cao hơn so với nhóm kia, là một vấn đề đặc biệt
      nan giải &mdash; và nó chỉ tự điều chỉnh nhờ rất nhiều trận đấu chéo trong thời gian dài. Định nghĩa của
      họ về một chỉ số đáng tin cậy cũng lưu ý rằng các ván đấu với đối thủ đã có chỉ số xác lập được tính
      trọng số cao hơn.</p>
      <p>Vậy nên nếu khu vực của bạn dày đặc người chơi giỏi, hoặc gần như không kết nối với mạng lưới rộng
      hơn, hoặc mới gia nhập hệ thống, thì con số bạn mang theo đang nói điều gì đó về môi trường quanh bạn
      chứ không chỉ về bạn. Chuyển đi nơi khác, nó có thể không còn mang ý nghĩa như hồi ở quê nhà.</p>
      <p><a href="absolute-vs-relative-pool-rating.html">Chỉ số tuyệt đối và tương đối, giải thích &rarr;</a></p>

      <h2>Một chỉ số tuyệt đối làm gì thay vào đó</h2>
      <p>Runout Rank loại bỏ hoàn toàn đối thủ khỏi phép đo. Thay vì hỏi bạn đã thắng ai, nó đặt một thế bi đã
      định nghĩa lên bàn và hỏi bạn có dọn sạch được nó hay không.</p>
      <p>Bạn chơi mười thế bi được tạo ra ở cùng một cấp độ, mỗi thế một lần, không đánh lại và không bỏ qua,
      rồi ghi lại từng ván là dọn sạch hay trượt. Mười câu trả lời thành một điểm số, một chỉ số 0&ndash;100
      và một hạng từ Rookie đến Master. Bảy trên mười là vượt qua cấp độ. Toàn bộ mất khoảng một giờ trên
      chính chiếc bàn bạn vẫn chơi.</p>
      <p>Vì các thế bi chính là thước đo, và thước đo không bao giờ thay đổi, con số mang cùng một ý nghĩa bất
      kể còn ai khác trong phòng, và mang cùng ý nghĩa vào năm sau như năm nay. Nó được kiếm ngay từ buổi đầu
      tiên, chứ không tích lũy suốt một mùa.</p>

      <h2>Đặt cạnh nhau</h2>
      <div class="table-wrap">
        <table>
          <caption class="sr-only">So sánh chỉ số giải đấu tương đối với chỉ số tuyệt đối của Runout Rank</caption>
          <thead>
            <tr>
              <th scope="col"></th>
              <th scope="col">Chỉ số tương đối (Fargo Rate và tương tự)</th>
              <th scope="col">Runout Rank</th>
            </tr>
          </thead>
          <tbody>
            <tr><th scope="row">Đo cái gì</th><td>Kết quả đối đầu với những người chơi đã có chỉ số</td><td>Các lượt dọn bàn trên thế bi cố định được tạo ra</td></tr>
            <tr><th scope="row">Bao lâu thì có ý nghĩa</th><td>200 ván để chỉ số được xác lập; dưới mức đó có trộn thêm một chỉ số khởi đầu</td><td>Một bài kiểm tra mười ván, khoảng một giờ</td></tr>
            <tr><th scope="row">Bạn cần gì</th><td>Một giải đấu có báo cáo hoặc các sự kiện tính điểm, đối thủ, lệ phí, một lịch cố định</td><td>Một bàn bi-a và một chiếc điện thoại</td></tr>
            <tr><th scope="row">Ảnh hưởng của cộng đồng địa phương</th><td>Có thật: mức độ kết nối và sức mạnh của nhóm đối thủ đều tác động tới con số</td><td>Không có: không đối thủ nào tham gia</td></tr>
            <tr><th scope="row">Tính mang đi được</th><td>Đi được trong nội bộ mạng lưới; các khu vực kết nối lỏng lẻo có thể trôi dạt</td><td>Cùng ràng buộc cấp độ ở mọi nơi, trên cả Android và iOS</td></tr>
            <tr><th scope="row">Tốt cho việc</th><td>Chấp điểm trận đấu, xếp nhánh giải, điều kiện dự giải</td><td>Biết mặt bằng của chính bạn và điều cần luyện tiếp theo</td></tr>
            <tr><th scope="row">Không dùng để</th><td>Trả lời &ldquo;mình giỏi đến đâu?&rdquo; ngay ngày đầu tiên</td><td>Chấp điểm trong trận đấu với người khác &mdash; nó không phải hệ thống chấp điểm</td></tr>
            <tr><th scope="row">Chi phí và tài khoản</th><td>Phí hội viên giải đấu; một hồ sơ trực tuyến</td><td>Ứng dụng miễn phí, không tài khoản, chạy hoàn toàn ngoại tuyến</td></tr>
          </tbody>
        </table>
      </div>

      <h2>Nói rõ Runout Rank không phải là gì</h2>
      <p>Nó không thay thế chỉ số giải đấu trong việc chấp điểm, và nó sẽ không giúp bạn được xếp hạt giống ở
      một giải nào. Không liên đoàn nào công nhận nó. Nó cũng thành thật về biến số của chính mình: bạn đang
      chơi trên thiết bị của mình, nên một chiếc bàn lỗ hẹp với mặt nỉ chậm sẽ cho kết quả khác với bàn nhỏ
      trong quán. Hãy làm bài kiểm tra trên chính chiếc bàn bạn thi đấu, và so sánh những gì tương đương theo
      thời gian.</p>
      <p>Thứ nó cho bạn là điều mà một hệ thống tương đối không thể cho bạn một cách rẻ tiền: một con số thật,
      ngay hôm nay, từ lối chơi của chính bạn, và không phụ thuộc vào bất kỳ ai khác.</p>

      <h2>Câu trả lời hiển nhiên: dùng cả hai</h2>
      <p>Chúng đo những thứ khác nhau và không hề mâu thuẫn. Nếu bạn chơi giải, hãy giữ Fargo Rate cho các
      trận đấu, và dùng Runout Rank giữa những trận đó để biết phần nào trong lối chơi của bạn đang tụt lại
      &mdash; một bài kiểm tra dọn bàn gọi tên cấp độ đang chặn bạn và trao ngay phần luyện tập ở đó, điều mà
      một chỉ số dựa trên kết quả trận đấu không làm được. Nếu bạn không chơi giải, Runout Rank chính là con
      số bạn thực sự có thể có.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="how-it-works.html">Xem bài kiểm tra hoạt động thế nào</a>
        <a class="btn btn--ghost" href="pool-rating-without-a-league.html">Có chỉ số mà không cần giải đấu</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

NO_LEAGUE_TITLE = "Cách có chỉ số bi-a mà không cần tham gia giải đấu"
NO_LEAGUE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Có chỉ số mà không cần giải đấu")}
      <h1>Cách có chỉ số bi-a mà không cần tham gia giải đấu</h1>
      <p class="lead">Mọi hệ thống chỉ số đã thành danh đều thu cùng một khoản vé vào cửa: hàng trăm trận đấu
      với những người chơi đã có chỉ số. Nếu đó không phải cuộc sống của bạn, không phải bạn không thể được
      chấm điểm &mdash; bạn chỉ cần một chỉ số đo chiếc bàn thay vì đo căn phòng.</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Vì sao người chơi phong trào rốt cuộc chẳng có con số nào</h2>
      <p>Lời khuyên thường gặp là: tham gia một giải đấu có báo cáo về một hệ thống chỉ số, chơi một mùa, rồi
      chỉ số của bạn sẽ ổn định. Đó là lời khuyên hợp lý, và với nhiều người chơi nó cũng là điều bất khả thi.
      Nó đòi hỏi một buổi tối cố định mỗi tuần, phí hội viên, một địa điểm có tổ chức giải đấu báo cáo, và đủ
      nhiều đối thủ mà bản thân họ cũng đã có chỉ số.</p>
      <p>Rồi còn vấn đề số lượng. FargoRate xem 200 ván là độ vững tối thiểu để gọi một chỉ số là đã xác lập;
      dưới mức đó, một phần những gì bạn nhìn thấy là chỉ số khởi đầu mà hệ thống gán cho bạn chứ không phải
      những gì bạn đã làm. Hai trăm ván có tính điểm là một mùa giải hoặc hơn với đa số người chơi giải, và là
      chuyện viển vông với tất cả những người còn lại.</p>
      <p>Nên với một người chơi phong trào, kết luận trung thực là: công sức để kiếm một chỉ số tương đối lớn
      hơn giá trị của việc biết nó. Phần lớn mọi người lặng lẽ bỏ cuộc và quay về đoán mò dựa trên việc họ
      thắng được ai ở câu lạc bộ.</p>

      <h2>Điều bạn thực sự muốn biết</h2>
      <p>Gạt các hệ thống sang một bên, bên dưới thường là ba câu hỏi:</p>
      <ul>
        <li><strong>Mình đang ở đâu?</strong> Mình là một tay chơi câu lạc bộ khá, hay giỏi hơn mình tưởng,
        hay tệ hơn?</li>
        <li><strong>Mình có đang tiến bộ không?</strong> Không phải &ldquo;tối nay mình thấy ổn&rdquo;
        &mdash; đường cong có đang đi lên không?</li>
        <li><strong>Mình nên luyện gì?</strong> Phần nào của trận đấu đang thực sự kéo phần còn lại xuống?</li>
      </ul>
      <p>Không câu nào trong ba câu đó cần tới một đối thủ. Chúng cần một nhiệm vụ cố định, lặp lại được, đủ
      khó để có thể thất bại, và một bản ghi về việc bạn hoàn thành nó thường xuyên đến đâu.</p>

      <h2>Bài kiểm tra trả lời được chúng</h2>
      <p>Lượt dọn bàn là đơn vị đúng: dọn sạch một bàn huy động khả năng đọc thế bi, chạy bi, kiểm soát lực và
      bản lĩnh theo đúng thứ tự mà chiếc bàn đòi hỏi, điều một bài tập đưa bi vào lỗ đơn thuần không làm được.
      Hãy đặt nó thành mười ván ở cùng một cấp độ khó, mỗi ván một lần, không đánh lại và không bỏ qua, và bạn
      có một phép đo thay vì một buổi luyện tập.</p>
      <p>Đó chính là điều Runout Rank làm. Ứng dụng vẽ từng thế bi từ trên xuống, bạn sắp lại trên bàn của
      mình, chơi một lần rồi chạm vào &ldquo;dọn sạch&rdquo; hoặc &ldquo;trượt&rdquo;. Cuối cùng bạn nhận được
      điểm số trên mười, một chỉ số 0&ndash;100, một hạng từ Rookie đến Master, việc bạn có vượt qua cấp độ
      hay không, và cấp độ hiện đang chặn bạn lại. Mất khoảng một giờ và không cần ai khác trong tòa nhà.</p>
      <p>Thế bi được tạo mới cho mỗi bài kiểm tra, nên không có gì để học thuộc, trong khi các ràng buộc của
      cấp độ &mdash; số bi, đặt bi cái tự do, khoảng cách, bi cản &mdash; là những hằng số cố định giống nhau
      với mọi người chơi trên Android lẫn iOS. Thế bi mới mỗi lần, độ khó như nhau mỗi lần.</p>

      <h2>Một quy trình thực tế cho người chơi một mình</h2>
      <ol>
        <li><strong>Kiểm tra ở cấp độ bạn nghĩ mình vượt qua được.</strong> Không cấp nào bị khóa, nên hãy bắt
        đầu ở nơi bạn nghĩ mình thuộc về, thay vì từ dưới đáy.</li>
        <li><strong>Đi lên cho tới khi một cấp chặn bạn lại.</strong> Bảy trên mười là vượt qua; khi bạn không
        làm nổi bảy ván, bạn đã tìm thấy giới hạn của mình.</li>
        <li><strong>Luyện tập ở cấp độ giới hạn đó,</strong> ghi lại mọi lượt thử để tỷ lệ dọn bàn là một sự
        thật chứ không phải một ấn tượng.</li>
        <li><strong>Kiểm tra lại cấp độ đó khi tỷ lệ đã dịch chuyển.</strong> Hai đến bốn tuần một lần hợp với
        đa số người chơi &mdash; đủ thường để bám theo công sức thật, đủ thưa để bạn không đo nhiễu.</li>
        <li><strong>So sánh chỉ số, đừng so sánh cảm giác.</strong> Mức thay đổi chỉ số trên màn hình kết quả
        chính là toàn bộ ý nghĩa của việc này.</li>
      </ol>

      <h2>Nó tốn của bạn những gì</h2>
      <p>Một giờ, một chiếc bàn bạn đặt được, và không gì khác. Ứng dụng miễn phí tải về, không có tài khoản
      nào phải tạo, nó chạy hoàn toàn ngoại tuyến, và lịch sử của bạn nằm trong bộ nhớ riêng của ứng dụng trên
      thiết bị của chính bạn. Runout Pro là tùy chọn và bổ sung phần lịch sử: chỉ số của bạn vẽ thành đồ thị
      qua mọi bài kiểm tra, diễn tiến theo từng cấp độ và xuất file CSV. Việc bạn đang ở đâu thì miễn phí
      vĩnh viễn.</p>

      <h2>Nếu bạn có chơi giải</h2>
      <p>Thì hãy giữ chỉ số giải đấu của bạn &mdash; nó là công cụ đúng để chấp điểm trong trận đấu, và bài
      viết này không nhằm thay thế nó. Hãy dùng một bài kiểm tra dọn bàn song song, bởi một chỉ số dựa trên
      kết quả trận đấu cho bạn biết bạn ở mức nào mà không cho biết phần nào trong lối chơi của bạn đang tụt
      lại. Xem <a href="fargo-rate-alternative.html">so sánh đầy đủ với Fargo Rate</a>.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="how-it-works.html">Bài kiểm tra hoạt động thế nào</a>
        <a class="btn btn--ghost" href="levels.html">Xem sáu cấp độ</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

ABSOLUTE_TITLE = "Chỉ số bi-a tuyệt đối và tương đối: vì sao thành phố của bạn làm thay đổi con số"
ABSOLUTE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Chỉ số tuyệt đối và tương đối")}
      <h1>Chỉ số bi-a tuyệt đối và tương đối</h1>
      <p class="lead">Hai người chơi có trình độ giống hệt nhau, một người ở thành phố mạnh và một người ở nơi
      trầm lắng, có thể mang những chỉ số tương đối khác nhau suốt nhiều năm. Đó không phải lỗi của phép toán
      &mdash; đó chính là ý nghĩa của chữ &ldquo;tương đối&rdquo;. Đây là điểm khác biệt, và mỗi loại chỉ số
      tốt cho việc gì.</p>
{byline(UI, UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Chỉ số tương đối là gì</h2>
      <p>Một chỉ số tương đối &mdash; Elo, Glicko, Fargo Rate và phần còn lại của họ nhà này &mdash; không có
      khái niệm về một chuẩn tuyệt đối. Nó chỉ biết các kết quả: bạn thắng họ, họ thắng người khác. Từ một
      mạng lưới đủ lớn các kết quả đó, hệ thống tìm ra bộ con số giải thích tốt nhất những gì đã xảy ra. Chưa
      từng có ai được đo trực tiếp; mọi chỉ số đều là một vị trí trong mạng lưới các chỉ số khác.</p>
      <p>Đó là một thiết kế thanh lịch và nó hoạt động tốt đến đáng kinh ngạc khi mạng lưới dày đặc. Nó cũng
      kéo theo hai hệ quả mà không phép toán khéo léo nào loại bỏ được.</p>

      <h2>Hệ quả thứ nhất: nó cần rất nhiều ván đấu</h2>
      <p>Một kết quả là một bit bằng chứng, và một bit thì rất ít. Nên hệ thống cần số lượng thì mới tách được
      bạn khỏi may rủi &mdash; đó là lý do FargoRate dùng thước đo độ vững và xem 200 ván là mức tối thiểu để
      gọi một chỉ số là đã xác lập, đồng thời trộn một chỉ số khởi đầu vào con số cho tới khi bạn đạt mốc đó.
      Cho tới khi bạn trả xong cái giá ấy bằng các ván đấu, chỉ số của bạn một phần vẫn là phỏng đoán về bạn.</p>

      <h2>Hệ quả thứ hai: nó được neo vào những người quanh bạn</h2>
      <p>Vì mọi chỉ số đều được định nghĩa dựa trên các chỉ số khác, một nhóm người chơi chỉ khớp đúng với phần
      còn lại của thế giới nếu có đủ ván đấu nối họ với thế giới đó. Nơi kết nối mỏng &mdash; một khu vực biệt
      lập, một giải đấu mới, một cộng đồng mà người chơi hiếm khi đi đánh giải mở &mdash; cả nhóm có thể ổn
      định ở một mức không tương ứng với chính những con số đó ở nơi khác. FargoRate mô tả đúng trường hợp
      này, hai nhóm gần như biệt lập với một nhóm được chấm cao hơn so với nhóm kia, là một vấn đề nan giải,
      và lưu ý rằng các ván đấu với đối thủ đã xác lập chỉ số có giá trị hơn cũng chính vì lý do đó.</p>
      <p>Phiên bản thực tế dành cho người chơi: nếu thành phố của bạn dày đặc người chơi giỏi, hoặc gần như
      không kết nối với cộng đồng đã có chỉ số rộng hơn, thì con số của bạn một phần là lời phát biểu về môi
      trường quanh bạn. Hai người cùng mặt bằng ở hai cộng đồng khác nhau không nhất thiết cho ra cùng một con
      số, và cả hai đều chẳng thể làm gì ngoài việc chơi thêm nhiều ván với người ngoài.</p>

      <h2>Chỉ số tuyệt đối là gì</h2>
      <p>Một chỉ số tuyệt đối đo thành tích so với một chuẩn cố định thay vì so với con người. Điểm chấp trong
      golf vận hành như vậy so với par. Điền kinh vận hành như vậy so với đồng hồ bấm giờ. Chiếc đồng hồ bấm
      giờ không quan tâm còn ai khác trên đường chạy, và 10,4 giây ở Manila cũng là 10,4 giây ở Manchester.</p>
      <p>Bi-a theo truyền thống không có thứ như vậy, bởi bi-a thiếu một chiếc đồng hồ hiển nhiên. Runout Rank
      cung cấp thứ tương đương: một bộ thế bi đã định nghĩa và một câu hỏi &mdash; bạn có dọn sạch được không?
      Mười ván ở một cấp độ, mỗi ván một lần, không đánh lại và không bỏ qua. Con số cho ra được tính hoàn
      toàn từ kết quả của chính bạn trước các thế bi đó.</p>
      <p>Vậy nên không có nhóm đối thủ nào để mạnh hay yếu, không có gì để trôi dạt theo, và không có số ván
      tối thiểu nào trước khi phép đo có hiệu lực. Bạn có chỉ số của mình ngay khi kết thúc buổi đầu tiên, và
      nó mang cùng ý nghĩa ở bất cứ đâu.</p>

      <h2>Làm sao một chuẩn cố định tránh được việc trở thành bài kiểm tra trí nhớ</h2>
      <p>Phản biện hiển nhiên: một bộ thế bi cố định sẽ thôi đo kỹ năng ngay khi bạn đã chơi nó vài lần, vì khi
      đó bạn đang nhớ lại lời giải chứ không phải đi tìm nó.</p>
      <p>Runout Rank tránh điều đó bằng cách cố định <em>độ khó</em> chứ không cố định các ván. Một cấp độ là
      một bộ hằng số được công bố &mdash; số bi mục tiêu, có đặt bi cái tự do hay không, khoảng cách tối thiểu,
      bi cản &mdash; và thế bi được tạo mới bên trong những quy tắc đó mỗi lần. Bạn không bao giờ thấy cùng
      một ván hai lần, và mọi ván đều đặt ra cùng một câu hỏi. Mười ván liên tiếp sẽ san đều phần may rủi còn
      lại.</p>

      <h2>Điều một chỉ số tuyệt đối không làm được</h2>
      <p>Nó không phải hệ thống chấp điểm, và không nên được dùng như vậy. Một chỉ số tương đối tồn tại để dự
      đoán một trận đấu giữa hai người cụ thể, và nó làm việc đó tốt hơn hẳn bất kỳ phép đo tuyệt đối nào
      &mdash; bởi kết quả các trận đấu chính là thứ nó được dựng nên từ đó.</p>
      <p>Một chỉ số tuyệt đối cũng có biến số của riêng nó cần thành thật: thiết bị. Kiểu cắt lỗ, kích thước
      bàn và tốc độ mặt nỉ đều làm thay đổi độ khó của một lượt dọn bàn, nên một chỉ số lấy trên bàn chín feet
      lỗ hẹp là một phép đo khác với chỉ số lấy trên bàn nhỏ trong quán. Hãy cố định điều kiện của bạn, làm bài
      kiểm tra trên chiếc bàn bạn thi đấu, và so sánh các con số của riêng bạn theo thời gian.</p>

      <h2>Bạn muốn loại nào?</h2>
      <div class="compare" style="margin:24px 0">
        <div class="card">
          <h3>Dùng chỉ số tương đối khi</h3>
          <ul class="ticks">
            <li>Bạn cần một mức chấp cho một trận đấu hoặc một nhánh giải</li>
            <li>Giải đấu của bạn yêu cầu phải có</li>
            <li>Bạn vốn đã chơi đủ nhiều ván tính điểm để giữ nó luôn vững</li>
          </ul>
        </div>
        <div class="card card--gold">
          <h3>Dùng chỉ số tuyệt đối khi</h3>
          <ul class="ticks ticks--gold">
            <li>Bạn muốn biết mình đang ở đâu mà không phải chơi trọn một mùa trước đã</li>
            <li>Bạn luyện tập một mình, đi lại nhiều, hoặc chuyển giữa các cộng đồng</li>
            <li>Bạn muốn biết <em>nên luyện gì</em>, chứ không chỉ mình xếp thứ mấy</li>
          </ul>
        </div>
      </div>
      <p>Chúng trả lời những câu hỏi khác nhau, và một người chơi nghiêm túc hoàn toàn có thể mang cả hai.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="fargo-rate-alternative.html">So sánh với Fargo Rate</a>
        <a class="btn btn--ghost" href="how-it-works.html">Chỉ số được tính thế nào</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

FAQ_ITEMS = [
    ("Tôi có cần một bàn bi-a thật để dùng Runout Rank không?",
     "Có. Runout Rank không phải một trò chơi bi-a &mdash; nó là người bạn đồng hành của một chiếc bàn thật. "
     "Ứng dụng vẽ từng thế bi từ trên xuống, bạn sắp lại trên mặt nỉ trước mặt mình, chơi nó, rồi ghi lại "
     "điều đã xảy ra."),
    ("Tôi có cần tài khoản hay kết nối Internet không?",
     "Không, cả hai đều không. Không có gì để đăng ký và không có gì để đăng nhập, và ứng dụng chạy hoàn toàn "
     "ngoại tuyến. Các bài kiểm tra, lượt thử, mục yêu thích và thống kê của bạn chỉ nằm trong bộ nhớ riêng "
     "của ứng dụng trên thiết bị của chính bạn."),
    ("Chỉ số được tính như thế nào?",
     "Bạn chơi mười thế bi được tạo ra ở cùng một cấp độ, mỗi thế một lần. Điểm số trên mười được quy thành "
     "chỉ số 0&ndash;100 kèm một hạng có tên gọi, và bảy trên mười là vượt qua cấp độ. Kết quả cũng cho thấy "
     "chỉ số của bạn đã dịch chuyển bao nhiêu so với bài kiểm tra trước."),
    ("Nếu các bài kiểm tra là ngẫu nhiên, làm sao so sánh được hai điểm số?",
     "Bởi thứ cố định là cấp độ, không phải các thế bi. Mỗi cấp độ định nghĩa số bi mục tiêu, việc bạn có được "
     "đặt bi cái tự do hay không, khoảng cách tối thiểu giữa các bi và số bi cản, và những hằng số đó giống "
     "hệt nhau với mọi người chơi trên cả hai nền tảng. Thế bi được tạo mới bên trong các quy tắc ấy, và mười "
     "ván liên tiếp san đều phần may rủi &mdash; nên bảy trên mười ở Level 4 mang cùng một ý nghĩa, bất kể ai "
     "đạt được nó."),
    ("Tôi có thể chơi lại một ván mình đã đánh hỏng không?",
     "Không, trong một bài kiểm tra &mdash; mỗi ván một lần, không đánh lại và không bỏ qua, và chính điều đó "
     "làm cho điểm số có ý nghĩa. Trong luyện tập tự do, bạn có thể chơi lại đúng thế bi đó bao nhiêu lần tùy "
     "thích."),
    ("Điều gì xảy ra nếu tôi bị gián đoạn giữa bài kiểm tra?",
     "Bài kiểm tra tiếp tục đúng ở ván bạn đã dừng lại. Nếu bạn chủ động thoát, ứng dụng sẽ hỏi xác nhận trước "
     "và giải thích rằng một lượt chơi dở dang thì không thể chấm điểm."),
    ("Tôi có phải bắt đầu từ Level 1 không?",
     "Không. Không có gì bị khóa cả. Bạn có thể làm bài kiểm tra ở bất kỳ cấp nào trong sáu cấp độ, và làm lại "
     "bất kỳ cấp nào bạn đã kiểm tra."),
    ("&ldquo;Cấp độ giới hạn&rdquo; của tôi là gì?",
     "Là cấp độ hiện đang chặn bạn lại &mdash; bậc cao nhất mà bạn chưa vượt qua được. Đó là cấp đáng luyện "
     "tập nhất, và cả màn hình kết quả lẫn màn hình Rank đều cho bạn nhảy thẳng vào đó."),
    ("Runout Pro giá bao nhiêu, và nó bổ sung những gì?",
     "Runout Pro là gói đăng ký tùy chọn theo tháng hoặc theo năm, do cửa hàng của bạn định giá bằng đơn vị "
     "tiền tệ của chính bạn. Nó bổ sung phần lịch sử: chỉ số của bạn vẽ thành đồ thị qua mọi bài kiểm tra, "
     "diễn tiến điểm số theo từng cấp độ, tỷ lệ dọn bàn theo thời gian, nhật ký kiểm tra đầy đủ, và xuất file "
     "CSV. Mọi thứ cho bạn biết bạn đang ở đâu ngay lúc này thì vẫn miễn phí."),
    ("Lịch sử của tôi có an toàn khi ứng dụng cập nhật không?",
     "Có. Các bài kiểm tra, lượt thử và mục yêu thích hiện có của bạn được giữ lại qua các lần cập nhật ứng "
     "dụng. Vì dữ liệu nằm ở máy, việc gỡ cài đặt ứng dụng hoặc xóa dữ liệu của nó sẽ xóa mất chúng."),
    ("Cái này khác Fargo Rate ở chỗ nào?",
     "Fargo Rate là một chỉ số tương đối: nó tính con số của bạn từ kết quả đối đầu với những người chơi đã có "
     "chỉ số, và đó là lý do FargoRate xem 200 ván là độ vững tối thiểu để một chỉ số được coi là đã xác lập, "
     "cũng như lý do một cộng đồng địa phương kết nối lỏng lẻo có thể trôi dạt so với phần còn lại của mạng "
     "lưới. Runout Rank thì tuyệt đối &mdash; nó đo bạn với các thế bi cố định được tạo ra, nên một buổi mười "
     "ván cho bạn một chỉ số đầy đủ và không nhóm đối thủ nào ảnh hưởng tới nó. Nó không phải hệ thống chấp "
     "điểm và không thay thế chỉ số giải đấu trong việc chấp điểm trận đấu."),
    ("Tôi cần chơi bao nhiêu ván thì chỉ số Runout Rank của tôi mới có ý nghĩa?",
     "Mười ván &mdash; một bài kiểm tra, khoảng một giờ. Không có giai đoạn đủ điều kiện và không có giai đoạn "
     "tạm tính, bởi chỉ số được tính từ các lượt dọn bàn của bạn trước những thế bi đã định nghĩa, chứ không "
     "phải từ lịch sử kết quả đối đầu với người chơi khác."),
    ("Nơi tôi sống có ảnh hưởng tới chỉ số của tôi không?",
     "Không. Các ràng buộc của mọi cấp độ đều là những hằng số như nhau ở khắp nơi, và không đối thủ nào tham "
     "gia vào phép tính. Biến số địa phương duy nhất là thiết bị của bạn: kiểu cắt lỗ, kích thước bàn và tốc "
     "độ mặt nỉ làm thay đổi độ khó của một lượt dọn bàn, nên hãy làm bài kiểm tra trên chính chiếc bàn bạn "
     "vẫn chơi và so sánh các con số của riêng bạn theo thời gian."),
    ("Tôi có thể dùng Runout Rank cùng với một chỉ số giải đấu không?",
     "Có, và đó là điều hợp lý nên làm nếu bạn có chơi giải. Hãy giữ chỉ số giải đấu để chấp điểm các trận đấu, "
     "và dùng bài kiểm tra dọn bàn để tìm ra cấp độ nào đang chặn bạn và luyện tập ở đó &mdash; điều mà một "
     "chỉ số dựa trên kết quả trận đấu không thể cho bạn biết."),
    ("Runout Rank có giống nhau trên Android và iOS không?",
     "Có. Định nghĩa các cấp độ, bộ tạo thế bi và phép toán tính chỉ số đều là mã dùng chung chạy trên cả hai "
     "nền tảng, nên chiếc điện thoại bạn sở hữu không ảnh hưởng gì tới chỉ số của bạn."),
]

FAQ_BODY_ITEMS = faq_body(FAQ_ITEMS)
FAQ_SCHEMA = faq_schema(FAQ_ITEMS)

FAQ = f"""  <section class="page-head">
    <div class="container">
{breadcrumb(UI, "Hỏi đáp")}
      <h1>Câu hỏi thường gặp</h1>
      <p class="lead">Bài kiểm tra, chỉ số, các cấp độ, gói đăng ký và dữ liệu của bạn.</p>
    </div>
  </section>

  <section>
    <div class="container" style="max-width:52rem">
{FAQ_BODY_ITEMS}
      <p style="margin-top:28px">Vẫn chưa rõ con số ấy được tạo ra thế nào?
      <a href="how-it-works.html">Đọc cách chỉ số hoạt động &rarr;</a></p>
    </div>
  </section>

{CTA}
"""

NOT_FOUND = """  <section class="page-head">
    <div class="container">
      <h1>Ván bi đó chưa được sắp</h1>
      <p class="lead">Trang bạn đang tìm không tồn tại. Đây là đường quay lại.</p>
      <div class="btn-row" style="margin-bottom:40px">
        <a class="btn btn--primary" href="index.html">Về trang chủ</a>
        <a class="btn btn--ghost" href="how-it-works.html">Bài kiểm tra diễn ra thế nào</a>
      </div>
    </div>
  </section>
"""


PAGES = [
    dict(slug="index.html",
         title="Runout Rank — Bài kiểm tra trình độ bi-a tuyệt đối cho Android và iOS",
         description="Có chỉ số bi-a thật chỉ trong một buổi, thay vì sau 200 ván đấu giải. Runout Rank đo "
                     "bạn với mười thế bi được tạo ra chứ không phải với các đối thủ quanh bạn, nên con số "
                     "0–100 mang cùng ý nghĩa ở mọi thành phố. Không cần giải đấu, không cần tài khoản, "
                     "chạy ngoại tuyến.",
         body=INDEX,
         schema=[app_schema(LOCALE, UI), site_schema(LOCALE, UI)],
         keywords="chỉ số bi-a tuyệt đối, thay thế fargo rate, kiểm tra trình độ bi-a, ứng dụng chấm điểm "
                  "bi-a, chỉ số bi-a không cần giải đấu, bài kiểm tra dọn bàn, ứng dụng luyện bi-a"),

    dict(slug="how-it-works.html",
         title="Chỉ số Runout Rank hoạt động thế nào — mười ván, mỗi ván một lần",
         description="Mười thế bi ngẫu nhiên ở cùng một cấp độ, mỗi thế một lần chơi, quy thành chỉ số bi-a "
                     "tuyệt đối 0–100 và một hạng. Thế bi mới ở mỗi bài kiểm tra, ràng buộc cấp độ cố định, "
                     "nên con số mang cùng ý nghĩa ở mọi thành phố.",
         body=HOW,
         schema=[breadcrumb_schema(LOCALE, UI, "Cách hoạt động", "how-it-works.html")]),

    dict(slug="levels.html",
         title="Sáu cấp độ — từ Rookie đến Master | Runout Rank",
         description="Rookie, Regular, League, Competitor, Advanced, Master. Điều gì thay đổi ở mỗi bậc thang "
                     "— số bi, đặt bi cái tự do, độ sát nhau và bi cản — và vì sao không cấp nào bị khóa.",
         body=LEVELS,
         schema=[breadcrumb_schema(LOCALE, UI, "Các cấp độ", "levels.html")]),

    dict(slug="practice.html",
         title="Luyện tập bi-a và một nhật ký ghi nhớ mọi thứ | Runout Rank",
         description="Vô số thế bi luyện tập được tạo ngẫu nhiên ở cấp độ bạn chọn, ghi lại bằng một chạm, "
                     "chơi lại và bỏ qua, mục yêu thích, cùng nhật ký đầy đủ mọi ván bạn từng chơi.",
         body=PRACTICE,
         schema=[breadcrumb_schema(LOCALE, UI, "Luyện tập", "practice.html")]),

    dict(slug="fargo-rate-alternative.html",
         dated=True,
         title=FARGO_ALT_TITLE + " | Runout Rank",
         description="Fargo Rate cần 200 ván thì chỉ số mới được xác lập, và một chỉ số tương đối luôn neo vào "
                     "những người quanh bạn. Runout Rank là chỉ số bi-a tuyệt đối từ một buổi mười ván — so "
                     "sánh cạnh nhau, một cách công bằng.",
         body=FARGO_ALT,
         schema=[article_schema(LOCALE, UI,
             FARGO_ALT_TITLE,
             "Vì sao một chỉ số giải đấu tương đối cần 200 ván để xác lập và dao động theo nhóm người chơi "
             "quanh bạn, một chỉ số dọn bàn tuyệt đối làm gì thay vào đó, và bạn muốn cái nào trong hai cái.",
             "fargo-rate-alternative.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "Giải pháp thay thế Fargo Rate", "fargo-rate-alternative.html")],
         published=UPDATED,
         keywords="thay thế fargo rate, giải pháp thay thế chỉ số fargo, ứng dụng chấm điểm bi-a, chỉ số bi-a "
                  "tuyệt đối, fargo rate 200 ván, chỉ số fargo đã xác lập, độ chính xác fargo rate"),

    dict(slug="pool-rating-without-a-league.html",
         dated=True,
         title=NO_LEAGUE_TITLE + " | Runout Rank",
         description="Mọi chỉ số giải đấu đều đòi hàng trăm trận đấu với người chơi đã có chỉ số thì con số mới "
                     "là thật. Đây là cách một người chơi phong trào hoặc chơi một mình có được chỉ số bi-a "
                     "0–100 trung thực chỉ trong một buổi, trên chính chiếc bàn của mình.",
         body=NO_LEAGUE,
         schema=[article_schema(LOCALE, UI,
             NO_LEAGUE_TITLE,
             "Cách một người chơi phong trào hoặc chơi một mình có được chỉ số bi-a trung thực trong một buổi "
             "mà không cần tham gia giải đấu hay chơi 200 ván tính điểm.",
             "pool-rating-without-a-league.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "Có chỉ số mà không cần giải đấu", "pool-rating-without-a-league.html")],
         published=UPDATED,
         keywords="chỉ số bi-a không cần giải đấu, cách có chỉ số bi-a, chỉ số cho người chơi bi-a phong trào, "
                  "chỉ số luyện bi-a một mình, được chấm điểm bi-a, đánh giá trình độ bi-a"),

    dict(slug="absolute-vs-relative-pool-rating.html",
         dated=True,
         title=ABSOLUTE_TITLE + " | Runout Rank",
         description="Elo, Glicko và Fargo Rate đều là tương đối: mỗi chỉ số là một vị trí trong mạng lưới các "
                     "chỉ số khác, nên cả số lượng ván đấu lẫn mức độ kết nối địa phương đều quan trọng. Một "
                     "chỉ số bi-a tuyệt đối đo gì thay vào đó, và mỗi loại tốt cho việc gì.",
         body=ABSOLUTE,
         schema=[article_schema(LOCALE, UI,
             ABSOLUTE_TITLE,
             "Vì sao chỉ số bi-a tương đối phụ thuộc vào những người quanh bạn, một chỉ số tuyệt đối đo gì thay "
             "vào đó, và loại nào trả lời câu hỏi nào.",
             "absolute-vs-relative-pool-rating.html", UPDATED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "Chỉ số tuyệt đối và tương đối", "absolute-vs-relative-pool-rating.html")],
         published=UPDATED,
         keywords="chỉ số bi-a tuyệt đối và tương đối, hệ thống chỉ số tương đối, chỉ số elo bi-a, "
                  "chênh lệch chỉ số fargo theo vùng, giải thích chỉ số bi-a"),

    dict(slug="runout-pro.html",
         title="Runout Pro — toàn bộ lịch sử chỉ số và xuất file CSV | Runout Rank",
         description="Bạn đang ở đâu thì miễn phí, vĩnh viễn. Runout Pro bổ sung việc bạn đến đó bằng cách nào: "
                     "chỉ số vẽ thành đồ thị qua mọi bài kiểm tra, diễn tiến theo từng cấp độ, nhật ký kiểm tra "
                     "đầy đủ và xuất file CSV.",
         body=PRO,
         schema=[breadcrumb_schema(LOCALE, UI, "Runout Pro", "runout-pro.html")]),

    dict(slug="pool-skill-level-test.html",
         dated=True,
         title=GUIDE_TITLE,
         description="Điều phân biệt một bài kiểm tra trình độ bi-a đáng làm với một bài tập bạn tình cờ thích: "
                     "trọn lượt dọn bàn, thế bi khó đoán, độ khó được định nghĩa, mỗi ván một lần chơi, và làm "
                     "gì với con số đó.",
         body=GUIDE,
         schema=[article_schema(LOCALE, UI,
             GUIDE_TITLE,
             "Điều phân biệt một bài kiểm tra trình độ bi-a đáng làm với một bài tập bạn tình cờ thích.",
             "pool-skill-level-test.html", FIRST_PUBLISHED, UPDATED),
             breadcrumb_schema(LOCALE, UI, "Kiểm tra trình độ bi-a", "pool-skill-level-test.html")],
         keywords="cách kiểm tra trình độ bi-a, kiểm tra trình độ bi-a, đánh giá kỹ năng bi-a, bài tập dọn bàn, "
                  "hệ thống chấm điểm bi-a"),

    dict(slug="faq.html",
         title="Hỏi đáp Runout Rank — bài kiểm tra, chỉ số, các cấp độ và dữ liệu của bạn",
         description="Có cần bàn thật không? Có cần giải đấu không? Chỉ số được tính thế nào, nó khác Fargo Rate "
                     "ra sao, và Runout Pro bổ sung những gì? Giải đáp các câu hỏi thường gặp.",
         body=FAQ,
         schema=[FAQ_SCHEMA, breadcrumb_schema(LOCALE, UI, "Hỏi đáp", "faq.html")]),
]
