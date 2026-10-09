@echo off
cd /d "%~dp0.."
py main.py "scripts\demo-vfs.json" "log-default.csv" "scripts\start.txt"
