"""
EduFlow Streamlit Application

Main entry point for the Streamlit dashboard application.
This module handles initial page configuration and routes to the landing page.
"""
import streamlit as st
from pages import landing
import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.append(str(Path(__file__).parent))
from utils.helpers import hide_streamlit_elements


def _configure_page() -> None:
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="EduFlow",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': None
        }
    )


def _hide_sidebar() -> None:
    """Hide the sidebar completely using CSS"""
    st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        button[data-testid="baseButton-header"] {
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)


def main() -> None:
    """
    Main application entry point
    
    Configures the page, hides default UI elements, and renders
    the landing page (unprotected route).
    """
    _configure_page()
    _hide_sidebar()
    hide_streamlit_elements()
    
    # Always show landing page first (unprotected route)
    landing.render_landing_page()


if __name__ == "__main__":
    main()

