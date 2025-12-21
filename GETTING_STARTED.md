# EduFlow - Getting Started Guide

## Prerequisites

- Python 3.11 or higher
- Git (optional)
- Backend server (eduflowServer)

## Project Structure

```
eduflowClient/          # Frontend (Streamlit)
eduflowServer/backend/  # Backend (FastAPI + Airtable)
```

## Quick Start

### 1. Start the Backend Server

```powershell
# Navigate to backend directory
cd C:\Users\user\OneDrive\Desktop\eduflowServer\backend

# Activate virtual environment
.\.venv\Scripts\activate

# Start the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at: **http://localhost:8000**

### 2. Start the Frontend Server

```powershell
# Open a new terminal
# Navigate to frontend directory
cd C:\Users\user\OneDrive\Desktop\eduflowClient

# Activate virtual environment
.\.venv\Scripts\activate

# Start Streamlit
streamlit run Home.py
```

The frontend will be available at: **http://localhost:8501** or **http://localhost:8502**

## One-Command Startup

### Start Both Servers

```powershell
# Start backend (opens in new window)
cd C:\Users\user\OneDrive\Desktop\eduflowServer\backend; Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; .\.venv\Scripts\activate; uvicorn main:app --reload --host 0.0.0.0 --port 8000" -WindowStyle Normal

# Wait 3 seconds, then start frontend
Start-Sleep -Seconds 3; cd C:\Users\user\OneDrive\Desktop\eduflowClient; .\.venv\Scripts\activate; streamlit run Home.py
```

## Default Login Credentials

- **Email**: admin@eduflow.com
- **Password**: admin123

## Environment Configuration

### Backend (.env)
Located at: `eduflowServer\backend\.env`

```env
AIRTABLE_API_KEY=your_key_here
AIRTABLE_BASE_ID=your_base_id_here
JWT_SECRET_KEY=your_secret_key_here
```

### Frontend (.env)
Located at: `eduflowClient\.env`

```env
BACKEND_URL=http://localhost:8000
```

## Docker Deployment (Alternative)

### Option 1: Full Stack (Frontend + Backend + n8n)

```powershell
cd C:\Users\user\OneDrive\Desktop\eduflowClient
docker-compose --profile full up -d
```

- Frontend: http://localhost:8501
- Backend: http://localhost:8000
- n8n: http://localhost:5678

### Option 2: Frontend Only

```powershell
cd C:\Users\user\OneDrive\Desktop\eduflowClient
docker-compose -f docker-compose.simple.yml up -d
```

### Option 3: Interactive Startup Script

```powershell
cd C:\Users\user\OneDrive\Desktop\eduflowClient
.\docker-start.ps1
```

## Available Pages

Once logged in, you can access:

- **Dashboard** - Overview metrics and statistics
- **Courses** - Manage and view courses
- **Participants** - Track participant enrollments
- **Payments** - View and record payments
- **Employees** - Manage staff members
- **Admin** - User management
- **Add Course** - Create new courses
- **Add User** - Register new users

## Troubleshooting

### Backend Not Running
```powershell
# Check if backend process exists
Get-Process -Name "uvicorn" -ErrorAction SilentlyContinue

# Test backend health
curl http://localhost:8000/health
```

### Frontend Not Running
```powershell
# Check Streamlit process
Get-Process -Name "streamlit" -ErrorAction SilentlyContinue
```

### Clear Cache
```powershell
cd C:\Users\user\OneDrive\Desktop\eduflowClient
Remove-Item -Path "__pycache__" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "pages\__pycache__" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".streamlit\cache" -Recurse -Force -ErrorAction SilentlyContinue
```

### Port Already in Use
```powershell
# Kill process on port 8000 (backend)
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess | Stop-Process -Force

# Kill process on port 8501 (frontend)
Get-Process -Id (Get-NetTCPConnection -LocalPort 8501).OwningProcess | Stop-Process -Force
```

## API Documentation

When the backend is running, access interactive API docs at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Support

For issues or questions, check:
- `DATABASE_CONNECTION_FIX.md` - Database setup issues
- `FRONTEND_API_USAGE.md` - API endpoint reference
- `DOCKER_GUIDE.md` - Docker deployment details
