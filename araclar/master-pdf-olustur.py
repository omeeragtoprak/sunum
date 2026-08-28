#!/usr/bin/env python
"""
EBB Akıllı Şehir Projeleri — Master Sunum PDF üreticisi.

NEDEN: NotebookLM'e 11 ayrı PDF verildiğinde anlatım sırasını kendi seçiyor ve
projelerin çoğunu atlıyor. Tek bir master PDF; kapak, içindekiler ve numaralı
bölüm ayraçlarıyla sırayı ve eksiksizliği yapısal olarak dayatır.

ÜRETTİĞİ YAPI:
  1. Kapak            — EBB logosu + daire/şube adı + başlık
  2. İçindekiler      — 11 proje, istenen sırada (anlatım sırası sinyali)
  3. Her proje için   — numaralı bölüm ayracı + projenin orijinal sayfaları
     (Otopark bölümüne 3 adet PNG ekran görüntüsü tam sayfa eklenir)

KULLANIM:  python araclar/master-pdf-olustur.py
ÇIKTI:     kaynaklar/master/EBB-Akilli-Sehir-Projeleri-Master-Sunum.pdf
"""
import os
import sys

import pymupdf

KAYNAK = "/Users/omer/Desktop/sunum/kaynaklar"
CIKTI_DIZIN = os.path.join(KAYNAK, "master")
CIKTI = os.path.join(CIKTI_DIZIN, "EBB-Akilli-Sehir-Projeleri-Master-Sunum.pdf")
LOGO = os.path.join(KAYNAK, "EBB_Logo.pdf")

LACIVERT = (0 / 255, 60 / 255, 126 / 255)      # #003C7E — EBB kurumsal mavi
GRI = (0.42, 0.45, 0.50)
ACIK_GRI = (0.90, 0.92, 0.95)
BEYAZ = (1, 1, 1)

FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

A4_W, A4_H = 595.0, 841.9

# Anlatım sırası — kullanıcının belirlediği öncelik sıralaması.
PROJELER = [
    ("OTOPARK SUNUM (1).pdf",
     "ParkNet — Akıllı Otopark Yönetim Sistemi",
     "Plaka tanıma ile girişten çıkışa, ödemeden faturaya kadar tek platformdan "
     "otopark yönetimi. İnternet kesilse dahi çalışan yerli çözüm."),

    ("AYKOME-Kazi-Ruhsat-Yonetici-Ozeti.pdf",
     "AYKOME Kazı Ruhsat Yönetim Sistemi",
     "Şehrin tüm altyapı kazıları tek dijital platformda: başvuru, onay süreci ve "
     "harita üzerinden anlık izleme."),

    ("BozukYolTespit_Tanitim.pdf",
     "Bozuk Yol Tespit Sistemi",
     "Belediye araçları günlük görevini yaparken yolu tarar; görüntü tanıma ile "
     "çukur ve çatlağı bulur, haritaya işler, ekibe atar."),

    ("TYS_Tanitim.pdf",
     "Temizlik Yönetim Sistemi (TYS)",
     "Şehir genelindeki temizlik hizmetinin merkezi planlanması, sahadan yönetimi "
     "ve anlık takibi. Web paneli ve amir mobil uygulaması."),

    ("BPBS_Kim_Kimdir_Yonetici_Ozeti.pdf",
     "BPBS — Kim Kimdir? Belediye Personel Bilgi Sistemi",
     "11 iştirak şirketinin 5.345 personel kaydı tek arama ekranında; görev ve "
     "iletişim bilgisine saniyeler içinde erişim."),

    ("EBB_AI_Emlak_Istimlak_Yonetim_Ozeti.pdf",
     "EBB AI — Yapay Zekâ Destekli Taşınmaz Yönetim Sistemi",
     "6.750 taşınmaz kaydı tek ekranda; günlük Türkçe ile soru sorularak liste ve "
     "resmî rapor üretimi."),

    ("uydupro-tanitim.pdf",
     "Uydu Pro — Toplu Ulaşım Denetim ve Takip Sistemi",
     "Denetimin fotoğraf ve videosuyla kaydı, yönetmelikten otomatik ceza puanı, "
     "tutanak üretimi ve encümen/disiplin akışı."),

    ("Ticari_Arac_Tescil_Sistemi_Yonetici_Ozeti.pdf",
     "Ticari Araç Tescil ve Takip Sistemi",
     "Taksi, minibüs, servis, okul ve hat araçlarının kaydı, devri ve resmî "
     "evrakının tek merkezden yönetimi."),

    ("erisim-kontrol-rapor-v11.pdf",
     "Erişim Kontrol ve İzleme Sistemi",
     "Web siteleri, sunucular, PDKS cihazları, LED ekranlar, IP telefonlar ve "
     "UPS'lerin SNMP ile 7/24 proaktif izlenmesi."),

    ("Imar_Planlama_ve_Takip_Sistemi.pdf",
     "İmar Planlama ve Takip Sistemi",
     "İmar süreçlerinin harita üzerinde görüntülenmesi, kayıt oluşturma, onay "
     "takibi ve arşiv yönetimi."),

    ("Ertansa-Ariza-Takip-Tanitim.pdf",
     "ERTANSA Arıza Takip ve İş Emri Yönetim Sistemi",
     "58 birim ve şubede arıza bildiriminden kapanışa kadar tek akış; 592 işlenen "
     "arıza kaydı."),
]

