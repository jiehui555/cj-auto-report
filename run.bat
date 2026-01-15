@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ========================================
echo Auto Screenshot Job - %date% %time%
echo ========================================

:: Activate virtual environment if exists
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

:: Run the screenshot job
python main.py

echo Job completed at %date% %time%
echo ========================================
pause