@echo off
REM =========================================================================
REM JAYMANI KRISHI SEWA — Digital Agritech Marketplace & Bahi-Khata Ledger
REM B.Tech Computer Science Capstone / Evaluation-3 Launch Script
REM =========================================================================
title Jaymani Krishi Sewa - Evaluation-3 Prototype
cd /d "%~dp0"

echo [1/2] Verifying Python Environment...
python --version
if errorlevel 1 (
    echo Python not found on standard PATH. Please ensure Python 3.10+ is installed.
    pause
    exit /b 1
)

echo [2/2] Launching Prototype Server at http://127.0.0.1:5000 ...
python app.py
pause
