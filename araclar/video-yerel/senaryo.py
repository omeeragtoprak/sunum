# -*- coding: utf-8 -*-
"""
Anlatım senaryosu — EBB Akıllı Şehir Projeleri tanıtım videosu.

KURALLAR (kullanıcı talebi):
  · Tamamen Türkçe, resmî kurum dili, birinci çoğul şahıs
  · Dolgu cümle yok — her cümle bilgi taşır
  · 11 projenin tamamı, eksiksiz
  · Otopark en ayrıntılı bölüm
  · Kapanışta "gelecek planları" bölümü yok

YAPI:  her bölüm için  {no, ad, kisa_ad, giris, kareler[]}
  giris    : bölüm başlık kartı üzerinde okunan metin
  kareler  : (görsel_anahtari, ekran_basligi, anlatim) üçlüleri
             görsel_anahtari  "sayfa:N"  → kaynak PDF'in N. sayfası render edilir
                              "gorsel:X" → çıkarılan X numaralı ekran görüntüsü
"""

ACILIS = {
    "baslik": "AKILLI ŞEHİR PROJELERİ",
    "alt": "Kurumsal Tanıtım Sunumu · 2026",
    "anlatim": (
        "Erzurum Büyükşehir Belediyesi Bilgi İşlem Daire Başkanlığı Akıllı Şehirler "
        "Şube Müdürlüğü olarak, kentimizin dijital dönüşümü kapsamında öz kaynaklarımızla "
        "geliştirdiğimiz on bir yazılım projesini tanıtıyoruz. Tüm sistemler kendi "
        "personelimiz tarafından tasarlanmış, kodlanmış ve hizmete alınmıştır."
    ),
}

KAPANIS = {
    "baslik": "TEŞEKKÜR EDERİZ",
    "alt": "Erzurum Büyükşehir Belediyesi · Bilgi İşlem Daire Başkanlığı · Akıllı Şehirler Şube Müdürlüğü",
    "anlatim": (
        "Bilgi İşlem Daire Başkanlığı Akıllı Şehirler Şube Müdürlüğü olarak, yerli yazılım "
        "çözümlerimizle Erzurum'a değer katmayı sürdürmekteyiz."
    ),
}

