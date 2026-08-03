<img src="./readme/card-titles/title1.svg"/>
<br>

## License

This project was created for the SEFactory Hackathon 2025. Add a `LICENSE` file before distributing or reusing it outside its intended scope.

<br><br>
<!-- project overview -->
<img src="./readme/card-titles/title2.svg"/>

> EduFlow Client is the Streamlit dashboard frontend for an HR training and course management system built for SEFactory Hackathon 2025.<br>
> It connects to a FastAPI backend, reads training data from Airtable, supports role-based workflows, and visualizes courses, participants, payments, employees, users, and operational metrics.

<br>

### Backend Required

Before running the frontend, configure and start the backend from `eduflowServer/backend` with Airtable credentials:

```env
AIRTABLE_API_KEY=your_key_here
AIRTABLE_BASE_ID=your_base_id_here
JWT_SECRET_KEY=any-random-secret-key
```

Then start the backend:

```powershell
cd ..\eduflowServer\backend
python -m uvicorn app.main:app --reload
```

Validate the client connection:

```powershell
python test_backend.py
```

Full setup notes are in [DATABASE_CONNECTION_FIX.md](DATABASE_CONNECTION_FIX.md).

<br>
<!-- System Design -->
<img src="./readme/card-titles/title3.svg"/>

### System Architecture

| Layer | Purpose |
|------|---------|
| **Streamlit Client** | Dashboard UI, navigation, forms, charts, and authenticated page workflows |
| **FastAPI Backend** | REST API, JWT auth, RBAC, users, courses, participants, payments, and metrics |
| **Airtable Database** | Cloud-hosted tables for HR training data |
| **n8n Automation** | Optional Google Drive to Airtable ingestion workflow |
| **Docker Compose** | Frontend, backend, and optional n8n orchestration |

<br>

### Data Flow

```text
Google Drive -> n8n Workflow -> Airtable -> FastAPI Backend -> Streamlit Dashboard
```

<br>

### Repository Map

| Path | Description |
|------|-------------|
| `Home.py` | Main Streamlit landing page |
| `api_client.py` | Backend API client with authentication handling |
| `pages/dashboard.py` | Metrics overview |
| `pages/courses.py` | Course listing and management |
| `pages/course_details.py` | Course detail workflow |
| `pages/participants.py` | Participant tracking |
| `pages/payments.py` | Payment monitoring |
| `pages/admin.py` | User management/admin panel |
| `pages/employees.py` | Employee-related dashboard page |
| `pages/add_course.py` | Course creation form |
| `pages/add_user.py` | User creation form |
| `assets/` | Logo and dashboard images |
| `docker-compose.yml` | Full stack orchestration |
| `docker-compose.simple.yml` | Frontend-only Docker setup |
| `docker-start.ps1` | Interactive Windows Docker startup |

<br><br>
<!-- Project Highlights -->
<img src="./readme/card-titles/title4.svg"/>

### Core Features

- **Authentication-aware client**: Connects to JWT-protected backend endpoints through `api_client.py`.<br>
- **Role-based workflows**: Supports HR, Finance, Admin, Instructor, and Student-oriented access patterns.<br>
- **Training dashboard**: Shows KPIs, completion tracking, enrollment stats, revenue metrics, and payment status.<br>
- **Course management**: Create, view, edit, and classify courses by type, category, price, status, and instructor.<br>
- **Participant tracking**: Monitor enrollment, payment status, progress, and completion state.<br>
- **Payment operations**: Review paid, pending, failed, and refunded payment records.<br>
- **Automation-ready data**: Designed for Google Drive uploads flowing through n8n into Airtable.<br>

<br>

### Frontend Pages

| Page | Purpose |
|------|---------|
| Dashboard | Metrics and KPI overview |
| Courses | Course list and management |
| Course Details | Individual course review |
| Participants | Enrollment and progress tracking |
| Payments | Payment status and revenue visibility |
| Admin | User management |
| Add Course | Course creation |
| Add User | User creation |
| Employees | Employee data view |

