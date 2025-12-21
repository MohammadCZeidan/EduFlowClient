"""
Complete backend integration test with authentication
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get backend URL
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:8000')

print(f"🔍 Testing EduFlow Backend Connection")
print(f"Backend URL: {BACKEND_URL}")
print("=" * 60)

# Test 1: Health check
print("\n✓ Step 1: Health Check")
try:
    response = requests.get(f"{BACKEND_URL}/health", timeout=5)
    if response.status_code == 200:
        print(f"  ✅ Backend is running: {response.json()}")
    else:
        print(f"  ❌ Health check failed: {response.status_code}")
        exit(1)
except Exception as e:
    print(f"  ❌ Cannot connect to backend: {str(e)}")
    print("\n🔧 Troubleshooting:")
    print("  1. Make sure backend is running:")
    print("     cd ../eduflowServer/backend")
    print("     python -m uvicorn app.main:app --reload")
    print("  2. Check backend is on port 8000")
    exit(1)

# Test 2: Try to signup a test user
print("\n✓ Step 2: Create Test User (Signup)")
test_email = "test@eduflow.com"
test_password = "testpass123"
test_name = "Test User"

try:
    response = requests.post(
        f"{BACKEND_URL}/api/v1/auth/signup",
        json={
            "email": test_email,
            "password": test_password,
            "full_name": test_name,
            "role": "hr"
        },
        timeout=5
    )
    
    if response.status_code == 201:
        print(f"  ✅ User created successfully")
        data = response.json()
        token = data.get('access_token')
    elif response.status_code == 400:
        print(f"  ℹ️  User already exists, will try to login")
        token = None
    else:
        print(f"  ⚠️  Signup returned status {response.status_code}: {response.text}")
        token = None
except Exception as e:
    print(f"  ❌ Signup error: {str(e)}")
    token = None

# Test 3: Login
print("\n✓ Step 3: Login")
try:
    response = requests.post(
        f"{BACKEND_URL}/api/v1/auth/login",
        json={
            "email": test_email,
            "password": test_password
        },
        timeout=5
    )
    
    if response.status_code == 200:
        data = response.json()
        token = data.get('access_token')
        user = data.get('user', {})
        print(f"  ✅ Login successful")
        print(f"     User: {user.get('full_name')} ({user.get('email')})")
        print(f"     Role: {user.get('role')}")
        print(f"     Token: {token[:20]}...")
    else:
        print(f"  ❌ Login failed: {response.status_code}")
        print(f"     Response: {response.text}")
        print("\n🔧 Backend may not be properly configured.")
        print("   Check backend/.env file for:")
        print("   - AIRTABLE_API_KEY")
        print("   - AIRTABLE_BASE_ID")
        print("   - JWT_SECRET_KEY")
        exit(1)
except Exception as e:
    print(f"  ❌ Login error: {str(e)}")
    exit(1)

# Test 4: Test authenticated endpoints
print("\n✓ Step 4: Test Protected Endpoints")
headers = {"Authorization": f"Bearer {token}"}

endpoints_to_test = [
    ("/api/v1/courses", "Courses"),
    ("/api/v1/participants", "Participants"),
    ("/api/v1/payments", "Payments"),
    ("/api/v1/metrics/summary", "Metrics Summary"),
    ("/api/v1/users", "Users"),
]

all_passed = True
for endpoint, name in endpoints_to_test:
    try:
        response = requests.get(f"{BACKEND_URL}{endpoint}", headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Check if it's a paginated response
            if isinstance(data, dict) and 'total' in data:
                count = data.get('total', 0)
                print(f"  ✅ {name}: {count} records")
            elif isinstance(data, list):
                print(f"  ✅ {name}: {len(data)} records")
            else:
                print(f"  ✅ {name}: Data received")
        else:
            print(f"  ❌ {name}: Status {response.status_code}")
            all_passed = False
    except Exception as e:
        print(f"  ❌ {name}: {str(e)}")
        all_passed = False

# Final Summary
print("\n" + "=" * 60)
if all_passed:
    print("✅ ALL TESTS PASSED - Backend is fully operational!")
    print("\n📝 Next Steps:")
    print("  1. Run the frontend: streamlit run Home.py")
    print("  2. Login with:")
    print(f"     Email: {test_email}")
    print(f"     Password: {test_password}")
else:
    print("⚠️  SOME TESTS FAILED")
    print("\n🔧 Troubleshooting:")
    print("  1. Check backend logs for errors")
    print("  2. Verify Airtable credentials in backend/.env")
    print("  3. Make sure all Airtable tables exist")
    print("  4. Check backend documentation in ../eduflowServer/docs/")
