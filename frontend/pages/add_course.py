"""
Add Course Page for EduFlow
Page for adding a new course
"""
import streamlit as st
from datetime import datetime
import sys
from pathlib import Path

# Add parent directory to path to import components
sys.path.append(str(Path(__file__).parent.parent))
from components.sidebar import render_sidebar

def render_add_course():
    """Render the add course form page"""
    
    # Check authentication
    if not st.session_state.get('authenticated', False):
        st.warning("Please login to access this page")
        st.switch_page("pages/login.py")
        return
    
    # Main CSS
    add_course_css = """
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
        
        .image-upload-area:hover {
            background: #C9C8C8;
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
        .stNumberInput > div > div > input,
        .stDateInput > div > div > input {
            border: 1px solid #C9C8C8 !important;
            border-radius: 5px !important;
            padding: 4px 13px !important;
            font-family: 'Roboto', sans-serif;
            font-size: 15px;
            color: #2E2E2E;
        }
        
        .stTextInput > div > div > input::placeholder,
        .stNumberInput > div > div > input::placeholder {
            color: #999999;
        }
        
        /* Selectbox styling */
        .stSelectbox > div > div {
            border: 1px solid #C9C8C8 !important;
            border-radius: 5px !important;
            padding: 4px 13px !important;
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
            cursor: pointer;
        }
        
        .weekly-button:hover {
            background: #F4F4F4;
        }
    </style>
    """
    
    st.markdown(add_course_css, unsafe_allow_html=True)
    
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
            st.markdown('<span style="color: #6B7280;">Add New Course</span>', unsafe_allow_html=True)
    
    # Form container
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        # Image upload area
        st.markdown("""
        <div class="image-upload-area">
            <span class="image-upload-text">+ Add Image</span>
        </div>
        """, unsafe_allow_html=True)
        
        # File uploader (hidden styling)
        uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'], key="course_image", label_visibility="collapsed")
        if uploaded_file:
            st.image(uploaded_file, width=200)
        
        # Form fields in rows
        with st.form("add_course_form", clear_on_submit=False):
            # Row 1: Course Name and Instructor Name
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="form-field-label">Course Name</div>', unsafe_allow_html=True)
                course_name = st.text_input("", placeholder="Enter Course Name", key="course_name", label_visibility="collapsed")
            
            with col2:
                st.markdown('<div class="form-field-label">Instructor Name</div>', unsafe_allow_html=True)
                instructor_name = st.text_input("", placeholder="Enter Instructor Name", key="instructor_name", label_visibility="collapsed")
            
            # Row 2: Cohort and Category
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="form-field-label">Cohort</div>', unsafe_allow_html=True)
                cohort = st.text_input("", placeholder="eg. UIX04", key="cohort", label_visibility="collapsed")
            
            with col2:
                st.markdown('<div class="form-field-label">Category</div>', unsafe_allow_html=True)
                category = st.selectbox(
                    "",
                    ["Select Category", "Business", "Technology", "Design", "Marketing"],
                    key="category",
                    label_visibility="collapsed"
                )
            
            # Row 3: Status and Type
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="form-field-label">Status</div>', unsafe_allow_html=True)
                status = st.selectbox(
                    "",
                    ["Select Status", "Active", "Inactive", "Draft"],
                    key="status",
                    label_visibility="collapsed"
                )
            
            with col2:
                st.markdown('<div class="form-field-label">Type</div>', unsafe_allow_html=True)
                course_type = st.selectbox(
                    "",
                    ["Select Type", "Online", "In-Person", "Hybrid"],
                    key="course_type",
                    label_visibility="collapsed"
                )
            
            # Row 4: Price and Capacity
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="form-field-label">Price</div>', unsafe_allow_html=True)
                price = st.number_input("", min_value=0.0, step=0.01, placeholder="0.00$", key="price", label_visibility="collapsed", format="%.2f")
            
            with col2:
                st.markdown('<div class="form-field-label">Capacity</div>', unsafe_allow_html=True)
                capacity = st.number_input("", min_value=0, step=1, placeholder="0", key="capacity", label_visibility="collapsed")
            
            # Row 5: Start Date and End Date
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="form-field-label">Start Date</div>', unsafe_allow_html=True)
                start_date = st.date_input("", key="start_date", label_visibility="collapsed")
            
            with col2:
                st.markdown('<div class="form-field-label">End Date</div>', unsafe_allow_html=True)
                end_date = st.date_input("", key="end_date", label_visibility="collapsed")
            
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
                submit_button = st.form_submit_button("Create Course", type="primary", use_container_width=True)
            
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
                    # TODO: Implement API call to create course
                    st.success(f"Course '{course_name}' created successfully!")
                    st.session_state['course_created'] = True
                    # Redirect to courses page after 2 seconds
                    import time
                    time.sleep(1)
                    st.switch_page("pages/courses.py")
        
        st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main add course page function"""
    st.set_page_config(
        page_title="Add Course - EduFlow",
        page_icon="➕",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Render sidebar
    with st.sidebar:
        render_sidebar(current_page="courses")
    
    # Render add course form
    render_add_course()

if __name__ == "__main__":
    main()

