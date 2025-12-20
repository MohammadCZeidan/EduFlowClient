"""
View Course Page for EduFlow
Page for viewing course details
"""
import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path to import components
sys.path.append(str(Path(__file__).parent.parent))
from components.sidebar import render_sidebar

def render_view_course():
    """Render the view course page"""
    
    # Check authentication
    if not st.session_state.get('authenticated', False):
        st.warning("Please login to access this page")
        st.switch_page("pages/login.py")
        return
    
    # Get course ID from query params or session
    course_id = st.query_params.get('id', st.session_state.get('viewing_course_id', None))
    
    if not course_id:
        st.error("No course selected")
        st.switch_page("pages/courses.py")
        return
    
    # TODO: Fetch course data from backend API using course_id
    # Example API call:
    # import requests
    # response = requests.get(f"{BACKEND_URL}/api/v1/courses/{course_id}")
    # course_data = response.json()
    
    # For now, use sample data based on course_id
    sample_courses = {
        '0': {
            'id': '0',
            'title': 'Leadership Basics',
            'description': 'Learn fundamental leadership skills and techniques to lead teams effectively.',
            'instructor': 'John Smith',
            'students': 245,
            'price': '$299',
            'duration': '8 weeks',
            'status': 'Active',
            'category': 'Business',
            'cohort': 'LB01',
            'type': 'Online',
            'capacity': 250,
            'start_date': '2024-02-01',
            'end_date': '2024-03-29',
            'image_url': None
        },
        '1': {
            'id': '1',
            'title': 'UI/UX Design Principles',
            'description': 'Learn the core principles of user interface and user experience design.',
            'instructor': 'Emily Chen',
            'students': 195,
            'price': '$349',
            'duration': '12 weeks',
            'status': 'Active',
            'category': 'Design',
            'cohort': 'UIX04',
            'type': 'Online',
            'capacity': 200,
            'start_date': '2024-01-15',
            'end_date': '2024-04-15',
            'image_url': None
        }
    }
    
    course_data = sample_courses.get(str(course_id), sample_courses['1'])
    
    # Main CSS
    view_course_css = """
    <style>
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .stApp {
            background: rgba(247, 248, 250, 0.94902);
        }
        
        .main .block-container {
            padding-top: 2rem;
            padding-left: 280px;
            padding-right: 2rem;
            max-width: 100%;
        }
        
        /* Breadcrumb navigation */
        .breadcrumb {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            padding: 0px;
            margin-bottom: 20px;
        }
        
        .breadcrumb-items {
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 8px;
        }
        
        .breadcrumb-item {
            font-family: 'Roboto', sans-serif;
            font-weight: 500;
            font-size: 15px;
            line-height: 18px;
            color: #6B7280;
            cursor: pointer;
        }
        
        .breadcrumb-separator {
            font-family: 'Roboto', sans-serif;
            font-weight: 500;
            font-size: 15px;
            line-height: 18px;
            color: #6B7280;
        }
        
        /* Weekly button */
        .weekly-button {
            box-sizing: border-box;
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 3px 17px;
            gap: 10px;
            width: 60px;
            height: 32px;
            background: #FFFFFF;
            border-radius: 20px;
            font-family: 'Roboto', sans-serif;
            font-weight: 500;
            font-size: 15px;
            line-height: 18px;
            color: #51287E;
        }
        
        /* Course info container */
        .course-info-container {
            background: #FFFFFF;
            border-radius: 15px;
            padding: 18px 20px;
            gap: 16px;
            box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
        }
        
        /* Image display area */
        .image-display-area {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 32px 403px;
            gap: 10px;
            width: 100%;
            height: 125px;
            background: #D8D7D7;
            border-radius: 15px;
            margin-bottom: 16px;
        }
        
        .course-title-display {
            font-family: 'Roboto', sans-serif;
            font-weight: 400;
            font-size: 20px;
            line-height: 23px;
            color: #000000;
            text-align: center;
        }
        
        /* Info grid */
        .info-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-top: 16px;
        }
        
        .info-item {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        
        .info-label {
            font-family: 'Roboto', sans-serif;
            font-weight: 400;
            font-size: 15px;
            line-height: 18px;
            color: #2E2E2E;
        }
        
        .info-value {
            font-family: 'Roboto', sans-serif;
            font-weight: 500;
            font-size: 16px;
            line-height: 19px;
            color: #101828;
        }
        
        /* Action buttons */
        .action-buttons {
            display: flex;
            flex-direction: row;
            gap: 12px;
            margin-top: 24px;
        }
    </style>
    """
    
    st.markdown(view_course_css, unsafe_allow_html=True)
    
    # Breadcrumb navigation
    col_breadcrumb, col_weekly = st.columns([3, 1])
    with col_breadcrumb:
        breadcrumb_col1, breadcrumb_col2, breadcrumb_col3, breadcrumb_col4 = st.columns([0.1, 1, 0.1, 1])
        with breadcrumb_col1:
            if st.button("←", key="back_arrow", help="Go back to Courses"):
                st.switch_page("pages/courses.py")
        with breadcrumb_col2:
            if st.button("Courses", key="breadcrumb_courses"):
                st.switch_page("pages/courses.py")
        with breadcrumb_col3:
            st.markdown('<span style="color: #6B7280;">/</span>', unsafe_allow_html=True)
        with breadcrumb_col4:
            st.markdown(f'<span style="color: #6B7280;">{course_data["title"]}</span>', unsafe_allow_html=True)
    
    with col_weekly:
        st.markdown("""
        <div class="weekly-button">
            weekly
        </div>
        """, unsafe_allow_html=True)
    
    # Course info container
    with st.container():
        st.markdown('<div class="course-info-container">', unsafe_allow_html=True)
        
        # Image display area
        if course_data.get('image_url'):
            st.image(course_data['image_url'], width=966)
        else:
            st.markdown(f"""
            <div class="image-display-area">
                <span class="course-title-display">{course_data['title']}</span>
            </div>
            """, unsafe_allow_html=True)
        
        # Course information grid
        st.markdown('<div class="info-grid">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<div class="info-item"><div class="info-label">Course Name</div><div class="info-value">{course_data["title"]}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-item"><div class="info-label">Instructor</div><div class="info-value">{course_data["instructor"]}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-item"><div class="info-label">Cohort</div><div class="info-value">{course_data["cohort"]}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-item"><div class="info-label">Category</div><div class="info-value">{course_data["category"]}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-item"><div class="info-label">Status</div><div class="info-value">{course_data["status"]}</div></div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f'<div class="info-item"><div class="info-label">Type</div><div class="info-value">{course_data["type"]}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-item"><div class="info-label">Price</div><div class="info-value">{course_data["price"]}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-item"><div class="info-label">Capacity</div><div class="info-value">{course_data["capacity"]}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-item"><div class="info-label">Start Date</div><div class="info-value">{course_data["start_date"]}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-item"><div class="info-label">End Date</div><div class="info-value">{course_data["end_date"]}</div></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Description
        st.markdown(f'<div style="margin-top: 24px;"><div class="info-label">Description</div><div class="info-value" style="margin-top: 8px;">{course_data["description"]}</div></div>', unsafe_allow_html=True)
        
        # Action buttons
        col_edit, col_delete, _ = st.columns([1, 1, 6])
        with col_edit:
            if st.button("Edit Course", type="primary", use_container_width=True):
                st.session_state['editing_course_id'] = course_data['id']
                st.query_params['id'] = course_data['id']
                st.switch_page("pages/edit_course.py")
        with col_delete:
            if st.button("Delete Course", use_container_width=True):
                st.warning("Delete functionality will be implemented")
                # TODO: Implement delete API call
                # Example: requests.delete(f"{BACKEND_URL}/api/v1/courses/{course_id}")
        
        st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main view course page function"""
    st.set_page_config(
        page_title="View Course - EduFlow",
        page_icon="👁️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Render sidebar
    with st.sidebar:
        render_sidebar(current_page="courses")
    
    # Render view course page
    render_view_course()

if __name__ == "__main__":
    main()

