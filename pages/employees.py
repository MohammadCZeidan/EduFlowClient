import streamlit as st

st.set_page_config(page_title="Employees - EduFlow", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        * {
            font-family: 'Roboto', sans-serif !important;
        }
        
        .stApp {
            background-color: #f7f8fa !important;
        }
        
        [data-testid="stSidebar"] {
            background-color: white !important;
        }
        
        .nav-item {
            padding: 10px 20px;
            border-radius: 0;
            text-align: left;
            font-size: 16px;
            color: #2E2E2E;
            margin-bottom: 20px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .nav-item.active {
            background: #E8E6FF;
            border-left: 2px solid #51287E;
            color: #51287E;
            font-weight: 400;
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
    
    if st.button("📚  Courses", key="nav_courses", use_container_width=True):
        st.switch_page("pages/courses.py")
    
    if st.button("👥  Participants", key="nav_participants", use_container_width=True):
        st.switch_page("pages/participants.py")
    
    if st.button("💳  Payments", key="nav_payments", use_container_width=True):
        st.switch_page("pages/payments.py")
    
    if st.button("👤  Employees", key="nav_employees", use_container_width=True, type="primary"):
        st.switch_page("pages/employees.py")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    
    if st.button("🚪  Logout", key="logout"):
        st.switch_page("pages/login.py")

# Main Content
st.markdown('<h2 style="color: #2E2E2E; margin-bottom: 30px;">Employees Management</h2>', unsafe_allow_html=True)

st.markdown("""
<div style="background: white; padding: 40px; border-radius: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
    <h3 style="color: #2E2E2E; margin-bottom: 20px;">All Employees</h3>
    <p style="color: #565656; font-size: 16px;">Employee management interface coming soon...</p>
</div>
""", unsafe_allow_html=True)
