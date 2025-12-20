"""
Landing Page for EduFlow
Clean, modern landing page implementation - Fully Responsive
"""
import streamlit as st
import base64
from pathlib import Path

def get_landing_css():
    """Get all CSS styling for the landing page"""
    return """
    <style>
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden !important; display: none !important;}
        footer {visibility: hidden !important; display: none !important;}
        header {visibility: hidden !important; display: none !important;}
        section[data-testid="stSidebar"] {display: none !important; visibility: hidden !important;}
        button[data-testid="baseButton-header"] {display: none !important; visibility: hidden !important;}
        
       
        html, body {
            margin: 0 !important;
            padding: 0 !important;
            width: 100% !important;
            height: 100% !important;
            overflow-x: hidden !important;
        }
        
        .stApp {
            background: #ECEDEF !important;
            padding: 0 !important;
            margin: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .main {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        .main .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
            width: 100% !important;
        }
        
        [data-testid="stAppViewContainer"] {
            padding: 0 !important;
            margin: 0 !important;
            width: 100% !important;
            height: 100% !important;
        }
        
        [data-testid="stAppViewContainer"] > div {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        [data-testid="stVerticalBlock"] {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        [data-testid="stVerticalBlock"] > div {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        [data-testid="element-container"] {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Main container - Exact dimensions from design */
        .landing-container {
            position: relative;
            width: 1280px;
            height: 832px;
            background: #ECEDEF;
            overflow: hidden;
            margin: 0 auto;
            padding: 0;
            z-index: 0;
            box-sizing: border-box;
        }
        
        /* Ellipse 11 - Top Right */
        .ellipse-top-right {
            position: absolute;
            width: 956px;
            height: 956px;
            left: 1003px;
            top: -247px;
            background: rgba(214, 210, 255, 0.34);
            filter: blur(75px);
            border-radius: 50%;
            pointer-events: none;
            z-index: 1;
        }
        
        /* Ellipse 11 - Bottom Left */
        .ellipse-bottom-left {
            position: absolute;
            width: 956px;
            height: 956px;
            left: -316px;
            top: 463px;
            background: rgba(214, 210, 254, 0.34);
            filter: blur(75px);
            border-radius: 50%;
            pointer-events: none;
            z-index: 1;
        }
        
        @media (max-width: 1200px) {
            .ellipse-top-right {
                width: 600px;
                height: 600px;
                right: -150px;
                top: -150px;
            }
            .ellipse-bottom-left {
                width: 600px;
                height: 600px;
                left: -200px;
                bottom: -150px;
            }
        }
        
        @media (max-width: 768px) {
            .ellipse-top-right {
                width: 400px;
                height: 400px;
                right: -100px;
                top: -100px;
            }
            .ellipse-bottom-left {
                width: 400px;
                height: 400px;
                left: -150px;
                bottom: -100px;
            }
        }
        
        /* Logo - Exact position from design */
        .logo {
            position: absolute;
            width: 180px;
            height: 45px;
            left: 159px;
            top: 57px;
            z-index: 11;
            visibility: visible;
        }
        
        .logo > div {
            width: 180px !important;
            height: 45px !important;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 20px !important;
            line-height: 23px !important;
            color: #2E2E2E;
        }
        
        @media (max-width: 1024px) {
            .logo {
                left: 30px;
                top: 30px;
                width: 240px;
                height: 60px;
            }
            .logo > div {
                width: 240px !important;
                height: 60px !important;
                font-size: 28px !important;
                line-height: 34px !important;
            }
        }
        
        @media (max-width: 768px) {
            .logo {
                left: 20px;
                top: 20px;
                width: 200px;
                height: 50px;
            }
            .logo > div {
                width: 200px !important;
                height: 50px !important;
                font-size: 24px !important;
                line-height: 30px !important;
            }
        }
        
        @media (max-width: 480px) {
            .logo {
                left: 15px;
                top: 15px;
                width: 160px;
                height: 40px;
            }
            .logo > div {
                width: 160px !important;
                height: 40px !important;
                font-size: 20px !important;
                line-height: 24px !important;
            }
        }
        
        /* Frame 267 - Header frame - Exact dimensions */
        .header-frame {
            position: absolute;
            width: 1110px;
            height: 45px;
            left: 71px;
            top: 49px;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            padding: 0px;
            gap: 830px;
            z-index: 10;
        }
        
        @media (max-width: 1024px) {
            .header-frame {
                left: 30px;
                right: 30px;
                width: calc(100% - 60px);
                top: 30px;
            }
        }
        
        @media (max-width: 768px) {
            .header-frame {
                left: 20px;
                right: 20px;
                width: calc(100% - 40px);
                top: 20px;
            }
        }
        
        @media (max-width: 480px) {
            .header-frame {
                left: 15px;
                right: 15px;
                width: calc(100% - 30px);
                top: 15px;
            }
        }
        
        /* Frame 178 - Login button - Exact dimensions */
        .login-button {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 3px 17px;
            gap: 10px;
            width: 130px;
            height: 43px;
            background: #51287E;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            position: absolute;
            right: 71px;
            top: 49px;
            z-index: 11;
            text-decoration: none;
            transition: background 0.3s ease;
        }
        
        @media (max-width: 1024px) {
            .login-button {
                right: 30px;
                top: 30px;
                width: 160px;
                height: 56px;
                padding: 10px 28px;
            }
        }
        
        @media (max-width: 768px) {
            .login-button {
                right: 20px;
                top: 20px;
                width: 140px;
                height: 50px;
                padding: 8px 24px;
            }
        }
        
        @media (max-width: 480px) {
            .login-button {
                right: 15px;
                top: 15px;
                width: 120px;
                height: 46px;
                padding: 6px 20px;
            }
        }
        
        .login-button:hover {
            background: #3d1f5e;
        }
        
        .login-button a {
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 500;
            font-size: 15px;
            line-height: 18px;
            color: #FFFFFF;
            text-decoration: none;
            cursor: pointer;
            white-space: nowrap;
            width: 38px;
            height: 18px;
        }
        
        @media (max-width: 1024px) {
            .login-button a {
                font-size: 18px;
                line-height: 22px;
            }
        }
        
        @media (max-width: 768px) {
            .login-button a {
                font-size: 16px;
                line-height: 20px;
            }
        }
        
        @media (max-width: 480px) {
            .login-button a {
                font-size: 15px;
                line-height: 18px;
            }
        }
        
        /* Frame 283 - Content frame - Exact dimensions */
        .content-frame {
            position: absolute;
            width: 679px;
            height: 379px;
            left: 71px;
            top: 219px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: flex-start;
            padding: 0px;
            z-index: 10;
        }
        
        @media (max-width: 1200px) {
            .content-frame {
                width: calc(55% - 60px);
                max-width: 700px;
                left: 40px;
                top: 180px;
                gap: 28px;
            }
        }
        
        @media (max-width: 1024px) {
            .content-frame {
                left: 40px;
                width: calc(55% - 50px);
                max-width: 600px;
                top: 160px;
                gap: 26px;
            }
        }
        
        @media (max-width: 768px) {
            .content-frame {
                left: 20px;
                width: calc(100% - 40px);
                top: 140px;
                position: relative;
                margin-bottom: 50px;
                max-width: 100%;
                gap: 24px;
            }
        }
        
        @media (max-width: 480px) {
            .content-frame {
                left: 15px;
                width: calc(100% - 30px);
                top: 120px;
                gap: 20px;
            }
        }
        
        /* Hero text - Exact dimensions */
        .hero-text {
            margin: 0 auto;
            width: 679px;
            height: 150px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 500;
            font-size: 64px;
            line-height: 75px;
            color: #2E2E2E;
            flex: none;
            order: 0;
            align-self: stretch;
            flex-grow: 0;
        }
        
        @media (max-width: 1024px) {
            .hero-text {
                font-size: 60px;
                line-height: 70px;
                letter-spacing: -0.5px;
            }
        }
        
        @media (max-width: 768px) {
            .hero-text {
                font-size: 44px;
                line-height: 52px;
                max-width: 100%;
                letter-spacing: -0.5px;
            }
        }
        
        @media (max-width: 480px) {
            .hero-text {
                font-size: 32px;
                line-height: 40px;
                letter-spacing: 0px;
            }
        }
        
        /* Description text - Exact dimensions */
        .description-text {
            margin: 0 auto;
            width: 537px;
            height: 65px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 24px;
            line-height: 28px;
            color: #2E2E2E;
            flex: none;
            order: 1;
            flex-grow: 0;
        }
        
        @media (max-width: 1024px) {
            .description-text {
                font-size: 24px;
                line-height: 32px;
            }
        }
        
        @media (max-width: 768px) {
            .description-text {
                font-size: 20px;
                line-height: 28px;
                max-width: 100%;
            }
        }
        
        @media (max-width: 480px) {
            .description-text {
                font-size: 18px;
                line-height: 24px;
            }
        }
        
        /* Frame 282 - Buttons frame - Exact dimensions */
        .buttons-frame {
            margin: 0 auto;
            width: 407px;
            height: 64px;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            padding: 0px;
            gap: 26px;
            flex: none;
            order: 2;
            flex-grow: 0;
        }
        
        @media (max-width: 768px) {
            .buttons-frame {
                max-width: 100%;
                gap: 18px;
            }
        }
        
        @media (max-width: 480px) {
            .buttons-frame {
                flex-direction: column;
                width: 100%;
                gap: 14px;
            }
        }
        
        /* Frame 179 - Primary CTA button - Exact dimensions */
        .cta-primary {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 6px 63px;
            gap: 10px;
            margin: 0 auto;
            width: 195px;
            height: 50px;
            background: #51287E;
            border-radius: 40px;
            border: none;
            cursor: pointer;
            text-decoration: none;
            transition: background 0.3s ease;
            flex: none;
            order: 0;
            flex-grow: 0;
        }
        
        @media (max-width: 768px) {
            .cta-primary {
                padding: 12px 40px;
                min-width: 180px;
                height: 58px;
            }
        }
        
        @media (max-width: 480px) {
            .cta-primary {
                width: 100%;
                min-width: 100%;
                padding: 14px 24px;
                height: 56px;
            }
        }
        
        .cta-primary:hover {
            background: #3d1f5e;
            transform: translateY(-2px);
            box-shadow: 0px 6px 20px rgba(81, 40, 126, 0.4);
        }
        
        .cta-primary a {
            width: 144px;
            height: 28px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 500;
            font-size: 24px;
            line-height: 28px;
            color: #FFFFFF;
            text-decoration: none;
            white-space: nowrap;
            flex: none;
            order: 0;
            flex-grow: 0;
        }
        
        @media (max-width: 768px) {
            .cta-primary a {
                font-size: 20px;
                line-height: 24px;
            }
        }
        
        @media (max-width: 480px) {
            .cta-primary a {
                font-size: 18px;
                line-height: 22px;
            }
        }
        
        /* Frame 180 - Secondary CTA button - Exact dimensions */
        .cta-secondary {
            box-sizing: border-box;
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 6px 26px;
            gap: 10px;
            margin: 0 auto;
            width: 195px;
            height: 50px;
            border: 1px solid #51287E;
            border-radius: 40px;
            background: transparent;
            cursor: pointer;
            text-decoration: none;
            transition: background 0.3s ease;
            flex: none;
            order: 1;
            flex-grow: 0;
        }
        
        @media (max-width: 768px) {
            .cta-secondary {
                padding: 12px 32px;
                min-width: 180px;
                height: 58px;
            }
        }
        
        @media (max-width: 480px) {
            .cta-secondary {
                width: 100%;
                min-width: 100%;
                padding: 14px 24px;
                height: 56px;
            }
        }
        
        .cta-secondary:hover {
            background: rgba(81, 40, 126, 0.1);
            transform: translateY(-2px);
            border-color: #3d1f5e;
        }
        
        .cta-secondary a {
            width: 119px;
            height: 28px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 500;
            font-size: 24px;
            line-height: 28px;
            color: #51287E;
            text-decoration: none;
            white-space: nowrap;
            flex: none;
            order: 0;
            flex-grow: 0;
        }
        
        @media (max-width: 768px) {
            .cta-secondary a {
                font-size: 20px;
                line-height: 24px;
            }
        }
        
        @media (max-width: 480px) {
            .cta-secondary a {
                font-size: 18px;
                line-height: 22px;
            }
        }
        
        /* Frame 294 - Dashboard preview container - Exact dimensions */
        .dashboard-preview-container {
            position: absolute;
            width: 435.21px;
            height: 292px;
            left: 775px;
            top: 306px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 18px 21px;
            gap: 10px;
            isolation: isolate;
            z-index: 10;
        }
        
        @media (max-width: 1400px) {
            .dashboard-preview-container {
                transform: scale(1.3);
            }
        }
        
        @media (max-width: 1200px) {
            .dashboard-preview-container {
                width: 570px;
                height: 390px;
                right: 40px;
                top: 150px;
                transform: scale(1.2);
            }
        }
        
        @media (max-width: 1024px) {
            .dashboard-preview-container {
                width: 525px;
                height: 360px;
                right: 40px;
                top: 130px;
                transform: scale(1.1);
            }
        }
        
        @media (max-width: 768px) {
            .dashboard-preview-container {
                position: relative;
                left: auto;
                right: auto;
                top: 0;
                margin: 40px auto 0;
                width: 90%;
                max-width: 652px;
                height: auto;
                min-height: 375px;
                transform: scale(1);
                transform-origin: center;
            }
        }
        
        @media (max-width: 480px) {
            .dashboard-preview-container {
                width: calc(100% - 30px);
                margin: 30px auto 0;
                padding: 15px;
                transform: scale(1);
            }
        }
        
        /* Group 230 - Dashboard preview wrapper - Exact dimensions */
        .dashboard-preview {
            position: absolute;
            width: 435.21px;
            height: 292px;
            left: 0px;
            top: 0px;
            z-index: 0;
            flex: none;
            order: 0;
            flex-grow: 0;
        }
        
        /* Rectangle 79 - Background - Exact dimensions */
        .dashboard-preview-bg {
            position: absolute;
            width: 435.21px;
            height: 292px;
            left: 0px;
            top: 0px;
            background: #D6D2FF;
            border-radius: 35px;
        }
        
        /* Dashboard image - Exact dimensions */
        .dashboard-image {
            width: 392.22px;
            height: 254.94px;
            background-size: cover;
            background-position: center;
            box-shadow: 0px 4px 11.2px rgba(0, 0, 0, 0.25);
            border-radius: 20px;
            position: relative;
            z-index: 1;
            flex: none;
            order: 1;
            flex-grow: 0;
        }
        
        @media (max-width: 1200px) {
            .dashboard-image {
                width: 510px;
                height: 330px;
            }
        }
        
        @media (max-width: 1024px) {
            .dashboard-image {
                width: 465px;
                height: 300px;
            }
        }
        
        @media (max-width: 768px) {
            .dashboard-image {
                width: 100%;
                max-width: 588px;
                height: auto;
                aspect-ratio: 588 / 382;
                margin: 22.5px auto;
            }
        }
        
        @media (max-width: 480px) {
            .dashboard-image {
                margin: 15px auto;
                border-radius: 22.5px;
            }
        }
        
        .dashboard-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 30px;
        }
        
        @media (max-width: 480px) {
            .dashboard-image img {
                border-radius: 22.5px;
            }
        }
    </style>
    """


