"""
Edit Course Page for EduFlow
Page for editing an existing course (reuses add_course form with pre-filled data)
"""
import streamlit as st
from datetime import datetime
from pages import add_course
import sys
from pathlib import Path

# Add parent directory to path to import components
sys.path.append(str(Path(__file__).parent.parent))
from components.sidebar import render_sidebar

def render_edit_course():
    """Render the edit course form page"""
    
    # Check authentication
    if not st.session_state.get('authenticated', False):
        st.warning("Please login to access this page")
        st.switch_page("pages/login.py")
        return
    
    # Get course ID from query params or session
    course_id = st.query_params.get('id', st.session_state.get('editing_course_id', None))
    
    if not course_id:
        st.error("No course selected for editing")
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
            'instructor': 'John Smith',
            'cohort': 'LB01',
            'category': 'Business',
            'status': 'Active',
            'type': 'Online',
            'price': 299.00,
            'capacity': 250,
            'start_date': datetime(2024, 2, 1),
            'end_date': datetime(2024, 3, 29),
            'description': 'Learn fundamental leadership skills and techniques to lead teams effectively.',
            'image_url': None
        },
        '1': {
            'id': '1',
            'title': 'UI/UX Design Principles',
            'instructor': 'Emily Chen',
            'cohort': 'UIX04',
            'category': 'Design',
            'status': 'Active',
            'type': 'Online',
            'price': 349.00,
            'capacity': 200,
            'start_date': datetime(2024, 1, 15),
            'end_date': datetime(2024, 4, 15),
            'description': 'Learn the core principles of user interface and user experience design.',
            'image_url': None
        }
    }
    
    course_data = sample_courses.get(str(course_id), sample_courses['1'])
    
    # Main CSS (same as add_course)
    edit_course_css = """
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
        
        /* Form container */
        .form-container {
            background: #FFFFFF;
            border-radius: 15px;
            padding: 18px 12px;
            gap: 16px;
            box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
        }
        
        /* Image upload area */
        .image-upload-area {
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
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .image-upload-text {
            font-family: 'Roboto', sans-serif;
            font-weight: 400;
            font-size: 20px;
            line-height: 23px;
            color: #2E2E2E;
        }
        
        /* Form field styling */
        .form-field-label {
            font-family: 'Roboto', sans-serif;
            font-weight: 400;
            font-size: 15px;
            line-height: 18px;
            color: #2E2E2E;
            margin-bottom: 8px;
        }
        
        /* Input styling */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            border: 1px solid #C9C8C8 !important;
            border-radius: 5px !important;
            padding: 4px 13px !important;
            font-family: 'Roboto', sans-serif;
            font-size: 15px;
            color: #2E2E2E;
            height: 38px;
        }
        
        .stTextInput > div > div > input::placeholder,
        .stNumberInput > div > div > input::placeholder {
            color: #999999 !important;
        }
        
        /* Selectbox styling */
        .stSelectbox > div > div {
            border: 1px solid #C9C8C8 !important;
            border-radius: 5px !important;
            padding: 4px 13px !important;
            height: 38px;
        }
        
        /* Date input styling */
        .stDateInput > div > div > input {
            border: 1px solid #C9C8C8 !important;
            border-radius: 5px !important;
            padding: 4px 13px !important;
            font-family: 'Roboto', sans-serif;
            font-size: 15px;
            color: #2E2E2E;
            height: 38px;
        }
    </style>
    """
    
    st.markdown(edit_course_css, unsafe_allow_html=True)
    
    # Breadcrumb navigation
    col_breadcrumb, _ = st.columns([3, 1])
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
            st.markdown(f'<span style="color: #6B7280;">Edit {course_data["title"]}</span>', unsafe_allow_html=True)
    
    # Form container
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        # Image upload area
        if course_data.get('image_url'):
            st.image(course_data['image_url'], width=200)
        else:
            st.markdown("""
            <div class="image-upload-area">
                <span class="image-upload-text">+ Add Image</span>
            </div>
            """, unsafe_allow_html=True)
        
        # File uploader
        uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'], key="course_image", label_visibility="collapsed")
        if uploaded_file:
            st.image(uploaded_file, width=200)
        
        # Form fields with pre-filled data
        with st.form("edit_course_form", clear_on_submit=False):
            # Row 1: Course Name and Instructor Name
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="form-field-label">Course Name</div>', unsafe_allow_html=True)
                course_name = st.text_input("", value=course_data['title'], placeholder="Enter Course Name", key="course_name", label_visibility="collapsed")
            
            with col2:
                st.markdown('<div class="form-field-label">Instructor Name</div>', unsafe_allow_html=True)
                instructor_name = st.text_input("", value=course_data['instructor'], placeholder="Enter Instructor Name", key="instructor_name", label_visibility="collapsed")
            
            # Row 2: Cohort and Category
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="form-field-label">Cohort</div>', unsafe_allow_html=True)
                cohort = st.text_input("", value=course_data['cohort'], placeholder="eg. UIX04", key="cohort", label_visibility="collapsed")
            
            with col2:
                st.markdown('<div class="form-field-label">Category</div>', unsafe_allow_html=True)
                category_options = ["Select Category", "Business", "Technology", "Design", "Marketing"]
                category_index = category_options.index(course_data['category']) if course_data['category'] in category_options else 0
                category = st.selectbox("", category_options, index=category_index, key="category", label_visibility="collapsed")
            
            # Row 3: Status and Type
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="form-field-label">Status</div>', unsafe_allow_html=True)
                status_options = ["Select Status", "Active", "Inactive", "Draft"]
                status_index = status_options.index(course_data['status']) if course_data['status'] in status_options else 0
                status = st.selectbox("", status_options, index=status_index, key="status", label_visibility="collapsed")
            
            with col2:
                st.markdown('<div class="form-field-label">Type</div>', unsafe_allow_html=True)
                type_options = ["Select Type", "Online", "In-Person", "Hybrid"]
                type_index = type_options.index(course_data['type']) if course_data['type'] in type_options else 0
                course_type = st.selectbox("", type_options, index=type_index, key="course_type", label_visibility="collapsed")
            
            # Row 4: Price and Capacity
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="form-field-label">Price</div>', unsafe_allow_html=True)
                price = st.number_input("", min_value=0.0, step=0.01, value=float(course_data['price']), key="price", label_visibility="collapsed", format="%.2f")
            
            with col2:
                st.markdown('<div class="form-field-label">Capacity</div>', unsafe_allow_html=True)
                capacity = st.number_input("", min_value=0, step=1, value=int(course_data['capacity']), key="capacity", label_visibility="collapsed")
            
            # Row 5: Start Date and End Date
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="form-field-label">Start Date</div>', unsafe_allow_html=True)
                start_date = st.date_input("", value=course_data['start_date'], key="start_date", label_visibility="collapsed")
            
            with col2:
                st.markdown('<div class="form-field-label">End Date</div>', unsafe_allow_html=True)
                end_date = st.date_input("", value=course_data['end_date'], key="end_date", label_visibility="collapsed")
            
            # Description
            st.markdown('<div class="form-field-label" style="margin-top: 16px;">Description</div>', unsafe_allow_html=True)
            description = st.text_area("", value=course_data.get('description', ''), key="description", label_visibility="collapsed", height=100)
            
            # Weekly button and submit
            col1, col2, col3 = st.columns([2, 2, 6])
            with col1:
                st.markdown("""
                <div style="display: flex; justify-content: flex-end; align-items: center; margin-top: 20px;">
                    <div style="
                        box-sizing: border-box;
                        display: flex;
                        flex-direction: row;
                        justify-content: center;
                        align-items: center;
                        padding: 3px 17px;
                        gap: 10px;
                        width: 158px;
                        height: 32px;
                        border: 1px solid #51287E;
                        border-radius: 20px;
                        background: transparent;
                        font-family: 'Roboto', sans-serif;
                        font-weight: 500;
                        font-size: 15px;
                        line-height: 18px;
                        color: #51287E;
                    ">
                        weekly
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                submit_button = st.form_submit_button("Update Course", type="primary", use_container_width=True)
            
            if submit_button:
                # Validate form
                if not course_name:
                    st.error("Please enter a course name")
                elif not instructor_name:
                    st.error("Please enter an instructor name")
                elif category == "Select Category":
                    st.error("Please select a category")
                elif status == "Select Status":
                    st.error("Please select a status")
                elif course_type == "Select Type":
                    st.error("Please select a type")
                else:
                    # TODO: Implement API call to update course
                    st.success(f"Course '{course_name}' updated successfully!")
                    st.session_state['course_updated'] = True
                    # Redirect to view course page
                    st.session_state['viewing_course_id'] = course_id
                    import time
                    time.sleep(1)
                    st.switch_page("pages/view_course.py")
        
        st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main edit course page function"""
    st.set_page_config(
        page_title="Edit Course - EduFlow",
        page_icon="✏️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Render sidebar
    with st.sidebar:
        render_sidebar(current_page="courses")
    
    # Render edit course form
    render_edit_course()

if __name__ == "__main__":
    main()