# Otopark bölümüne eklenecek ek ekran görüntüleri (PNG).
OTOPARK_GORSELLERI = [
    ("otoparkgorsel.png",
     "ParkNet — Sisteme Giriş Ekranı",
     "Plaka tanıma teknolojisi ile bariyer kontrolü ve yetkili kullanıcı girişi."),
    ("desktop.png",
     "ParkNet Desktop — Canlı Giriş/Çıkış Kontrol Ekranı",
     "Giriş ve çıkış kameraları, okunan plakalar, ücret hesabı, manuel bariyer "
     "kontrolü ve anlık geçiş listesi tek ekranda."),
    ("web.png",
     "ParkNet Web Paneli — Gelir ve Doluluk Gösterge Panosu",
     "Günlük gelir kırılımı, son 7 gün cirosu, saatlik giriş yoğunluğu, anlık "
     "doluluk ve şubeler arası gelir karşılaştırması."),
]


def font_ekle(sayfa):
    """Sayfaya Türkçe karakter destekli fontları tanıtır."""
    sayfa.insert_font(fontname="TR", fontfile=FONT)
    sayfa.insert_font(fontname="TRB", fontfile=FONT_BOLD)


def yaz(sayfa, metin, x, y, boyut, renk=(0, 0, 0), kalin=False, genislik=None,
        hiza=0, satir_araligi=1.35):
    """Metni kutuya yerleştirir; sığmazsa punto düşürerek dener."""
    fnt = "TRB" if kalin else "TR"
    if genislik is None:
        genislik = A4_W - 2 * x
    for punto in [boyut, boyut * 0.92, boyut * 0.85, boyut * 0.78]:
        kutu = pymupdf.Rect(x, y, x + genislik, y + 400)
        sonuc = sayfa.insert_textbox(
            kutu, metin, fontname=fnt, fontsize=punto, color=renk,
            align=hiza, lineheight=satir_araligi)
        if sonuc >= 0:
            return punto
    return boyut


def logo_bas(sayfa, hedef):
    """EBB logosunu vektör olarak verilen dikdörtgene basar."""
    if not os.path.exists(LOGO):
        return
    with pymupdf.open(LOGO) as lg:
        sayfa.show_pdf_page(hedef, lg, 0)


def kapak_olustur(doc):
    s = doc.new_page(width=A4_W, height=A4_H)
    font_ekle(s)

    # Üst lacivert bant
    s.draw_rect(pymupdf.Rect(0, 0, A4_W, 8), color=None, fill=LACIVERT)

    logo_bas(s, pymupdf.Rect(A4_W / 2 - 70, 70, A4_W / 2 + 70, 210))

    yaz(s, "T.C.", 60, 235, 11, GRI, kalin=True, hiza=1)
    yaz(s, "ERZURUM BÜYÜKŞEHİR BELEDİYESİ", 60, 252, 15, LACIVERT, kalin=True, hiza=1)
    yaz(s, "BİLGİ İŞLEM DAİRE BAŞKANLIĞI", 60, 276, 12, LACIVERT, kalin=True, hiza=1)
    yaz(s, "AKILLI ŞEHİRLER ŞUBE MÜDÜRLÜĞÜ", 60, 294, 12, LACIVERT, kalin=True, hiza=1)

    s.draw_line(pymupdf.Point(A4_W / 2 - 110, 330), pymupdf.Point(A4_W / 2 + 110, 330),
                color=LACIVERT, width=1.6)

    yaz(s, "AKILLI ŞEHİR PROJELERİ", 45, 372, 31, LACIVERT, kalin=True, hiza=1)
    yaz(s, "Kurumsal Tanıtım Sunumu", 60, 424, 17, (0.2, 0.2, 0.2), hiza=1)

    yaz(s, "Şube Müdürlüğümüz bünyesinde geliştirilen 11 yazılım projesinin "
           "bütünleşik tanıtım dosyası",
        90, 460, 11, GRI, genislik=A4_W - 180, hiza=1)

    # Alt bilgi şeridi
    s.draw_rect(pymupdf.Rect(0, A4_H - 96, A4_W, A4_H), color=None, fill=ACIK_GRI)
    yaz(s, "11 PROJE  ·  TEK BÜTÜNLEŞİK SUNUM  ·  2026",
        60, A4_H - 70, 12, LACIVERT, kalin=True, hiza=1)
    yaz(s, "Tüm projeler öz kaynaklarımızla, kendi personelimiz tarafından geliştirilmiştir.",
        60, A4_H - 48, 9.5, GRI, hiza=1)
    return s


