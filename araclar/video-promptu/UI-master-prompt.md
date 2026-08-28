# NotebookLM arayüzünden video üretimi — master prompt

**Nereye:** Notebook → Studio → **Videolu Özet** → sağdaki `>` oku → *"Videolu Özet'i özelleştirin"*

**Ayarlar:**

| Alan | Seçim |
|---|---|
| Biçim | **Açıklayıcı** |
| Dil seçin | **Türkçe** |
| Kaynaklar | 1 kaynak (master PDF) |
| Görsel stil seçin | **Özel** |

Sonra aşağıdaki iki metni ilgili kutulara yapıştır.

---

## KUTU 1 — "Özel bir görsel stil tanımlayın"

```
Resmî kurumsal tanıtım videosu. Erzurum Büyükşehir Belediyesi kurumsal kimliği: lacivert (#003C7E) ve beyaz, temiz ve ciddi kurumsal tasarım. Görsel malzeme YALNIZCA kaynak belgedeki gerçek yazılım arayüzü ekran görüntüleridir; her ekran görüntüsü tam ekran, büyük ve yazıları okunacak netlikte gösterilir. Belgede olmayan hiçbir arayüz, pano veya ekran görseli üretilmez, temsilî olarak yeniden çizilmez. Karikatür, çizgi film, kawaii, anime, suluboya, el çizimi üslubu ve emoji kullanılmaz. LOGO: Kaynak belgenin "KURUMSAL KİMLİK" sayfasında ve her bölüm ayracında yer alan Erzurum Büyükşehir Belediyesi logosu (lacivert Çifte Minareli Medrese amblemi ve altında ERZURUM BÜYÜKŞEHİR BELEDİYESİ yazısı) videoda aynen kullanılır. Yeni logo, arma, amblem veya rozet TASARLANMAZ; belgedeki logo değiştirilmez, yeniden çizilmez, stilize edilmez. Her bölümün başında sade, lacivert zeminli, bu logoyu taşıyan bir başlık kartı bulunur; alt şeritte ERZURUM BÜYÜKŞEHİR BELEDİYESİ · BİLGİ İŞLEM DAİRE BAŞKANLIĞI · AKILLI ŞEHİRLER ŞUBE MÜDÜRLÜĞÜ yazar.
```

---

## KUTU 2 — "Yapay zeka sunucuları neye odaklanmalı?"

