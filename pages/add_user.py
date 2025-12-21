import streamlit as st
import sys
import os

# Add parent directory to path to import api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_client import APIClient

# Page config
st.set_page_config(page_title="Add New User", page_icon="👤", layout="wide")

# Initialize API client
if 'api_client' not in st.session_state:
    st.session_state.api_client = APIClient()

# Check if user is logged in
if 'access_token' not in st.session_state:
    st.warning("Please login to add users")
    st.switch_page("pages/login.py")

# Custom CSS for styling
st.markdown("""
<style>
    /* Force light theme */
    [data-testid="stAppViewContainer"] {
        background-color: rgba(247, 248, 250, 0.949) !important;
    }
    
    /* Roboto font */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
    
    * {
        font-family: 'Roboto', sans-serif !important;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
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
    
    /* Main content area */
    .main .block-container {
        padding: 37px 50px !important;
        max-width: 100% !important;
    }
    
    /* Breadcrumb */
    .breadcrumb {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 16px;
    }
    
    .breadcrumb-link {
        font-size: 15px;
        color: #000000;
        text-decoration: none;
        cursor: pointer;
    }
    
    .breadcrumb-separator {
        font-size: 15px;
        color: #000000;
    }
    
    /* Form container */
    .form-container {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 18px 16px;
        max-width: 650px;
    }
    
    .form-title {
        font-size: 20px;
        font-weight: 500;
        color: #000000;
        margin-bottom: 16px;
    }
    
    .form-field {
        margin-bottom: 12px;
    }
    
    .form-label {
        font-size: 15px;
        font-weight: 400;
        color: #000000;
        margin-bottom: 8px;
        display: block;
    }
    
    .form-input {
        width: 100%;
        padding: 4px 13px;
        border: 1px solid #C9C8C8;
        border-radius: 5px;
        font-size: 15px;
        color: #000000;
        background: white;
        height: 38px;
    }
    
    .form-input::placeholder {
        color: #000000;
    }
    
    .submit-button {
        display: flex;
        justify-content: flex-end;
        margin-top: 16px;
    }
    
    .submit-btn {
        padding: 3px 17px;
        border: 1px solid #000000;
        border-radius: 20px;
        background: white;
        color: #000000;
        font-size: 15px;
        font-weight: 500;
        cursor: pointer;
        width: 142px;
        height: 32px;
        text-align: center;
    }
    
    /* Streamlit input styling */
    .stTextInput > div > div > input {
        border: 1px solid #C9C8C8;
        border-radius: 5px;
        padding: 4px 13px;
        font-size: 15px;
        height: 38px;
        background: white !important;
        color: #000000 !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #000000;
    }
    
    .stTextInput label {
        color: #000000 !important;
    }
    
    .stSelectbox > div > div {
        border: 1px solid #C9C8C8;
        border-radius: 5px;
        background: white;
    }
    
    .stSelectbox label {
        color: #000000 !important;
    }
    
    .stSelectbox > div > div > div {
        color: #000000 !important;
        background: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("assets/logo.png", width=180)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("📊 Dashboard", key="nav_dashboard", use_container_width=True):
        st.switch_page("pages/dashboard.py")
    
    if st.button("📚 Courses", key="nav_courses", use_container_width=True):
        st.switch_page("pages/courses.py")
    
    if st.button("👥 Participants", key="nav_participants", use_container_width=True):
        st.switch_page("pages/participants.py")
    
    if st.button("💰 Payments", key="nav_payments", use_container_width=True):
        st.switch_page("pages/payments.py")
    
    if st.button("👤 Admin", key="nav_admin", type="primary", use_container_width=True):
        st.switch_page("pages/admin.py")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("🚪 Logout", key="nav_logout", use_container_width=True):
        st.switch_page("Home.py")

# Main content
# Breadcrumb navigation
if st.button("← Users", key="back_to_users"):
    st.switch_page("pages/admin.py")

st.markdown('<div class="breadcrumb-separator">/ Add New User</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Form container
st.markdown('<div class="form-container">', unsafe_allow_html=True)
st.markdown('<div class="form-title">Add New User</div>', unsafe_allow_html=True)

# Form fields
name = st.text_input("Name", placeholder="Enter Name", label_visibility="visible", key="user_name")
st.markdown("<br>", unsafe_allow_html=True)

email = st.text_input("Email", placeholder="Enter Email", label_visibility="visible", key="user_email")
st.markdown("<br>", unsafe_allow_html=True)

password = st.text_input("Password", placeholder="Enter Password", type="password", label_visibility="visible", key="user_password")
st.markdown("<br>", unsafe_allow_html=True)

role = st.selectbox("Role", ["Select Role", "hr", "finance", "admin", "instructor", "student"], key="user_role")
st.markdown("<br>", unsafe_allow_html=True)

confirm_password = st.text_input("Confirm Password", placeholder="Confirm Password", type="password", label_visibility="visible", key="user_confirm_password")

# Submit button
st.markdown('<div class="submit-button">', unsafe_allow_html=True)
if st.button("+ Add New User", key="submit_user"):
    if password == confirm_password and name and email and role != "Select Role":
        # Call API to create user
        with st.spinner("Creating user..."):
            result = st.session_state.api_client.create_user(
                email=email,
                full_name=name,
                role=role,
                password=password
            )
        
        if "error" in result:
            st.error(f"Failed to create user: {result['error']}")
        else:
            st.success("User added successfully!")
            st.switch_page("pages/admin.py")
    elif password != confirm_password:
        st.error("Passwords do not match!")
    else:
        st.error("Please fill all fields!")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
