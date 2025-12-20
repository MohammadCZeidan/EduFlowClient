"""
Constants used throughout the EduFlow application
"""
from typing import List, Tuple

# Color Palette
COLORS = {
    'primary': '#51287E',
    'primary_hover': '#3d1f5e',
    'primary_light': '#E8E6FF',
    'secondary': '#B3B3B3',
    'text_dark': '#2E2E2E',
    'text_medium': '#565656',
    'text_light': '#C9C8C8',
    'background': '#ECEDEF',
    'background_light': '#F4F4F4',
    'white': '#FFFFFF',
    'success': '#56BB81',
    'warning': '#DCB104',
    'error': '#C97A86',
    'ellipse_top': 'rgba(214, 210, 255, 0.34)',
    'ellipse_bottom': 'rgba(214, 210, 254, 0.34)',
    'dashboard_bg': '#D6D2FF',
}

# Typography
FONTS = {
    'primary': "'Roboto', sans-serif",
    'secondary': "'Arial', sans-serif",
    'inter': "'Inter', sans-serif",
}

# Spacing Scale
SPACING = {
    'xs': '5px',
    'sm': '10px',
    'md': '20px',
    'lg': '30px',
    'xl': '40px',
    'xxl': '50px',
}

# Sidebar Configuration
SIDEBAR_CONFIG = {
    'background': COLORS['white'],
    'padding': '35px 30px 50px',
    'logo_font_size': '20px',
    'logo_line_height': '23px',
    'logo_margin_bottom': '38px',
    'nav_item_width': '220px',
    'nav_item_height': '44px',
    'nav_item_padding': '10px 20px',
    'nav_item_gap': '12px',
    'nav_item_margin_bottom': '20px',
}

# Navigation Items Configuration
NAVIGATION_ITEMS: List[Tuple[str, str, str, str]] = [
    ("Dashboard", "📊", "dashboard", "pages/dashboard.py"),
    ("Courses", "📚", "courses", "pages/courses.py"),
    ("Participants", "👥", "participants", "pages/participants.py"),
    ("Payments", "💳", "payments", "pages/payments.py"),
    ("Registrations", "📝", "registrations", "pages/registrations.py"),
    ("Employees", "👤", "employees", "pages/employees.py"),
]

# Landing Page Dimensions
LANDING_PAGE = {
    'width': '1280px',
    'height': '832px',
    'container_padding': '71px',
    'header_top': '49px',
    'content_top': '219px',
}

# Login Page Dimensions
LOGIN_PAGE = {
    'container_width': '593px',
    'container_height': '536px',
    'content_width': '380px',
    'content_height': '408px',
    'welcome_section_width': '258px',
    'welcome_section_height': '90px',
}