def get_landing_html():
    """Get HTML content structure for the landing page"""
    return """<div class="landing-container">
        <div class="ellipse-top-right"></div>
        <div class="ellipse-bottom-left"></div>
        
        <div class="header-frame">
            <div class="logo">
                <div style="font-family: 'Roboto', sans-serif; font-weight: 700; font-size: 20px; line-height: 23px; color: #2E2E2E; width: 180px; height: 45px; display: flex; align-items: center;">
                    <span style="color: #B3B3B3;">Edu</span><span style="color: #51287E;">flow</span>
                </div>
            </div>
            <div class="login-button" id="login-btn">
                <a href="/login">Login</a>
            </div>
        </div>
        
        <div class="content-frame">
            <h1 class="hero-text">Your Smart Workspace starts here</h1>
            <p class="description-text">Organize courses, plan schedules, and manage payments all from one intuitive dashboard.</p>
            <div class="buttons-frame">
                <div class="cta-primary" id="preview-btn">
                    <a href="/dashboard">View Preview</a>
                </div>
                <div class="cta-secondary" id="contact-btn">
                    <a href="#">Contact Us</a>
                </div>
            </div>
        </div>
        
        <div class="dashboard-preview-container">
            <div class="dashboard-preview">
                <div class="dashboard-preview-bg"></div>
            </div>
            <div class="dashboard-image" id="dashboard-img-container"></div>
        </div>
    </div>"""


