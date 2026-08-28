#!/usr/bin/env python
"""
Aşama 2 — Kareleri çizer, seslendirir ve videoyu birleştirir.

Her anlatım parçası için:
  1. 1920x1080 kurumsal kare çizilir (ekran görüntüsü tam ekran + başlık + altbilgi)
  2. macOS Yelda sesiyle Türkçe seslendirme üretilir
  3. Karenin süresi = kendi seslendirmesinin süresi (+ nefes payı)
Sonra tüm kareler ve sesler ffmpeg ile tek videoda birleştirilir.

KULLANIM: python araclar/video-yerel/2-video-kur.py [--hizli]
  --hizli : seslendirmeyi atlar, yalnızca kareleri çizer (önizleme için)
"""
import json
import os
import shutil
import subprocess
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senaryo  # noqa: E402

KOK = "/Users/omer/Desktop/sunum"
KAYNAK = os.path.join(KOK, "kaynaklar")
BURASI = os.path.join(KOK, "araclar", "video-yerel")
URETIM = os.path.join(BURASI, "uretim")
GORSEL_DIZIN = os.path.join(URETIM, "gorseller")
KARE_DIZIN = os.path.join(URETIM, "kareler")
SES_DIZIN = os.path.join(URETIM, "sesler")
CIKTI = os.path.join(KOK, "ciktilar", "yerel",
                     "EBB-Akilli-Sehir-Projeleri-Tanitim-2026-YEREL.mp4")

W, H = 1920, 1080
LACIVERT = (0 / 255, 60 / 255, 126 / 255)
LACIVERT_KOYU = (0 / 255, 44 / 255, 92 / 255)
BEYAZ = (1, 1, 1)
ACIK = (0.82, 0.87, 0.93)
GRI = (0.45, 0.48, 0.53)
CERCEVE = (0.80, 0.83, 0.87)

FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
LOGO_PDF = os.path.join(KAYNAK, "EBB_Logo.pdf")
LOGO_PNG = os.path.join(URETIM, "_logo.png")

SES = "Yelda"
KONUSMA_HIZI = 168          # kelime/dakika — resmî sunum temposu
NEFES_PAYI = 0.45           # her parçadan sonra sessizlik (saniye)
ALT_SERIT = ("ERZURUM BÜYÜKŞEHİR BELEDİYESİ  ·  BİLGİ İŞLEM DAİRE BAŞKANLIĞI  ·  "
             "AKILLI ŞEHİRLER ŞUBE MÜDÜRLÜĞÜ")

# Ekran görüntüsü sayılmayan logo/dekoratif görseller (görsel incelemesiyle belirlendi)
HARIC = {"b05_bpbs_01", "b06_ebbai_01", "b11_ertansa_01"}


# ────────────────────────────── yardımcılar ──────────────────────────────

def komut(argv, **kw):
    return subprocess.run(argv, check=True, capture_output=True, text=True, **kw)


def logo_hazirla():
    if not os.path.exists(LOGO_PNG):
        with pymupdf.open(LOGO_PDF) as d:
            d[0].get_pixmap(dpi=260).save(LOGO_PNG)
    return LOGO_PNG


def yeni_sayfa(doc):
    s = doc.new_page(width=W, height=H)
    s.insert_font(fontname="TR", fontfile=FONT)
    s.insert_font(fontname="TRB", fontfile=FONT_BOLD)
    return s


def metin(s, yazi, kutu, punto, renk, kalin=False, hiza=0, satir=1.32):
    """Kutuya sığana kadar puntoyu düşürerek metni yerleştirir."""
    fnt = "TRB" if kalin else "TR"
    p = punto
    for _ in range(14):
        if s.insert_textbox(kutu, yazi, fontname=fnt, fontsize=p, color=renk,
                            align=hiza, lineheight=satir) >= 0:
            return p
        p *= 0.93
    return p


def logo_chip(s, x, y, boy):
    """Lacivert zemin üzerine beyaz yuvarlak kutu içinde logo."""
    pad = boy * 0.14
    s.draw_rect(pymupdf.Rect(x, y, x + boy, y + boy), color=None, fill=BEYAZ,
                radius=0.16)
    s.insert_image(pymupdf.Rect(x + pad, y + pad, x + boy - pad, y + boy - pad),
                   filename=logo_hazirla())