def icindekiler_olustur(doc):
    s = doc.new_page(width=A4_W, height=A4_H)
    font_ekle(s)

    s.draw_rect(pymupdf.Rect(0, 0, A4_W, 74), color=None, fill=LACIVERT)
    yaz(s, "SUNUM PLANI VE PROJE SIRASI", 48, 26, 16, BEYAZ, kalin=True)
    yaz(s, "Projeler bu sırayla tanıtılmaktadır", 48, 48, 9.5, (0.82, 0.87, 0.93))

    y = 96
    for i, (_, baslik, ozet) in enumerate(PROJELER, start=1):
        # Numara rozeti — y1 mutlak değil, y'ye göreli olmalı (ters dikdörtgen hatası)
        s.draw_rect(pymupdf.Rect(46, y - 3, 72, y + 21), color=None, fill=LACIVERT,
                    radius=0.18)
        yaz(s, f"{i}", 46, y + 2, 12, BEYAZ, kalin=True, genislik=26, hiza=1)

        yaz(s, baslik, 84, y, 11.2, LACIVERT, kalin=True, genislik=A4_W - 130)
        yaz(s, ozet, 84, y + 15, 8.3, GRI, genislik=A4_W - 130, satir_araligi=1.25)

        y += 62
        if i < len(PROJELER):
            s.draw_line(pymupdf.Point(46, y - 13), pymupdf.Point(A4_W - 46, y - 13),
                        color=ACIK_GRI, width=0.8)

    yaz(s, "Bilgi İşlem Daire Başkanlığı · Akıllı Şehirler Şube Müdürlüğü",
        48, A4_H - 42, 8.5, GRI, hiza=1)
    return s


def ayrac_olustur(doc, no, baslik, ozet):
    s = doc.new_page(width=A4_W, height=A4_H)
    font_ekle(s)

    # Sol dikey lacivert şerit
    s.draw_rect(pymupdf.Rect(0, 0, 26, A4_H), color=None, fill=LACIVERT)

    logo_bas(s, pymupdf.Rect(A4_W - 118, 52, A4_W - 54, 116))

    yaz(s, f"BÖLÜM {no}", 62, 300, 11, GRI, kalin=True)

    # Büyük bölüm numarası
    s.insert_text(pymupdf.Point(60, 400), f"{no}", fontname="TRB", fontsize=76,
                  color=LACIVERT)

    s.draw_line(pymupdf.Point(62, 424), pymupdf.Point(A4_W - 62, 424),
                color=LACIVERT, width=1.4)

    yaz(s, baslik, 62, 444, 21, LACIVERT, kalin=True, genislik=A4_W - 124)
    yaz(s, ozet, 62, 516, 11.5, (0.25, 0.27, 0.30), genislik=A4_W - 124,
        satir_araligi=1.45)

    yaz(s, "ERZURUM BÜYÜKŞEHİR BELEDİYESİ", 62, A4_H - 78, 9, LACIVERT, kalin=True)
    yaz(s, "Bilgi İşlem Daire Başkanlığı · Akıllı Şehirler Şube Müdürlüğü",
        62, A4_H - 64, 8.5, GRI)
    return s


