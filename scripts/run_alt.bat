@echo off
cd /d "%~dp0.."
py main.py "scripts\alternate-vfs.json" "log-alt.csv" "scripts\start_alt.txt"
