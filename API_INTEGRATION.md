# Backend API Integration Summary

## API Endpoints Used

### Authentication APIs (`/api/v1/auth/`)

| Endpoint | Method | Used In | Purpose |
|----------|--------|---------|---------|
| `/api/v1/auth/signup` | POST | Login page | Create new user account |
| `/api/v1/auth/login` | POST | Login page | Authenticate and get JWT token |

**Implementation**: `api_client.py` → `signup()`, `login()`

---

### User Management APIs (`/api/v1/users/`)

| Endpoint | Method | Used In | Purpose |
|----------|--------|---------|---------|
| `/api/v1/users` | GET | `pages/admin.py` | List all users with filtering |
| `/api/v1/users` | POST | `pages/add_user.py` | Create new user |
| `/api/v1/users/{id}` | DELETE | `pages/admin.py` | Delete user |

**Implementation**: `api_client.py` → `get_users()`, `create_user()`, `delete_user()`

**Backend File**: `app/api/users.py`

**Example Usage in Frontend**:
```python
# In pages/admin.py
from api_client import get_api_client

api_client = get_api_client()

# Fetch users with optional filtering
users_response = api_client.get_users(role="HR", search="john")

# Delete user
delete_response = api_client.delete_user(user_id="rec123")
```

---

### Course Management APIs (`/api/v1/courses/`)

| Endpoint | Method | Used In | Purpose |
|----------|--------|---------|---------|
| `/api/v1/courses` | GET | `pages/courses.py` | List all courses |
| `/api/v1/courses` | POST | `pages/add_course.py` | Create new course |

**Implementation**: `api_client.py` → `get_courses()`, `create_course()`

**Backend File**: `app/api/courses.py`

**Example Usage**:
```python
# Fetch courses
courses_response = api_client.get_courses(course_type="External", status="active")

# Create course
course_data = api_client.create_course(
    name="Leadership Training",
    course_type="external",
    category="Leadership",
    price=500.0,
    status="active"
)
```

---

### Participant APIs (`/api/v1/participants/`)

| Endpoint | Method | Used In | Purpose |
|----------|--------|---------|---------|
| `/api/v1/participants` | GET | `pages/participants.py` | List participants with filtering |

**Implementation**: `api_client.py` → `get_participants()`

**Backend File**: `app/api/participants.py`

**Example Usage**:
```python
# Fetch participants
participants_response = api_client.get_participants(
    course_name="UI/UX Design",
    participant_type="External"
)
```

---

### Payment APIs (`/api/v1/payments/`)

| Endpoint | Method | Used In | Purpose |
|----------|--------|---------|---------|
| `/api/v1/payments` | GET | `pages/payments.py` | List payments with status filter |

**Implementation**: `api_client.py` → `get_payments()`

**Backend File**: `app/api/payments.py`

**Example Usage**:
```python
# Fetch payments
payments_response = api_client.get_payments(status="paid")
```

---

### Dashboard Metrics APIs (`/api/v1/metrics/`)

| Endpoint | Method | Used In | Purpose |
|----------|--------|---------|---------|
| `/api/v1/metrics/overview` | GET | `pages/dashboard.py` | Get dashboard overview metrics |
| `/api/v1/metrics/revenue-by-month` | GET | `pages/dashboard.py` | Get monthly revenue data |

**Implementation**: `api_client.py` → `get_metrics_overview()`, `get_revenue_by_month()`

**Backend File**: `app/api/metrics.py`

**Example Usage**:
```python
# Fetch overview metrics
metrics = api_client.get_metrics_overview()
# Returns: total_courses, active_participants, total_revenue, etc.

# Fetch revenue by month
revenue_data = api_client.get_revenue_by_month(year=2025)
```

---

### Health Check API

| Endpoint | Method | Used In | Purpose |
|----------|--------|---------|---------|
| `/health` | GET | System monitoring | Check if backend is running |

**Implementation**: `api_client.py` → `health_check()`

**Backend File**: `app/api/health.py`

---

## Authentication Flow

