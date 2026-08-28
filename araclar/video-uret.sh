#!/usr/bin/env bash
# EBB Akıllı Şehir Projeleri — tanıtım videosu üretimi.
# Prompt metinleri araclar/video-promptu/ altında versiyonlanır.
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
cd "$(dirname "$0")/.."

NB="${1:-ebb-master}"
FOCUS="$(cat araclar/video-promptu/focus-anlatim.txt)"
STYLE="$(cat araclar/video-promptu/style-gorsel.txt)"

echo "notebook   : $NB"
echo "focus      : ${#FOCUS} karakter"
echo "style      : ${#STYLE} karakter"
echo

nlm video create "$NB" \
  --format explainer \
  --language tr \
  --focus "$FOCUS" \
  --style-prompt "$STYLE" \
  -y --json
