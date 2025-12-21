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
        
        [data-testid="stSidebar"] {
            background-color: white !important;
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
    
    if st.button("👤  Employees", key="nav_employees", use_container_width=True):
        st.switch_page("pages/employees.py")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    
    if st.button("🚪  Logout", key="logout"):
        st.switch_page("pages/login.py")

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
