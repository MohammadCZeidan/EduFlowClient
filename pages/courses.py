import streamlit as st
import pandas as pd
import sys
import os

# Add parent directory to path to import api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_client import APIClient

st.set_page_config(page_title="Courses - EduFlow", layout="wide")

# Initialize API client
if 'api_client' not in st.session_state:
    st.session_state.api_client = APIClient()

# Check if user is logged in
if 'access_token' not in st.session_state:
    st.warning("Please login to access courses")
    st.switch_page("pages/login.py")

# Enhanced Custom CSS matching Figma design
st.markdown("""
    <style>
        * {
            font-family: 'Roboto', sans-serif !important;
        }
        
        .stApp {
            background-color: #f7f8fa !important;
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
        [data-testid="stSidebar"] .stButton > button {
            width: 100%;
            border-radius: 8px;
            padding: 10px 10px;
            font-size: 16px;
            font-weight: 400;
            border: none;
            background-color: transparent;
            color: #2E2E2E;
            text-align: left;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        [data-testid="stSidebar"] .stButton > button:hover {
            background-color: #f5f5f5;
        }
        
        [data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background-color: #E8E6FF !important;
            color: #51287E !important;
            border-left: 2px solid #51287E !important;
        }
        
        /* Add New Course button - override everything */
        .main div[data-testid="column"]:nth-child(2) .stButton > button,
        .main div[data-testid="column"]:nth-child(2) button[data-testid="baseButton-secondary"] {
            background: #51287E !important;
            border: 1px solid #51287E !important;
            border-radius: 30px !important;
            color: #FFFFFF !important;
            font-family: 'Roboto', sans-serif !important;
            font-weight: 700 !important;
            font-size: 15px !important;
            padding: 10px 20px !important;
            height: 40px !important;
            text-align: center !important;
            justify-content: center !important;
            display: flex !important;
            align-items: center !important;
        }
        
        /* View More Details button - override everything */
        .main [data-testid="column"] .detail-card .stButton > button,
        .main [data-testid="column"] .detail-card button[data-testid="baseButton-secondary"] {
            background: #51287E !important;
            border: 1px solid #51287E !important;
            border-radius: 30px !important;
            color: #FFFFFF !important;
            font-family: 'Roboto', sans-serif !important;
            font-weight: 700 !important;
            font-size: 15px !important;
            padding: 10px 20px !important;
            text-align: center !important;
            justify-content: center !important;
            display: flex !important;
            align-items: center !important;
        }
        
        .main [data-testid="column"] .detail-card .stButton > button:hover,
        .main [data-testid="column"] .detail-card button[data-testid="baseButton-secondary"]:hover {
            background: #3d1e5f !important;
        }
        
        .metric-card {
            background: white;
            padding: 13px 20px;
            border-radius: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            height: 150px;
        }
        
        .metric-value {
            font-size: 24px;
            font-weight: 500;
            color: #2E2E2E;
            margin: 13px 0;
        }
        
        .metric-label {
            font-size: 16px;
            font-weight: 500;
            color: #565656;
        }
        
        .icon-box {
            width: 41px;
            height: 41px;
            background-color: #F4F4F4;
            border-radius: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .filter-dropdown {
            background: #ECEDEF;
            padding: 4px 20px;
            border-radius: 20px;
            font-size: 15px;
            font-weight: 500;
            color: #2E2E2E;
            display: inline-block;
            margin-right: 16px;
        }
        
        .course-table {
            background: white;
            border-radius: 15px;
            padding: 12px;
        }
        
        .table-header {
            border-top: 1px solid #EBE6E6;
            border-bottom: 1px solid #EBE6E6;
            padding: 20px 33px;
            display: flex;
            justify-content: space-between;
            font-size: 18px;
            font-weight: 500;
            color: #565656;
        }
        
        .table-row {
            padding: 20px 33px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .table-row:hover {
            background: #f9f9f9;
        }
        
        .table-row.selected {
            background: #E8E6FF;
        }
        
        .category-badge {
            background: #ECEDEF;
            padding: 3px 15px;
            border-radius: 20px;
            font-size: 16px;
            color: #51287E;
            display: inline-block;
        }
        
        .status-indicator {
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        
        .status-dot {
            width: 10px;
            height: 10px;
            background: #6B7280;
            border-radius: 50%;
        }
        
        .detail-card {
            background: white;
            padding: 25px 12px;
            border-radius: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        
        .course-image {
            width: 100%;
            height: 159px;
            background: #D8D7D7;
            border-radius: 15px;
            margin-bottom: 20px;
        }
        
        .detail-row {
            margin-bottom: 32px;
            font-size: 16px;
            color: #2E2E2E;
        }
        
        .add-course-btn {
            background: white;
            padding: 3px 17px;
            border-radius: 20px;
            font-size: 15px;
            font-weight: 500;
            color: #51287E;
            border: none;
            cursor: pointer;
        }
        
        .view-details-btn {
            border: 1px solid #51287E;
            background: transparent;
            padding: 3px 17px;
            border-radius: 20px;
            font-size: 15px;
            font-weight: 500;
            color: #51287E;
            width: 100%;
            cursor: pointer;
        }
        
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Selectbox and TextInput styling */
        .stSelectbox > div > div {
            background: white !important;
            color: #000000 !important;
            border-radius: 20px;
        }
        
        .stSelectbox > div > div > div {
            background: white !important;
            color: #000000 !important;
        }
        
        .stSelectbox [data-baseweb="select"] {
            background: white !important;
        }
        
        .stSelectbox [data-baseweb="select"] > div {
            background: white !important;
            color: #000000 !important;
        }
        
        .stTextInput > div {
            background: white !important;
        }
        
        .stTextInput > div > div {
            background: white !important;
        }
        
        .stTextInput > div > div > input {
            background: white !important;
            color: #000000 !important;
            border-radius: 20px;
        }
        
        .stTextInput > div > div > input::placeholder {
            color: #000000 !important;
        }
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
    
    if st.button("👤 Admin", key="nav_admin", use_container_width=True):
        st.switch_page("pages/admin.py")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("🚪  Logout", key="nav_logout", use_container_width=True):
        st.switch_page("Home.py")

# Main Content
col_header1, col_header2 = st.columns([2, 1])
with col_header1:
    st.markdown('<h2 style="color: #2E2E2E; margin-bottom: 20px; font-size: 20px; font-weight: 500;">Courses</h2>', unsafe_allow_html=True)
with col_header2:
    if st.button("+ Add New Course", key="add_course", use_container_width=True):
        st.switch_page("pages/add_course.py")

# Metrics Row - Fetch course data for metrics
st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

with st.spinner("Loading metrics..."):
    courses_metrics_response = st.session_state.api_client.get_courses()

if "error" not in courses_metrics_response:
    courses_list_metrics = courses_metrics_response.get('courses', [])
    total_courses_count = len(courses_list_metrics)
    completed_courses_count = sum(1 for c in courses_list_metrics if c.get('status', '').lower() == 'completed')
    ongoing_courses_count = sum(1 for c in courses_list_metrics if c.get('status', '').lower() == 'active')
else:
    total_courses_count = 0
    completed_courses_count = 0
    ongoing_courses_count = 0

col1, col2, col3 = st.columns(3, gap="small")

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="icon-box">📚</div>
        <div class="metric-value">{total_courses_count}</div>
        <div class="metric-label">Total Courses</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="icon-box">✅</div>
        <div class="metric-value">{completed_courses_count}</div>
        <div class="metric-label">Completed Courses</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="icon-box">⏱️</div>
        <div class="metric-value">{ongoing_courses_count}</div>
        <div class="metric-label">Ongoing Courses</div>
    </div>
    """, unsafe_allow_html=True)

