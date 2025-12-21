import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
import calendar
import sys
import os

# Add parent directory to path to import api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_client import APIClient

st.set_page_config(page_title="EduFlow Dashboard", layout="wide")

# Initialize API client
if 'api_client' not in st.session_state:
    st.session_state.api_client = APIClient()

# Check if user is logged in
if 'access_token' not in st.session_state:
    st.warning("Please login to access the dashboard")
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
        .stButton > button {
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
        
        .stButton > button:hover {
            background-color: #f5f5f5;
        }
        
        .stButton > button[kind="primary"] {
            background-color: #E8E6FF !important;
            color: #51287E !important;
            border-left: 2px solid #51287E !important;
        }
        
        .metric-card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 150px;
        }
        
        .metric-value {
            font-size: 24px;
            font-weight: 500;
            color: #2E2E2E;
            margin: 8px 0;
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
            margin-bottom: 13px;
        }
        
        .event-card {
            background: #ECEDEF;
            padding: 15px 20px;
            border-radius: 10px;
            border-left: 5px solid;
            margin-bottom: 10px;
        }
        
        .event-title {
            font-size: 15px;
            color: #2E2E2E;
            margin-bottom: 8px;
            font-weight: 500;
        }
        
        .event-time {
            font-size: 12px;
            color: #565656;
        }
        
        .chart-container {
            background: white;
            padding: 34px;
            border-radius: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        
        .calendar-container {
            background: white;
            padding: 27px 28px;
            border-radius: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        
        .section-title {
            font-size: 16px;
            font-weight: 500;
            color: #565656;
            margin-bottom: 16px;
        }
        
        .course-card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 16px;
        }
        
        .course-name {
            font-size: 20px;
            font-weight: 400;
            color: #2E2E2E;
            margin-bottom: 12px;
        }
        
        .course-stats {
            display: flex;
            gap: 22px;
            font-size: 16px;
        }
        
        .stat-value {
            font-weight: 400;
            color: #56BB81;
        }
        
        .stat-label {
            color: #2E2E2E;
        }
        
        .stat-value.negative {
            color: #D14540;
        }
        
        .sidebar-nav {
            background: white;
            padding: 35px 30px 50px;
            border-radius: 0;
        }
        
        [data-testid="stSidebar"] {
            background-color: white !important;
        }
        
        [data-testid="stSidebarNav"] {
            background-color: white !important;
        }
        
        .nav-item {
            padding: 10px 20px;
            border-radius: 0;
            text-align: center;
            font-size: 16px;
            color: #2E2E2E;
            margin-bottom: 20px;
            cursor: pointer;
        }
        
        .nav-item.active {
            background: #E8E6FF;
            border-left: 2px solid #51287E;
            color: #51287E;
            font-weight: 400;
        }
        
        /* Sidebar button styling */
        [data-testid="stSidebar"] [data-testid="stButton"] button {
            background: transparent !important;
            border: none !important;
            color: #2E2E2E !important;
            text-align: left !important;
            padding: 10px 20px !important;
            font-size: 16px !important;
            font-weight: 400 !important;
            border-radius: 0 !important;
            width: 100% !important;
            margin-bottom: 0px !important;
        }
        
        [data-testid="stSidebar"] [data-testid="stButton"] button:hover {
            background: #f5f5f5 !important;
        }
        
        [data-testid="stSidebar"] [data-testid="stButton"] button[kind="primary"] {
            background: #E8E6FF !important;
            border-left: 2px solid #51287E !important;
            color: #51287E !important;
            font-weight: 400 !important;
        }
        
        [data-testid="stSidebar"] [data-testid="stButton"] button[kind="primary"]:hover {
            background: #E8E6FF !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("assets/logo.png", width=180)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigation buttons
    if st.button("📊  Dashboard", key="nav_dashboard", use_container_width=True, type="primary"):
        st.switch_page("pages/dashboard.py")
    
    if st.button("📚  Courses", key="nav_courses", use_container_width=True):
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

# Main Dashboard Content
# Get user info and metrics from API
user_name = st.session_state.get('user', {}).get('full_name', "User")
st.markdown(f'<h2 style="color: #2E2E2E; margin-bottom: 30px;">Hello, {user_name}</h2>', unsafe_allow_html=True)

# Fetch all data from API to calculate metrics
with st.spinner("Loading dashboard metrics..."):
    courses_response = st.session_state.api_client.get_courses()
    participants_response = st.session_state.api_client.get_participants()
    payments_response = st.session_state.api_client.get_payments()
    users_response = st.session_state.api_client.get_users()

# Calculate metrics from actual data
total_courses = 0
total_registrations = 0
total_employees = 0
total_participants = 0
total_revenue = 0
payments_collected = 0
payments_pending = 0
completion_rate = 0

# Count courses
if "error" not in courses_response:
    courses_list = courses_response.get('courses', [])
    total_courses = len(courses_list)

# Count participants and registrations
if "error" not in participants_response:
    participants_list = participants_response.get('participants', [])
    total_participants = len(participants_list)
    total_registrations = participants_response.get('total', len(participants_list))
    
    # Calculate completion rate
    completed = sum(1 for p in participants_list if p.get('course_status', '').lower() == 'completed')
    if total_participants > 0:
        completion_rate = (completed / total_participants) * 100

# Count payments and revenue
if "error" not in payments_response:
    payments_list = payments_response.get('payments', [])
    total_revenue = sum(p.get('amount', 0) for p in payments_list)
    payments_collected = sum(p.get('amount', 0) for p in payments_list if p.get('status', '').lower() == 'paid')
    payments_pending = sum(p.get('amount', 0) for p in payments_list if p.get('status', '').lower() == 'pending')

# Count employees
if "error" not in users_response:
    users_list = users_response.get('users', [])
    # Count users with roles: hr, finance, admin, instructor
    total_employees = sum(1 for u in users_list if u.get('role', '').lower() in ['hr', 'finance', 'admin', 'instructor'])

# ===== METRICS ROW 1 (4 columns) =====
st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="icon-box">📚</div>
        <div class="metric-value">{total_courses}</div>
        <div class="metric-label">Total Courses</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="icon-box">📝</div>
        <div class="metric-value">{total_registrations:,}</div>
        <div class="metric-label">Total Registration</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="icon-box">👥</div>
        <div class="metric-value">{total_employees}</div>
        <div class="metric-label">Total Employees</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="icon-box">👤</div>
        <div class="metric-value">{total_participants}</div>
        <div class="metric-label">Total Participants</div>
    </div>
    """, unsafe_allow_html=True)

# ===== METRICS ROW 2 (4 columns) =====
st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="icon-box">💰</div>
        <div class="metric-value">${total_revenue:,.2f}</div>
        <div class="metric-label">Total Revenue</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="icon-box">✅</div>
        <div class="metric-value">${payments_collected:,.2f}</div>
        <div class="metric-label">Payments Collected</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="icon-box">⏳</div>
        <div class="metric-value">${payments_pending:,.2f}</div>
        <div class="metric-label">Payments Pending</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="icon-box">⏱️</div>
        <div class="metric-value">{completion_rate:.0f}%</div>
        <div class="metric-label">Courses Completion Rate</div>
    </div>
    """, unsafe_allow_html=True)

# ===== REGISTRATIONS CHART =====
st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)
col_chart, col_courses = st.columns([1.5, 0.8], gap="medium")

