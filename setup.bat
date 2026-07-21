@echo off
REM Quick Start Script for ResumePro (Windows)

echo ==================================
echo   ResumePro - Advanced Resume Builder
echo ==================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed. Please install Python 3.7+
    pause
    exit /b 1
)

echo OK Python found: 
python --version

REM Create virtual environment
echo.
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ==================================
echo OK Setup Complete!
echo ==================================
echo.
echo To start the application, run:
echo   python app.py
echo.
echo Then visit: http://localhost:5000
echo.
pause