# Course List and Detail
st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)
col_list, col_detail = st.columns([1.8, 1], gap="medium")

with col_list:
    st.markdown('<div class="course-table">', unsafe_allow_html=True)
    
    # Filters and Search
    col_f1, col_f2, col_f3, col_search = st.columns([1, 1, 1, 2])
    with col_f1:
        st.selectbox("Status", ["All Status", "Ongoing", "Completed"], key="status_filter", label_visibility="collapsed")
    with col_f2:
        st.selectbox("Category", ["All Categories", "Skills", "Leadership", "Technical"], key="category_filter", label_visibility="collapsed")
    with col_f3:
        st.selectbox("Type", ["All Types", "External", "Internal"], key="type_filter", label_visibility="collapsed")
    with col_search:
        st.text_input("Search", placeholder="Search...", key="search", label_visibility="collapsed")
    
    st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)
    
    # Fetch courses from API
    with st.spinner("Loading courses..."):
        courses_data = st.session_state.api_client.get_courses()
    
    # Check for errors
    if "error" in courses_data:
        st.error(f"Failed to load courses: {courses_data['error']}")
        courses = []
    else:
        # Extract courses array from paginated response
        courses = courses_data.get('courses', [])
    
    # Table Header
    st.markdown("""
    <div class="table-header">
        <div style="width: 25%;">Course Name</div>
        <div style="width: 25%; text-align: center;">Category</div>
        <div style="width: 25%; text-align: center;">Status</div>
        <div style="width: 25%; text-align: center;">Type</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Store selected course in session state
    if 'selected_course_index' not in st.session_state:
        st.session_state.selected_course_index = 0
    
    # Course rows
    for i, course in enumerate(courses):
        selected_class = "selected" if i == st.session_state.selected_course_index else ""
        course_name = course.get('title', course.get('name', 'N/A'))
        course_id = course.get('id', 'N/A')
        category = course.get('category', 'N/A')
        status = course.get('status', 'N/A')
        course_type = course.get('type', 'N/A')
        
        # Create a button for each row to make it clickable
        if st.button(
            f"{course_name}", 
            key=f"course_btn_{i}",
            use_container_width=True,
            type="secondary" if i != st.session_state.selected_course_index else "primary"
        ):
            st.session_state.selected_course_index = i
            st.rerun()
        
        # Hide the button with CSS and show custom HTML
        st.markdown(f"""
        <style>
            button[data-testid="baseButton-secondary"]:has([key="course_btn_{i}"]),
            button[data-testid="baseButton-primary"]:has([key="course_btn_{i}"]) {{
                display: none;
            }}
        </style>
        <div class="table-row {selected_class}" onclick="document.querySelector('[key=course_btn_{i}]').click();" style="cursor: pointer;">
            <div style="width: 25%;">
                <div style="font-size: 16px; color: #2E2E2E;">{course_name}</div>
                <div style="font-size: 16px; color: #565656; margin-top: 4px;">ID: {course_id[:15] if len(str(course_id)) > 15 else course_id}...</div>
            </div>
            <div style="width: 25%; text-align: center;">
                <span class="category-badge">{category}</span>
            </div>
            <div style="width: 25%; text-align: center;">
                <div class="status-indicator" style="justify-content: center;">
                    <span class="status-dot"></span>
                    <span style="color: #6B7280; font-size: 16px;">{status}</span>
                </div>
            </div>
            <div style="width: 25%; text-align: center; color: #2E2E2E; font-size: 16px;">
                {course_type}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    if not courses:
        st.info("No courses found")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col_detail:
    st.markdown('<div class="detail-card">', unsafe_allow_html=True)
    
    # Course image placeholder
    st.markdown('<div class="course-image"></div>', unsafe_allow_html=True)
    
    # Course details from selected course
    if courses and st.session_state.selected_course_index < len(courses):
        course = courses[st.session_state.selected_course_index]
        course_name = course.get('title', course.get('name', 'N/A'))
        category = course.get('category', 'N/A')
        course_type = course.get('type', 'N/A')
        status = course.get('status', 'N/A')
        price = course.get('price', 0)
        instructor = course.get('instructor', 'N/A')
        
        # Course details
        detail_col1, detail_col2 = st.columns(2)
        with detail_col1:
            st.markdown(f'<div class="detail-row"><strong>Name:</strong> {course_name}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="detail-row"><strong>Category:</strong> {category}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="detail-row"><strong>Type:</strong> {course_type}</div>', unsafe_allow_html=True)
        
        with detail_col2:
            st.markdown(f'<div class="detail-row"><strong>Instructor:</strong> {instructor}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="detail-row"><strong>Status:</strong> {status}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="detail-row"><strong>Price:</strong> ${price:,.2f}</div>', unsafe_allow_html=True)
    else:
        st.info("Select a course to view details")
    
    st.markdown('<div style="margin-top: 40px;"></div>', unsafe_allow_html=True)
    
    if st.button("View More Details", key="view_details", use_container_width=True):
        st.switch_page("pages/course_details.py")
    
    st.markdown('</div>', unsafe_allow_html=True)