### 1. User Signup/Login
```
Frontend (pages/login.py)
    ↓
API Client (api_client.py)
    ↓ HTTP POST /api/v1/auth/login
Backend (app/api/auth.py)
    ↓
Airtable (Users table)
    ↓ Returns user + JWT token
API Client stores token in st.session_state
    ↓
All subsequent requests include:
Authorization: Bearer <token>
```

### 2. Authenticated Request Example
```python
# In api_client.py
def _get_headers(self, include_auth: bool = True):
    headers = {"Content-Type": "application/json"}
    
    if include_auth and 'access_token' in st.session_state:
        headers["Authorization"] = f"Bearer {st.session_state.access_token}"
    
    return headers
```

---

## Data Flow

### Complete Request Flow
```
User Action (Button click in Streamlit)
    ↓
Frontend Page (e.g., pages/admin.py)
    ↓
API Client Method (api_client.get_users())
    ↓
HTTP Request with JWT
    ↓
FastAPI Backend (app/api/users.py)
    ↓
Airtable Client (app/services/airtable_client.py)
    ↓
Airtable Database
    ↓ Returns data
Backend processes & validates
    ↓ Returns JSON
API Client processes response
    ↓
Frontend displays data
```

---

## API Client Structure

The `api_client.py` file is organized as:

```python
class APIClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.api_prefix = "/api/v1"
    
    # Authentication Methods
    def signup(email, password, full_name, role) → Dict
    def login(email, password) → Dict
    def logout() → None
    
    # User Methods
    def get_users(role=None, search=None) → Dict
    def create_user(email, full_name, role, password) → Dict
    def delete_user(user_id) → Dict
    
    # Course Methods
    def get_courses(course_type=None, status=None) → Dict
    def create_course(...) → Dict
    
    # Participant Methods
    def get_participants(course_name=None, type=None) → Dict
    
    # Payment Methods
    def get_payments(status=None) → Dict
    
    # Metrics Methods
    def get_metrics_overview() → Dict
    def get_revenue_by_month(year=None) → Dict
    
    # Utility Methods
    def health_check() → Dict
    def _get_headers(include_auth=True) → Dict
    def _handle_response(response) → Dict
```

---

## Error Handling

All API methods include comprehensive error handling:

```python
def get_users(self, role=None, search=None):
    try:
        response = requests.get(url, params=params, headers=self._get_headers())
        return self._handle_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Connection error: {str(e)}", "status_code": 500}
```

Common error responses:
- `401`: Token expired/invalid → Auto-logout and redirect to login
- `404`: Resource not found
- `500`: Server error
- Connection errors: Backend not reachable

---

## Environment Configuration

### Frontend (.env)
```env
BACKEND_URL=http://localhost:8000
```

### Backend (../eduflowServer/backend/.env)
```env
AIRTABLE_API_KEY=your_key_here
AIRTABLE_BASE_ID=your_base_id_here
JWT_SECRET_KEY=your_secret_key_here
```

---

## Testing the Integration

### 1. Start Backend
```bash
cd ../eduflowServer/backend
python -m uvicorn app.main:app --reload
```

### 2. Test Backend Health
```bash
curl http://localhost:8000/health
```

### 3. Start Frontend
```bash
cd ../../eduflowClient
.\start.ps1
```

### 4. Test Authentication
1. Open http://localhost:8501
2. Click "Create Account" or login with existing credentials
3. Check browser console for any errors
4. Verify JWT token in session storage

### 5. Test API Calls
1. Navigate to Admin page
2. View users list (calls `/api/v1/users`)
3. Delete a user (calls `/api/v1/users/{id}`)
4. Check backend logs for API requests

---

## Backend API Documentation

Full interactive API documentation available at:
```
http://localhost:8000/docs
```

This Swagger UI shows:
- All available endpoints
- Request/response schemas
- Authentication requirements
- Try-it-out functionality

---

## Summary

✅ **Complete Integration Achieved**:
- All backend APIs are accessible through `api_client.py`
- JWT authentication implemented
- Error handling and session management
- All CRUD operations supported
- Ready for Docker deployment

The frontend now communicates with your FastAPI backend using all the endpoints defined in:
- `app/api/auth.py`
- `app/api/users.py`
- `app/api/courses.py`
- `app/api/participants.py`
- `app/api/payments.py`
- `app/api/metrics.py`
