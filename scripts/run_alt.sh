#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/.."
exec python3 main.py "scripts/alternate-vfs.json" "log-alt.csv" "scripts/start_alt.txt"
