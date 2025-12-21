"""
API Client for EduFlow Backend Integration
Handles all HTTP requests to the FastAPI backend with JWT authentication
"""

import requests
from typing import Optional, Dict, List, Any
import streamlit as st
from datetime import datetime, timedelta
import os


class APIClient:
    """Client for communicating with EduFlow FastAPI backend"""
    
    def __init__(self, base_url: Optional[str] = None):
        if base_url is None:
            # Try to get from environment variable, fallback to default
            base_url = os.getenv('BACKEND_URL', 'http://localhost:8000')
        self.base_url = base_url.rstrip('/')
        self.api_prefix = "/api/v1"
        
    def _get_headers(self, include_auth: bool = True) -> Dict[str, str]:
        """Get headers including JWT token if available"""
        headers = {"Content-Type": "application/json"}
        
        if include_auth and 'access_token' in st.session_state:
            headers["Authorization"] = f"Bearer {st.session_state.access_token}"
            
        return headers
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response and errors"""
        try:
            data = response.json()
        except:
            data = {}
            
        if response.status_code == 401:
            # Token expired or invalid
            if 'access_token' in st.session_state:
                del st.session_state.access_token
            if 'user' in st.session_state:
                del st.session_state.user
            st.error("Session expired. Please login again.")
            return {"error": "Unauthorized", "status_code": 401}
            
        if not response.ok:
            return {
                "error": data.get("detail", "An error occurred"),
                "status_code": response.status_code
            }
            
        return data
    
    # ==================== AUTH ENDPOINTS ====================
    
    def signup(self, email: str, password: str, full_name: str, role: str = "hr") -> Dict[str, Any]:
        """Create a new user account"""
        url = f"{self.base_url}{self.api_prefix}/auth/signup"
        payload = {
            "email": email,
            "password": password,
            "full_name": full_name,
            "role": role
        }
        
        try:
            response = requests.post(url, json=payload, headers=self._get_headers(include_auth=False))
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}", "status_code": 500}
    
    def login(self, email: str, password: str) -> Dict[str, Any]:
        """Login and get JWT token"""
        url = f"{self.base_url}{self.api_prefix}/auth/login"
        payload = {"email": email, "password": password}
        
        try:
            response = requests.post(url, json=payload, headers=self._get_headers(include_auth=False))
            data = self._handle_response(response)
            
            if "access_token" in data:
                # Store token in session
                st.session_state.access_token = data["access_token"]
                st.session_state.user = data.get("user", {})
                
            return data
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}", "status_code": 500}
    
    def logout(self):
        """Clear session data"""
        if 'access_token' in st.session_state:
            del st.session_state.access_token
        if 'user' in st.session_state:
            del st.session_state.user
    
    # ==================== USER ENDPOINTS ====================
    
    def get_users(self, role: Optional[str] = None, search: Optional[str] = None) -> Dict[str, Any]:
        """Get all users with optional filtering"""
        url = f"{self.base_url}{self.api_prefix}/users"
        params = {}
        
        if role and role != "All Roles":
            params["role"] = role.lower()
        if search:
            params["search"] = search
            
        try:
            response = requests.get(url, params=params, headers=self._get_headers())
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}", "status_code": 500}
    
    def create_user(self, email: str, full_name: str, role: str, password: str) -> Dict[str, Any]:
        """Create a new user"""
        url = f"{self.base_url}{self.api_prefix}/users"
        payload = {
            "email": email,
            "full_name": full_name,
            "role": role,
            "password": password,
            "is_active": True
        }
        
        try:
            response = requests.post(url, json=payload, headers=self._get_headers())
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}", "status_code": 500}
    
    def delete_user(self, user_id: str) -> Dict[str, Any]:
        """Delete a user by ID"""
        url = f"{self.base_url}{self.api_prefix}/users/{user_id}"
        
        try:
            response = requests.delete(url, headers=self._get_headers())
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}", "status_code": 500}
    
    # ==================== COURSE ENDPOINTS ====================
    
    def get_courses(self, course_type: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
        """Get all courses with optional filtering"""
        url = f"{self.base_url}{self.api_prefix}/courses"
        params = {}
        
        if course_type and course_type != "All Types":
            params["type"] = course_type.lower()
        if status and status != "All Status":
            params["status"] = status.lower()
            
        try:
            response = requests.get(url, params=params, headers=self._get_headers())
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}", "status_code": 500}
    
    def create_course(self, name: str, course_type: str, category: str, price: float, 
                     status: str = "active", description: str = "") -> Dict[str, Any]:
        """Create a new course"""
        url = f"{self.base_url}{self.api_prefix}/courses"
        payload = {
            "name": name,
            "type": course_type,
            "category": category,
            "price": price,
            "status": status,
            "description": description
        }
        
        try:
            response = requests.post(url, json=payload, headers=self._get_headers())
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}", "status_code": 500}
    
    # ==================== PARTICIPANT ENDPOINTS ====================
    
    def get_participants(self, course_name: Optional[str] = None, 
                        participant_type: Optional[str] = None) -> Dict[str, Any]:
        """Get all participants with optional filtering"""
        url = f"{self.base_url}{self.api_prefix}/participants"
        params = {}
        
        if course_name and course_name != "All Courses":
            params["course_name"] = course_name
        if participant_type and participant_type != "All Types":
            params["type"] = participant_type.lower()
            
        try:
            response = requests.get(url, params=params, headers=self._get_headers())
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}", "status_code": 500}
    
    # ==================== PAYMENT ENDPOINTS ====================
    
    def get_payments(self, status: Optional[str] = None) -> Dict[str, Any]:
        """Get all payments with optional status filter"""
        url = f"{self.base_url}{self.api_prefix}/payments"
        params = {}
        
        if status and status != "All Status":
            params["status"] = status.lower()
            
        try:
            response = requests.get(url, params=params, headers=self._get_headers())
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}", "status_code": 500}
    
    # ==================== METRICS ENDPOINTS ====================
    
    def get_metrics_overview(self) -> Dict[str, Any]:
        """Get dashboard overview metrics"""
        url = f"{self.base_url}{self.api_prefix}/metrics/overview"
        
        try:
            response = requests.get(url, headers=self._get_headers())
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}", "status_code": 500}
    
    def get_revenue_by_month(self, year: Optional[int] = None) -> Dict[str, Any]:
        """Get revenue by month"""
        url = f"{self.base_url}{self.api_prefix}/metrics/revenue-by-month"
        params = {}
        
        if year:
            params["year"] = year
        else:
            params["year"] = datetime.now().year
            
        try:
            response = requests.get(url, params=params, headers=self._get_headers())
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}", "status_code": 500}
    
    # ==================== HEALTH CHECK ====================
    
    def health_check(self) -> Dict[str, Any]:
        """Check if backend is running"""
        url = f"{self.base_url}/health"
        
        try:
            response = requests.get(url, timeout=5)
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {"error": f"Backend not reachable: {str(e)}", "status_code": 500}


# Global API client instance
def get_api_client() -> APIClient:
    """Get or create API client instance"""
    if 'api_client' not in st.session_state:
        # Get backend URL from environment or use default
        import os
        backend_url = os.getenv('BACKEND_URL', 'http://localhost:8000')
        st.session_state.api_client = APIClient(backend_url)
    
    return st.session_state.api_client
