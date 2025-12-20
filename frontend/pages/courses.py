"""
Courses Page for EduFlow
Course management and listing page
"""
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import sys
from pathlib import Path

# Add parent directory to path to import components
sys.path.append(str(Path(__file__).parent.parent))
from components.sidebar import render_sidebar

def render_courses():
    """Render the main courses page"""
    
    # Check authentication
    if not st.session_state.get('authenticated', False):
        st.warning("Please login to access the courses page")
        st.switch_page("pages/login.py")
        return
    
    # Get user name from session
    user_email = st.session_state.get('user_email', 'User')
    user_name = user_email.split('@')[0].title() if '@' in user_email else 'User'
    
    # Main courses CSS
    courses_css = """
    <style>
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .stApp {
            background: #ECEDEF;
        }
        
        .main .block-container {
            padding-top: 2rem;
            padding-left: 280px;
            padding-right: 2rem;
            max-width: 100%;
        }
        
        /* Header */
        .courses-header {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            padding: 0px;
            margin-bottom: 30px;
        }
        
        .page-title {
            font-family: 'Roboto', sans-serif;
            font-weight: 700;
            font-size: 32px;
            line-height: 38px;
            color: #2E2E2E;
        }
        
        /* Search and filter bar */
        .search-filter-bar {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            margin-bottom: 24px;
        }
        
        /* Course card */
        .course-card {
            background: #FFFFFF;
            border-radius: 15px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
            transition: box-shadow 0.3s;
        }
        
        .course-card:hover {
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .course-header {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 16px;
        }
        
        .course-title {
            font-family: 'Roboto', sans-serif;
            font-weight: 600;
            font-size: 20px;
            line-height: 24px;
            color: #101828;
            margin-bottom: 8px;
        }
        
        .course-description {
            font-family: 'Roboto', sans-serif;
            font-weight: 400;
            font-size: 14px;
            line-height: 20px;
            color: #565656;
            margin-bottom: 16px;
        }
        
        .course-meta {
            display: flex;
            flex-direction: row;
            gap: 24px;
            margin-bottom: 16px;
        }
        
        .meta-item {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        
        .meta-label {
            font-family: 'Roboto', sans-serif;
            font-weight: 400;
            font-size: 12px;
            line-height: 14px;
            color: #565656;
        }
        
        .meta-value {
            font-family: 'Roboto', sans-serif;
            font-weight: 500;
            font-size: 16px;
            line-height: 19px;
            color: #101828;
        }
        
        .course-actions {
            display: flex;
            flex-direction: row;
            gap: 12px;
            margin-top: 16px;
        }
        
        .btn-primary {
            background: #51287E;
            color: #FFFFFF;
            border: none;
            border-radius: 8px;
            padding: 8px 16px;
            font-family: 'Roboto', sans-serif;
            font-weight: 500;
            font-size: 14px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .btn-primary:hover {
            background: #3d1f5e;
        }
        
        .btn-secondary {
            background: transparent;
            color: #51287E;
            border: 1px solid #51287E;
            border-radius: 8px;
            padding: 8px 16px;
            font-family: 'Roboto', sans-serif;
            font-weight: 500;
            font-size: 14px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .btn-secondary:hover {
            background: #F4F4F4;
        }
        
        /* Empty state */
        .empty-state {
            text-align: center;
            padding: 60px 20px;
            background: #FFFFFF;
            border-radius: 15px;
        }
        
        .empty-state-icon {
            font-size: 64px;
            margin-bottom: 16px;
        }
        
        .empty-state-text {
            font-family: 'Roboto', sans-serif;
            font-weight: 400;
            font-size: 16px;
            line-height: 24px;
            color: #565656;
        }
    </style>
    """
    
    st.markdown(courses_css, unsafe_allow_html=True)
    
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<div class="page-title">Courses</div>', unsafe_allow_html=True)
    with col2:
        if st.button("+ Add New Course", type="primary", use_container_width=True):
            st.switch_page("pages/add_course.py")
    
    # Search and filter bar
    col_search, col_filter1, col_filter2 = st.columns([2, 1, 1])
    with col_search:
        search_query = st.text_input("", placeholder="Search courses...", key="course_search", label_visibility="collapsed")
    with col_filter1:
        filter_status = st.selectbox("Status", ["All", "Active", "Inactive", "Draft"], key="status_filter", label_visibility="collapsed")
    with col_filter2:
        filter_category = st.selectbox("Category", ["All", "Business", "Technology", "Design", "Marketing"], key="category_filter", label_visibility="collapsed")
    
    # Sample courses data
    courses_data = [
        {
            "title": "Leadership Basics",
            "description": "Learn fundamental leadership skills and techniques to lead teams effectively.",
            "instructor": "John Smith",
            "students": 245,
            "price": "$299",
            "duration": "8 weeks",
            "status": "Active",
            "category": "Business"
        },
        {
            "title": "Excel Essentials",
            "description": "Master Excel formulas, functions, and data analysis techniques.",
            "instructor": "Sarah Johnson",
            "students": 180,
            "price": "$199",
            "duration": "6 weeks",
            "status": "Active",
            "category": "Technology"
        },
        {
            "title": "Digital Marketing Fundamentals",
            "description": "Comprehensive guide to digital marketing strategies and tools.",
            "instructor": "Mike Davis",
            "students": 320,
            "price": "$249",
            "duration": "10 weeks",
            "status": "Active",
            "category": "Marketing"
        },
        {
            "title": "UI/UX Design Principles",
            "description": "Learn the core principles of user interface and user experience design.",
            "instructor": "Emily Chen",
            "students": 195,
            "price": "$349",
            "duration": "12 weeks",
            "status": "Active",
            "category": "Design"
        },
        {
            "title": "Python Programming",
            "description": "Introduction to Python programming for beginners.",
            "instructor": "David Wilson",
            "students": 410,
            "price": "$179",
            "duration": "8 weeks",
            "status": "Active",
            "category": "Technology"
        },
    ]
    
    # Filter courses based on search and filters
    filtered_courses = courses_data
    if search_query:
        filtered_courses = [c for c in filtered_courses if search_query.lower() in c["title"].lower() or search_query.lower() in c["description"].lower()]
    if filter_status != "All":
        filtered_courses = [c for c in filtered_courses if c["status"] == filter_status]
    if filter_category != "All":
        filtered_courses = [c for c in filtered_courses if c["category"] == filter_category]
    
    # Display courses
    if filtered_courses:
        for idx, course in enumerate(filtered_courses):
            course_html = f"""
            <div class="course-card">
                <div class="course-header">
                    <div style="flex: 1;">
                        <div class="course-title">{course['title']}</div>
                        <div class="course-description">{course['description']}</div>
                    </div>
                    <div style="
                        padding: 4px 12px;
                        background: {'#E8F5E9' if course['status'] == 'Active' else '#FFF3E0'};
                        color: {'#2E7D32' if course['status'] == 'Active' else '#E65100'};
                        border-radius: 12px;
                        font-family: 'Roboto', sans-serif;
                        font-size: 12px;
                        font-weight: 500;
                    ">{course['status']}</div>
                </div>
                <div class="course-meta">
                    <div class="meta-item">
                        <div class="meta-label">Instructor</div>
                        <div class="meta-value">{course['instructor']}</div>
                    </div>
                    <div class="meta-item">
                        <div class="meta-label">Students</div>
                        <div class="meta-value">{course['students']}</div>
                    </div>
                    <div class="meta-item">
                        <div class="meta-label">Price</div>
                        <div class="meta-value">{course['price']}</div>
                    </div>
                    <div class="meta-item">
                        <div class="meta-label">Duration</div>
                        <div class="meta-value">{course['duration']}</div>
                    </div>
                    <div class="meta-item">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">{course['category']}</div>
                    </div>
                </div>
            </div>
            """
            st.markdown(course_html, unsafe_allow_html=True)
            
            # Action buttons using Streamlit
            col_view, col_edit, col_delete, _ = st.columns([1, 1, 1, 5])
            with col_view:
                if st.button("View Details", key=f"view_{idx}", use_container_width=True):
                    st.session_state['viewing_course_id'] = idx
                    st.switch_page("pages/view_course.py")
            with col_edit:
                if st.button("Edit", key=f"edit_{idx}", use_container_width=True):
                    st.session_state['editing_course_id'] = idx
                    st.switch_page("pages/edit_course.py")
            with col_delete:
                if st.button("Delete", key=f"delete_{idx}", use_container_width=True):
                    st.warning(f"Delete functionality for: {course['title']}")
                    # TODO: Implement delete API call
    else:
        empty_state_html = """
        <div class="empty-state">
            <div class="empty-state-icon">📚</div>
            <div class="empty-state-text">No courses found matching your criteria.</div>
        </div>
        """
        st.markdown(empty_state_html, unsafe_allow_html=True)
    

def main():
    """Main courses page function"""
    st.set_page_config(
        page_title="Courses - EduFlow",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Render sidebar
    with st.sidebar:
        render_sidebar(current_page="courses")
    
    # Render main courses page
    render_courses()

if __name__ == "__main__":
    main()