def kaydet(doc, yol):
    # Sayfa zaten 1920x1080 punto — 72 dpi'de birebir 1920x1080 piksel verir.
    doc[0].get_pixmap(dpi=72).save(yol)
    doc.close()


# ────────────────────────────── kare çizimleri ──────────────────────────────

def kare_acilis(yol):
    doc = pymupdf.open()
    s = yeni_sayfa(doc)
    s.draw_rect(pymupdf.Rect(0, 0, W, H), color=None, fill=LACIVERT)
    s.draw_rect(pymupdf.Rect(0, H - 190, W, H), color=None, fill=LACIVERT_KOYU)

    logo_chip(s, W / 2 - 115, 140, 230)
    metin(s, "T.C.  ERZURUM BÜYÜKŞEHİR BELEDİYESİ",
          pymupdf.Rect(200, 424, W - 200, 470), 27, ACIK, kalin=True, hiza=1)
    metin(s, "BİLGİ İŞLEM DAİRE BAŞKANLIĞI  ·  AKILLI ŞEHİRLER ŞUBE MÜDÜRLÜĞÜ",
          pymupdf.Rect(200, 464, W - 200, 506), 22, ACIK, hiza=1)
    s.draw_line(pymupdf.Point(W / 2 - 190, 540), pymupdf.Point(W / 2 + 190, 540),
                color=BEYAZ, width=2.2)
    metin(s, senaryo.ACILIS["baslik"],
          pymupdf.Rect(140, 580, W - 140, 690), 74, BEYAZ, kalin=True, hiza=1)
    metin(s, senaryo.ACILIS["alt"],
          pymupdf.Rect(200, 706, W - 200, 756), 30, ACIK, hiza=1)
    metin(s, "11 PROJE  ·  TEK BÜTÜNLEŞİK SUNUM",
          pymupdf.Rect(200, H - 130, W - 200, H - 88), 24, BEYAZ, kalin=True, hiza=1)
    metin(s, "Tüm projeler öz kaynaklarımızla, kendi personelimiz tarafından geliştirilmiştir.",
          pymupdf.Rect(200, H - 82, W - 200, H - 46), 18, ACIK, hiza=1)
    kaydet(doc, yol)


def kare_bolum(yol, no, ad, ozet):
    doc = pymupdf.open()
    s = yeni_sayfa(doc)
    s.draw_rect(pymupdf.Rect(0, 0, W, H), color=None, fill=LACIVERT)
    s.draw_rect(pymupdf.Rect(0, 0, 34, H), color=None, fill=BEYAZ)

    logo_chip(s, W - 250, 92, 150)
    # Hayalet bölüm numarası — sağ boşlukta, metinden uzakta
    s.insert_text(pymupdf.Point(W - 430, 720), str(no), fontname="TRB", fontsize=300,
                  color=(1, 1, 1), fill_opacity=0.13)
    metin(s, f"BÖLÜM {no}", pymupdf.Rect(140, 320, 700, 366), 26, ACIK, kalin=True)
    metin(s, ad, pymupdf.Rect(140, 386, W - 470, 620), 58, BEYAZ, kalin=True)
    s.draw_line(pymupdf.Point(142, 660), pymupdf.Point(W - 470, 660),
                color=BEYAZ, width=2)
    metin(s, ozet, pymupdf.Rect(142, 690, W - 470, 920), 27, ACIK, satir=1.45)
    metin(s, ALT_SERIT, pymupdf.Rect(140, H - 90, W - 140, H - 50), 17, ACIK)
    kaydet(doc, yol)


