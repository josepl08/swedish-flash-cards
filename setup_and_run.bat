@echo off
setlocal

:: Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python to proceed.
    exit /b 1
)

:: Create a virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating a virtual environment...
    python -m venv venv
)

:: Activate the virtual environment
call "venv\Scripts\activate.bat"

:: Install packages from requirements.txt
if exist requirements.txt (
    echo Installing packages from requirements.txt...
    pip install -r requirements.txt
) else (
    echo requirements.txt not found. Please make sure it exists in the current directory.
    exit /b 1
)

:: Run the main Python script
if exist flash-card-app.py (
    echo Running flash-card-app.py...
    python flash-card-app.py
) else (
    echo flash-card-app.py not found. Please make sure it exists in the current directory.
    exit /b 1
)

:: Deactivate the virtual environment
deactivate
