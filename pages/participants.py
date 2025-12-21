import streamlit as st
import plotly.graph_objects as go
import sys
import os

# Add parent directory to path to import api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_client import APIClient

# Page config
st.set_page_config(page_title="Participants", page_icon="👥", layout="wide")

# Initialize API client
if 'api_client' not in st.session_state:
    st.session_state.api_client = APIClient()

# Check if user is logged in
if 'access_token' not in st.session_state:
    st.warning("Please login to access participants")
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
    
    /* Chart container */
    .chart-container {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 30px 25px;
    }
    
    /* Table styling */
    .table-container {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 12px;
    }
    
    .table-header {
        display: grid;
        grid-template-columns: 2fr 1fr 1.5fr 1fr;
        align-items: center;
        padding: 0px 33px;
        height: 65px;
        border-top: 1px solid #EBE6E6;
        border-bottom: 1px solid #EBE6E6;
        gap: 20px;
    }
    
    .table-header-text {
        font-size: 18px;
        font-weight: 500;
        color: #565656;
    }
    
    .table-row {
        display: grid;
        grid-template-columns: 2fr 1fr 1.5fr 1fr;
        align-items: center;
        padding: 0px 33px;
        height: 65px;
        gap: 20px;
    }
    
    .table-row.selected {
        background: #E8E6FF;
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
    
    .status-accepted {
        color: #7CB342;
    }
    
    .status-pending {
        color: #2E2E2E;
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
    
    /* Year breakdown table */
    .breakdown-container {
        padding: 24px 0px 0px;
    }
    
    .breakdown-title {
        font-size: 16px;
        color: #2E2E2E;
        margin-bottom: 16px;
    }
    
    .breakdown-table-header {
        display: flex;
        justify-content: space-between;
        padding-bottom: 4px;
        border-bottom: 0.67px solid #E2E8F0;
    }
    
    .breakdown-table-header-cell {
        font-size: 14px;
        font-weight: 700;
        color: #565656;
    }
    
    .breakdown-table-body {
        display: flex;
        flex-direction: column;
        gap: 4px;
    }
    
    .breakdown-row {
        display: flex;
        justify-content: space-between;
        padding: 11px 0px;
        border-bottom: 0.67px solid #F1F5F9;
    }
    
    .breakdown-row:last-child {
        border-bottom: none;
    }
    
    .breakdown-cell {
        font-size: 16px;
        color: #2E2E2E;
    }
    
    .breakdown-growth {
        color: #00A63E;
        font-size: 16px;
    }
    
    .breakdown-growth-none {
        color: #90A1B9;
        font-size: 16px;
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
    
    if st.button("👥 Participants", key="nav_participants", type="primary", use_container_width=True):
        st.switch_page("pages/participants.py")
    
    if st.button("💰 Payments", key="nav_payments", use_container_width=True):
        st.switch_page("pages/payments.py")
    
    if st.button("� Admin", key="nav_admin", use_container_width=True):
        st.switch_page("pages/admin.py")    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("🚪 Logout", key="nav_logout", use_container_width=True):
        st.switch_page("Home.py")
# Main content
st.markdown('<div class="page-header">Participants</div>', unsafe_allow_html=True)

# Metric cards - Fetch participant data for metrics
with st.spinner("Loading metrics..."):
    participants_metrics_response = st.session_state.api_client.get_participants()

if "error" not in participants_metrics_response:
    participants_list_metrics = participants_metrics_response.get('participants', [])
    total_participants_count = len(participants_list_metrics)
    completed_count = sum(1 for p in participants_list_metrics if p.get('course_status', '').lower() == 'completed')
    ongoing_count = sum(1 for p in participants_list_metrics if p.get('course_status', '').lower() in ['active', 'in progress', 'ongoing'])
else:
    total_participants_count = 0
    completed_count = 0
    ongoing_count = 0

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">👥</div>
        <div class="metric-value">{total_participants_count}</div>
        <div class="metric-label">Total Participants</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">✓</div>
        <div class="metric-value">{completed_count}</div>
        <div class="metric-label">Completed Courses</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">🔄</div>
        <div class="metric-value">{ongoing_count}</div>
        <div class="metric-label">Ongoing Courses</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Chart and Year Breakdown section
chart_col, breakdown_col = st.columns([1.4, 1])

with chart_col:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    
    # Fetch participant analytics from API
    # TODO: Add API endpoint for participant growth by year
    # For now, using the participant count from current data
    with st.spinner("Loading analytics..."):
        participants_response = st.session_state.api_client.get_participants()
    
    if "error" not in participants_response:
        total_participants = participants_response.get('total', 0)
        participants_list = participants_response.get('participants', [])
        
        # Group by year if date field exists
        year_counts = {}
        for p in participants_list:
            # This assumes there's a created_at or year field in the data
            # Adjust based on actual API response structure
            year = "2025"  # Default to current year
            year_counts[year] = year_counts.get(year, 0) + 1
        
        # Create chart with available data
        if year_counts:
            years = sorted(year_counts.keys())
            counts = [year_counts[y] for y in years]
        else:
            years = ['2025']
            counts = [total_participants]
        
        fig = go.Figure(data=[
            go.Bar(
                x=years,
                y=counts,
                marker=dict(color='#51287E'),
                name='Participants'
            )
        ])
        
        fig.update_layout(
            height=300,
            margin=dict(l=50, r=20, t=20, b=50),
            plot_bgcolor='white',
            paper_bgcolor='white',
            xaxis=dict(
                showgrid=True,
                gridcolor='#E2E8F0',
                gridwidth=1,
                griddash='dash',
                title='',
                tickfont=dict(family='Inter', size=12, color='#64748B')
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='#E2E8F0',
                gridwidth=1,
                griddash='dash',
                title='',
                tickfont=dict(family='Inter', size=12, color='#64748B')
            ),
            showlegend=True,
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='center',
                x=0.5,
                font=dict(family='Roboto', size=16, color='#51287E')
            )
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    else:
        st.error(f"Failed to load analytics: {participants_response.get('error', 'Unknown error')}")
    
    st.markdown('</div>', unsafe_allow_html=True)

with breakdown_col:
    # Fetch year-by-year breakdown from API
    st.markdown('<div class="chart-container breakdown-container">', unsafe_allow_html=True)
    st.markdown('<div class="breakdown-title">Year-by-Year Breakdown</div>', unsafe_allow_html=True)
    
    if "error" not in participants_response:
        participants_list = participants_response.get('participants', [])
        
        # Group participants by year and calculate growth
        year_data = {}
        for p in participants_list:
            # Extract year from participant data (adjust field name as needed)
            # For now, counting current participants
            year = "2025"  # Default year, should come from API data
            year_data[year] = year_data.get(year, 0) + 1
        
        # Sort years and calculate growth
        sorted_years = sorted(year_data.keys())
        
        st.markdown("""
        <div class="breakdown-table-header">
            <div class="breakdown-table-header-cell">Year</div>
            <div class="breakdown-table-header-cell">Participants</div>
            <div class="breakdown-table-header-cell">Growth</div>
        </div>
        <div class="breakdown-table-body">
        """, unsafe_allow_html=True)
        
        prev_count = 0
        for i, year in enumerate(sorted_years):
            count = year_data[year]
            if i == 0:
                growth_html = '<div class="breakdown-growth-none">-</div>'
            else:
                growth_pct = ((count - prev_count) / prev_count * 100) if prev_count > 0 else 0
                growth_html = f'<div class="breakdown-growth">+{growth_pct:.1f}%</div>'
            
            st.markdown(f"""
            <div class="breakdown-row">
                <div class="breakdown-cell">{year}</div>
                <div class="breakdown-cell">{count}</div>
                {growth_html}
            </div>
            """, unsafe_allow_html=True)
            prev_count = count
        
        if not sorted_years:
            st.info("No year-by-year data available")
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("Unable to load breakdown data")
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Participants table
st.markdown('<div class="table-container">', unsafe_allow_html=True)

# Filter bar
filter_col1, filter_col2, filter_col3 = st.columns([1, 1, 1.5])

with filter_col1:
    st.selectbox("Course", ["All Courses", "UI/UX", "Leadership", "Excel"], key="course_filter", label_visibility="collapsed")

with filter_col2:
    st.selectbox("Type", ["All Types", "External", "Internal"], key="type_filter", label_visibility="collapsed")

with filter_col3:
    st.text_input("Search", placeholder="Search....", key="search", label_visibility="collapsed")

# Table header
st.markdown("""
<div class="table-header">
    <div class="table-header-text">Participants</div>
    <div class="table-header-text">Status</div>
    <div class="table-header-text">Course</div>
    <div class="table-header-text">Type</div>
</div>
""", unsafe_allow_html=True)

# Fetch participants from API
with st.spinner("Loading participants..."):
    participants_data_response = st.session_state.api_client.get_participants()

# Check for errors
if "error" in participants_data_response:
    st.error(f"Failed to load participants: {participants_data_response['error']}")
    participants_data = []
else:
    # Extract participants array from paginated response
    participants_data = participants_data_response.get('participants', [])

# Selected participant (first one by default)
selected_participant = participants_data[0] if participants_data else None

for i, participant in enumerate(participants_data):
    selected_class = "selected" if i == 0 else ""
    name = participant.get('name', 'N/A')
    status = participant.get('status', 'Pending')
    status_color = status.lower().replace(' ', '_')
    course = participant.get('course_name', 'N/A')
    participant_type = participant.get('type', 'N/A')
    
    st.markdown(f"""
    <div class="table-row {selected_class}">
        <div class="participant-info">
            <div class="participant-avatar">👤</div>
            <div class="participant-name">{name}</div>
        </div>
        <div class="status-{status_color}">{status}</div>
        <div class="participant-name">{course}</div>
        <div class="participant-name">{participant_type}</div>
    </div>
    """, unsafe_allow_html=True)

if not participants_data:
    st.info("No participants found")

st.markdown('</div>', unsafe_allow_html=True)