def kare_icerik(yol, bolum_no, bolum_ad, baslik, gorsel_yolu):
    doc = pymupdf.open()
    s = yeni_sayfa(doc)
    s.draw_rect(pymupdf.Rect(0, 0, W, H), color=None, fill=BEYAZ)

    # üst bant
    UST = 116
    s.draw_rect(pymupdf.Rect(0, 0, W, UST), color=None, fill=LACIVERT)
    logo_chip(s, W - 116, 16, 84)
    metin(s, f"BÖLÜM {bolum_no}  ·  {bolum_ad}",
          pymupdf.Rect(44, 18, W - 150, 52), 21, ACIK, kalin=True)
    metin(s, baslik, pymupdf.Rect(44, 52, W - 150, 104), 33, BEYAZ, kalin=True)

    # alt şerit
    ALT = 52
    s.draw_rect(pymupdf.Rect(0, H - ALT, W, H), color=None, fill=LACIVERT)
    metin(s, ALT_SERIT, pymupdf.Rect(44, H - ALT + 16, W - 44, H - 12), 16, ACIK)

    # ekran görüntüsü — kullanılabilir alana sığdır
    with pymupdf.open(gorsel_yolu) as im:
        gw, gh = im[0].rect.width, im[0].rect.height
    yan, ust_bosluk, alt_bosluk = 54, UST + 26, ALT + 26
    kw, kh = W - 2 * yan, H - ust_bosluk - alt_bosluk
    olcek = min(kw / gw, kh / gh)
    w, h = gw * olcek, gh * olcek
    x0, y0 = (W - w) / 2, ust_bosluk + (kh - h) / 2
    s.draw_rect(pymupdf.Rect(x0 - 2, y0 - 2, x0 + w + 2, y0 + h + 2),
                color=CERCEVE, width=2)
    s.insert_image(pymupdf.Rect(x0, y0, x0 + w, y0 + h), filename=gorsel_yolu)
    kaydet(doc, yol)


def kare_kapanis(yol):
    doc = pymupdf.open()
    s = yeni_sayfa(doc)
    s.draw_rect(pymupdf.Rect(0, 0, W, H), color=None, fill=LACIVERT)
    logo_chip(s, W / 2 - 105, 240, 210)
    metin(s, senaryo.KAPANIS["baslik"],
          pymupdf.Rect(160, 520, W - 160, 620), 62, BEYAZ, kalin=True, hiza=1)
    s.draw_line(pymupdf.Point(W / 2 - 220, 650), pymupdf.Point(W / 2 + 220, 650),
                color=BEYAZ, width=2)
    metin(s, senaryo.KAPANIS["alt"],
          pymupdf.Rect(220, 686, W - 220, 780), 25, ACIK, hiza=1, satir=1.5)
    metin(s, "Yerli yazılım çözümlerimizle Erzurum'a değer katıyoruz.",
          pymupdf.Rect(220, 820, W - 220, 870), 22, BEYAZ, hiza=1)
    kaydet(doc, yol)


# ────────────────────────────── seslendirme ──────────────────────────────

def seslendir(yazi, hedef_wav):
    aiff = hedef_wav.replace(".wav", ".aiff")
    komut(["say", "-v", SES, "-r", str(KONUSMA_HIZI), "-o", aiff, yazi])
    komut(["ffmpeg", "-v", "error", "-i", aiff,
           "-af", f"aresample=48000,apad=pad_dur={NEFES_PAYI}",
           "-ar", "48000", "-ac", "2", hedef_wav, "-y"])
    os.remove(aiff)
    return sure(hedef_wav)


