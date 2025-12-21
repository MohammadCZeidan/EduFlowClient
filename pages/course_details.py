import streamlit as st

st.set_page_config(page_title="Course Details - EduFlow", layout="wide")

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
        
        .detail-container {
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        
        .detail-section {
            margin-bottom: 30px;
        }
        
        .detail-label {
            font-size: 14px;
            color: #565656;
            font-weight: 500;
            margin-bottom: 5px;
        }
        
        .detail-value {
            font-size: 18px;
            color: #2E2E2E;
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
col_back, col_title = st.columns([0.5, 5])
with col_back:
    if st.button("← Back"):
        st.switch_page("pages/courses.py")
with col_title:
    st.markdown('<h2 style="color: #2E2E2E; margin-bottom: 30px;">Course Details</h2>', unsafe_allow_html=True)

st.markdown('<div class="detail-container">', unsafe_allow_html=True)

# Course Image
st.markdown("""
<div style="width: 100%; max-width: 600px; height: 300px; background: #D8D7D7; border-radius: 15px; margin-bottom: 40px;"></div>
""", unsafe_allow_html=True)

# Course Details
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="detail-section">
        <div class="detail-label">Course Name</div>
        <div class="detail-value">UI/UX Design Fundamentals</div>
    </div>
    
    <div class="detail-section">
        <div class="detail-label">Category</div>
        <div class="detail-value">Skills</div>
    </div>
    
    <div class="detail-section">
        <div class="detail-label">Type</div>
        <div class="detail-value">External</div>
    </div>
    
    <div class="detail-section">
        <div class="detail-label">Enrolled Participants</div>
        <div class="detail-value">45 Students</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="detail-section">
        <div class="detail-label">Cohort</div>
        <div class="detail-value">UIX07</div>
    </div>
    
    <div class="detail-section">
        <div class="detail-label">Status</div>
        <div class="detail-value">Ongoing</div>
    </div>
    
    <div class="detail-section">
        <div class="detail-label">Price</div>
        <div class="detail-value">1,000$</div>
    </div>
    
    <div class="detail-section">
        <div class="detail-label">Duration</div>
        <div class="detail-value">8 Weeks</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="detail-section">
    <div class="detail-label">Course Description</div>
    <div class="detail-value" style="line-height: 1.6;">
        This comprehensive UI/UX Design course covers the fundamentals of user interface and user experience design. 
        Students will learn design principles, prototyping tools, user research methods, and best practices for 
        creating intuitive and engaging digital experiences.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="margin-top: 40px;"></div>', unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 3])
with col_btn1:
    if st.button("Edit Course", type="primary", use_container_width=True):
        st.info("Edit functionality coming soon!")

with col_btn2:
    if st.button("Delete Course", use_container_width=True):
        st.warning("Delete functionality coming soon!")

st.markdown('</div>', unsafe_allow_html=True)
