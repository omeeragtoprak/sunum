#!/usr/bin/env python
"""
Aşama 1 — Kaynak PDF'lerden tüm ekran görüntülerini ve açıklamalarını çıkarır.

Her görsel için:
  - PNG dosyası (özgün çözünürlükte)
  - sayfa numarası, sayfadaki dikey konumu (anlatım sırası için)
  - hemen altındaki açıklama metni (varsa) — ekranda alt yazı olarak kullanılır

ÇIKTI: araclar/video-yerel/uretim/gorseller/  +  manifest.json
"""
import hashlib
import json
import os
import sys

import pymupdf

KOK = "/Users/omer/Desktop/sunum"
KAYNAK = os.path.join(KOK, "kaynaklar")
CIKTI = os.path.join(KOK, "araclar", "video-yerel", "uretim")
GORSEL_DIZIN = os.path.join(CIKTI, "gorseller")

# Görsel kabul eşiği — bundan küçükler ikon/logo sayılır.
MIN_W, MIN_H = 300, 180

# Anlatım sırası: (dosya, bölüm no, bölüm adı, kısa ad)
BOLUMLER = [
    ("OTOPARK SUNUM (1).pdf", 1,
     "ParkNet — Akıllı Otopark Yönetim Sistemi", "parknet"),
    ("AYKOME-Kazi-Ruhsat-Yonetici-Ozeti.pdf", 2,
     "AYKOME Kazı Ruhsat Yönetim Sistemi", "aykome"),
    ("BozukYolTespit_Tanitim.pdf", 3,
     "Bozuk Yol Tespit Sistemi", "bozukyol"),
    ("TYS_Tanitim.pdf", 4,
     "Temizlik Yönetim Sistemi", "tys"),
    ("BPBS_Kim_Kimdir_Yonetici_Ozeti.pdf", 5,
     "BPBS — Kim Kimdir? Belediye Personel Bilgi Sistemi", "bpbs"),
    ("EBB_AI_Emlak_Istimlak_Yonetim_Ozeti.pdf", 6,
     "EBB AI — Yapay Zekâ Destekli Taşınmaz Yönetim Sistemi", "ebbai"),
    ("uydupro-tanitim.pdf", 7,
     "Uydu Pro — Toplu Ulaşım Denetim ve Takip Sistemi", "uydupro"),
    ("Ticari_Arac_Tescil_Sistemi_Yonetici_Ozeti.pdf", 8,
     "Ticari Araç Tescil ve Takip Sistemi", "ticari"),
    ("erisim-kontrol-rapor-v11.pdf", 9,
     "Erişim Kontrol ve İzleme Sistemi", "erisim"),
    ("Imar_Planlama_ve_Takip_Sistemi.pdf", 10,
     "İmar Planlama ve Takip Sistemi", "imar"),
    ("Ertansa-Ariza-Takip-Tanitim.pdf", 11,
     "ERTANSA Arıza Takip ve İş Emri Yönetim Sistemi", "ertansa"),
]

# Otopark bölümüne eklenen ayrı PNG ekran görüntüleri.
EK_PNG = [
    ("otoparkgorsel.png", "ParkNet sisteme giriş ekranı — plaka tanıma ile bariyer kontrolü"),
    ("desktop.png", "ParkNet Desktop — canlı giriş/çıkış kontrol ekranı ve kamera görüntüleri"),
    ("web.png", "ParkNet web paneli — gelir, doluluk ve şube karşılaştırma göstergeleri"),
]


def altyazi_bul(sayfa, gorsel_rect):
    """Görselin hemen altındaki açıklama metnini döndürür."""
    if gorsel_rect is None:
        return ""
    arama = pymupdf.Rect(
        gorsel_rect.x0 - 20, gorsel_rect.y1,
        gorsel_rect.x1 + 20, min(gorsel_rect.y1 + 46, sayfa.rect.y1))
    metin = sayfa.get_textbox(arama).strip()
    metin = " ".join(metin.split())
    # Sayfa altbilgisi / sayfa numarası gibi kalıntıları ele
    if len(metin) < 12 or len(metin) > 190:
        return ""
    if metin.lower().startswith(("sayfa", "erzurum büyükşehir belediyesi ·")):
        return ""
    return metin


