# EBB Bilgi İşlem Daire Başkanlığı — Proje Tanıtım Sunumu Üretimi

Erzurum Büyükşehir Belediyesi Bilgi İşlem Daire Başkanlığı bünyesinde geliştirilen
yazılım projelerinin **tek bir kurumsal tanıtım sunumu** hâline getirilmesi için
kurulmuş çalışma alanı.

Üretim, Google **Gemini Notebook (NotebookLM)** üzerinden
[`jacob-bd/gemini-notebook-mcp-cli`](https://github.com/jacob-bd/gemini-notebook-mcp-cli)
MCP sunucusu ile yapılır; Claude Code bu MCP'yi kullanarak kaynak PDF'lerden
video, slayt, rapor ve sesli özet üretir.

---

## 🎯 Hedef Çıktı

Tüm projeler **ayrı ayrı değil, tek bir bütünleşik sunumda** anlatılacaktır.

| Gereksinim | Kural |
|---|---|
| **Dil** | Kesinlikle **Türkçe** (`--language tr`) |
| **Ton** | Resmî kurum dili |
| **Anlatıcı ağzı** | Birinci çoğul şahıs — *"Bilgi İşlem Daire Başkanlığı olarak geliştirdiğimiz…"* |
| **Kapsam** | `kaynaklar/` altındaki tüm projeler tek sunumda |
| **Biçimler** | NotebookLM'in tüm imkânları: video + slayt + rapor + sesli özet + infografik |

**Ton örneği:**
> "Bilgi İşlem Daire Başkanlığı olarak, kentimizin dijital dönüşümü kapsamında
> geliştirdiğimiz Akıllı Otopark Yönetim Sistemi, plaka tanıma teknolojisi ile
> otopark kapasitesinin gerçek zamanlı takibini sağlamaktadır."

Kaçınılacak: samimi/sohbet dili, İngilizce terim yığını, "biz de düşündük ki" gibi
gündelik ifadeler, birinci tekil şahıs.

---

## ⚠️ Mevcut Durum

**Kaynak toplama aşaması sürüyor — henüz üretim yapılmayacaktır.**
Tüm PDF'ler `kaynaklar/` klasörüne eklendikten sonra üretim başlatılacaktır.

---

## 📦 Kurulum (sıfırdan, yeni makinede)

### 1. `uv` kur

> **⚠️ Apple Silicon (M1–M4) tuzağı:** Homebrew `/usr/local` altındaysa (Intel/Rosetta),
> `brew install uv` **x86_64** ikili kurar; paket x86_64 wheel indirir, arm64 Python
> bunları yükleyemez ve şu hatayı alırsın:
> `ImportError: ... incompatible architecture (have 'x86_64', need 'arm64')`
> Bu yüzden Homebrew yerine resmî yükleyiciyi kullan:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
file ~/.local/bin/uv    # "arm64" yazmalı (Apple Silicon'da)
```

### 2. MCP paketini kur

```bash
uv tool install --python 3.13 notebooklm-mcp-cli
nlm --version    # 0.9.14+
```

`--python 3.13` önemlidir: uv kendi yönettiği Python'u indirir, sistemdeki
universal2 Python'un mimari karışıklığından kurtulursun.

### 3. Google hesabına giriş yap

```bash
nlm login          # tarayıcı açar, Google girişi yapılır, çerezler saklanır
nlm login --check  # durum kontrolü
```

Çerezler ~2–4 haftada bir düşer; `nlm doctor` "stale" derse `nlm login` tekrarlanır.

### 4. Claude Code'a MCP olarak ekle

```bash
nlm setup add claude-code
# veya elle:
claude mcp add --scope user gemini-notebook-mcp notebooklm-mcp
```

Doğrulama: `claude mcp list` çıktısında
`gemini-notebook-mcp: notebooklm-mcp - ✔ Connected` görünmelidir.

### 5. Claude Code becerisini (skill) kur

```bash
nlm skill install claude-code
```

`~/.claude/skills/nlm-skill` altına uzman kılavuzu kurar; Claude 43 MCP aracını
doğru kullanmayı böyle öğrenir.

### 6. Her şeyi doğrula

```bash
nlm doctor        # tüm kontroller yeşil olmalı
nlm notebook list # hesabındaki notebook'lar listelenmeli
```

---

## 📁 Klasör Yapısı

```
sunum/
├── README.md          # bu dosya
├── CLAUDE.md          # Claude Code çalışma protokolü (otomatik okunur)
├── kaynaklar/         # girdi PDF'leri
├── ciktilar/          # indirilen üretimler
└── .nlm/
    ├── index.json           # notebook ↔ yerel dosya kayıt defteri (KALICI HAFIZA)
    └── kayit-sablonu.json   # yeni kayıt şablonu
```

### Doküman hafızası nasıl çalışır

`.nlm/index.json` bu deponun kalıcı hafızasıdır. Hangi PDF'in hangi notebook'a
yüklendiği, hangi içeriğin üretildiği burada tutulur. Claude her oturuma bu dosyayı
okuyarak başlar; böylece aynı PDF ikinci kez yüklenmez, var olan notebook yeniden
oluşturulmaz. Her işlemden sonra bu dosya güncellenir.

Notebook kimlikleri UUID olduğu için okunabilir takma ad verilir:

```bash
nlm alias set ebb-sunum <notebook-id>
# sonraki tüm komutlarda UUID yerine "ebb-sunum" yazılabilir
```

---

## 🚀 Kullanım

### Notebook hazırlama

```bash
nlm notebook create "EBB Bilgi İşlem — Proje Tanıtımı" --json
nlm alias set ebb-sunum <notebook-id>

# Tüm PDF'leri ekle (--wait: işlenmesini bekler)
for f in kaynaklar/*.pdf; do
  nlm source add ebb-sunum --file "$f" --wait
done
```

### Üretim

```bash
nlm video create  ebb-sunum --format explainer --language tr \
    --focus "Bilgi İşlem Daire Başkanlığı olarak geliştirdiğimiz projelerin resmî kurumsal tanıtımı" -y
nlm slides create      ebb-sunum --language tr -y
nlm report create      ebb-sunum --language tr -y
nlm audio create       ebb-sunum --language tr -y
nlm infographic create ebb-sunum --language tr -y
```

### Takip ve indirme

```bash
nlm studio status ebb-sunum                 # üretim asenkrondur, durumu buradan izle
nlm download all  ebb-sunum                 # tamamlananları indir
nlm download video ebb-sunum -o ciktilar/
```

---

## 🎬 Üretim Tipleri

| Komut | Çıktı |
|---|---|
| `nlm video create` | MP4 — `explainer` (varsayılan), `brief`, `cinematic`, `short` (dikey) |
| `nlm slides create` | Slayt destesi (PDF/PPTX) — `nlm slides revise` ile revize edilir |
| `nlm report create` | Markdown yönetici raporu |
| `nlm audio create` | Sohbet tarzı sesli özet |
| `nlm infographic create` | PNG infografik |
| `nlm mindmap / quiz / flashcards / data-table create` | Zihin haritası / test / kart / CSV |

**Video görsel stilleri:** `auto_select`, `classic`, `whiteboard`, `kawaii`, `anime`,
`watercolor`, `retro_print`, `heritage`, `paper_craft`, `custom`
(`--style-prompt "…"` ile serbest tarif).

Kurumsal tanıtım için `classic` veya `--style-prompt` ile kurum kimliğine uygun
tarif önerilir; `kawaii`/`anime` gibi stiller resmî sunum için uygun değildir.

---

## 🔧 Sorun Giderme

| Belirti | Çözüm |
|---|---|
| `incompatible architecture (have 'x86_64', need 'arm64')` | Intel `uv` kurulmuş. Kaldır, resmî yükleyiciyle arm64 sürümü kur (bkz. Kurulum §1) |
| `ENOENT: Executable not found in $PATH: "notebooklm-mcp"` | Paket kurulu değil ya da `~/.local/bin` PATH'te değil. `uv tool install --python 3.13 notebooklm-mcp-cli` |
| `nlm doctor` → çerez "stale" | `nlm login` tekrarla |
| Üretim boş/eksik içerik | Kaynak işlenmeden üretim istenmiş. `nlm source add … --wait` kullan |
| Komut aniden bozuldu | Dahili API değişmiş olabilir: `uv tool upgrade notebooklm-mcp-cli` |
| Günlük kota doldu | Ücretsiz katmanda ~50 sorgu/gün. İşi güne yay |

---

## 📌 Notlar

- Bu MCP sunucusu Google'ın **belgelenmemiş dahili API'lerini** kullanır; resmî
  Google ürünü değildir ve haber verilmeden değişebilir.
- Üretim komutları **asenkrondur**: komut anında döner, içerik hazır olmaz.
  `nlm studio status` ile beklenir.
- Kaynak PDF'ler kurumsal dokümanlardır. Yüklendikleri Google hesabının kurum
  politikasına uygun olmasına dikkat edilmelidir. Çoklu hesap:
  `nlm login --profile kurumsal` → komutlara `-p kurumsal`.