with col_chart:
    st.markdown('<p class="section-title">Registrations per week</p>', unsafe_allow_html=True)
    
    weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    registrations = [120, 135, 110, 150, 165, 140, 125]
    
    fig = go.Figure(data=[
        go.Bar(
            x=weeks,
            y=registrations,
            marker_color='#51287E',
            hovertemplate='<b>%{x}</b><br>Registrations: %{y}<extra></extra>'
        )
    ])
    
    fig.update_layout(
        height=350,
        margin=dict(l=40, r=20, t=20, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            showgrid=False,
            showline=True,
            linewidth=1,
            linecolor='#6B7280',
            tickfont=dict(color='#6B7280', size=12)
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='#E5E7EB',
            showline=True,
            linewidth=1,
            linecolor='#6B7280',
            tickfont=dict(color='#6B7280', size=12)
        ),
        hovermode='x unified',
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

with col_courses:
    st.markdown('<p class="section-title" style="margin-top: 0;">Best Performing<br>Course</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="course-card">
        <div class="course-name">Leadership Basics</div>
        <div class="course-stats">
            <div><span class="stat-value">82%</span><br><span class="stat-label">Conversion</span></div>
            <div><span class="stat-value">18.2k$</span><br><span class="stat-label">Revenue</span></div>
        </div>
    </div>
    
    <p class="section-title">Underperforming<br>Course</p>
    
    <div class="course-card">
        <div class="course-name">Excel Essentials</div>
        <div class="course-stats">
            <div><span class="stat-value negative">34%</span><br><span class="stat-label">Conversion</span></div>
            <div><span class="stat-value negative">4.1k$</span><br><span class="stat-label">Revenue</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