BOLUMLER = [
    # ─────────────────────────── 1 · PARKNET ───────────────────────────
    {
        "no": 1,
        "ad": "ParkNet — Akıllı Otopark Yönetim Sistemi",
        "kisa": "parknet",
        "giris": (
            "Birinci bölüm. ParkNet Akıllı Otopark Yönetim Sistemi. "
            "Otoparklarımızı girişten çıkışa, ödemeden faturaya kadar tek platformdan "
            "yöneten, internet kesilse dahi çalışmaya devam eden yerli çözümümüzdür."
        ),
        "kareler": [
            ("sayfa:1", "ParkNet Otopark Yönetim Sistemi",
             "ParkNet, otopark işletmeciliğinin tamamını tek yazılımda birleştiren "
             "sistemimizdir."),
            ("sayfa:2", "ParkNet nedir?",
             "Sistemimiz; aracın girişini plakasından tanır, süresini hesaplar, ücretini "
             "tahsil eder ve faturasını üretir. Bu işlemlerin tamamı operatör "
             "müdahalesine gerek kalmadan yürür."),
            ("sayfa:3", "ParkNet ne yapar? — Temel özellikler",
             "Plaka tanıma ile otomatik bariyer, ödeme ve elektronik fatura, tarife ve "
             "abonelik yönetimi, kara liste uygulaması, merkezî yönetim ve raporlama "
             "sistemimizin temel yetenekleridir. Tüm otoparklar tek panelden yönetilir; "
             "doluluk, gelir ve raporlar merkezden anlık izlenir."),
            ("gorsel:35", "Sisteme giriş ekranı",
             "Plaka tanıma teknolojimiz aracın plakasını okur, yetkiyi doğrular ve "
             "bariyeri açar. İşlem saniyeler içinde tamamlanır."),
            ("gorsel:36", "ParkNet Desktop — canlı giriş ve çıkış kontrolü",
             "Giriş ve çıkış kameralarının canlı görüntüsü, okunan plakalar, hesaplanan "
             "ücret ve anlık geçiş listesi tek ekranda toplanır. Görevli gerektiğinde "
             "manuel giriş, manuel çıkış ve bariyer açma işlemlerini buradan yapar."),
            ("gorsel:37", "Web paneli — gelir ve doluluk göstergeleri",
             "Yönetim paneli; günlük gelirin abonelik ve geçiş kırılımını, son yedi günün "
             "cirosunu, saatlik giriş yoğunluğunu, anlık doluluk oranını ve şubeler arası "
             "gelir karşılaştırmasını sunar."),
            ("sayfa:4", "Mevcut durum — HOBİ sisteminin eksikleri",
             "Hâlen kullanılan HOBİ yazılımı kurumumuza finansal ve operasyonel yük "
             "getirmektedir. Abone ve süre takibi zayıftır; tahsil edilemeyen gelir "
             "oluşmaktadır. Ücretsiz veya kaçak çıkışlar kayıt altına alınmamakta, "
             "merkezî denetim yapılamamaktadır."),
            ("sayfa:5", "HOBİ ve ParkNet karşılaştırması",
             "Karşılaştırma tablomuz iki sistemi kalem kalem ortaya koymaktadır. Merkezî "
             "yönetim, plaka tanıma, elektronik fatura, kara liste ve otomatik "
             "güncelleme özelliklerinin tamamı ParkNet'te bulunmaktadır."),
            ("sayfa:6", "Bir yıllık finansal etki",
             "Mali tablomuz şunu göstermektedir: iki yüz abone, aylık bin lira üzerinden "
             "yılda iki milyon dört yüz bin liralık gelir, tam takip sağlanamadığı için "
             "mevcut sistemde kaybolmaktadır. ParkNet'in bir milyon yüz kırk bin liralık "
             "tek seferlik bedeli yaklaşık beş ayda geri kazanılmakta, birinci yıl sonunda "
             "bir milyon yedi yüz yedi bin yüz yirmi lira avantaj oluşmaktadır."),
            ("sayfa:7", "Sonuç — Neden ParkNet?",
             "ParkNet; gelir kaybını durduran, denetimi merkezîleştiren ve dışa "
             "bağımlılığı ortadan kaldıran yerli çözümümüzdür."),
        ],
    },
    # ─────────────────────────── 2 · AYKOME ───────────────────────────
    {
        "no": 2,
        "ad": "AYKOME Kazı Ruhsat Yönetim Sistemi",
        "kisa": "aykome",
        "giris": (
            "İkinci bölüm. AYKOME Kazı Ruhsat Yönetim Sistemi. "
            "Şehrimizdeki tüm altyapı kazılarını tek dijital platformda planlayan, "
            "onaylayan ve harita üzerinden anlık izleyen sistemimizdir."
        ),
        "kareler": [
            ("gorsel:1", "Harita üzerinde kazı takibi",
             "Su, elektrik ve doğalgaz gibi farklı kurumların şehirde yaptığı kazılar "
             "eskiden dağınık ve elle yönetiliyordu. Sistemimiz sahadaki tüm kazıları "
             "harita üzerinde konumlarıyla birlikte göstermektedir."),
            ("gorsel:2", "Gösterge paneli",
             "Gösterge panelimiz tüm ruhsatların durumunu ve şehir geneli özeti tek "
             "bakışta sunar. Hangi kurumun nerede, hangi aşamada kazı yaptığı anında "
             "görülür."),
            ("gorsel:3", "Ruhsat listesi",
             "Tüm başvurular durumlarıyla birlikte listelenir; filtrelerle saniyeler "
             "içinde erişilir."),
            ("gorsel:4", "Ruhsat detayı ve onay akışı",
             "Ruhsat detayında mali ve çevre onayları, konum haritası ve iş akışı "
             "adımları bir arada bulunur. Başvurudan kapanışa kadar her adım kayıt "
             "altındadır ve kurumlar arası koordinasyon tek yerden sağlanır."),
        ],
    },
    # ─────────────────────── 3 · BOZUK YOL TESPİT ───────────────────────
    {
        "no": 3,
        "ad": "Bozuk Yol Tespit Sistemi",
        "kisa": "bozukyol",
        "giris": (
            "Üçüncü bölüm. Bozuk Yol Tespit Sistemi. "
            "Belediye araçlarımız günlük görevini yaparken şehrin yollarını tarayan, "
            "bozukluğu bulan, fotoğraflayan ve doğru ekibin önüne koyan yapay zekâ "
            "destekli sistemimizdir."
        ),
        "kareler": [
            ("gorsel:1", "Yönetim panosu",
             "Yönetim panomuz özet sayıları ve şehir haritasında fotoğraflı, önem "
             "dereceli tespitleri göstermektedir. Yol bozuklukları artık vatandaş "
             "şikâyetiyle değil, araçlarımızın günlük mesaisi sırasında kendiliğinden "
             "tespit edilmektedir."),
            ("gorsel:2", "Görüntü tanıma ile tespit",
             "Araç ön camına yerleştirilen kamera yol yüzeyini sürekli izler. Görüntü "
             "tanıma teknolojimiz çukur, çatlak ve benzeri bozuklukları kendiliğinden "
             "fark eder."),
            ("gorsel:3", "Tespit raporu",
             "Her bulgu; fotoğrafı, tam konumu, adresi ve önem derecesiyle birlikte "
             "anında kayda geçer."),
            ("gorsel:4", "İş listesi",
             "İş listemizde önem derecesi, durum, adres ve fotoğrafla tüm kayıtlar tek "
             "yerde toplanır. Her kayıt önem sırasına göre dizilir ve ilgili ekibe "
             "atanır."),
            ("gorsel:5", "Tespit kartı ve ekip ataması",
             "Tespit kartında fotoğraf üzerinde işaretlenmiş sorun, adres, ekip ataması "
             "ve saha notu bulunur. Onarım tamamlanana kadar kayıt izlenir."),
            ("gorsel:6", "Dönem raporu",
             "Dönem raporumuz özet sayıları, tür ve önem dağılımını, tarama kapsamını ve "
             "tam listeyi sunar. Yönetimimiz neyin bulunduğunu, neyin onarıldığını ve "
             "şehrin hangi bölgesinin ne zaman kontrol edildiğini tek ekrandan görür."),
        ],
    },
    # ───────────────────── 4 · TEMİZLİK YÖNETİM SİSTEMİ ─────────────────────
    {
        "no": 4,
        "ad": "Temizlik Yönetim Sistemi",
        "kisa": "tys",
        "giris": (
            "Dördüncü bölüm. Temizlik Yönetim Sistemi. "
            "Şehir genelindeki temizlik hizmetini tek merkezden planlayan, sahadan "
            "yöneten ve anlık takip eden bütünleşik platformumuzdur."
        ),
        "kareler": [
            ("gorsel:1", "Yönetim panosu",
             "Yüzlerce personelin, araç filosunun ve şehir genelindeki rotaların "
             "planlaması, ataması ve denetimi dijital ortama taşınmıştır. Personel, "
             "rotasyon, araç ve atama sayıları anlık olarak tek bakışta izlenir."),
            ("gorsel:2", "Canlı harita",
             "Rotalar, ekipler ve araçlar tek şehir haritasında gerçek konumlarıyla ve "
             "renk kodlu olarak izlenir."),
            ("gorsel:3", "Yol haritası",
             "Yüz otuz altı yolun tamamı harita üzerinde yol tipine göre renklendirilmiş "
             "biçimde görünür; toplam yüz elli dokuz kilometrelik yol ağı kapsanmaktadır."),
            ("gorsel:4", "Rotasyon haritası",
             "Rotasyonlar renkli yollarla harita üzerinde gösterilir; yeni rotasyon "
             "doğrudan harita üzerinden yol seçilerek tanımlanır."),
            ("gorsel:5", "Amir özel koşulları",
             "Belirli amirlerin belirli gün ve rotasyonlarda otomatik atanması için "
             "kurallar tanımlanabilmektedir."),
            ("gorsel:6", "Araç yönetimi",
             "Yirmi üç araçlık filomuz plaka, durum ve bakım bilgisiyle birlikte canlı "
             "olarak takip edilir."),
            ("gorsel:7", "İzin yönetimi",
             "İzin talepleri, onay süreçleri ve izin takvimi sistem üzerinden yürütülür; "
             "bekleyen ve onaylanan talepler ayrı ayrı izlenir."),
            ("gorsel:8", "Haftalık ve aylık görünüm",
             "Atamalar takvim üzerinde aylık ve haftalık özetlerle takip edilir."),
            ("gorsel:9", "Kanban planlama",
             "Vardiya bazlı kanban görünümü, otomatik atama algoritması ve doluluk oranı "
             "planlamayı kolaylaştırır."),
            ("gorsel:10", "Amir kontrol çizelgesi",
             "Günlük vardiya görevlilerinin amir bazlı kontrol çizelgesi tutulur."),
            ("gorsel:11", "Profesyonel PDF raporlar",
             "Aylık analiz, kural uyumu, doluluk ve algoritma önerileri tek tıkla rapora "
             "dönüştürülür."),
            ("gorsel:12", "Rapor kütüphanesi",
             "Personel, vardiya, izin, rotasyon ve araç raporları kategoriler hâlinde "
             "arşivlenir."),
            ("gorsel:13", "Günlük vardiya durumu",
             "Vardiya bazlı günlük personel kontrol çizelgesi ve doluluk oranı izlenir."),
            ("gorsel:14", "Yönetim panosu — anlık göstergeler",
             "Anlık gösterge kartları ile vardiya ve atama trendleri grafiklerle sunulur."),
            ("gorsel:15", "Amir mobil uygulaması — günlük özet",
             "Amir mobil uygulamamızda bugünkü vardiya, ekip ve atama bilgisi ana ekranda "
             "özetlenir."),
            ("gorsel:16", "Amir mobil uygulaması — haftalık dağılım",
             "Haftanın günlük atama dağılımı ve detayları sahadan görüntülenir."),
            ("gorsel:17", "Amir mobil uygulaması — saha kontrolü",
             "Sahada anlık görev kontrolü yapılır, görev doğrulanır ve fotoğraf eklenir."),
        ],
    },
    # ─────────────────────────── 5 · BPBS ───────────────────────────
    {
        "no": 5,
        "ad": "BPBS — Kim Kimdir? Belediye Personel Bilgi Sistemi",
        "kisa": "bpbs",
        "giris": (
            "Beşinci bölüm. Belediye Personel Bilgi Sistemi, kısa adıyla Kim Kimdir. "
            "Belediyemize bağlı on bir iştirak şirketinin tüm personelini tek ekranda "
            "toplayan kurumsal rehberimizdir."
        ),
        "kareler": [
            ("gorsel:2", "Kim Kimdir? — genel görünüm",
             "On bir iştirak şirketimizin beş bin üç yüz kırk beş personel kaydı tek "
             "arama kutusunda toplanmıştır. Personel bilgileri daha önce şirket şirket "
             "ayrı listelerde tutuluyor ve güncelliğini yitiriyordu."),
            ("gorsel:3", "Arama ekranı",
             "Kullanıcı bir ad yazdığı anda sonuçlar listelenir; istenirse arama tek bir "
             "şirkete daraltılır. İlgili personelin şirketi, departmanı, görevi ve "
             "iletişim bilgisi anında ekrana gelir."),
            ("gorsel:4", "Personel kartı",
             "Personel kartında kişinin kimlik, görev ve iletişim bilgileri düzenli "
             "biçimde toplanır; acil durum bilgisi de kartta yer alır."),
            ("gorsel:5", "Mobil kullanım",
             "Sistemimiz bilgisayar, tablet ve telefon üzerinden aynı hızda "
             "kullanılabilmektedir."),
            ("gorsel:6", "Yönetim paneli",
             "Yönetim panelinde on bir şirketin personel sayıları ve durumu tek tabloda "
             "izlenir. Her şirket kendi kayıtlarını günceller; kurum genelinde tek ve "
             "ortak bir rehber oluşur."),
        ],
    },
    # ─────────────────────────── 6 · EBB AI ───────────────────────────
    {
        "no": 6,
        "ad": "EBB AI — Yapay Zekâ Destekli Taşınmaz Yönetim Sistemi",
        "kisa": "ebbai",
        "giris": (
            "Altıncı bölüm. EBB AI Yapay Zekâ Destekli Taşınmaz Yönetim Sistemi. "
            "Belediyemize ait taşınmazların tamamını tek ekranda toplayan, personelin "
            "günlük Türkçe ile soru sorabildiği yapay zekâ destekli sistemimizdir."
        ),
        "kareler": [
            ("gorsel:2", "Ana ekran ve doğal dil sorgulama",
             "Sistemimizde yirmi ilçede altı bin yedi yüz elli taşınmaz kaydı "
             "bulunmaktadır; bunların altı bin yüz altmış yedisi tapuda kayıtlıdır. "
             "Kullanıcı sorusunu günlük Türkçe ile yazar; örneğin Yakutiye'deki arsaları "
             "listele ya da iki bin yirmi dörtte edinilen taşınmazlar."),
            ("gorsel:3", "Sorgu sonuçları",
             "Sistemimiz soruyu yazıldığı hâliyle anlar ve sonucu tablo, kısa yanıt veya "
             "resmî rapor olarak sunar."),
            ("gorsel:4", "Taşınmaz icmal cetveli",
             "Resmî raporlar saniyeler içinde üretilir; taşınmaz icmal cetveli doğrudan "
             "sistemden alınır."),
            ("gorsel:5", "Dönemsel değişiklik takibi",
             "İki dönemin tapu kayıtları karşılaştırılır; yeni edinilen ve elden çıkarılan "
             "taşınmazlar otomatik olarak listelenir."),
        ],
    },
    # ─────────────────────────── 7 · UYDU PRO ───────────────────────────
    {
        "no": 7,
        "ad": "Uydu Pro — Toplu Ulaşım Denetim ve Takip Sistemi",
        "kisa": "uydupro",
        "giris": (
            "Yedinci bölüm. Uydu Pro Toplu Ulaşım Denetim ve Takip Sistemi. "
            "Şehir içi toplu taşımada yapılan denetimlerin deliliyle birlikte kayda "
            "alındığı ve resmî işleme dönüştürüldüğü ortak çalışma ekranımızdır."
        ),
        "kareler": [
            ("gorsel:1", "Denetim kayıtları tek ekranda",
             "Denetim görevlisi ihlali fotoğraf ve videosuyla birlikte girer. Ceza puanı "
             "ve grubu yönetmelik tanımından otomatik işlenir. Bir sürücünün tüm kayıtları "
             "tek ekranda toplanır; gerektiğinde sürücü veya araç için yasak tanımlanır."),
            ("gorsel:2", "Resmî tutanak tek tuşla",
             "Resmî evrak tek tuşla oluşturulur; yazdırılır veya elektronik belge olarak "
             "alınır. Rapor, aracın bağlı olduğu şirkete göre encümene ya da disiplin "
             "kuruluna yönlendirilir."),
        ],
    },
    # ───────────────────── 8 · TİCARİ ARAÇ TESCİL ─────────────────────
    {
        "no": 8,
        "ad": "Ticari Araç Tescil ve Takip Sistemi",
        "kisa": "ticari",
        "giris": (
            "Sekizinci bölüm. Ticari Araç Tescil ve Takip Sistemi. "
            "Erzurum'daki tüm ticari araçların kaydını, devrini ve resmî evraklarını tek "
            "merkezden yöneten platformumuzdur."
        ),
        "kareler": [
            ("gorsel:1", "Kontrol paneli",
             "Taksi, minibüs, servis, okul ve hat araçlarının tamamı sistemimizde "
             "kayıtlıdır. Filo büyüklüğü, açık borç ve son işlemler tek bakışta "
             "görülmektedir."),
            ("gorsel:2", "Araç listesi",
             "Araç listesinde plaka, sahip, borç, durum ve geçerlilik bilgisi anında "
             "görünür; arama ve filtreyle saniyeler içinde erişilir."),
            ("gorsel:3", "Otomatik resmî evrak üretimi",
             "Önceden her plaka türü ayrı ve dağınık dosyalarla elle takip ediliyor, "
             "resmî yazılar tek tek hazırlanıyordu. Sistemimiz uygunluk belgesi gibi "
             "resmî çıktıları otomatik üretmektedir."),
        ],
    },
    # ───────────────────── 9 · ERİŞİM KONTROL ─────────────────────
    {
        "no": 9,
        "ad": "Erişim Kontrol ve İzleme Sistemi",
        "kisa": "erisim",
        "giris": (
            "Dokuzuncu bölüm. Erişim Kontrol ve İzleme Sistemi. "
            "Belediyemizin tüm bilişim altyapısını yedi gün yirmi dört saat esasıyla "
            "izleyen proaktif denetim platformumuzdur."
        ),
        "kareler": [
            ("gorsel:1", "Cihaz hiyerarşisi ve bağımlılık ağacı",
             "Sistemimiz; tüm web sitelerimizi, uygulama arayüzlerini, sanal ve fiziksel "
             "sunucuları, personel devam kontrol cihazlarını, bilgilendirme ekranlarını, "
             "internet protokollü telefonları ve sistem odası kesintisiz güç kaynaklarını "
             "izlemektedir. Cihazlar arasındaki topolojik bağımlılık ağaç yapısıyla "
             "yönetilir."),
            ("gorsel:2", "Canlı sistem ve servis tepki süreleri",
             "İzleme, ağ protokolleriyle saniyeler bazında yapılır. Kesinti ve "
             "yavaşlamalar milisaniyeler düzeyinde tespit edilir."),
            ("gorsel:3", "Akıllı bildirim ve sorumluluk matrisi",
             "Tespit edilen sorun, sorumluluk matrisi üzerinden ilgili teknik personele "
             "kısa mesaj ve elektronik posta ile iletilir."),
            ("gorsel:4", "Canlı izleme göstergeleri",
             "Böylece hata oluştuktan sonra şikâyet üzerine müdahale etme modeli ortadan "
             "kalkmış; sorunlar vatandaşlarımıza yansımadan çözülür hâle gelmiştir."),
        ],
    },
    # ───────────────────── 10 · İMAR PLANLAMA ─────────────────────
    {
        "no": 10,
        "ad": "İmar Planlama ve Takip Sistemi",
        "kisa": "imar",
        "giris": (
            "Onuncu bölüm. İmar Planlama ve Takip Sistemi. "
            "İmar süreçlerini harita üzerinde görüntüleme, kayıt oluşturma, onay takibi "
            "ve arşiv yönetimini tek ekranda birleştiren kurumsal platformumuzdur."
        ),
        "kareler": [
            ("gorsel:1", "Sistem ana ekranı",
             "Ana ekranımız güncel kayıt sayılarını, personel ve imar durum dağılımlarını "
             "sunar. Mecliste, komisyonda veya onay aşamasında olan dosyalar tek bakışta "
             "takip edilir."),
            ("gorsel:2", "Yeni imar kaydı oluşturma",
             "İlçe, mahalle ve ada-parsel bilgileri girilerek yeni kayıt açılır. Konum "
             "harita üzerinde işaretlenir; tapu türü ve ilgili personel atanarak kayıt "
             "sürece dâhil edilir."),
            ("gorsel:3", "Kayıt detayı ve süreç takibi",
             "Her imar kaydı için meclis karar tarihi, komisyon raporu, onay aşaması ve "
             "arşiv durumu tek kartta izlenir. Böylece vatandaşımız ve personelimiz imar "
             "durumunu saniyeler içinde öğrenmektedir."),
        ],
    },
    # ───────────────────── 11 · ERTANSA ARIZA TAKİP ─────────────────────
    {
        "no": 11,
        "ad": "ERTANSA Arıza Takip ve İş Emri Yönetim Sistemi",
        "kisa": "ertansa",
        "giris": (
            "On birinci bölüm. ERTANSA Arıza Takip ve İş Emri Yönetim Sistemi. "
            "Şubelerde ve marketlerde oluşan arızaların tek bir yerden bildirildiği, "
            "teknik ekip tarafından üstlenildiği ve kapanışına kadar takip edildiği "
            "kurumsal platformumuzdur."
        ),
        "kareler": [
            ("gorsel:2", "Arıza bildirim formu",
             "Elli sekiz bağlı birim ve şube, elli beş kayıtlı kullanıcı ve beş yüz "
             "doksan iki işlenen arıza kaydıyla sistemimiz aktif olarak kullanılmaktadır. "
             "Arızalar daha önce telefon ve mesaj gruplarından iletiliyor, talebin kime "
             "ulaştığı kayıt altında tutulmuyordu."),
            ("gorsel:3", "Şube kullanıcısının bildirim ekranı",
             "Şube kullanıcımız arızayı açıklamasıyla, fotoğrafıyla ve konumuyla birlikte "
             "sisteme girer."),
            ("gorsel:4", "Teknikerin iş listesi",
             "Teknikerimiz açık talepleri, üzerindeki aktif işleri ve ekibin devam eden "
             "işlerini tek listede görür."),
            ("gorsel:5", "Arıza detayı ve hedef süre takibi",
             "Arıza detayında hedef sürelere uyum, ilgili birim ve kişiler, atanan ekip "
             "ve yüklenen fotoğraflar bir arada bulunur."),
            ("gorsel:6", "Yönetim panosu",
             "Yönetim panomuz açık arıza sayısını, gün içinde açılan talepleri, kritik "
             "talepleri ve hedef süre aşımlarını özetler."),
        ],
    },
]
