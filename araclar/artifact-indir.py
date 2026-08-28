#!/usr/bin/env python
"""
NotebookLM artifact indirici — CLI'nin bozuk indirme kapısını atlar.

NEDEN GEREKLİ:
  `nlm download video <nb>` şu kontrole takılıyor (services/downloads.py:549):
      if artifact.get("status") != "completed": ... skip
  Ancak NotebookLM API'si `status` alanını hiç döndürmüyor; CLI varsayılan olarak
  "unknown" yazıyor (cli/formatters.py:240). "unknown" != "completed" olduğu için
  video/slayt indirme HİÇBİR ZAMAN çalışmıyor.
  Ayrıca download_async(wait=True) da işe yaramıyor: yeniden deneme yalnızca
  debug_code == "artifact_not_ready" iken devreye giriyor, fakat _download_once_async
  hatayı bu kodu koymadan sarmalıyor.

BU SCRIPT:
  Kütüphanenin düşük seviyeli _download_once_async fonksiyonunu doğrudan çağırır,
  artifact hazır olana kadar 30 sn aralıkla yoklar ve hazır olunca indirir.

KULLANIM:
  python araclar/artifact-indir.py <notebook-id> <artifact-id> <tip> <cikti-yolu>
  tip: video | slide_deck | audio | infographic
"""
import asyncio, sys, time
from notebooklm_tools.cli.utils import get_client
from notebooklm_tools.services import downloads

if len(sys.argv) != 5:
    print(__doc__)
    sys.exit(1)

NB, AID, TIP, OUT = sys.argv[1:5]
ZAMAN_ASIMI = 3600   # saniye
ARALIK = 30

def ilerleme(cur, tot):
    if tot and cur >= tot:
        print(f"indirme tamamlandi: {tot//1024//1024} MB", flush=True)

async def main():
    bitis = time.monotonic() + ZAMAN_ASIMI
    tur = 0
    with get_client(None) as client:
        while time.monotonic() < bitis:
            tur += 1
            try:
                r = await downloads._download_once_async(
                    client, NB, TIP, OUT, AID, "json", ilerleme, "pdf")
                print(f"HAZIR: {r}", flush=True)
                return 0
            except Exception as e:
                msg = str(e)
                if "not ready" in msg or "does not exist" in msg:
                    if tur % 4 == 1:
                        print(f"... {TIP} henuz hazir degil ({tur*ARALIK//60} dk beklendi)", flush=True)
                    await asyncio.sleep(ARALIK)
                else:
                    print(f"BEKLENMEYEN HATA: {type(e).__name__}: {msg[:300]}", flush=True)
                    return 1
    print(f"ZAMAN ASIMI: {ZAMAN_ASIMI//60} dk sonunda {TIP} hazir olmadi", flush=True)
    return 2

sys.exit(asyncio.run(main()))
