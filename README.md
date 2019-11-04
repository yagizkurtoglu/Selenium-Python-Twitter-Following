# Selenium-Python-Twitter-Bot-Following
Python Selenium kütüphanesi ile takip ettiğin kullanıcıları diziye &amp; dosyaya kayıt etme. \n
Fonksiyonun kullanımı için Login koşulu vardır. \n
Tarayıcı (driver) default ingilizce ayarlarda başlatılmalır.
Login olan kullanıcı fonksiyona parametre olarak giden user'ın  Takipci listesine driver.get() ile erişir.
notFollowing dizisi içerisinde takipci öner kısımdaki 3 öneriyi tutar.
Twitter scrollu aşağı indirdikce yeni takipcileri ekler bu yüzden driver.execute_script() scripti kullanıldı. sayfayı sürekli en aşağı konuma ilerletir. 
temp değişkeni sayfa içerisindeki yüklenmiş olan takipci bilgilerini tutar.
5 kere ard arda following[] dizisinin boyutu değişmez ise scroll daha fazla aşağı inemiyor demektir ve buda bütün takip edilenler alınmış anlamını taşır. 


