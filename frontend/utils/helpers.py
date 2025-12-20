"""
Helper functions for EduFlow application
"""
import streamlit as st
from datetime import datetime
from typing import Optional


def hide_streamlit_elements() -> None:
    """
    Hide default Streamlit UI elements (header, footer, menu)
    """
    st.markdown("""
    <style>
        #MainMenu {visibility: hidden !important; display: none !important;}
        footer {visibility: hidden !important; display: none !important;}
        header {visibility: hidden !important; display: none !important;}
        section[data-testid="stSidebar"] {display: none !important; visibility: hidden !important;}
        button[data-testid="baseButton-header"] {display: none !important; visibility: hidden !important;}
    </style>
    """, unsafe_allow_html=True)


def apply_custom_css(css: str) -> None:
    """
    Apply custom CSS to the page
    
    Args:
        css: CSS string to apply
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def check_authentication(redirect_to: str = "pages/login.py") -> bool:
    """
    Check if user is authenticated, redirect if not
    
    Args:
        redirect_to: Page to redirect to if not authenticated
        
    Returns:
        True if authenticated, False otherwise
    """
    if not st.session_state.get('authenticated', False):
        st.switch_page(redirect_to)
        return False
    return True


def format_currency(amount: float, currency: str = "$") -> str:
    """
    Format a number as currency
    
    Args:
        amount: The amount to format
        currency: Currency symbol
        
    Returns:
        Formatted currency string
    """
    return f"{currency}{amount:,.0f}"


def format_date(date: datetime, format_str: str = "%B %d, %Y") -> str:
    """
    Format a datetime object as a string
    
    Args:
        date: The datetime object to format
        format_str: Format string
        
    Returns:
        Formatted date string
    """
    return date.strftime(format_str)


def remove_streamlit_spacing() -> None:
    """
    Remove all default Streamlit spacing and padding
    """
    st.markdown("""
    <style>
        .main .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        
        [data-testid="stAppViewContainer"] {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        [data-testid="stVerticalBlock"] {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        [data-testid="element-container"] {
            padding: 0 !important;
            margin: 0 !important;
        }
    </style>
    """, unsafe_allow_html=True)