def sure(yol):
    r = komut(["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "csv=p=0", yol])
    return float(r.stdout.strip())


# ────────────────────────────── ana akış ──────────────────────────────

def gorsel_bul(bolum_kisa, no, bolum_manifest):
    """gorsel:N → o bölümün N sıralı ekran görüntüsünün dosya yolu."""
    for k in bolum_manifest:
        if k["sira"] == no:
            ad = os.path.splitext(k["dosya"])[0]
            if ad in HARIC:
                return None
            return os.path.join(GORSEL_DIZIN, k["dosya"])
    return None


def sayfa_render(pdf_dosya, sayfa_no, hedef):
    with pymupdf.open(os.path.join(KAYNAK, pdf_dosya)) as d:
        d[sayfa_no - 1].get_pixmap(dpi=160).save(hedef)
    return hedef


OTOPARK_PDF = "OTOPARK SUNUM (1).pdf"


def main():
    hizli = "--hizli" in sys.argv
    for d in (KARE_DIZIN, SES_DIZIN):
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d, exist_ok=True)
    os.makedirs(os.path.dirname(CIKTI), exist_ok=True)

    manifest = json.load(open(os.path.join(URETIM, "manifest.json"), encoding="utf-8"))
    parcalar = []   # (kare_png, anlatim_metni)

    # açılış
    p = os.path.join(KARE_DIZIN, "000_acilis.png")
    kare_acilis(p)
    parcalar.append((p, senaryo.ACILIS["anlatim"]))

    atlanan = []
    for b in senaryo.BOLUMLER:
        no, ad = b["no"], b["ad"]
        bm = [k for k in manifest if k["bolum"] == no]

        p = os.path.join(KARE_DIZIN, f"{no:02d}_000_bolum.png")
        kare_bolum(p, no, ad, b["kareler"][0][2][:150] if False else
                   b["giris"].split(". ", 2)[-1])
        parcalar.append((p, b["giris"]))

        for i, (anahtar, baslik, anlatim) in enumerate(b["kareler"], start=1):
            hedef_png = os.path.join(KARE_DIZIN, f"{no:02d}_{i:03d}.png")
            if anahtar.startswith("sayfa:"):
                sn = int(anahtar.split(":")[1])
                gorsel = sayfa_render(OTOPARK_PDF, sn,
                                      os.path.join(URETIM, f"_sayfa_{no}_{sn}.png"))
            else:
                gn = int(anahtar.split(":")[1])
                gorsel = gorsel_bul(b["kisa"], gn, bm)
            if not gorsel or not os.path.exists(gorsel):
                atlanan.append(f"bölüm {no} · {anahtar} · {baslik}")
                continue
            kare_icerik(hedef_png, no, ad, baslik, gorsel)
            parcalar.append((hedef_png, anlatim))

    p = os.path.join(KARE_DIZIN, "999_kapanis.png")
    kare_kapanis(p)
    parcalar.append((p, senaryo.KAPANIS["anlatim"]))

    print(f"✓ {len(parcalar)} kare çizildi")
    if atlanan:
        print("! atlanan kareler:")
        for a in atlanan:
            print("   ", a)
    if hizli:
        print("--hizli: seslendirme ve birleştirme atlandı")
        return 0

    # seslendirme
    sesler, sureler = [], []
    for i, (_, yazi) in enumerate(parcalar):
        wav = os.path.join(SES_DIZIN, f"{i:03d}.wav")
        sureler.append(seslendir(yazi, wav))
        sesler.append(wav)
        print(f"\r  seslendirme {i + 1}/{len(parcalar)}", end="", flush=True)
    print(f"\n✓ toplam süre: {int(sum(sureler) // 60)} dk {int(sum(sureler) % 60)} sn")

    # video listesi
    liste = os.path.join(URETIM, "kareler.txt")
    with open(liste, "w", encoding="utf-8") as fh:
        for (png, _), d in zip(parcalar, sureler):
            fh.write(f"file '{png}'\nduration {d:.3f}\n")
        fh.write(f"file '{parcalar[-1][0]}'\n")

    ses_liste = os.path.join(URETIM, "sesler.txt")
    with open(ses_liste, "w", encoding="utf-8") as fh:
        for w in sesler:
            fh.write(f"file '{w}'\n")

    birlesik_ses = os.path.join(URETIM, "_ses.m4a")
    komut(["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0", "-i", ses_liste,
           "-c:a", "aac", "-b:a", "192k", birlesik_ses, "-y"])

    komut(["ffmpeg", "-v", "error",
           "-f", "concat", "-safe", "0", "-i", liste,
           "-i", birlesik_ses,
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
           "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,"
                  "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:white",
           "-preset", "medium", "-crf", "20",
           "-c:a", "copy", "-shortest", CIKTI, "-y"])

    mb = os.path.getsize(CIKTI) / 1024 / 1024
    print(f"\n✓ VİDEO: {CIKTI}\n  {mb:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