<br>
<!-- Demo -->
<img src="./readme/card-titles/title5.svg"/>

### Local Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the client environment file:

```bash
cp .env.example .env
```

Set the backend URL:

```env
BACKEND_URL=http://localhost:8000
```

Run the client:

```bash
streamlit run Home.py
```

Open the dashboard at:

```text
http://localhost:8501
```

<br>

### Docker Quick Start

Interactive Windows startup:

```powershell
.\docker-start.ps1
```

Run frontend + backend:

```bash
docker-compose up --build
```

Run frontend + backend + n8n:

```bash
docker-compose --profile full up --build
```

Access URLs:

| Service | URL |
|---------|-----|
| Streamlit Dashboard | `http://localhost:8501` |
| FastAPI Backend | `http://localhost:8000` |
| API Docs | `http://localhost:8000/docs` |
| n8n Automation | `http://localhost:5678` |

<br><br>
<!-- Development & Testing -->
<img src="./readme/card-titles/title6.svg"/>

### Development Commands

| Command | Purpose |
|---------|---------|
| `streamlit run Home.py` | Start the frontend locally |
| `python test_backend.py` | Test backend connectivity |
| `python test_connection.py` | Test configured connection behavior |
| `docker-compose up --build` | Run frontend and backend containers |
| `docker-compose --profile full up --build` | Run full stack with n8n |
| `docker-compose logs -f` | Follow container logs |
| `docker-compose down` | Stop services |

<br>

### Client Dependencies

| Package | Purpose |
|---------|---------|
| **Streamlit** | Dashboard UI framework |
| **Plotly** | Charts and visual analytics |
| **Pillow** | Image handling |
| **requests** | Backend API calls |
| **python-dotenv** | Environment configuration |

<br>

### Documentation

| File | Purpose |
|------|---------|
| [GETTING_STARTED.md](GETTING_STARTED.md) | Setup walkthrough |
| [DOCKER_GUIDE.md](DOCKER_GUIDE.md) | Docker usage guide |
| [API_INTEGRATION.md](API_INTEGRATION.md) | API integration notes |
| [FRONTEND_API_USAGE.md](FRONTEND_API_USAGE.md) | Frontend API usage examples |
| [DATABASE_CONNECTION_FIX.md](DATABASE_CONNECTION_FIX.md) | Backend/Airtable connection fix guide |

<br><br>
<!-- Extras -->
<img src="./readme/card-titles/title7.svg"/>

### Automation Workflow

The optional n8n workflow supports this HR data pipeline:

1. HR uploads CSV/Excel training data to Google Drive.
2. n8n detects the file and extracts rows.
3. The workflow normalizes dates, statuses, and currency values.
4. Records are inserted into Airtable.
5. FastAPI exposes the updated data through REST endpoints.
6. Streamlit displays the updated metrics and management views.

Sample participant CSV:

```csv
name,email,course_name,payment_status,payment_amount,completion_status
John Doe,john@example.com,Leadership Training,paid,500,in_progress
Jane Smith,jane@example.com,Excel Mastery,pending,300,not_started
```

<br>

### Backend API Surface

The client expects the backend API at:

```text
http://localhost:8000/api/v1
```

Key backend routes include:

| Method | Endpoint | Purpose |
|--------|----------|---------|
| `POST` | `/api/v1/auth/signup` | Create user |
| `POST` | `/api/v1/auth/login` | Login and receive JWT |
| `GET` | `/api/v1/users` | List users |
| `GET` | `/api/v1/courses` | List courses |
| `POST` | `/api/v1/courses` | Create course |
| `GET` | `/api/v1/participants` | List participants |
| `GET` | `/api/v1/payments` | List payments |
| `GET` | `/api/v1/metrics/overview` | Dashboard metrics |
| `GET` | `/health` | Health check |

<br>

---

**EduFlow Client** - Streamlit HR training dashboard for courses, participants, payments, users, and Airtable-backed metrics.

*Training operations, cleaned up into one dashboard.*
