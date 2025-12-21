# 🔧 Backend Database Connection Fix

## Problem
The frontend cannot connect to the database because the **backend is not properly configured** with Airtable credentials.

## Error Message
```
"Illegal header value b'Bearer '"
"Login failed: Illegal header value b'Bearer '"
```

This indicates that the backend's Airtable configuration is missing or incorrect.

## ✅ Solution Steps

### Step 1: Configure Backend Environment Variables

1. Navigate to the backend directory:
   ```powershell
   cd C:\Users\user\OneDrive\Desktop\eduflowServer\backend
   ```

2. Open the `.env` file in the backend directory

3. Make sure it contains these required variables:
   ```env
   # Airtable Configuration (REQUIRED)
   AIRTABLE_API_KEY=your_airtable_api_key_here
   AIRTABLE_BASE_ID=your_base_id_here

   # JWT Authentication
   JWT_SECRET_KEY=your-secret-key-change-in-production
   JWT_ALGORITHM=HS256
   JWT_EXPIRES_MINUTES=10080

   # CORS Configuration
   CORS_ORIGINS=http://localhost:8501,http://localhost:3000

   # Table Names
   AIRTABLE_TABLE_COURSES=Courses
   AIRTABLE_TABLE_COHORTS=Cohorts
   AIRTABLE_TABLE_PARTICIPANTS=Participants
   AIRTABLE_TABLE_PAYMENTS=Payments
   AIRTABLE_TABLE_USERS=Users
   AIRTABLE_TABLE_SCHEDULES=Schedules
   AIRTABLE_TABLE_REGISTRATIONS=Registrations
   AIRTABLE_TABLE_EMPLOYEES=Employees
   ```

### Step 2: Get Your Airtable Credentials

#### Get API Key:
1. Go to https://airtable.com/account
2. Scroll down to "API" section
3. Click "Generate API key" or copy your existing key
4. It should start with `key` or `pat`

#### Get Base ID:
1. Open your Airtable base
2. Look at the URL: `https://airtable.com/appXXXXXXXXXXXXXX/...`
3. The Base ID is `appXXXXXXXXXXXXXX` (starts with `app`)

### Step 3: Update the Backend .env File

Replace the placeholders in the backend `.env` file:

```env
AIRTABLE_API_KEY=keyYourActualKeyHere
AIRTABLE_BASE_ID=appYourActualBaseIdHere
```

### Step 4: Restart the Backend Server

1. Stop the current backend server (Ctrl+C in the terminal)

2. Start it again:
   ```powershell
   cd C:\Users\user\OneDrive\Desktop\eduflowServer\backend
   python -m uvicorn app.main:app --reload
   ```

### Step 5: Test the Connection

Run the test script again:
```powershell
cd C:\Users\user\OneDrive\Desktop\eduflowClient
& .venv\Scripts\python.exe test_backend.py
```

You should see:
```
✅ ALL TESTS PASSED - Backend is fully operational!
```

### Step 6: Start the Frontend

Once the backend is working:
```powershell
cd C:\Users\user\OneDrive\Desktop\eduflowClient
streamlit run Home.py
```

## 🎯 Quick Fix Command

If you just want to check if backend is running:
```powershell
curl http://localhost:8000/health
```

Should return: `{"status":"ok"}`

## 📋 Checklist

- [ ] Backend `.env` file exists in `eduflowServer/backend/`
- [ ] `AIRTABLE_API_KEY` is set with your actual Airtable API key
- [ ] `AIRTABLE_BASE_ID` is set with your actual Airtable base ID
- [ ] Backend server is running on port 8000
- [ ] Test script passes all tests
- [ ] Frontend can connect to backend

## 🆘 Still Having Issues?

### Issue: "Backend not running"
**Solution:** 
```powershell
cd C:\Users\user\OneDrive\Desktop\eduflowServer\backend
python -m uvicorn app.main:app --reload --port 8000
```

### Issue: "Airtable tables not found"
**Solution:** Make sure your Airtable base has these tables:
- Courses
- Cohorts  
- Participants
- Payments
- Users
- Schedules
- Registrations
- Employees

### Issue: "401 Unauthorized"
**Solution:** The JWT_SECRET_KEY needs to be set. Use any random string:
```env
JWT_SECRET_KEY=my-super-secret-key-123
```

### Issue: "CORS errors"
**Solution:** Add your frontend URL to CORS_ORIGINS:
```env
CORS_ORIGINS=http://localhost:8501,http://localhost:3000
```

## 📚 More Help

See the backend documentation:
- `C:\Users\user\OneDrive\Desktop\eduflowServer\docs\TROUBLESHOOTING.md`
- `C:\Users\user\OneDrive\Desktop\eduflowServer\docs\FRONTEND_INTEGRATION_GUIDE.md`
