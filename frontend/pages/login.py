"""
Login Page for EduFlow
Clean, modern login page implementation
"""
import streamlit as st

def render_login_page():
    """Render the login page with custom CSS styling"""
    
    # Custom CSS based on provided styles
    login_css = """
    <style>
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .stApp {
            background: #ECEDEF;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 100%;
        }
        
        /* Main login container - Frame 188 */
        .login-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 0px;
            position: relative;
            width: 593px;
            height: 536px;
            background: #FFFFFF;
            border-radius: 10px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
            margin: 0 auto;
        }
        
        /* Frame 266 - Main content wrapper */
        .login-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 0px;
            gap: 53px;
            width: 380px;
            height: 408px;
        }
        
        /* Frame 264 - Logo and welcome section */
        .welcome-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 0px;
            gap: 5px;
            width: 258px;
            height: 90px;
        }
        
        /* Logo - Eduflow with proper colors */
        .login-logo {
            width: 258px;
            height: 23px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 20px;
            line-height: 23px;
            text-align: center;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .login-logo .edu-part {
            color: #B3B3B3;
        }
        
        .login-logo .flow-part {
            color: #51287E;
        }
        
        /* Welcome Back ! */
        .welcome-title {
            width: 258px;
            height: 42px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 36px;
            line-height: 42px;
            color: #2E2E2E;
            margin: 0;
            text-align: center;
        }
        
        /* Start your journey with us today */
        .welcome-subtitle {
            width: 258px;
            height: 15px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 13px;
            line-height: 15px;
            text-align: center;
            color: #2E2E2E;
            margin: 0;
        }
        
        /* Frame 265 - Form section */
        .login-form {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 0px;
            gap: 17px;
            width: 380px;
            height: 265px;
        }
        
        /* Frame 261 - Email section */
        .email-section {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: flex-start;
            padding: 0px;
            gap: 13px;
            width: 380px;
            height: 68px;
        }
        
        /* Email label */
        .email-label {
            margin: 0 auto;
            width: 380px;
            height: 23px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 20px;
            line-height: 23px;
            color: #2E2E2E;
        }
        
        /* Frame 259 - Email input */
        .email-input-container {
            box-sizing: border-box;
            display: flex;
            flex-direction: row;
            align-items: center;
            padding: 12px 20px;
            gap: 10px;
            margin: 0 auto;
            width: 380px;
            height: 40px;
            border: 1px solid #C9C8C8;
            border-radius: 30px;
            background: #FFFFFF;
        }
        
        .email-input-container input {
            border: none;
            outline: none;
            width: 100%;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 13px;
            line-height: 15px;
            color: #2E2E2E;
        }
        
        .email-input-container input::placeholder {
            color: #C9C8C8;
        }
        
        /* Frame 262 - Password section */
        .password-section {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: flex-start;
            padding: 0px;
            gap: 20px;
            width: 380px;
            height: 70px;
        }
        
        /* Password label */
        .password-label {
            margin: 0 auto;
            width: 380px;
            height: 23px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 20px;
            line-height: 23px;
            color: #2E2E2E;
        }
        
        /* Frame 260 - Password input */
        .password-input-container {
            box-sizing: border-box;
            display: flex;
            flex-direction: row;
            align-items: center;
            padding: 6px 19px;
            gap: 10px;
            margin: 0 auto;
            width: 380px;
            height: 40px;
            border: 1px solid #C9C8C8;
            border-radius: 30px;
            background: #FFFFFF;
        }
        
        .password-input-container input {
            border: none;
            outline: none;
            width: 100%;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 13px;
            line-height: 15px;
            color: #2E2E2E;
        }
        
        .password-input-container input::placeholder {
            color: #C9C8C8;
            font-weight: 400;
        }
        
        /* Frame 263 - Remember me section */
        .remember-me-section {
            display: flex;
            flex-direction: row;
            align-items: center;
            padding: 0px;
            gap: 4px;
            width: 131px;
            height: 30px;
        }
        
        /* Checkbox styling */
        .remember-checkbox {
            width: 30px;
            height: 30px;
            position: relative;
            cursor: pointer;
        }
        
        .remember-checkbox input[type="checkbox"] {
            width: 100%;
            height: 100%;
            margin: 0;
            cursor: pointer;
            appearance: none;
            border: 1.5px solid #6E6E6E;
            border-radius: 4px;
            position: relative;
        }
        
        .remember-checkbox input[type="checkbox"]:checked {
            background: #51287E;
            border-color: #51287E;
        }
        
        .remember-checkbox input[type="checkbox"]:checked::after {
            content: "✓";
            position: absolute;
            color: white;
            font-size: 18px;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        
        /* Remember Me label */
        .remember-label {
            width: 97px;
            height: 17px;
            font-family: 'Inter', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 14px;
            line-height: 17px;
            text-align: center;
            color: #000000;
            margin: 0;
            cursor: pointer;
        }
        
        /* Frame 256 - Login button */
        .login-button-container {
            box-sizing: border-box;
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 5px 167px;
            gap: 10px;
            width: 380px;
            height: 46px;
            background: #51287E;
            border: 1px solid #51287E;
            border-radius: 30px;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        
        .login-button-container:hover {
            background: #3d1f5e;
        }
        
        .login-button-container button {
            width: 46px;
            height: 21px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 18px;
            line-height: 21px;
            color: #FFFFFF;
            background: transparent;
            border: none;
            cursor: pointer;
            padding: 0;
        }
        
        /* Streamlit input styling override */
        .stTextInput > div > div > input {
            border: none !important;
            box-shadow: none !important;
        }
        
        .stTextInput > div > div > input:focus {
            border: none !important;
            box-shadow: none !important;
        }
    </style>
    """
    
    # Apply CSS
    st.markdown(login_css, unsafe_allow_html=True)
    
    # Center the login form
    col1, col2, col3 = st.columns([1, 1.5, 1])
    
    with col2:
        # Welcome section - Logo first, then Welcome Back, then subtitle
        st.markdown("""
        <div class="welcome-section" style="margin-bottom: 53px;">
            <div class="login-logo">
                <span class="edu-part">Edu</span><span class="flow-part">flow</span>
            </div>
            <h2 class="welcome-title">Welcome Back !</h2>
            <p class="welcome-subtitle">Start your journey with us today</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Login form
        with st.form("login_form", clear_on_submit=False):
            # Email section
            st.markdown('<label class="email-label">Email</label>', unsafe_allow_html=True)
            email = st.text_input(
                "",
                placeholder="example@gmail.com",
                key="email_input",
                label_visibility="collapsed"
            )
            
            # Add spacing
            st.markdown('<div style="height: 17px;"></div>', unsafe_allow_html=True)
            
            # Password section
            st.markdown('<label class="password-label">Password</label>', unsafe_allow_html=True)
            password = st.text_input(
                "",
                type="password",
                placeholder=".........",
                key="password_input",
                label_visibility="collapsed"
            )
            
            # Remember me checkbox
            col_checkbox, col_label = st.columns([0.2, 0.8])
            with col_checkbox:
                remember_me = st.checkbox("", key="remember_me")
            with col_label:
                st.markdown('<p class="remember-label" style="margin-top: 8px; text-align: left;">Remember Me</p>', unsafe_allow_html=True)
            
            # Login button
            login_button = st.form_submit_button(
                "Login",
                use_container_width=True,
                type="primary"
            )
            
            if login_button:
                if email and password:
                    # TODO: Implement authentication logic with backend API
                    # For now, just set session state
                    st.session_state['authenticated'] = True
                    st.session_state['user_email'] = email
                    # Redirect to dashboard after authentication
                    st.switch_page("pages/dashboard.py")
                else:
                    st.error("Please fill in all fields")
    
    # Additional styling for Streamlit form elements
    st.markdown("""
    <style>
        /* Form container styling */
        .stForm {
            background: transparent;
            border: none;
            padding: 0;
        }
        
        div[data-testid="stForm"] {
            border: none;
            padding: 0;
            background: transparent;
        }
        
        /* Email input styling */
        div[data-testid="stTextInput"]:first-of-type {
            margin-top: 0;
        }
        
        div[data-testid="stTextInput"] > div > div > input {
            border: 1px solid #C9C8C8 !important;
            border-radius: 30px !important;
            padding: 12px 20px !important;
            font-family: 'Roboto', sans-serif;
            font-size: 13px;
            font-weight: 400;
            width: 380px;
            height: 40px;
            box-sizing: border-box;
        }
        
        div[data-testid="stTextInput"] > div > div > input:focus {
            border-color: #51287E !important;
            box-shadow: 0 0 0 2px rgba(81, 40, 126, 0.1) !important;
        }
        
        div[data-testid="stTextInput"] > div > div > input::placeholder {
            color: #C9C8C8;
        }
        
        /* Password input styling */
        div[data-testid="stTextInput"]:last-of-type > div > div > input {
            border: 1px solid #C9C8C8 !important;
            border-radius: 30px !important;
            padding: 6px 19px !important;
            font-family: 'Roboto', sans-serif;
            font-size: 13px;
            font-weight: 700;
            width: 380px;
            height: 40px;
            box-sizing: border-box;
        }
        
        div[data-testid="stTextInput"]:last-of-type > div > div > input::placeholder {
            color: #C9C8C8;
            font-weight: 400;
        }
        
        /* Login button styling */
        div[data-testid="stForm"] button[type="submit"] {
            background: #51287E !important;
            border: 1px solid #51287E !important;
            border-radius: 30px !important;
            color: #FFFFFF !important;
            font-family: 'Roboto', sans-serif;
            font-weight: 700;
            font-size: 18px;
            height: 46px;
            width: 380px;
            margin-top: 20px;
        }
        
        div[data-testid="stForm"] button[type="submit"]:hover {
            background: #3d1f5e !important;
            border-color: #3d1f5e !important;
        }
        
        /* Checkbox styling */
        div[data-testid="stCheckbox"] > label {
            display: none;
        }
        
        div[data-testid="stCheckbox"] > div {
            width: 30px;
            height: 30px;
        }
        
        div[data-testid="stCheckbox"] input[type="checkbox"] {
            width: 30px !important;
            height: 30px !important;
            border: 1.5px solid #6E6E6E !important;
            border-radius: 4px !important;
            cursor: pointer;
        }
        
        div[data-testid="stCheckbox"] input[type="checkbox"]:checked {
            background: #51287E !important;
            border-color: #51287E !important;
        }
        
        /* Container centering */
        .main .block-container {
            padding-top: 5rem;
            padding-bottom: 5rem;
        }
    </style>
    """, unsafe_allow_html=True)


def main():
    """Main login page function"""
    st.set_page_config(
        page_title="Login - EduFlow",
        page_icon="🔐",
        layout="centered",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': None
        }
    )
    
    # Hide sidebar completely
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
    
    # Login page is unprotected - no auth check needed
    render_login_page()

if __name__ == "__main__":
    main()

