@echo off
cd /d "%~dp0.."
py main.py "scripts\demo-vfs.json" "log-error.csv" "scripts\start_error.txt"
