# Selenium-Python-Twitter-Bot-Following
<p>Python Selenium k&uuml;t&uuml;phanesi ile takip ettiğin kullanıcıları diziye &amp; dosyaya kayıt etme. </p>
<ul>
<li>
<h4><span style="text-decoration: underline;"><strong>Fonksiyonun kullanımı i&ccedil;in Login koşulu vardır. </strong></span></h4>
</li>
<li>
<h4><span style="text-decoration: underline;"><strong>Tarayıcı (driver) default ingilizce ayarlarda başlatılmalır.</strong></span></h4>
</li>
<li>Login olan kullanıcı fonksiyona parametre olarak giden user'ın Takipci listesine <strong>driver.get()</strong> ile erişir.</li>
<li>notFollowing dizisi i&ccedil;erisinde takipci &ouml;ner kısımdaki 3 &ouml;neriyi tutar.</li>
<li>Twitter scrollu aşağı indirdikce yeni takipcileri ekler bu y&uuml;zden <strong>driver.execute_script()</strong> scripti kullanıldı. sayfayı s&uuml;rekli en aşağı konuma ilerletir. </li>
<li>temp değişkeni sayfa i&ccedil;erisindeki y&uuml;klenmiş olan takipci bilgilerini tutar.</li>
<li>5 kere ard arda following[] dizisinin boyutu değişmez ise scroll daha fazla aşağı inemiyor demektir ve buda b&uuml;t&uuml;n takip edilenler alınmış anlamını taşır.</li>
</ul>

