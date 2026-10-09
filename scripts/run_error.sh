#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/.."
exec python3 main.py "scripts/demo-vfs.json" "log-error.csv" "scripts/start_error.txt"
