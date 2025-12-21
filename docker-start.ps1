# Docker Start Script for EduFlow
# Simplified script to start the application with Docker

Write-Host "🚀 Starting EduFlow with Docker" -ForegroundColor Cyan
Write-Host "=" -NoNewline; for ($i=0; $i -lt 50; $i++) { Write-Host "=" -NoNewline }; Write-Host ""

# Check if Docker is running
Write-Host "`n📋 Checking Docker..." -ForegroundColor Yellow
$dockerRunning = docker info 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Docker is not running!" -ForegroundColor Red
    Write-Host "   Please start Docker Desktop and try again." -ForegroundColor Yellow
    exit 1
}
Write-Host "✅ Docker is running" -ForegroundColor Green

# Check backend .env file
Write-Host "`n📋 Checking backend configuration..." -ForegroundColor Yellow
$backendEnvPath = "..\eduflowServer\backend\.env"
if (-Not (Test-Path $backendEnvPath)) {
    Write-Host "❌ Backend .env file not found!" -ForegroundColor Red
    Write-Host "   Please create: $backendEnvPath" -ForegroundColor Yellow
    Write-Host "   See DATABASE_CONNECTION_FIX.md for instructions" -ForegroundColor Yellow
    exit 1
}

# Load and validate backend .env
$envContent = Get-Content $backendEnvPath -Raw
if ($envContent -notmatch "AIRTABLE_API_KEY=\w+") {
    Write-Host "⚠️  AIRTABLE_API_KEY not configured in backend .env" -ForegroundColor Yellow
}
if ($envContent -notmatch "AIRTABLE_BASE_ID=\w+") {
    Write-Host "⚠️  AIRTABLE_BASE_ID not configured in backend .env" -ForegroundColor Yellow
}
Write-Host "✅ Backend configuration found" -ForegroundColor Green

# Ask user which setup to use
Write-Host "`n🎯 Choose Docker setup:" -ForegroundColor Cyan
Write-Host "  1. Full Stack (Frontend + Backend + n8n)" -ForegroundColor White
Write-Host "  2. Frontend Only (Backend running locally)" -ForegroundColor White
Write-Host "  3. Stop all containers" -ForegroundColor White
$choice = Read-Host "`nEnter choice (1-3)"

switch ($choice) {
    "1" {
        Write-Host "`n🚀 Starting full stack..." -ForegroundColor Cyan
        Write-Host "   This includes:" -ForegroundColor Gray
        Write-Host "   - Frontend (Streamlit) on port 8501" -ForegroundColor Gray
        Write-Host "   - Backend (FastAPI) on port 8000" -ForegroundColor Gray
        Write-Host "   - n8n (Automation) on port 5678" -ForegroundColor Gray
        
        docker-compose --profile full up --build -d
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "`n✅ Full stack started successfully!" -ForegroundColor Green
            Write-Host "`n📊 Access your services:" -ForegroundColor Cyan
            Write-Host "   🎨 Frontend Dashboard: http://localhost:8501" -ForegroundColor White
            Write-Host "   🔧 Backend API: http://localhost:8000" -ForegroundColor White
            Write-Host "   📖 API Docs: http://localhost:8000/docs" -ForegroundColor White
            Write-Host "   🤖 n8n Automation: http://localhost:5678" -ForegroundColor White
            Write-Host "`n📝 View logs: docker-compose logs -f" -ForegroundColor Gray
            Write-Host "🛑 Stop all: docker-compose --profile full down" -ForegroundColor Gray
        }
    }
    "2" {
        Write-Host "`n🚀 Starting frontend only..." -ForegroundColor Cyan
        Write-Host "   Make sure backend is running locally on port 8000" -ForegroundColor Yellow
        
        docker-compose -f docker-compose.simple.yml up --build -d
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "`n✅ Frontend started successfully!" -ForegroundColor Green
            Write-Host "`n📊 Access your services:" -ForegroundColor Cyan
            Write-Host "   🎨 Frontend Dashboard: http://localhost:8501" -ForegroundColor White
            Write-Host "`n📝 View logs: docker-compose -f docker-compose.simple.yml logs -f" -ForegroundColor Gray
            Write-Host "🛑 Stop: docker-compose -f docker-compose.simple.yml down" -ForegroundColor Gray
        }
    }
    "3" {
        Write-Host "`n🛑 Stopping all containers..." -ForegroundColor Yellow
        docker-compose --profile full down
        docker-compose -f docker-compose.simple.yml down
        Write-Host "✅ All containers stopped" -ForegroundColor Green
    }
    default {
        Write-Host "`n❌ Invalid choice" -ForegroundColor Red
        exit 1
    }
}

Write-Host "`n" -NoNewline
Write-Host "=" -NoNewline; for ($i=0; $i -lt 50; $i++) { Write-Host "=" -NoNewline }; Write-Host ""