def get_landing_javascript(dashboard_img_src=""):
    """Get JavaScript for image loading and navigation"""
    if dashboard_img_src:
        return f"""<script>
            (function() {{
                var container = document.getElementById('dashboard-img-container');
                if (container) {{
                    var img = document.createElement('img');
                    img.src = '{dashboard_img_src}';
                    img.style.width = '100%';
                    img.style.height = '100%';
                    img.style.objectFit = 'cover';
                    img.style.borderRadius = '20px';
                    img.style.boxShadow = '0px 4px 11.2px rgba(0, 0, 0, 0.25)';
                    container.appendChild(img);
                }}
            }})();
            
            function navigateTo(path) {{
                window.location.href = path;
            }}
            
            document.addEventListener('DOMContentLoaded', function() {{
                var loginBtn = document.getElementById('login-btn');
                if (loginBtn) {{
                    loginBtn.style.cursor = 'pointer';
                    loginBtn.addEventListener('click', function(e) {{
                        e.preventDefault();
                        e.stopPropagation();
                        navigateTo('/login');
                    }}, true);
                    loginBtn.addEventListener('touchstart', function(e) {{
                        e.preventDefault();
                        navigateTo('/login');
                    }}, true);
                }}
                
                var previewBtn = document.getElementById('preview-btn');
                if (previewBtn) {{
                    previewBtn.style.cursor = 'pointer';
                    previewBtn.addEventListener('click', function(e) {{
                        e.preventDefault();
                        e.stopPropagation();
                        navigateTo('/dashboard');
                    }}, true);
                }}
                
                document.querySelectorAll('a[href^="/"]').forEach(function(link) {{
                    link.style.cursor = 'pointer';
                    link.addEventListener('click', function(e) {{
                        e.preventDefault();
                        e.stopPropagation();
                        var href = this.getAttribute('href');
                        if (href && href !== '#') {{
                            navigateTo(href);
                        }}
                    }}, true);
                }});
            }});
        </script>"""
    else:
        return """<script>
            (function() {{
                var container = document.getElementById('dashboard-img-container');
                if (container) {{
                    container.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
                    container.style.display = 'flex';
                    container.style.alignItems = 'center';
                    container.style.justifyContent = 'center';
                    container.style.color = 'white';
                    container.style.fontFamily = 'Roboto, sans-serif';
                    container.style.fontSize = '18px';
                    container.textContent = 'Dashboard Preview';
                }}
            }})();
            
            function navigateTo(path) {{
                window.location.href = path;
            }}
            
            document.addEventListener('DOMContentLoaded', function() {{
                var loginBtn = document.getElementById('login-btn');
                if (loginBtn) {{
                    loginBtn.style.cursor = 'pointer';
                    loginBtn.addEventListener('click', function(e) {{
                        e.preventDefault();
                        e.stopPropagation();
                        navigateTo('/login');
                    }}, true);
                    loginBtn.addEventListener('touchstart', function(e) {{
                        e.preventDefault();
                        navigateTo('/login');
                    }}, true);
                }}
                
                var previewBtn = document.getElementById('preview-btn');
                if (previewBtn) {{
                    previewBtn.style.cursor = 'pointer';
                    previewBtn.addEventListener('click', function(e) {{
                        e.preventDefault();
                        e.stopPropagation();
                        navigateTo('/dashboard');
                    }}, true);
                }}
                
                document.querySelectorAll('a[href^="/"]').forEach(function(link) {{
                    link.style.cursor = 'pointer';
                    link.addEventListener('click', function(e) {{
                        e.preventDefault();
                        e.stopPropagation();
                        var href = this.getAttribute('href');
                        if (href && href !== '#') {{
                            navigateTo(href);
                        }}
                    }}, true);
                }});
            }});
        </script>"""


def render_landing_page():
    """Render the landing page with separated styling and content"""
    
    # Add viewport meta tag for proper mobile rendering
    viewport_meta = """<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">"""
    st.markdown(f"<head>{viewport_meta}</head>", unsafe_allow_html=True)
    
    # Apply CSS styling
    st.markdown(f"<style>{get_landing_css()}</style>", unsafe_allow_html=True)
    
    # Render HTML content
    st.markdown(get_landing_html(), unsafe_allow_html=True)
    
    # Load dashboard image
    dashboard_img_src = ""
    try:
        base_path = Path(__file__).parent.parent
        dashboard_path = base_path / "assets" / "Dashboard.jpg"
        if dashboard_path.exists():
            with open(dashboard_path, "rb") as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
                dashboard_img_src = f"data:image/jpeg;base64,{img_data}"
    except Exception:
        pass
    
    # Apply JavaScript for image loading and navigation
    st.markdown(get_landing_javascript(dashboard_img_src), unsafe_allow_html=True)

def main():
    """Main landing page function"""
    st.set_page_config(
        page_title="EduFlow - Your Smart Workspace",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    render_landing_page()

if __name__ == "__main__":
    main()
