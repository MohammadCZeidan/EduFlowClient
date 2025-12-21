import streamlit as st

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
        padding: 35px 30px 50px !important;
    }
    
    /* Sidebar button styling */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        padding: 10px 20px;
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

# Main content
# Header section
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.markdown('<div class="page-title">Users</div>', unsafe_allow_html=True)
with header_col2:
    if st.button("+ Add New User", key="add_user_btn", use_container_width=True):
        st.switch_page("pages/add_user.py")

st.markdown("<br>", unsafe_allow_html=True)

# Table container
st.markdown('<div class="table-container">', unsafe_allow_html=True)

# Filter bar
filter_col1, filter_col2 = st.columns([0.15, 1])

with filter_col1:
    st.selectbox("Role", ["All Roles", "Admin", "Manager", "Instructor"], key="role_filter", label_visibility="collapsed")

with filter_col2:
    st.text_input("Search", placeholder="Search....", key="search", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# Table header
st.markdown("""
<div class="table-header">
    <div class="table-header-text">Users</div>
    <div class="table-header-text">Role</div>
</div>
""", unsafe_allow_html=True)

# Sample user data
users_data = [
    {"name": "User's name", "role": "HR"},
    {"name": "User's name", "role": "HR"},
    {"name": "User's name", "role": "HR"},
    {"name": "User's name", "role": "IT"},
    {"name": "User's name", "role": "HR"},
    {"name": "User's name", "role": "HR"},
    {"name": "User's name", "role": "HR"},
]

for user in users_data:
    st.markdown(f"""
    <div class="table-row">
        <div class="user-info">
            <div class="user-avatar">👤</div>
            <div class="user-name">{user['name']}</div>
        </div>
        <div style="display: flex; gap: 252px; align-items: center;">
            <div class="user-role">{user['role']}</div>
            <div class="menu-dots">
                <div class="menu-dot"></div>
                <div class="menu-dot"></div>
                <div class="menu-dot"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
