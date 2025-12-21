import streamlit as st

# Page config
st.set_page_config(page_title="User Details", page_icon="👤", layout="wide")

# Get user ID from query params (would come from clicking in admin page)
query_params = st.query_params
user_id = query_params.get("id", "1")
user_name = query_params.get("name", "User's name")
user_role = query_params.get("role", "HR")

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
    
    /* User details container */
    .details-container {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 30px;
        max-width: 800px;
    }
    
    .details-title {
        font-size: 20px;
        font-weight: 500;
        color: #000000;
        margin-bottom: 24px;
    }
    
    .user-avatar-large {
        width: 100px;
        height: 100px;
        background: #F4F4F4;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 48px;
        margin-bottom: 24px;
    }
    
    .detail-row {
        margin-bottom: 20px;
        padding-bottom: 20px;
        border-bottom: 1px solid #ECEDEF;
    }
    
    .detail-label {
        font-size: 14px;
        font-weight: 500;
        color: #565656;
        margin-bottom: 8px;
    }
    
    .detail-value {
        font-size: 16px;
        font-weight: 400;
        color: #000000;
    }
    
    .action-buttons {
        display: flex;
        gap: 16px;
        margin-top: 32px;
    }
    
    .delete-btn {
        padding: 8px 24px;
        border: 1px solid #D14540;
        border-radius: 20px;
        background: white;
        color: #D14540;
        font-size: 15px;
        font-weight: 500;
        cursor: pointer;
    }
    
    .back-btn {
        padding: 8px 24px;
        border: 1px solid #51287E;
        border-radius: 20px;
        background: white;
        color: #51287E;
        font-size: 15px;
        font-weight: 500;
        cursor: pointer;
    }
    
    /* Selectbox and TextInput styling */
    .stTextInput > div {
        background: white !important;
    }
    
    .stTextInput > div > div {
        background: white !important;
    }
    
    .stTextInput > div > div > input {
        background: white !important;
        color: #000000 !important;
        border: 1px solid #C9C8C8;
        border-radius: 5px;
        padding: 4px 13px;
        font-size: 15px;
        height: 38px;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #000000;
    }
    
    .stTextInput label {
        color: #000000 !important;
        font-size: 14px !important;
        font-weight: 500 !important;
    }
    
    .stSelectbox > div > div {
        background: white !important;
        color: #000000 !important;
        border: 1px solid #C9C8C8;
        border-radius: 5px;
    }
    
    .stSelectbox > div > div > div {
        background: white !important;
        color: #000000 !important;
    }
    
    .stSelectbox label {
        color: #000000 !important;
        font-size: 14px !important;
        font-weight: 500 !important;
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

st.markdown('<div class="breadcrumb-separator">/ User Details</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# User details container
st.markdown('<div class="details-container">', unsafe_allow_html=True)
st.markdown('<div class="details-title">User Details</div>', unsafe_allow_html=True)

# User avatar
st.markdown('<div class="user-avatar-large">👤</div>', unsafe_allow_html=True)

# Display mode vs Edit mode
if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False

if not st.session_state.edit_mode:
    # View mode
    st.markdown(f"""
    <div class="detail-row">
        <div class="detail-label">Full Name</div>
        <div class="detail-value">{user_name}</div>
    </div>
    
    <div class="detail-row">
        <div class="detail-label">Email</div>
        <div class="detail-value">user@company.com</div>
    </div>
    
    <div class="detail-row">
        <div class="detail-label">Role</div>
        <div class="detail-value">{user_role}</div>
    </div>
    
    <div class="detail-row">
        <div class="detail-label">Status</div>
        <div class="detail-value">Active</div>
    </div>
    
    <div class="detail-row">
        <div class="detail-label">Created Date</div>
        <div class="detail-value">2025-01-15</div>
    </div>
    
    <div class="detail-row">
        <div class="detail-label">Last Login</div>
        <div class="detail-value">2025-12-20 09:30 AM</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 3])
    
    with col1:
        if st.button("Edit User", key="edit_btn", use_container_width=True):
            st.session_state.edit_mode = True
            st.rerun()
    
    with col2:
        if st.button("Delete User", key="delete_btn", use_container_width=True):
            st.session_state.show_delete_confirm = True
            st.rerun()

else:
    # Edit mode
    st.markdown('<br>', unsafe_allow_html=True)
    
    name_input = st.text_input("Full Name", value=user_name, key="name_edit")
    email_input = st.text_input("Email", value="user@company.com", key="email_edit")
    role_input = st.selectbox("Role", ["Admin", "Manager", "Instructor", "HR"], index=["Admin", "Manager", "Instructor", "HR"].index(user_role) if user_role in ["Admin", "Manager", "Instructor", "HR"] else 3, key="role_edit")
    status_input = st.selectbox("Status", ["Active", "Inactive"], key="status_edit")
    
    st.markdown('<br>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 3])
    
    with col1:
        if st.button("Save Changes", key="save_btn", use_container_width=True):
            st.success("User updated successfully!")
            st.session_state.edit_mode = False
            st.rerun()
    
    with col2:
        if st.button("Cancel", key="cancel_btn", use_container_width=True):
            st.session_state.edit_mode = False
            st.rerun()

# Delete confirmation dialog
if 'show_delete_confirm' in st.session_state and st.session_state.show_delete_confirm:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.warning("⚠️ Are you sure you want to delete this user? This action cannot be undone.")
    
    col1, col2, col3 = st.columns([1, 1, 3])
    
    with col1:
        if st.button("Confirm Delete", key="confirm_delete_btn", use_container_width=True):
            st.success("User deleted successfully!")
            st.session_state.show_delete_confirm = False
            # Wait 2 seconds then redirect
            import time
            time.sleep(2)
            st.switch_page("pages/admin.py")
    
    with col2:
        if st.button("Cancel Delete", key="cancel_delete_btn", use_container_width=True):
            st.session_state.show_delete_confirm = False
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
