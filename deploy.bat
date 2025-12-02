@echo off
REM Deploy Jupyter Book to GitHub Pages (Windows batch script)
REM This is a simple wrapper that calls the Python script

echo ============================================================
echo Jupyter Book Deployment Script (Windows)
echo ============================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python and try again.
    pause
    exit /b 1
)

REM Run the Python deployment script
python deploy.py

if errorlevel 1 (
    echo.
    echo Deployment failed! Check the error messages above.
    pause
    exit /b 1
)

pause