```
KAYNAK: Tek bir master PDF — "EBB Akıllı Şehir Projeleri, Kurumsal Tanıtım Sunumu 2026", 69 sayfa. Sırasıyla kapak, KURUMSAL KİMLİK sayfası (resmî logo) ve sunum planı sayfası; ardından BÖLÜM 1'den BÖLÜM 11'e kadar numaralandırılmış on bir proje bölümü vardır. Her bölüm, bölüm ayracı sayfasıyla başlar ve o projenin özgün tanıtım sayfalarıyla devam eder.

1) DİL VE AĞIZ
Anlatım tamamen Türkçe ve resmî kurum dilidir. Birinci çoğul şahıs kullanılır: "Bilgi İşlem Daire Başkanlığı Akıllı Şehirler Şube Müdürlüğü olarak geliştirdiğimiz...", "Sistemimiz ... sağlamaktadır", "Uygulamamız ... sunmaktadır". Samimi sohbet dili, birinci tekil şahıs, espri, magazinsel anlatım ve gündelik ifadeler kullanılmaz.

2) ÜSLUP
Her cümle bilgi taşır. "Şimdi bakalım", "peki ya", "gördüğünüz gibi", "hayal edin", "gelin birlikte inceleyelim" gibi dolgu ve geçiş cümleleri kesinlikle kullanılmaz. Doğrudan sistemin ne yaptığı, hangi ihtiyacı çözdüğü ve hangi somut sonucu ürettiği anlatılır.

3) KAPSAM — EN KATI KURAL
On bir bölümün TAMAMI videoda yer alacaktır. Hiçbiri atlanmaz, hiçbiri tek cümleyle geçiştirilmez. Bölümler kaynak belgedeki numara ve adlarla, aynı sırayla anlatılır; projeler tematik başlıklar altında birleştirilmez, her projenin kendi numaralı bölümü ve kendi başlık kartı olur:

BÖLÜM 1 — ParkNet Akıllı Otopark Yönetim Sistemi (belgede 37 ekran görüntüsü) — EN AYRINTILI BÖLÜM
BÖLÜM 2 — AYKOME Kazı Ruhsat Yönetim Sistemi (4 ekran görüntüsü)
BÖLÜM 3 — Bozuk Yol Tespit Sistemi (6 ekran görüntüsü)
BÖLÜM 4 — Temizlik Yönetim Sistemi, TYS (17 ekran görüntüsü)
BÖLÜM 5 — BPBS Kim Kimdir? Belediye Personel Bilgi Sistemi (5 ekran görüntüsü)
BÖLÜM 6 — EBB AI Yapay Zekâ Destekli Taşınmaz Yönetim Sistemi (5 ekran görüntüsü)
BÖLÜM 7 — Uydu Pro Toplu Ulaşım Denetim ve Takip Sistemi (2 ekran görüntüsü)
BÖLÜM 8 — Ticari Araç Tescil ve Takip Sistemi (3 ekran görüntüsü)
BÖLÜM 9 — Erişim Kontrol ve İzleme Sistemi (4 ekran görüntüsü)
BÖLÜM 10 — İmar Planlama ve Takip Sistemi (2 ekran görüntüsü)
BÖLÜM 11 — ERTANSA Arıza Takip ve İş Emri Yönetim Sistemi (6 ekran görüntüsü)

4) EKRAN GÖRÜNTÜLERİ — MUTLAK KURAL
Kaynak belgede toplam 91 adet gerçek yazılım arayüzü ekran görüntüsü vardır. Videonun görsel akışı yalnızca bu gerçek ekran görüntüleri üzerine kurulur.
- Belgedeki ekran görüntülerinin TAMAMI kullanılır. Her bölümde o bölüme ait ekran görüntülerinin hepsi sırayla, tam ekran, büyük ve okunaklı biçimde gösterilir.
- Hiçbir proje, ekran görüntüsü gösterilmeden anlatılmaz.
- BELGEDE OLMAYAN EKRAN GÖRSELİ ÜRETİLMEZ. Hiçbir arayüz, pano, form, tablo, iş emri kartı veya uygulama ekranı uydurulmaz, yeniden çizilmez, temsilî olarak canlandırılmaz.
- İngilizce etiketli, uydurma kayıt numaralı veya belgedeki arayüzlere benzemeyen sahte ekran görselleri kesinlikle üretilmez.
- Ekran görüntüsünün yerine ikon, emoji, illüstrasyon veya soyut grafik konulmaz. Videoda emoji hiç kullanılmaz.
- LOGO: Belgedeki "KURUMSAL KİMLİK" sayfasında bulunan Erzurum Büyükşehir Belediyesi logosu aynen kullanılır. Yeni logo, arma veya amblem tasarlanmaz.

5) AĞIRLIK DAĞILIMI
ParkNet (Bölüm 1) videonun en uzun bölümüdür; diğer bölümlerin yaklaşık üç katı süre alır. İçeriğinde şunlar mutlaka bulunur: plaka tanıma ile otomatik giriş ve çıkış, internet kesintisinde dahi çalışabilme, abonelik ve ücretlendirme yönetimi, faturalama, kara liste, raporlama; ParkNet Desktop canlı giriş-çıkış kontrol ekranı ve kamera görüntüleri; web panelindeki günlük gelir, saatlik yoğunluk, anlık doluluk ve şubeler arası gelir karşılaştırması; hâlihazırdaki HOBİ yazılımıyla karşılaştırma ve mali tablo — birinci yıl sonunda 1.707.120 TL avantaj, 1.140.000 TL tutarındaki tek seferlik bedelin yaklaşık beş ayda geri kazanılması.
Diğer on bölüm birbirine yakın ve yeterli sürelerde, her biri en az üç dört cümlelik ayrıntıyla anlatılır; hiçbiri diğerinden belirgin biçimde kısa tutulmaz.
EBB AI bölümünde sistem genel hatlarıyla tanıtılır: yirmi ilçede 6.750 taşınmaz kaydı, günlük Türkçe ile sorgulama, otomatik liste ve resmî rapor üretimi.

6) KAPANIŞ
Video, Bölüm 11'in anlatımı bitince sona erer. "Bundan sonra ne yapacağız", "sıradaki adım ne olacak", "gelecek planlarımız", "geleceğin akıllı şehri" türünden ileriye dönük soru, temenni veya vizyon bölümü kesinlikle yer almaz. Kapanış, kurum kimliğini belirten tek cümlelik resmî bir bitiştir.
```

---

## Notlar

- **Kaynak:** master PDF `kaynaklar/master/EBB-Akilli-Sehir-Projeleri-Master-Sunum.pdf`
  (69 sayfa, 91 ekran görüntüsü, raster gömülü resmî logo). Notebook'ta tek kaynak olarak bulunmalı.
- Aynı promptu CLI'dan çalıştırmak için: `bash araclar/video-uret.sh ebb-master`
- **Bilinen sınır:** NotebookLM video özeti görselleri kendi üretir; kaynak belgedeki
  ekran görüntülerini bazen kullanır, bazen yerine kendi ürettiği temsilî arayüz
  görselini koyar. 4. maddedeki yasak bu riski azaltır ama tamamen ortadan
  kaldırdığı garanti edilemez. Üretilen videoyu bu açıdan kontrol et.
