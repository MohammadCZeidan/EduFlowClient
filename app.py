import streamlit as st

# Set page config
st.set_page_config(
    page_title="EduFlow - HR Training & Course Management",
    page_title_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

# Page routing
if st.session_state.page == 'landing':
    st.switch_page("frontend/pages/landing.py")
elif st.session_state.page == 'login':
    st.switch_page("frontend/pages/login.py")
elif st.session_state.page == 'dashboard':
    st.switch_page("frontend/pages/dashboard.py")