def gorsel_sayfasi(doc, png_yolu, baslik, aciklama):
    """PNG ekran görüntüsünü tam sayfa yerleştirir (16:9 yatay sayfa)."""
    G_W, G_H = 1440.0, 810.0
    s = doc.new_page(width=G_W, height=G_H)
    s.insert_font(fontname="TR", fontfile=FONT)
    s.insert_font(fontname="TRB", fontfile=FONT_BOLD)

    s.draw_rect(pymupdf.Rect(0, 0, G_W, G_H), color=None, fill=(1, 1, 1))
    s.draw_rect(pymupdf.Rect(0, 0, G_W, 74), color=None, fill=LACIVERT)

    s.insert_textbox(pymupdf.Rect(46, 16, G_W - 46, 44), baslik,
                     fontname="TRB", fontsize=19, color=BEYAZ)
    s.insert_textbox(pymupdf.Rect(46, 44, G_W - 46, 68), aciklama,
                     fontname="TR", fontsize=10.5, color=(0.82, 0.87, 0.93))

    with pymupdf.open(png_yolu) as im:
        pw, ph = im[0].rect.width, im[0].rect.height

    ust, alt, yan = 94, 44, 52
    kul_w, kul_h = G_W - 2 * yan, G_H - ust - alt
    olcek = min(kul_w / pw, kul_h / ph)
    w, h = pw * olcek, ph * olcek
    x0, y0 = (G_W - w) / 2, ust + (kul_h - h) / 2

    hedef = pymupdf.Rect(x0, y0, x0 + w, y0 + h)
    s.draw_rect(pymupdf.Rect(x0 - 1.5, y0 - 1.5, x0 + w + 1.5, y0 + h + 1.5),
                color=(0.78, 0.81, 0.85), width=1.5)
    s.insert_image(hedef, filename=png_yolu)
    return s


def main():
    for yol in (LOGO, FONT, FONT_BOLD):
        if not os.path.exists(yol):
            print(f"HATA: bulunamadı → {yol}")
            return 1

    os.makedirs(CIKTI_DIZIN, exist_ok=True)
    doc = pymupdf.open()

    kapak_olustur(doc)
    icindekiler_olustur(doc)
    print("✓ kapak + içindekiler")

    for i, (dosya, baslik, ozet) in enumerate(PROJELER, start=1):
        kaynak_yolu = os.path.join(KAYNAK, dosya)
        if not os.path.exists(kaynak_yolu):
            print(f"✗ EKSİK KAYNAK: {dosya}")
            return 1

        ayrac_olustur(doc, i, baslik, ozet)
        onceki = doc.page_count
        with pymupdf.open(kaynak_yolu) as src:
            doc.insert_pdf(src)
        eklenen = doc.page_count - onceki

        ek = ""
        if i == 1:  # Otopark — ek ekran görüntüleri
            for png, pb, pa in OTOPARK_GORSELLERI:
                png_yolu = os.path.join(KAYNAK, png)
                if os.path.exists(png_yolu):
                    gorsel_sayfasi(doc, png_yolu, pb, pa)
                else:
                    print(f"  ! PNG bulunamadı: {png}")
            ek = f" + {len(OTOPARK_GORSELLERI)} ekran görüntüsü"

        print(f"✓ {i:>2}. {baslik[:52]:<52} {eklenen} sayfa{ek}")

    doc.set_metadata({
        "title": "EBB Akıllı Şehir Projeleri — Kurumsal Tanıtım Sunumu 2026",
        "author": "Erzurum Büyükşehir Belediyesi · Bilgi İşlem Daire Başkanlığı · "
                  "Akıllı Şehirler Şube Müdürlüğü",
        "subject": "11 akıllı şehir yazılım projesinin bütünleşik kurumsal tanıtımı",
        "keywords": "Erzurum, akıllı şehir, ParkNet, AYKOME, bozuk yol tespit, "
                    "temizlik yönetim, BPBS, EBB AI, Uydu Pro, ticari araç tescil, "
                    "erişim kontrol, imar, arıza takip",
    })

    doc.set_toc([[1, "Kapak", 1], [1, "Sunum Planı", 2]] +
                [[1, f"{i}. {b}", None] for i, (_, b, _) in enumerate(PROJELER, 1)]
                and doc.get_toc() or [])

    doc.save(CIKTI, garbage=3, deflate=True)
    n = doc.page_count
    doc.close()

    mb = os.path.getsize(CIKTI) / 1024 / 1024
    print(f"\n✓ MASTER PDF: {CIKTI}")
    print(f"  {n} sayfa · {mb:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
