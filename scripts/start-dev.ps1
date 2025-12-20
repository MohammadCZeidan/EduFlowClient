# PowerShell development startup script for EduFlow Frontend

Write-Host "Starting EduFlow Frontend..." -ForegroundColor Green

# Check if Python is available
try {
    $pythonVersion = python --version
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Error: Python is not installed or not in PATH" -ForegroundColor Red
    exit 1
}

# Check if requirements are installed
if (-not (Test-Path "frontend\requirements-frontend.txt")) {
    Write-Host "Error: requirements-frontend.txt not found" -ForegroundColor Red
    exit 1
}

# Install/update dependencies
Write-Host "Installing frontend dependencies..." -ForegroundColor Yellow
python -m pip install -q --upgrade pip
python -m pip install -q -r requirements-frontend.txt

# Start Streamlit
Write-Host "Starting Streamlit on http://localhost:8501" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python -m streamlit run frontend/app.py --server.port=8501 --server.headless=true