def bolum_cikar(dosya, no, ad, kisa):
    yol = os.path.join(KAYNAK, dosya)
    d = pymupdf.open(yol)
    gorulmus = set()
    kayitlar = []

    for pno, sayfa in enumerate(d, start=1):
        # Sayfadaki görselleri dikey konuma göre sırala (okuma sırası)
        yerlesimler = []
        for im in sayfa.get_images(full=True):
            xref = im[0]
            try:
                rects = sayfa.get_image_rects(xref)
            except Exception:
                rects = []
            r = rects[0] if rects else None
            yerlesimler.append((r.y0 if r else 9999, xref, r))
        yerlesimler.sort(key=lambda t: t[0])

        for _, xref, rect in yerlesimler:
            try:
                px = d.extract_image(xref)
            except Exception:
                continue
            w, h = px["width"], px["height"]
            if w < MIN_W or h < MIN_H:
                continue
            imza = hashlib.md5(px["image"]).hexdigest()
            if imza in gorulmus:
                continue
            gorulmus.add(imza)

            sira = len(kayitlar) + 1
            dosya_adi = f"b{no:02d}_{kisa}_{sira:02d}.{px['ext']}"
            with open(os.path.join(GORSEL_DIZIN, dosya_adi), "wb") as fh:
                fh.write(px["image"])

            kayitlar.append({
                "bolum": no,
                "bolum_adi": ad,
                "sira": sira,
                "dosya": dosya_adi,
                "genislik": w,
                "yukseklik": h,
                "kaynak_sayfa": pno,
                "altyazi": altyazi_bul(sayfa, rect),
            })
    d.close()
    return kayitlar


def main():
    os.makedirs(GORSEL_DIZIN, exist_ok=True)
    for eski in os.listdir(GORSEL_DIZIN):
        os.remove(os.path.join(GORSEL_DIZIN, eski))

    manifest = []
    print(f"{'BÖLÜM':<6} {'PROJE':<46} {'GÖRSEL':>6}  {'ALTYAZILI':>9}")
    print("─" * 74)

    for dosya, no, ad, kisa in BOLUMLER:
        kayitlar = bolum_cikar(dosya, no, ad, kisa)

        if no == 1:  # Otopark — ek PNG ekranları
            for png, aciklama in EK_PNG:
                kaynak_png = os.path.join(KAYNAK, png)
                if not os.path.exists(kaynak_png):
                    print(f"  ! PNG yok: {png}")
                    continue
                sira = len(kayitlar) + 1
                hedef = f"b01_parknet_{sira:02d}.png"
                with open(kaynak_png, "rb") as src, \
                     open(os.path.join(GORSEL_DIZIN, hedef), "wb") as dst:
                    dst.write(src.read())
                with pymupdf.open(kaynak_png) as im:
                    r = im[0].rect
                kayitlar.append({
                    "bolum": 1, "bolum_adi": ad, "sira": sira, "dosya": hedef,
                    "genislik": int(r.width), "yukseklik": int(r.height),
                    "kaynak_sayfa": 0, "altyazi": aciklama,
                })

        altyazili = sum(1 for k in kayitlar if k["altyazi"])
        print(f"{no:<6} {ad[:44]:<46} {len(kayitlar):>6}  {altyazili:>9}")
        manifest.extend(kayitlar)

    print("─" * 74)
    print(f"{'':<6} {'TOPLAM':<46} {len(manifest):>6}  "
          f"{sum(1 for k in manifest if k['altyazi']):>9}")

    with open(os.path.join(CIKTI, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1)
    print(f"\n✓ {os.path.join(CIKTI, 'manifest.json')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
