import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path to import api_client
sys.path.append(str(Path(__file__).parent.parent))
from api_client import get_api_client

# Page config
st.set_page_config(page_title="Admin", page_icon="👥", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* Force light theme */
    [data-testid="stAppViewContainer"] {
        background-color: rgba(247, 248, 250, 0.949) !important;
    }
    
    /* Roboto font */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Gothic+A1:wght@500&display=swap');
    
    * {
        font-family: 'Roboto', sans-serif !important;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Selectbox and TextInput styling */
    .stSelectbox > div > div {
        background: white !important;
        color: #000000 !important;
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
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #000000 !important;
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
    
    /* Main content area */
    .main .block-container {
        padding: 35px 50px !important;
        max-width: 100% !important;
    }
    
    /* Header section */
    .header-section {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
    }
    
    .page-title {
        font-size: 20px;
        font-weight: 500;
        color: #000000;
    }
    
    /* Add user button specific styling */
    div[data-testid="column"]:nth-child(2) .stButton > button {
        background: #FFFFFF !important;
        border: 1px solid #51287E !important;
        border-radius: 20px !important;
        color: #51287E !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        padding: 3px 17px !important;
        height: 32px !important;
        width: 142px !important;
        text-align: center !important;
        justify-content: center !important;
        border-left: 1px solid #51287E !important;
    }
    
    /* Menu dots button styling */
    .stPopover > button {
        background: white !important;
        border: none !important;
        color: #2E2E2E !important;
        font-size: 20px !important;
        padding: 4px 8px !important;
        min-width: auto !important;
        height: 32px !important;
    }
    
    .stPopover > button:hover {
        background: white !important;
    }
    
    /* Force white background on all button states */
    .stPopover button[data-testid="baseButton-header"] {
        background-color: white !important;
        background: white !important;
        color: #2E2E2E !important;
        border: none !important;
        padding: 4px 8px !important;
    }
    
    .stPopover button[data-testid="baseButton-header"]:hover {
        background-color: white !important;
        background: white !important;
    }
    
    .stPopover button[data-testid="baseButton-header"]:active {
        background-color: white !important;
        background: white !important;
    }
    
    .stPopover button[data-testid="baseButton-header"]:focus {
        background-color: white !important;
        background: white !important;
    }
    
    /* Popover menu styling */
    [data-baseweb="popover"] {
        background: white !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
    }
    
    .menu-option-btn {
        background: white !important;
        border: none !important;
        color: #2E2E2E !important;
        text-align: left !important;
        padding: 8px 16px !important;
        width: 120px !important;
        font-size: 15px !important;
    }
    
    .menu-option-btn:hover {
        background: #f5f5f5 !important;
    }
    
    .delete-option-btn {
        color: #D14540 !important;
    }
    
    /* Style buttons inside popover */
    .stPopover .stButton > button {
        background: white !important;
        color: #2E2E2E !important;
        border: none !important;
        text-align: left !important;
        padding: 8px 16px !important;
        width: 100% !important;
        border-radius: 4px !important;
    }
    
    .stPopover .stButton > button:hover {
        background: #f5f5f5 !important;
    }
    
    /* Table container */
    .table-container {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 24px 12px;
    }
    
    /* Filter bar */
    .filter-bar {
        display: flex;
        gap: 16px;
        margin: 0 auto;
        width: 983px;
        margin-bottom: 20px;
    }
    
    .role-dropdown {
        background: #ECEDEF;
        border-radius: 20px;
        padding: 4px 20px;
        width: 129px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    
    .search-box {
        background: #ECEDEF;
        border-radius: 50px;
        padding: 5px 20px;
        width: 838px;
        height: 40px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Table header */
    .table-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0px 33px;
        height: 65px;
        border-top: 1px solid #ECEDEF;
        border-bottom: 1px solid #EBE6E6;
        margin: 0 auto;
        width: 983px;
    }
    
    .table-header-text {
        font-size: 18px;
        font-weight: 500;
        color: #565656;
    }
    
    /* Table row */
    .table-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0px 33px;
        height: 65px;
        margin: 0 auto;
        width: 983px;
    }
    
    .user-info {
        display: flex;
        align-items: center;
        gap: 21px;
    }
    
    .user-avatar {
        width: 34px;
        height: 32px;
        border-radius: 50%;
        background: linear-gradient(180deg, #FFC973 0%, #FFD7BF 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
    }
    
    .user-name {
        font-size: 16px;
        color: #2E2E2E;
    }
    
    .user-role {
        font-size: 16px;
        color: #2E2E2E;
    }
    
    .menu-dots {
        display: flex;
        flex-direction: column;
        gap: 4px;
    }
    
    .menu-dot {
        width: 4px;
        height: 4px;
        background: #C9C8C8;
        border-radius: 50%;
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
# Header section
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.markdown('<div class="page-title">Users</div>', unsafe_allow_html=True)
with header_col2:
    if st.button("+ Add New User", key="add_user_btn", use_container_width=True):
        st.switch_page("pages/add_user.py")

st.markdown("<br>", unsafe_allow_html=True)

# Get API client
api_client = get_api_client()

# Filter bar
filter_col1, filter_col2 = st.columns([0.15, 1])

with filter_col1:
    role_filter = st.selectbox("Role", ["All Roles", "HR", "IT", "Admin", "Finance"], key="role_filter", label_visibility="collapsed")

with filter_col2:
    search_filter = st.text_input("Search", placeholder="Search....", key="search", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# Table header
st.markdown("""
<div class="table-header">
    <div class="table-header-text" style="flex: 4; margin-left: 17px;">Users</div>
    <div class="table-header-text" style="flex: 1;">Role</div>
    <div style="flex: 0.2;"></div>
</div>
""", unsafe_allow_html=True)

# Fetch users from API
users_response = api_client.get_users(role=role_filter if role_filter != "All Roles" else None, 
                                     search=search_filter if search_filter else None)

if "error" in users_response:
    st.error(f"Failed to load users: {users_response['error']}")
    users_data = []
else:
    users_data = users_response.get("users", [])

if not users_data:
    st.info("No users found.")
else:
    for idx, user in enumerate(users_data):
        col1, col2, col3 = st.columns([2, 1, 0.2])
        
        with col1:
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 16px; padding: 20px 0;">
                <div class="user-avatar">👤</div>
                <div class="user-name">{user.get('full_name', user.get('name', 'Unknown'))}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style="padding: 20px 0;">
                <div class="user-role">{user.get('role', 'N/A').upper()}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            if st.button(" Delete", key=f"delete_{user.get('id', idx)}", use_container_width=True):
                # Call API to delete user
                delete_response = api_client.delete_user(user.get('id'))
                if "error" in delete_response:
                    st.error(f"Failed to delete user: {delete_response['error']}")
                else:
                    st.success(f"User {user.get('full_name', 'Unknown')} deleted successfully!")
                    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
