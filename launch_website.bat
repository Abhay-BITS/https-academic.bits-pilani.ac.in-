@echo off
echo ============================================================
echo BITS PILANI ACADEMIC WEBSITE LAUNCHER
echo ============================================================
echo.
echo Starting local web server...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.x from https://python.org
    echo.
    pause
    exit /b 1
)

REM Launch the Python server
python launch_website.py

pause
