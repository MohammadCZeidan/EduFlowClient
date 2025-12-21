import streamlit as st

st.set_page_config(page_title="Add New Course - EduFlow", layout="wide")

# Custom CSS
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
        
        .form-container {
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
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
    
    if st.button("👤  Admin", key="nav_admin", use_container_width=True):
        st.switch_page("pages/admin.py")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("🚪  Logout", key="nav_logout", use_container_width=True):
        st.switch_page("Home.py")

# Main Content
st.markdown('<h2 style="color: #2E2E2E; margin-bottom: 30px;">Add New Course</h2>', unsafe_allow_html=True)

st.markdown('<div class="form-container">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.text_input("Course Name", placeholder="Enter course name")
    st.selectbox("Category", ["Skills", "Leadership", "Technical", "Management"])
    st.selectbox("Type", ["External", "Internal"])
    
with col2:
    st.text_input("Cohort ID", placeholder="Enter cohort ID")
    st.selectbox("Status", ["Ongoing", "Completed", "Upcoming"])
    st.text_input("Price", placeholder="Enter price")

st.text_area("Course Description", placeholder="Enter course description", height=150)

st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 3])
with col_btn1:
    if st.button("Save Course", type="primary", use_container_width=True):
        st.success("Course added successfully!")
        st.switch_page("pages/courses.py")

with col_btn2:
    if st.button("Cancel", use_container_width=True):
        st.switch_page("pages/courses.py")

st.markdown('</div>', unsafe_allow_html=True)
