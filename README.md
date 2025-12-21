# EduFlow - HR Training & Course Management System

<div align="center">

![EduFlow Logo](assets/logo.png)

**Complete HR Training Management Dashboard with Authentication, Role-Based Access, and Automated Data Pipeline**

[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Airtable](https://img.shields.io/badge/Airtable-Database-FCBA03?logo=airtable)](https://airtable.com/)

</div>

---

## ⚠️ IMPORTANT: Backend Configuration Required

**Before running the frontend, you MUST configure the backend with Airtable credentials.**

### Quick Setup:

1. **Configure Backend .env file** (`eduflowServer/backend/.env`):
   ```env
   AIRTABLE_API_KEY=your_key_here
   AIRTABLE_BASE_ID=your_base_id_here
   JWT_SECRET_KEY=any-random-secret-key
   ```

2. **Get Airtable credentials**:
   - API Key: https://airtable.com/account (generate or copy)
   - Base ID: From your Airtable URL `https://airtable.com/appXXXXXX/...`

3. **Start Backend**:
   ```powershell
   cd ..\eduflowServer\backend
   python -m uvicorn app.main:app --reload
   ```

4. **Test Connection**:
   ```powershell
   cd eduflowClient
   python test_backend.py
   ```

**📖 Full instructions**: See [DATABASE_CONNECTION_FIX.md](DATABASE_CONNECTION_FIX.md)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Environment Setup](#-environment-setup)
- [Running with Docker](#-running-with-docker)
- [Automation Workflow](#-automation-workflow)
- [API Documentation](#-api-documentation)
- [Development Guide](#-development-guide)
- [Troubleshooting](#-troubleshooting)

---

## 🎯 Overview

**EduFlow** is a comprehensive HR training and course management system built for the SEFactory Hackathon 2025. It provides a complete solution for managing courses, tracking participants, processing payments, and monitoring training metrics.

### Technology Stack

- **Frontend**: Streamlit (Python) - Interactive dashboard UI
- **Backend**: FastAPI (Python) - RESTful API with JWT authentication
- **Database**: Airtable - Cloud-hosted data storage
- **Automation**: n8n - Workflow automation from Google Drive
- **Deployment**: Docker + Docker Compose - Containerized delivery

### Data Flow

```
Google Drive → n8n Workflow → Airtable → FastAPI Backend → Streamlit Dashboard
    ↓              ↓             ↓            ↓                    ↓
 HR Uploads    Extract &     Cloud DB    RESTful API        User Interface
              Transform                   + Auth
```

---

## ✨ Features

### 🔐 Authentication & Security
- JWT-based authentication with bcrypt password hashing
- Role-based access control (HR, Finance, Admin, Instructor, Student)
- Session management with token expiration
- Protected API endpoints

### 📊 Dashboard & Analytics
- Real-time metrics and KPIs
- Course completion tracking
- Revenue analytics by month/year
- Participant enrollment statistics
- Payment status monitoring

### 👥 User Management
- Create, view, and delete users
- Role assignment and management
- User search and filtering
- Activity tracking

### 📚 Course Management
- Course creation and editing
- Category and type classification
- Pricing and status management
- Instructor assignment

### 💳 Payment Tracking
- Payment status monitoring (Paid, Pending, Failed, Refunded)
- Revenue reporting
- Payment history
- Integration with Airtable

### 🔄 Automated Data Pipeline
- Google Drive to Airtable integration via n8n
- CSV/Excel file processing
- Automated data normalization
- Scheduled imports

---

## 🏗️ Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND LAYER                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │          Streamlit Dashboard (Port 8501)             │  │
│  │  • Home/Landing Page                                 │  │
│  │  • Login/Signup                                      │  │
│  │  • Dashboard (Metrics Overview)                      │  │
│  │  • Courses Management                                │  │
│  │  • Participants Tracking                             │  │
│  │  • Payments Processing                               │  │
│  │  • Admin Panel (User Management)                     │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↕ HTTP/REST
┌─────────────────────────────────────────────────────────────┐
│                      BACKEND LAYER                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │          FastAPI Server (Port 8000)                  │  │
│  │                                                       │  │
│  │  API Routes:                                         │  │
│  │  • /api/v1/auth/signup                               │  │
│  │  • /api/v1/auth/login                                │  │
│  │  • /api/v1/users                                     │  │
│  │  • /api/v1/courses                                   │  │
│  │  • /api/v1/participants                              │  │
│  │  • /api/v1/payments                                  │  │
│  │  • /api/v1/metrics/overview                          │  │
│  │                                                       │  │
│  │  Security: JWT Bearer Authentication                 │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↕ Airtable API
┌─────────────────────────────────────────────────────────────┐
│                     DATABASE LAYER                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                  Airtable Base                       │  │
│  │                                                       │  │
│  │  Tables:                                             │  │
│  │  • Users        • Courses      • Participants        │  │
│  │  • Payments     • Cohorts      • Schedules           │  │
│  │  • Registrations                                     │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↕ n8n Webhooks
┌─────────────────────────────────────────────────────────────┐
│                   AUTOMATION LAYER (Optional)               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              n8n Workflow (Port 5678)                │  │
│  │                                                       │  │
│  │  Workflow: Google Drive → Transform → Airtable      │  │
│  │  • Monitor Google Drive folder                       │  │
│  │  • Extract CSV/Excel data                            │  │
│  │  • Normalize and validate                            │  │
│  │  • Insert into Airtable                              │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Project Structure

```
eduflowClient/              # Frontend Application
├── api_client.py          # Backend API client with auth
├── Home.py                # Landing page (main entry point)
├── Dockerfile             # Frontend container
├── docker-compose.yml     # Full stack orchestration
├── requirements.txt       # Python dependencies
├── .env.example           # Environment template
├── start.ps1              # Quick start script
├── assets/                # Images and static files
│   └── logo.png
└── pages/                 # Streamlit pages
    ├── dashboard.py       # Metrics overview
    ├── courses.py         # Course management
    ├── participants.py    # Participant tracking
    ├── payments.py        # Payment processing
    ├── admin.py           # User management
    ├── add_course.py      # Course creation
    └── add_user.py        # User creation

eduflowServer/             # Backend Application
├── backend/
│   ├── app/
│   │   ├── main.py        # FastAPI app entry
│   │   ├── api/           # API endpoints
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   ├── courses.py
│   │   │   ├── participants.py
│   │   │   ├── payments.py
│   │   │   └── metrics.py
│   │   ├── core/          # Core functionality
│   │   │   ├── auth.py    # JWT authentication
│   │   │   ├── config.py  # Settings
│   │   │   └── rbac.py    # Role-based access
│   │   ├── models/        # Data models
│   │   └── services/      # Business logic
│   │       └── airtable_client.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
├── n8n/
│   ├── workflows/
│   │   └── google-drive-to-airtable.json
│   └── README.md
├── docs/                  # Documentation
│   ├── API_CONTRACT.md
│   ├── AIRTABLE_SCHEMA.md
│   ├── AUTH_AND_ROLES.md
│   └── FRONTEND_INTEGRATION_GUIDE.md
└── docker-compose.yml
```

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

- **Docker Desktop** (recommended) - [Download](https://www.docker.com/products/docker-desktop/)
  - Includes Docker Engine and Docker Compose
  - Available for Windows, macOS, and Linux
- **OR** Python 3.11+ (for local development without Docker)
- **Airtable Account** - [Sign up free](https://airtable.com/)
- **Git** (to clone the repository)

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd eduflowClient
```

### 2. Set Up Airtable

#### A. Create Airtable Account
1. Go to [airtable.com](https://airtable.com/)
2. Sign up for a free account
3. Create a new base called "EduFlow"

#### B. Get API Credentials

**Get API Key:**
1. Go to [Airtable Account](https://airtable.com/account)
2. Navigate to API section
3. Generate or copy your API Key (starts with `pat...` or `key...`)

**Get Base ID:**
1. Go to [Airtable API](https://airtable.com/api)
2. Select your "EduFlow" base
3. Copy the Base ID from the URL (starts with `app...`)

#### C. Create Required Tables

Create the following tables in your Airtable base:

**1. Users Table**
| Field Name | Type | Options |
|------------|------|---------|
| email | Email | Primary field, unique |
| password_hash | Single line text | |
| full_name | Single line text | |
| role | Single select | Options: hr, finance, admin, instructor, student |
| is_active | Checkbox | Default: checked |
| created_at | Created time | |

**2. Courses Table**
| Field Name | Type | Options |
|------------|------|---------|
| name | Single line text | Primary field |
| type | Single select | Options: internal, external |
| category | Single line text | |
| price | Currency | |
| status | Single select | Options: active, inactive, draft |
| instructor | Single line text | |
| description | Long text | |

**3. Participants Table**
| Field Name | Type | Options |
|------------|------|---------|
| name | Single line text | Primary field |
| email | Email | |
| course_name | Single line text | |
| payment_status | Single select | Options: registered, pending, paid |
| payment_amount | Currency | |
| completion_status | Single select | Options: not_started, in_progress, completed, dropped |

**4. Payments Table**
| Field Name | Type | Options |
|------------|------|---------|
| user_name | Single line text | Primary field |
| course_name | Single line text | |
| amount | Currency | |
| status | Single select | Options: pending, paid, failed, refunded |
| payment_date | Date | |

> **Note**: For full schema details, see [Backend AIRTABLE_SCHEMA.md](../eduflowServer/docs/AIRTABLE_SCHEMA.md)

---

## 🔧 Environment Setup

### 1. Backend Configuration

```bash
# Navigate to backend directory
cd ../eduflowServer/backend

# Copy environment template
cp .env.example .env

# Edit .env with your credentials
nano .env  # or use your preferred editor
```

**Edit `backend/.env`:**

```env
# === REQUIRED: Airtable Configuration ===
AIRTABLE_API_KEY=patXXXXXXXXXXXXXXXXXXXXXXXX
AIRTABLE_BASE_ID=appXXXXXXXXXXXXXX

# === REQUIRED: JWT Configuration ===
JWT_SECRET_KEY=<generate-secure-key-see-below>
JWT_ALGORITHM=HS256
JWT_EXPIRES_MINUTES=10080

# === OPTIONAL: Table Names (use defaults) ===
AIRTABLE_TABLE_USERS=Users
AIRTABLE_TABLE_COURSES=Courses
AIRTABLE_TABLE_PARTICIPANTS=Participants
AIRTABLE_TABLE_PAYMENTS=Payments
AIRTABLE_TABLE_COHORTS=Cohorts
AIRTABLE_TABLE_SCHEDULES=Schedules
AIRTABLE_TABLE_REGISTRATIONS=Registrations
AIRTABLE_TABLE_EMPLOYEES=Employees

# === OPTIONAL: CORS (defaults work) ===
CORS_ORIGINS=http://localhost:8501,http://localhost:3000

# === OPTIONAL: Logging ===
LOG_LEVEL=INFO
```

**Generate Secure JWT Secret:**

```bash
# On Linux/Mac
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# On Windows PowerShell
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 2. Frontend Configuration

```bash
# Navigate to frontend directory
cd ../../eduflowClient

# Copy environment template
cp .env.example .env
```

**Edit `eduflowClient/.env`:**

```env
# For local development
BACKEND_URL=http://localhost:8000

# For Docker deployment (uncomment when using docker-compose)
# BACKEND_URL=http://backend:8000
```

---

## 🐳 Running with Docker

### PowerShell Quick Start (Windows) 🎯

The easiest way to start with Docker:

```powershell
cd eduflowClient

# Interactive Docker startup script
.\docker-start.ps1
```

This script will:
- ✅ Check if Docker is running
- ✅ Validate backend configuration
- ✅ Let you choose: Full Stack, Frontend Only, or Stop All
- ✅ Display all access URLs

### Option 1: Full Stack (Recommended)

Run frontend + backend + n8n automation:

```bash
cd eduflowClient

# Interactive startup (Windows)
.\docker-start.ps1

# OR Manual command:
docker-compose --profile full up --build

# Or run in detached mode
docker-compose --profile full up --build -d
```

**Access URLs:**
- Frontend Dashboard: http://localhost:8501
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- n8n Automation: http://localhost:5678 (Login: admin / admin123)

### Option 2: Frontend + Backend Only

Run without n8n automation:

```bash
cd eduflowClient

# Start frontend and backend
docker-compose up --build

# Or run in detached mode
docker-compose up --build -d
```

**Access URLs:**
- Frontend Dashboard: http://localhost:8501
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Option 3: Frontend Only (Backend Running Locally)

If you're running backend locally and only want to containerize the frontend:

```bash
cd eduflowClient

# Use simplified docker-compose
docker-compose -f docker-compose.simple.yml up --build

# Or in detached mode
docker-compose -f docker-compose.simple.yml up --build -d
```

**Access:**
- Frontend Dashboard: http://localhost:8501
- Connects to backend at: http://localhost:8000

### Docker Commands Reference

```bash
# View running containers
docker-compose ps

# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f frontend
docker-compose logs -f backend

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Rebuild specific service
docker-compose up --build frontend

# Run backend health check
curl http://localhost:8000/health
```

### Health Checks

All services include health checks:

```bash
# Check backend health
curl http://localhost:8000/health

# Check frontend health
curl http://localhost:8501/_stcore/health

# View container health status
docker ps
```

---

## 🔄 Automation Workflow

### Google Drive → n8n → Airtable Pipeline

#### How It Works

1. **HR uploads training data** to a designated Google Drive folder
2. **n8n monitors** the folder for new CSV/Excel files
3. **Workflow extracts** data from the files
4. **Data is normalized** (status values, dates, currencies)
5. **Records are inserted** into Airtable
6. **Dashboard automatically** reflects new data

#### Workflow Diagram

```
┌─────────────────┐
│  Google Drive   │  HR uploads participant/payment CSV
│   Shared Folder │
└────────┬────────┘
         │ (1) File Upload Detected
         ↓
┌─────────────────┐
│  n8n Workflow   │
│  ┌───────────┐  │
│  │ Trigger   │  │  Google Drive Trigger (polls every 5 min)
│  └─────┬─────┘  │
│        ↓        │
│  ┌───────────┐  │
│  │ Download  │  │  Download file content
│  └─────┬─────┘  │
│        ↓        │
│  ┌───────────┐  │
│  │  Parse    │  │  Extract CSV/Excel data
│  └─────┬─────┘  │
│        ↓        │
│  ┌───────────┐  │
│  │Transform  │  │  Normalize data:
│  │           │  │  • Status: "paid" → "Paid"
│  │           │  │  • Dates: ISO format
│  │           │  │  • Currency: proper formatting
│  └─────┬─────┘  │
│        ↓        │
│  ┌───────────┐  │
│  │ Airtable  │  │  Insert records
│  │  Insert   │  │
│  └───────────┘  │
└─────────────────┘
         │ (2) Data Inserted
         ↓
┌─────────────────┐
│    Airtable     │  New records available
│   Database      │
└────────┬────────┘
         │ (3) API Fetch
         ↓
┌─────────────────┐
│ FastAPI Backend │  Serves data via REST API
└────────┬────────┘
         │ (4) UI Update
         ↓
┌─────────────────┐
│   Streamlit     │  Dashboard shows new data
│   Dashboard     │
└─────────────────┘
```

#### Setting Up n8n Workflow

1. **Access n8n UI**
   ```bash
   # Start with n8n
   docker-compose --profile full up -d
   
   # Access n8n
   open http://localhost:5678
   # Login: admin / admin123
   ```

2. **Import Workflow**
   - Click "Workflows" → "Import from File"
   - Select `../eduflowServer/n8n/workflows/google-drive-to-airtable.json`
   - Click "Import"

3. **Configure Google Drive**
   - Click "Google Drive Trigger" node
   - Click "Create New Credential"
   - Follow OAuth flow to authorize your Google account
   - Select the folder to monitor

4. **Configure Airtable**
   - Click "Airtable" node
   - Add Airtable credentials:
     - API Key: From your Airtable account
     - Base ID: From your EduFlow base

5. **Activate Workflow**
   - Toggle "Active" switch to ON
   - Workflow now monitors Google Drive every 5 minutes

6. **Test the Workflow**
   - Upload a test CSV to your Google Drive folder
   - Wait up to 5 minutes
   - Check "Executions" tab to see workflow run
   - Verify data appears in Airtable

#### Sample CSV Format

**participants.csv:**
```csv
name,email,course_name,payment_status,payment_amount,completion_status
John Doe,john@example.com,Leadership Training,paid,500,in_progress
Jane Smith,jane@example.com,Excel Mastery,pending,300,not_started
```

**payments.csv:**
```csv
user_name,course_name,amount,status,payment_date
John Doe,Leadership Training,500,paid,2025-12-01
Jane Smith,Excel Mastery,300,pending,2025-12-15
```

---

## 📚 API Documentation

### Base URL

```
http://localhost:8000/api/v1
```

### Interactive Documentation

Once the backend is running, access the auto-generated Swagger UI:

```
http://localhost:8000/docs
```

### Authentication Flow

All protected endpoints require a JWT Bearer token.

#### 1. Signup

```bash
curl -X POST "http://localhost:8000/api/v1/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "hr@example.com",
    "password": "SecurePass123!",
    "full_name": "HR Manager",
    "role": "hr"
  }'
```

**Response:**
```json
{
  "message": "User created successfully",
  "user": {
    "id": "rec123ABC",
    "email": "hr@example.com",
    "full_name": "HR Manager",
    "role": "hr",
    "is_active": true
  }
}
```

#### 2. Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "hr@example.com",
    "password": "SecurePass123!"
  }'
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": "rec123ABC",
    "email": "hr@example.com",
    "full_name": "HR Manager",
    "role": "hr"
  }
}
```

#### 3. Use Protected Endpoint

```bash
# Save token
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# Call protected endpoint
curl -X GET "http://localhost:8000/api/v1/users" \
  -H "Authorization: Bearer $TOKEN"
```

### Key Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | /api/v1/auth/signup | Create new user | No |
| POST | /api/v1/auth/login | Login and get token | No |
| GET | /api/v1/users | List all users | Yes (Admin/HR) |
| POST | /api/v1/users | Create user | Yes (Admin) |
| DELETE | /api/v1/users/{id} | Delete user | Yes (Admin) |
| GET | /api/v1/courses | List courses | Yes |
| POST | /api/v1/courses | Create course | Yes (HR/Admin) |
| GET | /api/v1/participants | List participants | Yes (HR) |
| GET | /api/v1/payments | List payments | Yes (Finance/Admin) |
| GET | /api/v1/metrics/overview | Dashboard metrics | Yes |
| GET | /health | Health check | No |

> For complete API documentation, see [Backend API_CONTRACT.md](../eduflowServer/docs/API_CONTRACT.md)

---

## 💻 Development Guide

### Local Development (Without Docker)

#### Backend Setup

```bash
cd ../eduflowServer/backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn app.main:app --reload --port 8000
```

#### Frontend Setup

```bash
cd ../../eduflowClient

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run frontend
streamlit run Home.py
```

### Making Changes

#### Add New Page

1. Create new file in `pages/`:
   ```python
   # pages/new_feature.py
   import streamlit as st
   import sys
   from pathlib import Path
   
   sys.path.append(str(Path(__file__).parent.parent))
   from api_client import get_api_client
   
   st.set_page_config(page_title="New Feature", layout="wide")
   
   api_client = get_api_client()
   
   st.title("New Feature")
   # Your code here
   ```

2. Streamlit automatically adds it to navigation

#### Add New API Endpoint

1. Add to backend `app/api/`:
   ```python
   # app/api/new_feature.py
   from fastapi import APIRouter, Depends
   from app.core.auth import get_current_user
   
   router = APIRouter(prefix="/new-feature", tags=["new-feature"])
   
   @router.get("/")
   async def get_feature(user=Depends(get_current_user)):
       return {"message": "Feature data"}
   ```

2. Register in `app/main.py`:
   ```python
   from app.api import new_feature
   app.include_router(new_feature.router, prefix="/api/v1")
   ```

3. Add to `api_client.py`:
   ```python
   def get_new_feature(self) -> Dict[str, Any]:
       url = f"{self.base_url}{self.api_prefix}/new-feature"
       response = requests.get(url, headers=self._get_headers())
       return self._handle_response(response)
   ```

---

## 🐛 Troubleshooting

### Common Issues

#### 1. Backend Connection Error

**Symptom:** Frontend shows "Connection error: Connection refused"

**Solution:**
```bash
# Check if backend is running
curl http://localhost:8000/health

# If not running, check backend logs
docker-compose logs backend

# Ensure .env is configured correctly
cat ../eduflowServer/backend/.env

# Restart services
docker-compose restart backend
```

#### 2. Airtable Authentication Failed

**Symptom:** "Airtable API error: Authentication failed"

**Solution:**
1. Verify API key in `.env`:
   ```bash
   cat ../eduflowServer/backend/.env | grep AIRTABLE_API_KEY
   ```
2. Check if key is valid at [Airtable Account](https://airtable.com/account)
3. Ensure key format is correct (starts with `pat...` or `key...`)
4. Restart backend:
   ```bash
   docker-compose restart backend
   ```

#### 3. JWT Token Expired

**Symptom:** "Session expired. Please login again."

**Solution:**
- This is normal behavior. Token expires after 7 days (default)
- Simply login again to get a new token
- To extend token lifetime, edit `JWT_EXPIRES_MINUTES` in backend `.env`

#### 4. Docker Build Fails

**Symptom:** Build errors during `docker-compose up --build`

**Solution:**
```bash
# Clear Docker cache
docker-compose down -v
docker system prune -a

# Rebuild from scratch
docker-compose build --no-cache

# Check for port conflicts
netstat -an | findstr "8000 8501 5678"
```

#### 5. n8n Workflow Not Triggering

**Symptom:** Files uploaded to Google Drive but workflow doesn't run

**Solution:**
1. Check if workflow is active (toggle should be green)
2. Verify Google Drive credentials are valid
3. Check workflow execution logs in n8n UI
4. Ensure trigger interval is set (default: 5 minutes)
5. Manually test workflow with "Execute Workflow" button

### Debug Mode

Enable detailed logging:

**Backend:**
```env
# In backend/.env
LOG_LEVEL=DEBUG
```

**Frontend:**
```bash
# Run with verbose logging
streamlit run Home.py --logger.level=debug
```

### Getting Help

1. Check [Backend TROUBLESHOOTING.md](../eduflowServer/docs/TROUBLESHOOTING.md)
2. Review [API Contract](../eduflowServer/docs/API_CONTRACT.md)
3. Check Docker logs: `docker-compose logs -f`
4. Verify Airtable schema matches requirements

---

## 📸 Screenshots

### Landing Page
![Landing Page](docs/screenshots/landing.png)

### Login
![Login Page](docs/screenshots/login.png)

### Dashboard
![Dashboard](docs/screenshots/dashboard.png)

### Admin Panel
![Admin Panel](docs/screenshots/admin.png)

### n8n Workflow
![n8n Automation](docs/screenshots/n8n-workflow.png)

---

## 📝 License

This project was created for the SEFactory Hackathon 2025.

---

## 👥 Team

**Building 1243, Basement (Floor -1)**  
Beirut Digital District (BDD)  
Nassif Yazigi, Beirut, Lebanon  
📧 info@sefactory.io

---

## 🎉 Acknowledgments

- SEFactory for hosting the hackathon
- Airtable for the database platform
- FastAPI and Streamlit communities
- n8n for automation capabilities

---

**Built with ❤️ for SEFactory Hackathon 2025**
