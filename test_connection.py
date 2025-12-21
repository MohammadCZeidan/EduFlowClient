"""
Test script to verify backend connection
Run this to check if the backend API is accessible
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get backend URL
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:8000')

print(f"🔍 Testing connection to: {BACKEND_URL}")
print("-" * 50)

# Test 1: Health check
print("\n1. Testing health endpoint...")
try:
    response = requests.get(f"{BACKEND_URL}/health", timeout=5)
    if response.status_code == 200:
        print(f"   ✅ Health check passed: {response.json()}")
    else:
        print(f"   ❌ Health check failed with status: {response.status_code}")
except Exception as e:
    print(f"   ❌ Connection error: {str(e)}")

# Test 2: Check API endpoints
print("\n2. Testing API endpoints...")
endpoints = [
    "/api/v1/courses",
    "/api/v1/participants",
    "/api/v1/payments",
]

for endpoint in endpoints:
    try:
        response = requests.get(f"{BACKEND_URL}{endpoint}", timeout=5)
        if response.status_code in [200, 401]:  # 401 is expected without auth
            print(f"   ✅ {endpoint} is accessible (status: {response.status_code})")
        else:
            print(f"   ⚠️  {endpoint} returned status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ {endpoint} error: {str(e)}")

# Test 3: Test login endpoint
print("\n3. Testing login endpoint...")
try:
    response = requests.post(
        f"{BACKEND_URL}/api/v1/auth/login",
        json={"email": "test@example.com", "password": "test123"},
        timeout=5
    )
    if response.status_code in [200, 401, 422]:  # Expected responses
        print(f"   ✅ Login endpoint is accessible (status: {response.status_code})")
        if response.status_code == 401:
            print("   ℹ️  Invalid credentials (expected if user doesn't exist)")
    else:
        print(f"   ❌ Login returned unexpected status: {response.status_code}")
except Exception as e:
    print(f"   ❌ Login endpoint error: {str(e)}")

print("\n" + "=" * 50)
print("✨ Connection test complete!")
print("\nIf all tests passed, your backend is running correctly.")
print("If you see errors, make sure:")
print("  1. Backend server is running (uvicorn app.main:app)")
print("  2. Backend is on port 8000")
print("  3. .env file has BACKEND_URL=http://localhost:8000")
