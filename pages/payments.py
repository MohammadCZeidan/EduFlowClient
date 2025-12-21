import streamlit as st
import sys
import os

# Add parent directory to path to import api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_client import APIClient

# Page config
st.set_page_config(page_title="Payment", page_icon="💰", layout="wide")

# Initialize API client
if 'api_client' not in st.session_state:
    st.session_state.api_client = APIClient()

# Check if user is logged in
if 'access_token' not in st.session_state:
    st.warning("Please login to access payments")
    st.switch_page("pages/login.py")

# Custom CSS for styling
st.markdown("""
<style>
    /* Force light theme */
    [data-testid="stAppViewContainer"] {
        background-color: rgba(247, 248, 250, 0.949) !important;
    }
    
    /* Roboto font */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Inter:wght@400&display=swap');
    
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
    
    /* Page header */
    .page-header {
        font-size: 20px;
        font-weight: 500;
        color: #2E2E2E;
        margin-bottom: 16px;
    }
    
    /* Metric cards */
    .metric-card {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 13px 20px;
        height: 150px;
        display: flex;
        flex-direction: column;
        gap: 13px;
    }
    
    .metric-icon {
        width: 41px;
        height: 41px;
        background: #F4F4F4;
        border-radius: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    }
    
    .metric-value {
        font-size: 24px;
        font-weight: 500;
        color: #2E2E2E;
        line-height: 28px;
    }
    
    .metric-label {
        font-size: 16px;
        font-weight: 500;
        color: #565656;
        line-height: 19px;
    }
    
    /* Table styling */
    .table-container {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 12px;
    }
    
    .table-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0px 27px 0px 33px;
        height: 65px;
        border-top: 1px solid #EBE6E6;
        border-bottom: 1px solid #EBE6E6;
    }
    
    .table-header-text {
        font-size: 18px;
        font-weight: 500;
        color: #565656;
    }
    
    .table-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0px 33px;
        height: 65px;
    }
    
    .participant-info {
        display: flex;
        align-items: center;
        gap: 21px;
    }
    
    .participant-avatar {
        width: 34px;
        height: 32px;
        border-radius: 50%;
        background: linear-gradient(180deg, #FFC973 0%, #FFD7BF 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
    }
    
    .participant-name {
        font-size: 16px;
        color: #2E2E2E;
    }
    
    .payment-completed {
        color: #7CB342;
    }
    
    .payment-pending {
        color: #6A7282;
    }
    
    .payment-overdue {
        color: #D14540;
    }
    
    /* Detail panel */
    .detail-panel {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 18px 21px;
    }
    
    .detail-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 28px;
    }
    
    .detail-avatar {
        width: 66px;
        height: 63px;
        border-radius: 50%;
        background: linear-gradient(180deg, #FFC973 0%, #FFD7BF 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    }
    
    .detail-name {
        font-size: 16px;
        font-weight: 500;
        color: #2E2E2E;
    }
    
    .detail-info {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-bottom: 20px;
    }
    
    .detail-item {
        font-size: 16px;
        color: #2E2E2E;
    }
    
    .detail-button {
        width: 100%;
        padding: 3px 17px;
        background: white;
        border: 1px solid #51287E;
        border-radius: 20px;
        color: #51287E;
        font-size: 15px;
        font-weight: 500;
        cursor: pointer;
        text-align: center;
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
    
    if st.button("💰 Payments", key="nav_payments", type="primary", use_container_width=True):
        st.switch_page("pages/payments.py")
    
    if st.button("� Admin", key="nav_admin", use_container_width=True):
        st.switch_page("pages/admin.py")    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("🚪 Logout", key="nav_logout", use_container_width=True):
        st.switch_page("Home.py")
# Main content
st.markdown('<div class="page-header">Payment</div>', unsafe_allow_html=True)

# Metric cards - Fetch payment data for metrics
with st.spinner("Loading metrics..."):
    payments_metrics_response = st.session_state.api_client.get_payments()

if "error" not in payments_metrics_response:
    payments_list_metrics = payments_metrics_response.get('payments', [])
    total_revenue = sum(p.get('amount', 0) for p in payments_list_metrics)
    completed_payment_count = sum(1 for p in payments_list_metrics if p.get('status', '').lower() == 'paid')
    pending_payment_count = sum(1 for p in payments_list_metrics if p.get('status', '').lower() == 'pending')
    overdue_payment_count = sum(1 for p in payments_list_metrics if p.get('status', '').lower() == 'overdue')
else:
    total_revenue = 0
    completed_payment_count = 0
    pending_payment_count = 0
    overdue_payment_count = 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">💰</div>
        <div class="metric-value">${total_revenue:,.0f}</div>
        <div class="metric-label">Total Revenue</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">✓</div>
        <div class="metric-value">{completed_payment_count}</div>
        <div class="metric-label">Completed Payment</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">⏳</div>
        <div class="metric-value">{pending_payment_count}</div>
        <div class="metric-label">Pending Payment</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">⚠️</div>
        <div class="metric-value">{overdue_payment_count}</div>
        <div class="metric-label">Overdue Payment</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Payment table and detail panel
table_col, detail_col = st.columns([1.56, 1])

with table_col:
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    
    # Filter bar
    filter_col1, filter_col2, filter_col3 = st.columns([0.8, 1.1, 1.5])
    
    with filter_col1:
        st.selectbox("Type", ["All Types", "External", "Internal"], key="type_filter", label_visibility="collapsed")
    
    with filter_col2:
        st.selectbox("Payment", ["All Payments", "Completed", "Pending", "Overdue"], key="payment_filter", label_visibility="collapsed")
    
    with filter_col3:
        st.text_input("Search", placeholder="Search....", key="search", label_visibility="collapsed")
    
    # Table header
    st.markdown("""
    <div class="table-header">
        <div class="table-header-text">Participants</div>
        <div style="display: flex; gap: 87px;">
            <div class="table-header-text">Payment</div>
            <div class="table-header-text">Course</div>
            <div class="table-header-text">Type</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Fetch payments from API
    with st.spinner("Loading payments..."):
        payments_response = st.session_state.api_client.get_payments()
    
    # Check for errors
    if "error" in payments_response:
        error_msg = payments_response['error']
        status_code = payments_response.get('status_code', 'Unknown')
        
        # If unauthorized, redirect to login
        if status_code == 401:
            st.warning("Session expired. Please login again.")
            st.switch_page("pages/login.py")
        else:
            st.error(f"Failed to load payments: {error_msg} (Status: {status_code})")
        payments_data = []
    else:
        # Extract payments array from paginated response
        payments_data = payments_response.get('payments', [])
    
    # Selected payment (first one by default)
    selected_payment = payments_data[0] if payments_data else None
    
    for i, payment in enumerate(payments_data):
        selected_class = "selected" if i == 0 else ""
        name = payment.get('user_name', 'N/A')
        payment_status = payment.get('status', 'Pending')
        payment_color = payment_status.lower().replace(' ', '_')
        course = payment.get('course_name', 'N/A')
        participant_type = payment.get('type', 'N/A')
        
        st.markdown(f"""
        <div class="table-row {selected_class}">
            <div class="participant-info">
                <div class="participant-avatar">👤</div>
                <div class="participant-name">{name}</div>
            </div>
            <div style="display: flex; gap: 64px;">
                <div class="payment-{payment_color}">{payment_status}</div>
                <div class="participant-name">{course}</div>
                <div class="participant-name">{participant_type}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    if not payments_data:
        st.info("No payments found")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Add payment section below the table
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("### Record New Payment", unsafe_allow_html=True)

# Fetch participants and courses for dropdowns
with st.spinner("Loading data..."):
    participants_response = st.session_state.api_client.get_participants()
    courses_response = st.session_state.api_client.get_courses()

# Extract data
participants_list = participants_response.get('participants', []) if "error" not in participants_response else []
courses_list = courses_response.get('courses', []) if "error" not in courses_response else []

# Create payment form
payment_col1, payment_col2, payment_col3, payment_col4 = st.columns([2, 2, 1, 1])

with payment_col1:
    # Create participant options
    participant_options = ["Select Candidate"] + [f"{p.get('name', 'N/A')} - {p.get('course_name', 'N/A')}" for p in participants_list]
    selected_participant = st.selectbox("Select Candidate", participant_options, key="payment_participant")

with payment_col2:
    # Create course options
    course_options = ["Select Course"] + [c.get('title', c.get('name', 'N/A')) for c in courses_list]
    selected_course = st.selectbox("Select Course", course_options, key="payment_course")

with payment_col3:
    payment_amount = st.number_input("Amount ($)", min_value=0.0, step=10.0, key="payment_amount")

with payment_col4:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Mark as Paid", use_container_width=True, type="primary"):
        if selected_participant != "Select Candidate" and selected_course != "Select Course" and payment_amount > 0:
            # Get participant index
            participant_index = participant_options.index(selected_participant) - 1
            if participant_index >= 0 and participant_index < len(participants_list):
                participant = participants_list[participant_index]
                participant_id = participant.get('id')
                
                # Get course index
                course_index = course_options.index(selected_course) - 1
                if course_index >= 0 and course_index < len(courses_list):
                    course = courses_list[course_index]
                    course_id = course.get('id')
                    
                    # Create payment record via API
                    with st.spinner("Recording payment..."):
                        result = st.session_state.api_client.create_payment(
                            participant_id=participant_id,
                            course_id=course_id,
                            amount=payment_amount,
                            status="paid"
                        )
                    
                    if "error" in result:
                        st.error(f"Failed to record payment: {result['error']}")
                    else:
                        st.success(f"Payment of ${payment_amount:.2f} recorded for {participant.get('name', 'N/A')} - {selected_course}")
                        st.rerun()
        else:
            st.error("Please fill in all fields (Candidate, Course, and Amount)")

with detail_col:
    if selected_payment:
        name = selected_payment.get('user_name', 'N/A')
        course = selected_payment.get('course_name', 'N/A')
        cohort = selected_payment.get('cohort_name', 'N/A')
        payment_status = selected_payment.get('status', 'N/A')
        amount = selected_payment.get('amount', 0)
        
        st.markdown(f"""
        <div class="detail-panel">
            <div class="detail-header">
                <div class="detail-avatar">👤</div>
                <div class="detail-name">{name}</div>
            </div>
            
            <div class="detail-info">
                <div class="detail-item">Course: {course}</div>
                <div class="detail-item">Cohort: {cohort}</div>
                <div class="detail-item">Amount: ${amount:,.2f}</div>
                <div class="detail-item">Payment Status: {payment_status}</div>
            </div>
            
            <div class="detail-button">View More Details</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("No payment selected")
