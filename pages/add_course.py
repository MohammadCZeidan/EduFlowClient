import streamlit as st
import sys
import os

# Add parent directory to path to import api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_client import APIClient

st.set_page_config(page_title="Add New Course - EduFlow", layout="wide")

# Initialize API client
if 'api_client' not in st.session_state:
    st.session_state.api_client = APIClient()

# Check if user is logged in
if 'access_token' not in st.session_state:
    st.warning("Please login to add courses")
    st.switch_page("pages/login.py")

# Custom CSS
st.markdown("""
    <style>
        * {
            font-family: 'Roboto', sans-serif !important;
        }
        
        .stApp {
            background-color: white !important;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: white !important;
            padding: 0 !important;
            max-width: 280px !important;
            min-width: 280px !important;
            width: 280px !important;
        }
        
        [data-testid="stSidebar"] > div:first-child {
            width: 280px !important;
        }
        
        /* Force sidebar to always be open and prevent collapse */
        [data-testid="stSidebar"][aria-expanded="false"] {
            margin-left: 0 !important;
        }
        
        [data-testid="collapsedControl"] {
            display: none !important;
        }
        
        section[data-testid="stSidebar"] {
            position: relative !important;
            transform: none !important;
            margin-left: 0 !important;
            max-width: 280px !important;
            width: 280px !important;
        }
        
        section[data-testid="stSidebar"] > div {
            transform: none !important;
            position: relative !important;
            width: 280px !important;
        }
        
        /* Sidebar button styling */
        .stButton > button {
            width: 100%;
            border-radius: 8px;
            padding: 10px 10px;
            font-size: 16px;
            font-weight: 400;
            border: none;
            background-color: white;
            color: black;
            text-align: left;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .stButton > button:hover {
            background-color: white;
        }
        
        .stButton > button[kind="primary"] {
            background-color: white !important;
            color: black !important;
            border-left: 2px solid black !important;
        }
        
        .form-container {
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
               /* Input fields styling */
        input, textarea, [data-baseweb="input"], [data-baseweb="textarea"] {
            background-color: white !important;
            color: black !important;
        }
        
        /* Select box styling */
        [data-baseweb="select"] > div {
            background-color: white !important;
            color: black !important;
        }
        
        [data-baseweb="select"] input {
            color: black !important;
        }
        
        /* Placeholder text */
        ::placeholder {
            color: #666 !important;
        }
    </style>
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("assets/logo.png", width=180)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigation buttons
    if st.button("📊  Dashboard", key="nav_dashboard", use_container_width=True):
        st.switch_page("pages/dashboard.py")
    
    if st.button("📚  Courses", key="nav_courses", use_container_width=True, type="primary"):
        st.switch_page("pages/courses.py")
    
    if st.button("👥  Participants", key="nav_participants", use_container_width=True):
        st.switch_page("pages/participants.py")
    
    if st.button("💳  Payments", key="nav_payments", use_container_width=True):
        st.switch_page("pages/payments.py")
    
    if st.button("👤  Admin", key="nav_admin", use_container_width=True):
        st.switch_page("pages/admin.py")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("🚪  Logout", key="nav_logout", use_container_width=True):
        st.switch_page("Home.py")

# Main Content
st.markdown('<h2 style="color: black; margin-bottom: 30px;">Add New Course</h2>', unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    course_name = st.text_input("Course Name", placeholder="Enter course name", key="course_name")
    category = st.selectbox("Category", ["Skills", "Leadership", "Technical", "Management"], key="course_category")
    course_type = st.selectbox("Type", ["External", "Internal"], key="course_type")
    
with col2:
    cohort_id = st.text_input("Cohort ID", placeholder="Enter cohort ID", key="cohort_id")
    status = st.selectbox("Status", ["Active", "Inactive", "Draft"], key="course_status")
    price = st.text_input("Price", placeholder="Enter price", key="course_price")

description = st.text_area("Course Description", placeholder="Enter course description", height=150, key="course_description")

st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 3])
with col_btn1:
    if st.button("Save Course", use_container_width=True):
        if course_name and category and course_type and price:
            try:
                price_float = float(price)
                
                # Call API to create course
                with st.spinner("Creating course..."):
                    result = st.session_state.api_client.create_course(
                        name=course_name,
                        course_type=course_type,
                        category=category,
                        price=price_float,
                        status=status,
                        description=description
                    )
                
                if "error" in result:
                    st.error(f"Failed to create course: {result['error']}")
                else:
                    st.success("Course added successfully!")
                    st.switch_page("pages/courses.py")
            except ValueError:
                st.error("Price must be a valid number")
        else:
            st.error("Please fill in all required fields (Name, Category, Type, Price)")

with col_btn2:
    if st.button("Cancel", use_container_width=True):
        st.switch_page("pages/courses.py")

st.markdown('</div>', unsafe_allow_html=True)
