import streamlit as st
from PIL import Image

st.set_page_config(page_title="EduFlow - Login", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS matching Figma design exactly
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Inter:wght@400&display=swap');
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        /* Hide Streamlit defaults */
        header { visibility: hidden; }
        footer { visibility: hidden; }
        [data-testid="stToolbar"] { display: none; }
        [data-testid="stHeader"] { display: none; }
        .stApp > header { display: none; }
        
        /* Main container */
        .main { 
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        
        /* Login card - Frame 188 */
        .login-card {
            background: #FFFFFF;
            border: 2px dashed #C9C8C8;
            border-radius: 15px;
            padding: 53px 40px;
            width: 593px;
            max-width: 90%;
            text-align: center;
        }
        
        /* Welcome title */
        .welcome-title {
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 36px;
            line-height: 42px;
            color: #2E2E2E;
            margin: 20px 0 5px 0;
        }
        
        /* Subtitle */
        .welcome-subtitle {
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 13px;
            line-height: 15px;
            text-align: center;
            color: #2E2E2E;
            margin-bottom: 53px;
        }
        
        /* Form labels */
        .form-label {
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 20px;
            line-height: 23px;
            color: #2E2E2E;
            text-align: left;
            display: block;
            margin-bottom: 13px;
        }
        
        /* Input fields */
        .stTextInput > div > div > input {
            border: 1px solid #C9C8C8 !important;
            border-radius: 30px !important;
            padding: 12px 20px !important;
            height: 40px !important;
            font-family: 'Roboto', sans-serif !important;
            font-size: 13px !important;
            color: #2E2E2E !important;
        }
        
        .stTextInput > div > div > input::placeholder {
            color: #C9C8C8 !important;
            font-family: 'Roboto', sans-serif !important;
            font-weight: 400 !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #51287E !important;
            box-shadow: none !important;
        }
        
        /* Checkbox */
        .stCheckbox {
            text-align: left;
            margin: 20px 0;
        }
        
        .stCheckbox > label {
            font-family: 'Inter', sans-serif !important;
            font-style: normal !important;
            font-weight: 400 !important;
            font-size: 14px !important;
            line-height: 17px !important;
            color: #000000 !important;
        }
        
        /* Login button */
        .stButton > button {
            background: #51287E !important;
            border: 1px solid #51287E !important;
            border-radius: 30px !important;
            padding: 12px 167px !important;
            height: 46px !important;
            width: 100% !important;
            font-family: 'Roboto', sans-serif !important;
            font-style: normal !important;
            font-weight: 700 !important;
            font-size: 18px !important;
            line-height: 21px !important;
            color: #FFFFFF !important;
            cursor: pointer !important;
            margin-top: 20px !important;
        }
        
        .stButton > button:hover {
            background: #3d1e5f !important;
            border-color: #3d1e5f !important;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .login-card {
                padding: 40px 30px;
                width: 90%;
            }
            
            .welcome-title {
                font-size: 28px;
            }
            
            .form-label {
                font-size: 18px;
            }
        }
        
        @media (max-width: 480px) {
            .login-card {
                padding: 30px 20px;
            }
            
            .welcome-title {
                font-size: 24px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Center the login form
col1, col2, col3 = st.columns([1, 2.5, 1])

with col2:
    st.markdown("<div class='login-card'>", unsafe_allow_html=True)
    
    # Logo
    try:
        logo = Image.open("assets/logo.png")
        st.image(logo, width=129)
    except:
        st.write("EduFlow")
    
    # Welcome message
    st.markdown("<h1 class='welcome-title'>Welcome Back !</h1>", unsafe_allow_html=True)
    st.markdown("<p class='welcome-subtitle'>Start your journey with us today</p>", unsafe_allow_html=True)
    
    # Email input
    st.markdown("<label class='form-label'>Email</label>", unsafe_allow_html=True)
    email = st.text_input("Email", placeholder="example@gmail.com", label_visibility="collapsed", key="email_input")
    
    st.write("")  # Spacing
    
    # Password input
    st.markdown("<label class='form-label'>Password</label>", unsafe_allow_html=True)
    password = st.text_input("Password", type="password", placeholder=".........", label_visibility="collapsed", key="password_input")
    
    # Remember me checkbox
    remember_me = st.checkbox("Remember Me")
    
    # Login button
    if st.button("Login", use_container_width=True):
        if email and password:
            st.success("Login successful!")
            st.switch_page("pages/dashboard.py")
        else:
            st.error("Please enter both email and password")
    
    st.markdown("</div>", unsafe_allow_html=True)
