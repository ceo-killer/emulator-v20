#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/.."
exec python3 main.py "scripts/demo-vfs.json" "log-default.csv" "scripts/start.txt"
