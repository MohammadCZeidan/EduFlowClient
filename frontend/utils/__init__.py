"""
Utility functions and constants for EduFlow
"""
from .constants import (
    COLORS,
    FONTS,
    SPACING,
    SIDEBAR_CONFIG,
    NAVIGATION_ITEMS
)
from .helpers import (
    hide_streamlit_elements,
    apply_custom_css,
    check_authentication,
    format_currency,
    format_date
)

__all__ = [
    'COLORS',
    'FONTS',
    'SPACING',
    'SIDEBAR_CONFIG',
    'NAVIGATION_ITEMS',
    'hide_streamlit_elements',
    'apply_custom_css',
    'check_authentication',
    'format_currency',
    'format_date'
]

