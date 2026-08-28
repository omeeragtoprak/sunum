# Claude Code Çalışma Protokolü — EBB Proje Tanıtım Sunumu

Bu depo, Erzurum Büyükşehir Belediyesi **Bilgi İşlem Daire Başkanlığı Akıllı Şehirler Şube Müdürlüğü** projelerinin
tek bir kurumsal tanıtım sunumuna dönüştürülmesi içindir.
Üretim aracı: Gemini Notebook (NotebookLM) MCP — `nlm` CLI / `gemini-notebook-mcp`.

Kurulum ve komut referansı için `README.md`'ye bak.

---

## 🚦 DURUM: Üretim başladı (2026-08-28)

Kaynaklar tamamlandı ve yüklendi. Aktif notebook:

| | |
|---|---|
| Takma ad | `ebb-sunum` |
| Notebook ID | `1b4b5c43-e387-48a5-98b9-bb55abafdabb` |
| Kaynak | 12 PDF (hepsi *ready*) |
| Üretimde | Video (explainer · classic · tr) — `381e6997-e301-4f25-8648-c61e2c51c332` |

Yeni notebook oluşturma, PDF'leri tekrar yükleme. `.nlm/index.json` güncel kaydı tutar.

---

## 🎯 Üretim hedefi

Projeler **ayrı ayrı değil, TEK bir bütünleşik sunumda** anlatılacak.
`kaynaklar/` altındaki tüm PDF'ler tek notebook'a yüklenir, tek sunum üretilir.

NotebookLM'in **tüm imkânları** kullanılacak: video, slayt destesi, rapor,
sesli özet, infografik.

---

## 🗣️ DİL VE TON — pazarlık konusu değil

| Kural | Değer |
|---|---|
| Dil | **Türkçe** — her komuta `--language tr` |
| Ton | **Resmî kurum dili** |
| Ağız | Birinci çoğul şahıs: *"Bilgi İşlem Daire Başkanlığı Akıllı Şehirler Şube Müdürlüğü olarak…"* |

**Doğru:**
> "Bilgi İşlem Daire Başkanlığı Akıllı Şehirler Şube Müdürlüğü olarak, kentimizin dijital dönüşümü kapsamında
> geliştirdiğimiz Akıllı Otopark Yönetim Sistemi, plaka tanıma teknolojisi ile
> otopark kapasitesinin gerçek zamanlı takibini sağlamaktadır."

**Yanlış:** samimi/sohbet dili · birinci tekil şahıs · gereksiz İngilizce terim ·
"biz de düşündük ki…" gibi gündelik ifadeler · magazinsel anlatım.

Bu tonu üretim komutlarına `--focus` / `--style-prompt` parametreleriyle geçir;
NotebookLM varsayılan olarak samimi anlatım üretme eğilimindedir, açıkça yönlendir.
Görsel stilde `kawaii`, `anime` gibi seçenekler resmî sunuma uygun değildir —
`classic` veya kurum kimliğine uygun `--style-prompt` kullan.

---

## 🧠 HAFIZA KURALI — her oturumda uygula

1. **Önce `.nlm/index.json` oku.** Hangi PDF hangi notebook'ta, ne üretilmiş —
   orada yazar. Notebook'u yeniden oluşturma, aynı PDF'i tekrar yükleme.
2. Yeni notebook / kaynak / üretim yaptıktan **hemen sonra** `index.json`'a kaydet
   (`.nlm/kayit-sablonu.json` formatında). Kaydetmezsen sonraki oturum kör başlar.
3. Notebook ID'leri UUID — insan okumaz. Her notebook'a takma ad ver:
   `nlm alias set <isim> <notebook-id>` → sonraki komutlarda ID yerine `<isim>`.

---

## ⚙️ İş akışı (üretim izni verildiğinde)

```bash
# 1) Notebook + takma ad
nlm notebook create "EBB Bilgi İşlem — Proje Tanıtımı" --json
nlm alias set ebb-sunum <notebook-id>

# 2) Tüm PDF'leri ekle (--wait şart)
for f in kaynaklar/*.pdf; do nlm source add ebb-sunum --file "$f" --wait; done

# 3) Üret — resmî ton yönlendirmesi ile
nlm video create ebb-sunum --format explainer --language tr --style classic \
    --focus "Bilgi İşlem Daire Başkanlığı Akıllı Şehirler Şube Müdürlüğü olarak geliştirdiğimiz projelerin resmî kurumsal tanıtımı; birinci çoğul şahıs, resmî kurum dili" -y
nlm slides create ebb-sunum --language tr -y
nlm report create ebb-sunum --language tr -y
nlm audio create  ebb-sunum --language tr -y

# 4) Takip (asenkron) → 5) indir
nlm studio status ebb-sunum
nlm download all  ebb-sunum
```

---

## ⚠️ Teknik kurallar

- Üretimler **asenkron**. Komut anında döner, içerik hazır olmaz —
  `nlm studio status` ile poll et, tamamlanmadan indirmeye çalışma.
- Kaynak eklerken **`--wait` kullan**; PDF işlenmeden üretim istersen boş içerik gelir.
- Ücretsiz katmanda **günlük ~50 sorgu limiti**. Toplu işte limiti gözet.
- Bu MCP **belgelenmemiş dahili API** kullanır. Komut bozulursa `nlm doctor`,
  gerekirse `uv tool upgrade notebooklm-mcp-cli`.
- Çerezler ~2-4 haftada düşer. `nlm doctor` "stale" derse `nlm login`.
- **Apple Silicon:** `uv` mutlaka arm64 olmalı (bkz. README Sorun Giderme).

## 🔒 Gizlilik

`kaynaklar/` altındaki PDF'ler kurumsal EBB dokümanlarıdır. Yüklendikleri NotebookLM
hesabının kurum politikasına uygunluğu kullanıcının sorumluluğundadır.
Kurumsal hesaba geçiş: `nlm login --profile kurumsal` → komutlara `-p kurumsal`.
