# EduFlow Frontend

A modern, clean Streamlit-based dashboard application for educational course management.

## 📁 Project Structure

```
frontend/
├── app.py                 # Main application entry point
├── components/            # Reusable UI components
│   ├── __init__.py
│   └── sidebar.py         # Shared sidebar navigation component
├── pages/                 # Application pages
│   ├── landing.py        # Landing page (unprotected)
│   ├── login.py          # Login page (unprotected)
│   ├── dashboard.py      # Main dashboard (protected)
│   ├── courses.py        # Courses listing (protected)
│   ├── add_course.py     # Add course form (protected)
│   ├── edit_course.py    # Edit course form (protected)
│   └── view_course.py    # View course details (protected)
├── utils/                 # Utility functions and constants
│   ├── __init__.py
│   ├── constants.py      # Application constants (colors, fonts, etc.)
│   └── helpers.py        # Helper functions
└── assets/                # Static assets (images, etc.)
    ├── Dashboard.jpg
    └── logo.png
```

## 🎨 Design System

### Colors
- **Primary**: `#51287E` (Purple)
- **Primary Light**: `#E8E6FF` (Light Purple)
- **Secondary**: `#B3B3B3` (Gray)
- **Text Dark**: `#2E2E2E`
- **Background**: `#ECEDEF`

### Typography
- **Primary Font**: Roboto
- **Secondary Font**: Arial

## 🚀 Getting Started

### Installation

```bash
pip install -r requirements-frontend.txt
```

### Running the Application

```bash
streamlit run app.py
```

Or use the provided script:

```powershell
.\scripts\start-dev.ps1
```

## 📝 Code Organization

### Components
Reusable UI components are located in `components/`:
- **Sidebar**: Shared navigation sidebar used across all dashboard pages

### Utils
Utility functions and constants in `utils/`:
- **constants.py**: All application constants (colors, fonts, spacing, configs)
- **helpers.py**: Reusable helper functions (authentication, formatting, etc.)

### Pages
Each page in `pages/` follows a consistent structure:
- Authentication check (for protected pages)
- Sidebar rendering
- Page-specific content

## 🔐 Authentication Flow

1. **Landing Page** → Unprotected, public access
2. **Login Page** → Unprotected, handles authentication
3. **Dashboard Pages** → Protected, require authentication

## 🎯 Best Practices

- **DRY Principle**: Reusable components and utilities
- **Separation of Concerns**: Clear separation between UI, logic, and data
- **Type Hints**: Functions include type hints for better code clarity
- **Documentation**: All modules and functions are documented
- **Constants**: All magic numbers and strings are in constants file

## 📦 Dependencies

- `streamlit`: Web application framework
- `plotly`: Interactive charts and graphs
- `pandas`: Data manipulation (if needed)

## 🛠️ Development

### Code Style
- Follow PEP 8 guidelines
- Use type hints where applicable
- Document all functions and classes
- Keep functions focused and single-purpose

### Adding New Pages

1. Create new file in `pages/` directory
2. Import sidebar component: `from components.sidebar import render_sidebar`
3. Check authentication: `from utils.helpers import check_authentication`
4. Use constants from `utils.constants` for styling

### Adding New Components

1. Create new file in `components/` directory
2. Export from `components/__init__.py`
3. Use constants from `utils.constants` for consistent styling
4. Document all functions and parameters

