"""
Shared Sidebar Component for EduFlow

This module provides a reusable sidebar navigation component that is used
across all dashboard pages. It includes navigation items, active state
management, and logout functionality.
"""
import streamlit as st
from typing import Optional
import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.append(str(Path(__file__).parent.parent))
from utils.constants import (
    COLORS,
    FONTS,
    SPACING,
    SIDEBAR_CONFIG,
    NAVIGATION_ITEMS
)


def _get_sidebar_css() -> str:
    """
    Generate CSS for the sidebar component
    
    Returns:
        CSS string for sidebar styling
    """
    return f"""
    <style>
        /* Hide Streamlit's default page navigation */
        [data-testid="stSidebar"] nav[data-testid="stSidebarNav"] {{
            display: none !important;
        }}
        
        [data-testid="stSidebar"] [data-testid="stSidebarNav"] {{
            display: none !important;
        }}
        
        /* Hide any default Streamlit navigation elements */
        [data-testid="stSidebar"] ul[class*="nav"] {{
            display: none !important;
        }}
        
        [data-testid="stSidebar"] div[class*="nav"] {{
            display: none !important;
        }}
        
        /* Sidebar container styling */
        [data-testid="stSidebar"] {{
            background: {SIDEBAR_CONFIG['background']};
            padding: {SIDEBAR_CONFIG['padding']};
        }}
        
        [data-testid="stSidebar"] > div:first-child {{
            padding-top: 0;
        }}
        
        /* Hide Streamlit's default sidebar content */
        [data-testid="stSidebar"] > div:first-child > div:first-child {{
            display: none !important;
        }}
        
        /* Logo styling */
        .sidebar-logo {{
            font-family: {FONTS['primary']};
            font-weight: 700;
            font-size: {SIDEBAR_CONFIG['logo_font_size']};
            line-height: {SIDEBAR_CONFIG['logo_line_height']};
            color: {COLORS['text_dark']};
            margin-bottom: {SIDEBAR_CONFIG['logo_margin_bottom']};
        }}
        
        /* Navigation item styling */
        .nav-item {{
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: {SIDEBAR_CONFIG['nav_item_padding']};
            gap: {SIDEBAR_CONFIG['nav_item_gap']};
            width: {SIDEBAR_CONFIG['nav_item_width']};
            height: {SIDEBAR_CONFIG['nav_item_height']};
            margin-bottom: {SIDEBAR_CONFIG['nav_item_margin_bottom']};
            border-radius: 0;
            cursor: pointer;
            transition: background 0.3s ease;
        }}
        
        .nav-item.active {{
            background: {COLORS['primary_light']};
            border-left: 2px solid {COLORS['primary']};
        }}
        
        .nav-item:hover {{
            background: {COLORS['background_light']};
        }}
    </style>
    """


def _render_logo() -> None:
    """Render the EduFlow logo in the sidebar"""
    st.markdown(
        '<div class="sidebar-logo">EduFlow</div>',
        unsafe_allow_html=True
    )


def _render_navigation_items(current_page: str) -> None:
    """
    Render navigation items in the sidebar
    
    Args:
        current_page: The current active page identifier
    """
    for item_name, icon, page_key, page_path in NAVIGATION_ITEMS:
        is_active = (current_page.lower() == page_key.lower())
        
        if st.button(
            f"{icon} {item_name}",
            key=f"nav_{page_key}",
            use_container_width=True
        ):
            if page_path:
                st.switch_page(page_path)


def _render_logout_button() -> None:
    """Render the logout button in the sidebar"""
    st.markdown(
        f'<div style="margin-top: {SPACING["xl"]};"></div>',
        unsafe_allow_html=True
    )
    
    if st.button("🚪 Logout", key="logout_btn", use_container_width=True):
        st.session_state['authenticated'] = False
        st.session_state.pop('user_email', None)
        st.switch_page("pages/login.py")


def render_sidebar(current_page: str = "dashboard") -> None:
    """
    Render the shared sidebar navigation component
    
    This function renders a complete sidebar with:
    - EduFlow logo
    - Navigation items (Dashboard, Courses, Participants, etc.)
    - Active state highlighting
    - Logout button
    
    Args:
        current_page: The current active page name (e.g., "dashboard", "courses")
                     Used to highlight the active navigation item
    """
    # Apply sidebar CSS
    st.markdown(_get_sidebar_css(), unsafe_allow_html=True)
    
    # Render sidebar components
    _render_logo()
    _render_navigation_items(current_page)
    _render_logout_button()

