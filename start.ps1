# EduFlow Client - Quick Start Script
# Run this in PowerShell

Write-Host "🚀 Starting EduFlow Client..." -ForegroundColor Green

# Check if .env exists
if (-not (Test-Path ".env")) {
    Write-Host "📝 Creating .env file from template..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
}

# Check if backend is running
Write-Host "🔍 Checking backend connection..." -ForegroundColor Cyan
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/health" -TimeoutSec 5 -UseBasicParsing
    Write-Host "✅ Backend is running at http://localhost:8000" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Backend is not running!" -ForegroundColor Yellow
    Write-Host "   Please start the backend first:" -ForegroundColor Yellow
    Write-Host "   cd ..\eduflowServer\backend" -ForegroundColor Yellow
    Write-Host "   python -m uvicorn app.main:app --reload" -ForegroundColor Yellow
    Write-Host ""
    $continue = Read-Host "Continue anyway? (y/N)"
    if ($continue -ne "y") {
        exit 1
    }
}

# Activate virtual environment if it exists
if (Test-Path ".venv\Scripts\Activate.ps1") {
    Write-Host "🔧 Activating virtual environment..." -ForegroundColor Cyan
    & .\.venv\Scripts\Activate.ps1
} else {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Cyan
    python -m venv .venv
    & .\.venv\Scripts\Activate.ps1
    
    Write-Host "📥 Installing dependencies..." -ForegroundColor Cyan
    pip install -r requirements.txt
}

# Start Streamlit
Write-Host "🌐 Starting EduFlow Dashboard..." -ForegroundColor Green
Write-Host ""
Write-Host "Dashboard: http://localhost:8501" -ForegroundColor Cyan
Write-Host "Backend API: http://localhost:8000" -ForegroundColor Cyan
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow
Write-Host ""

streamlit run Home.py
