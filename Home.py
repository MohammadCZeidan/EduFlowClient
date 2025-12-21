import streamlit as st
from PIL import Image

st.set_page_config(page_title="EduFlow Landing", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for styling
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-color: #FFFFFF !important;
        }
        
        .stApp {
            background-color: #FFFFFF !important;
        }
        
        body { background-color: #FFFFFF; }
        
        .main-title { 
            font-size: clamp(2.5em, 6vw, 4.5em); 
            font-weight: 700; 
            margin-bottom: 0.3em; 
            color: #1a1a1a; 
        }
        
        .subtitle { 
            font-size: clamp(1.1em, 2.5vw, 1.3em); 
            color: #666; 
            margin-bottom: 2.5em; 
            line-height: 1.6; 
        }
        
        .cta-btn {
            background: #6C4FF7;
            color: white;
            border: none;
            border-radius: 25px;
            padding: clamp(0.7em, 1.2vw, 1em) clamp(2em, 4vw, 2.8em);
            font-size: clamp(1em, 1.8vw, 1.15em);
            margin-right: 1.5em;
            margin-bottom: 2em;
            cursor: pointer;
            font-weight: 600;
        }
        
        .cta-btn-outline {
            background: white;
            color: #6C4FF7;
            border: 2px solid #6C4FF7;
            border-radius: 25px;
            padding: clamp(0.7em, 1.2vw, 1em) clamp(2em, 4vw, 2.8em);
            font-size: clamp(1em, 1.8vw, 1.15em);
            cursor: pointer;
            font-weight: 600;
        }
        
        .logo-container { margin-bottom: 3em; }
        
        .dashboard-preview {
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(108, 79, 247, 0.2);
            overflow: hidden;
        }
        
        /* Style login button */
        [data-testid="stButton"] button {
            background: #51287E !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 25px !important;
            padding: clamp(0.7em, 1.2vw, 1em) clamp(2em, 4vw, 2.8em) !important;
            font-weight: 600 !important;
            font-size: clamp(1em, 1.8vw, 1.15em) !important;
        }
    </style>
""", unsafe_allow_html=True)

# Header with Login button
col_header1, col_header2 = st.columns([1, 4])
with col_header1:
    st.image("assets/logo.png", width=180)
with col_header2:
    # Login button with navigation
    col_spacer, col_btn = st.columns([3, 1])
    with col_btn:
        if st.button("Login", key="login_nav", use_container_width=True):
            st.switch_page("pages/login.py")

st.write("")  # Spacing
st.write("")  # Spacing
st.write("")  # Spacing
st.write("")  # Spacing
st.write("")  # Spacing
st.write("")  # Spacing
st.write("")  # Spacing
st.write("")  # Spacing
st.write("")  # Spacing
st.write("")  # Spacing
st.write("")  # Spacing
st.write("")  # Spacing

# Main content: left (text/buttons), right (image)
col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("<div class='main-title'>Your Smart Workspace starts here</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Organize courses, plan schedules, and manage payments all from one intuitive dashboard.</div>", unsafe_allow_html=True)
    
    # CTA Buttons
    st.markdown("""
        <div>
            <a href='#'><button class='cta-btn'>View Preview</button></a>
            <a href='#'><button class='cta-btn-outline'>Contact Us</button></a>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='padding-bottom: 50px;'></div>", unsafe_allow_html=True)

with col2:
    # Dashboard preview image
    try:
        image = Image.open("assets/dasshboard.png")
        st.image(image, width='stretch')
    except FileNotFoundError:
        st.warning("Dashboard preview image not found")
    except Exception as e:
        st.warning(f"Could not load dashboard image: {str(e)}")

# Features/Benefits Section
st.markdown("<div style='padding-top: 80px; padding-bottom: 50px;'></div>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; margin-bottom: 60px;'>
    <h2 style='font-size: 2.5em; font-weight: 700; color: #1a1a1a; margin-bottom: 20px;'>Why Choose EduFlow?</h2>
    <p style='font-size: 1.2em; color: #666; max-width: 700px; margin: 0 auto;'>Streamline your training management with powerful analytics and intuitive tools</p>
</div>
""", unsafe_allow_html=True)

feat1, feat2, feat3 = st.columns(3, gap="large")

with feat1:
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: white; border-radius: 15px; box-shadow: 0 4px 16px rgba(0,0,0,0.08);'>
        <div style='font-size: 3em; margin-bottom: 20px;'>📊</div>
        <h3 style='font-size: 1.5em; font-weight: 600; color: #1a1a1a; margin-bottom: 15px;'>Smart Analytics</h3>
        <p style='color: #666; line-height: 1.6;'>Track registrations, conversions, and revenue in real-time with powerful dashboards</p>
    </div>
    """, unsafe_allow_html=True)

with feat2:
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: white; border-radius: 15px; box-shadow: 0 4px 16px rgba(0,0,0,0.08);'>
        <div style='font-size: 3em; margin-bottom: 20px;'>📚</div>
        <h3 style='font-size: 1.5em; font-weight: 600; color: #1a1a1a; margin-bottom: 15px;'>Course Management</h3>
        <p style='color: #666; line-height: 1.6;'>Organize courses, track participants, and manage payments from one platform</p>
    </div>
    """, unsafe_allow_html=True)

with feat3:
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: white; border-radius: 15px; box-shadow: 0 4px 16px rgba(0,0,0,0.08);'>
        <div style='font-size: 3em; margin-bottom: 20px;'>👥</div>
        <h3 style='font-size: 1.5em; font-weight: 600; color: #1a1a1a; margin-bottom: 15px;'>Team Collaboration</h3>
        <p style='color: #666; line-height: 1.6;'>Enable your team to work together seamlessly with role-based access</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='padding-bottom: 50px;'></div>", unsafe_allow_html=True)

