# Frontend API Usage Summary

This document summarizes all the backend API endpoints used by the frontend pages.

## Required API Endpoints

### Authentication Endpoints

| Frontend Page | Endpoint | Method | Purpose |
|--------------|----------|--------|---------|
| `pages/login.py` | `/api/v1/auth/login` | POST | User authentication, returns JWT token |
| All protected pages | `/api/v1/auth/me` | GET | Get current user profile (optional, for user info) |

### Dashboard Endpoints

| Frontend Page | Endpoint | Method | Purpose |
|--------------|----------|--------|---------|
| `pages/dashboard.py` | `/api/v1/metrics/summary` | GET | Get dashboard metrics (total courses, participants, revenue, etc.) |

### User Management Endpoints

| Frontend Page | Endpoint | Method | Purpose |
|--------------|----------|--------|---------|
| `pages/admin.py` | `/api/v1/users` | GET | List all users with filtering (role, search) |
| `pages/admin.py` | `/api/v1/users/{user_id}` | DELETE | Delete a user |
| `pages/add_user.py` | `/api/v1/users` | POST | Create a new user |

### Course Endpoints

| Frontend Page | Endpoint | Method | Purpose |
|--------------|----------|--------|---------|
| `pages/courses.py` | `/api/v1/courses` | GET | List all courses with filters |
| `pages/add_course.py` | `/api/v1/courses` | POST | Create a new course |

### Participant Endpoints

| Frontend Page | Endpoint | Method | Purpose |
|--------------|----------|--------|---------|
| `pages/participants.py` | `/api/v1/participants` | GET | List all participants with filters |

### Payment Endpoints

| Frontend Page | Endpoint | Method | Purpose |
|--------------|----------|--------|---------|
| `pages/payments.py` | `/api/v1/payments` | GET | List all payments with status filter |

## API Response Structures

### Metrics Summary Response
```json
{
  "total_courses": 100,
  "total_registered": 1000,
  "total_employees": 20,
  "total_participants": 50,
  "total_revenue": 2000.00,
  "total_paid": 2000.00,
  "total_pending": 0.00,
  "completion_rate": 75.0
}
```

### Courses List Response
```json
{
  "courses": [
    {
      "id": "recCOURSE123",
      "title": "UI/UX Design",
      "name": "UI/UX Design",
      "category": "Skills",
      "status": "Active",
      "type": "External",
      "price": 1000.00,
      "instructor": "John Doe"
    }
  ],
  "total": 10,
  "limit": 100,
  "offset": 0
}
```

### Participants List Response
```json
{
  "participants": [
    {
      "id": "recPARTICIPANT123",
      "name": "Ahmad",
      "email": "ahmad@example.com",
      "status": "Accepted",
      "course_name": "UI/UX",
      "cohort_name": "UIX07",
      "type": "External",
      "course_status": "Ongoing",
      "payment_status": "Completed"
    }
  ],
  "total": 50,
  "limit": 100,
  "offset": 0
}
```

### Payments List Response
```json
{
  "payments": [
    {
      "id": "recPAYMENT123",
      "user_name": "Ahmad",
      "course_name": "UI/UX",
      "cohort_name": "UIX07",
      "amount": 1000.00,
      "status": "Completed",
      "type": "External"
    }
  ],
  "total": 100,
  "limit": 100,
  "offset": 0
}
```

### Users List Response
```json
{
  "users": [
    {
      "id": "recUSER123",
      "email": "user@example.com",
      "full_name": "John Doe",
      "role": "hr",
      "is_active": true
    }
  ],
  "total": 20,
  "limit": 100,
  "offset": 0
}
```

## Authentication Flow

1. **Login** (`pages/login.py`):
   - User enters email and password
   - POST to `/api/v1/auth/login`
   - Receive JWT token and user info
   - Store token in `st.session_state.access_token`
   - Store user info in `st.session_state.user`

2. **Protected Pages**:
   - Check if `st.session_state.access_token` exists
   - If not, redirect to login page
   - Include token in all API requests via `Authorization: Bearer {token}` header

3. **Logout** (`Home.py` or logout button):
   - Clear `st.session_state.access_token`
   - Clear `st.session_state.user`
   - Redirect to login page

## Error Handling

All pages handle API errors gracefully:

```python
if "error" in response:
    st.error(f"Failed to load data: {response['error']}")
    # Use empty array or default values as fallback
    data = []
else:
    data = response.get('items', [])
```

## Environment Configuration

Frontend requires the following environment variable:

```env
BACKEND_URL=http://localhost:8000
```

This is used by the `APIClient` class to construct API endpoint URLs.

## API Client Usage

All pages use the centralized `APIClient` class from `api_client.py`:

```python
# Initialize API client
if 'api_client' not in st.session_state:
    st.session_state.api_client = APIClient()

# Use API client
result = st.session_state.api_client.get_courses()
```

The `APIClient` handles:
- JWT token management
- Request/response formatting
- Error handling
- Base URL configuration

## Pages Summary

### Pages with API Integration ✅
- ✅ `pages/login.py` - Authentication
- ✅ `pages/dashboard.py` - Metrics display
- ✅ `pages/courses.py` - Course listing
- ✅ `pages/participants.py` - Participant listing
- ✅ `pages/payments.py` - Payment listing
- ✅ `pages/admin.py` - User management (already integrated)
- ✅ `pages/add_course.py` - Course creation
- ✅ `pages/add_user.py` - User creation

### Pages without API Integration
- ⚠️ `pages/employees.py` - Placeholder page, no backend endpoint available
- ⚠️ `pages/course_details.py` - Detail view page (would use `/api/v1/courses/{id}`)
- ⚠️ `pages/user_details.py` - Detail view page (would use `/api/v1/users/{id}`)

## Next Steps

If you want to enhance the integration:

1. **Implement detail pages**: Add API integration for `course_details.py` and `user_details.py`
2. **Add employees endpoint**: If the backend adds `/api/v1/employees`, integrate it in `employees.py`
3. **Add filtering**: Use the filter dropdowns in courses.py to call API with filter parameters
4. **Add pagination**: Implement pagination for large datasets
5. **Add search**: Use search inputs to filter results via API
6. **Add refresh**: Add refresh buttons to reload data from API
7. **Add loading states**: Improve UX with loading spinners and skeleton screens
8. **Add error recovery**: Implement retry logic for failed API calls
