"""
Dashboard Page for EduFlow
Main dashboard with statistics, charts, and navigation
"""
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
from pathlib import Path

# Add parent directory to path to import components
sys.path.append(str(Path(__file__).parent.parent))
from components.sidebar import render_sidebar

def render_stat_card(title, value, icon_bg_color="#F4F4F4", icon_emoji="📊"):
    """Render a statistics card matching the design"""
    card_html = f"""
    <div style="
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding: 13px 20px;
        gap: 10px;
        width: 240px;
        height: 150px;
        background: #FFFFFF;
        border-radius: 15px;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
    ">
        <div style="display: flex; flex-direction: column; gap: 13px; width: 100%;">
            <div style="
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                padding: 4px 0px;
                width: 41px;
                height: 41px;
                background: {icon_bg_color};
                border-radius: 30px;
            ">
                <span style="font-size: 24px;">{icon_emoji}</span>
            </div>
            <div style="
                font-family: 'Roboto', sans-serif;
                font-weight: 500;
                font-size: 24px;
                line-height: 28px;
                color: #2E2E2E;
            ">{value}</div>
            <div style="
                font-family: 'Roboto', sans-serif;
                font-weight: 500;
                font-size: 16px;
                line-height: 19px;
                color: #565656;
            ">{title}</div>
        </div>
    </div>
    """
    return card_html

def render_dashboard():
    """Render the main dashboard with comprehensive styling"""
    
    # Check authentication
    if not st.session_state.get('authenticated', False):
        st.warning("Please login to access the dashboard")
        st.switch_page("pages/login.py")
        return
    
    # Get user name from session
    user_email = st.session_state.get('user_email', 'User')
    user_name = user_email.split('@')[0].title() if '@' in user_email else 'User'
    
    # Comprehensive dashboard CSS based on provided design
    dashboard_css = """
    <style>
        /* Main dashboard container */
        .stApp {
            background: rgba(247, 248, 250, 0.94902);
        }
        
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Main content area */
        .main .block-container {
            padding-top: 35px;
            padding-left: 245px;
            padding-right: 35px;
            padding-bottom: 20px;
            max-width: 100%;
        }
        
        /* Header greeting */
        .greeting {
            width: 169px;
            height: 23px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 500;
            font-size: 20px;
            line-height: 23px;
            color: #2E2E2E;
            margin-bottom: 16px;
        }
        
        /* Stat cards container - Frame 203 */
        .stats-row {
            display: flex;
            flex-direction: row;
            align-items: flex-start;
            padding: 0px;
            gap: 16px;
            width: 100%;
            margin-bottom: 16px;
        }
        
        /* Stat card styling - matching exact design */
        .stat-card {
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 13px 20px;
            gap: 10px;
            width: 240px;
            height: 150px;
            background: #FFFFFF;
            border-radius: 15px;
        }
        
        .stat-card-frame {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 0px;
            gap: 13px;
            width: 200px;
            height: 114px;
        }
        
        .stat-icon-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 4px 0px;
            gap: 10px;
            width: 41px;
            height: 41px;
            background: #F4F4F4;
            border-radius: 30px;
        }
        
        .stat-value {
            width: 200px;
            height: 28px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 500;
            font-size: 24px;
            line-height: 28px;
            color: #2E2E2E;
        }
        
        .stat-label {
            width: 200px;
            height: 19px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 500;
            font-size: 16px;
            line-height: 19px;
            color: #565656;
        }
        
        /* Completion Rate card - special styling */
        .completion-card {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: flex-start;
            padding: 13px 21px;
            gap: 41px;
            width: 240px;
            height: 149px;
            background: #FFFFFF;
            border-radius: 15px;
        }
        
        .completion-chart {
            margin: 0 auto;
            width: 91px;
            height: 91px;
            position: relative;
        }
        
        .completion-label {
            margin: 0 auto;
            width: 193px;
            height: 19px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 500;
            font-size: 16px;
            line-height: 19px;
            color: #565656;
            text-align: center;
        }
        
        /* Revenue by course calendar container */
        .calendar-container {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 27px 28px;
            gap: 129px;
            width: 100%;
            background: #FFFFFF;
            border-radius: 15px;
            margin-bottom: 16px;
        }
        
        .calendar-left {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: flex-start;
            padding: 0px;
            gap: 2px;
            width: 427px;
            height: 220px;
        }
        
        .calendar-header {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            padding: 0px;
            gap: 72px;
            width: 427px;
            height: 36px;
        }
        
        .calendar-date-selector {
            display: flex;
            flex-direction: row;
            align-items: center;
            padding: 0px;
            gap: 16px;
            width: 139px;
            height: 28px;
        }
        
        .calendar-month {
            width: 114px;
            height: 24px;
            font-family: 'Arial', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 16px;
            line-height: 24px;
            color: #2E2E2E;
        }
        
        .calendar-grid {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 0px;
            width: 427px;
            height: 167px;
        }
        
        .calendar-weekdays {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            padding: 0px;
            gap: 8px;
            width: 427px;
            height: 34px;
        }
        
        .calendar-weekday {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 7px 11px;
            gap: 10px;
            width: auto;
            height: 34px;
            font-family: 'Arial', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
            color: #62748E;
        }
        
        .calendar-days-grid {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            padding: 0px;
            width: 427px;
            height: 116px;
        }
        
        .calendar-week {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            padding: 0px;
            gap: 54px;
            width: 410px;
            height: 20px;
        }
        
        .calendar-day {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 0px;
            width: 20px;
            height: 20px;
            border-radius: 10px;
            font-family: 'Arial', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
            color: #2E2E2E;
        }
        
        .calendar-day.highlight-green {
            background: #CFE886;
            color: #FFFFFF;
            border-radius: 5px;
        }
        
        .calendar-day.highlight-purple {
            background: #51287E;
            color: #FFFFFF;
            border-radius: 5px;
        }
        
        .calendar-day.highlight-pink {
            background: #F8B6A8;
            color: #FFFFFF;
            border-radius: 5px;
        }
        
        .calendar-day.disabled {
            color: #CAD5E2;
        }
        
        /* Registration chart container */
        .registration-chart-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 37px 34px;
            gap: 35px;
            width: 100%;
            background: #FFFFFF;
            border-radius: 15px;
            margin-bottom: 16px;
        }
        
        .chart-header {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: flex-start;
            padding: 0px;
            gap: 35px;
            width: 100%;
            height: 36px;
        }
        
        .chart-title {
            width: 171px;
            height: 19px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 500;
            font-size: 16px;
            line-height: 19px;
            color: #565656;
        }
        
        /* Upcoming events container */
        .events-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 0px;
            gap: 9px;
            width: 328px;
        }
        
        .events-title {
            width: 328px;
            height: 20px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 16px;
            line-height: 20px;
            color: #2E2E2E;
        }
        
        .event-card {
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 15px 20px;
            gap: 10px;
            width: 328px;
            height: 69px;
            background: #ECEDEF;
            border-left: 5px solid;
            border-radius: 10px;
        }
        
        .event-content {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: flex-start;
            padding: 0px;
            gap: 8px;
            width: 101px;
            height: 39px;
        }
        
        .event-title {
            width: 101px;
            height: 17px;
            font-family: 'Arial', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 15px;
            line-height: 17px;
            color: #2E2E2E;
        }
        
        .event-time {
            width: 129px;
            height: 14px;
            font-family: 'Arial', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 12px;
            line-height: 14px;
            color: #565656;
        }
        
        /* Best performing course card */
        .course-performance-container {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: flex-start;
            padding: 0px;
            gap: 72px;
            width: 283px;
            height: 270px;
        }
        
        .course-performance-card {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 0px;
            gap: 16px;
            width: 283px;
            height: 94px;
        }
        
        .course-performance-title {
            width: 283px;
            height: 19px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 500;
            font-size: 16px;
            line-height: 19px;
            color: #565656;
        }
        
        .course-header {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: flex-end;
            padding: 0px;
            gap: 70px;
            width: 257px;
            height: 24px;
        }
        
        .course-name {
            width: 163px;
            height: 23px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 20px;
            line-height: 23px;
            color: #2E2E2E;
        }
        
        .course-metrics {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            padding: 0px;
            gap: 22px;
            width: 257px;
            height: 19px;
        }
        
        .metric-group {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            padding: 0px;
            gap: 13px;
            width: 119px;
            height: 19px;
        }
        
        .metric-value {
            width: 30px;
            height: 19px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 16px;
            line-height: 19px;
        }
        
        .metric-value.positive {
            color: #56BB81;
        }
        
        .metric-value.negative {
            color: #D14540;
        }
        
        .metric-label {
            width: 81px;
            height: 19px;
            font-family: 'Roboto', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 16px;
            line-height: 19px;
            color: #2E2E2E;
        }
    </style>
    """
    
    st.markdown(dashboard_css, unsafe_allow_html=True)
    
    # Header
    st.markdown(f'<div class="greeting">Hello, {user_name}\'s Name</div>', unsafe_allow_html=True)
    
    # First row of stat cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(render_stat_card("Total Courses", "100", "#F4F4F4", "🎓"), unsafe_allow_html=True)
    
    with col2:
        st.markdown(render_stat_card("Total Registrations", "1,000", "#F4F4F4", "📝"), unsafe_allow_html=True)
    
    with col3:
        st.markdown(render_stat_card("Total Employees", "20", "#F4F4F4", "👤"), unsafe_allow_html=True)
    
    with col4:
        st.markdown(render_stat_card("Total Participants", "50", "#F4F4F4", "👥"), unsafe_allow_html=True)
    
    # Second row of stat cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(render_stat_card("Total Revenue", "2,000$", "#F4F4F4", "💰"), unsafe_allow_html=True)
    
    with col2:
        st.markdown(render_stat_card("Payments Collected", "2,000$", "#F4F4F4", "✅"), unsafe_allow_html=True)
    
    with col3:
        st.markdown(render_stat_card("Payments Pending", "2,000$", "#F4F4F4", "⏳"), unsafe_allow_html=True)
    
    with col4:
        # Completion Rate card with circular progress
        completion_html = """
        <div class="completion-card">
            <div class="completion-chart">
                <svg width="91" height="91" style="transform: rotate(-90deg);">
                    <circle cx="45.5" cy="45.5" r="36.8" fill="none" stroke="#ECEDEF" stroke-width="7.36"/>
                    <circle cx="45.5" cy="45.5" r="36.8" fill="none" stroke="#51287E" stroke-width="7.36" 
                            stroke-dasharray="231.33" stroke-dashoffset="57.83" stroke-linecap="round"/>
                </svg>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); 
                            font-family: 'Roboto', sans-serif; font-size: 24px; color: #2E2E2E;">75%</div>
            </div>
            <div class="completion-label">Courses Completion Rate</div>
        </div>
        """
        st.markdown(completion_html, unsafe_allow_html=True)
    
    # Main content area - Calendar and Chart
    col_main, col_sidebar = st.columns([2, 1])
    
    with col_main:
        # Revenue by course calendar
        calendar_html = """
        <div class="calendar-container">
            <div class="calendar-left">
                <div class="calendar-header">
                    <div class="calendar-date-selector">
                        <div class="calendar-month">December 2025</div>
                        <div style="width: 20px; height: 20px; transform: rotate(90deg);">‹</div>
                    </div>
                </div>
                <div class="calendar-grid">
                    <div class="calendar-weekdays">
                        <div class="calendar-weekday">Sun</div>
                        <div class="calendar-weekday">Mon</div>
                        <div class="calendar-weekday">Tue</div>
                        <div class="calendar-weekday">Wed</div>
                        <div class="calendar-weekday">Thu</div>
                        <div class="calendar-weekday">Fri</div>
                        <div class="calendar-weekday">Sat</div>
                    </div>
                    <div class="calendar-days-grid">
                        <div class="calendar-week">
                            <div class="calendar-day disabled">30</div>
                            <div class="calendar-day">1</div>
                            <div class="calendar-day">2</div>
                            <div class="calendar-day">3</div>
                            <div class="calendar-day">4</div>
                            <div class="calendar-day">5</div>
                            <div class="calendar-day">6</div>
                        </div>
                        <div class="calendar-week">
                            <div class="calendar-day">7</div>
                            <div class="calendar-day">8</div>
                            <div class="calendar-day">9</div>
                            <div class="calendar-day">10</div>
                            <div class="calendar-day">11</div>
                            <div class="calendar-day">12</div>
                            <div class="calendar-day">13</div>
                        </div>
                        <div class="calendar-week">
                            <div class="calendar-day">14</div>
                            <div class="calendar-day highlight-green">15</div>
                            <div class="calendar-day">16</div>
                            <div class="calendar-day">17</div>
                            <div class="calendar-day highlight-purple">18</div>
                            <div class="calendar-day">19</div>
                            <div class="calendar-day">20</div>
                        </div>
                        <div class="calendar-week">
                            <div class="calendar-day">21</div>
                            <div class="calendar-day">22</div>
                            <div class="calendar-day">23</div>
                            <div class="calendar-day">24</div>
                            <div class="calendar-day highlight-pink">25</div>
                            <div class="calendar-day">26</div>
                            <div class="calendar-day">27</div>
                        </div>
                        <div class="calendar-week">
                            <div class="calendar-day">28</div>
                            <div class="calendar-day">29</div>
                            <div class="calendar-day">30</div>
                            <div class="calendar-day">31</div>
                            <div class="calendar-day disabled">1</div>
                            <div class="calendar-day disabled">2</div>
                            <div class="calendar-day disabled">3</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        st.markdown(calendar_html, unsafe_allow_html=True)
        
        # Registration chart
        st.markdown('<div class="registration-chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="chart-header"><div class="chart-title">Registrations per week</div></div>', unsafe_allow_html=True)
        
        # Create sample data for registration chart
        weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        registrations = [120, 180, 150, 200, 170, 140, 160]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=weeks,
            y=registrations,
            marker_color='#51287E',
            name='Registrations'
        ))
        
        fig.update_layout(
            height=300,
            showlegend=False,
            margin=dict(l=40, r=40, t=20, b=40),
            plot_bgcolor='white',
            paper_bgcolor='white',
            xaxis=dict(
                showgrid=False,
                tickfont=dict(family='Inter', size=12, color='#6B7280')
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='#E5E7EB',
                gridwidth=1,
                tickfont=dict(family='Inter', size=12, color='#6B7280')
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_sidebar:
        # Upcoming events
        st.markdown('<div class="events-container">', unsafe_allow_html=True)
        st.markdown('<div class="events-title">Upcoming events</div>', unsafe_allow_html=True)
        
        events = [
            ("Team Meeting", "Today at 2:00pm", "#CFE886"),
            ("Project Review", "December 18 at 2:00pm", "#51287E"),
            ("Team Meeting", "December 26 at 2:00pm", "#F8B6A8"),
        ]
        
        for event_title, event_time, border_color in events:
            event_html = f"""
            <div class="event-card" style="border-left-color: {border_color};">
                <div class="event-content">
                    <div class="event-title">{event_title}</div>
                    <div class="event-time">{event_time}</div>
                </div>
            </div>
            """
            st.markdown(event_html, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Best performing course
        st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)
        best_course_html = """
        <div class="course-performance-container">
            <div class="course-performance-card">
                <div class="course-performance-title">Best Performing Course</div>
                <div class="course-header">
                    <div class="course-name">Leadership Basics</div>
                    <div style="width: 24px; height: 24px;">→</div>
                </div>
                <div class="course-metrics">
                    <div class="metric-group">
                        <span class="metric-value positive">82%</span>
                        <span class="metric-label">Conversion</span>
                    </div>
                </div>
            </div>
        </div>
        """
        st.markdown(best_course_html, unsafe_allow_html=True)
        
        # Underperforming course
        st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)
        underperforming_course_html = """
        <div class="course-performance-container">
            <div class="course-performance-card">
                <div class="course-performance-title">Underperforming Course</div>
                <div class="course-header">
                    <div class="course-name">Excel Essentials</div>
                    <div style="width: 24px; height: 24px;">→</div>
                </div>
                <div class="course-metrics">
                    <div class="metric-group">
                        <span class="metric-value negative">34%</span>
                        <span class="metric-label">Conversion</span>
                    </div>
                </div>
            </div>
        </div>
        """
        st.markdown(underperforming_course_html, unsafe_allow_html=True)

def main():
    """Main dashboard function"""
    st.set_page_config(
        page_title="Dashboard - EduFlow",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': None
        }
    )
    
    # Render sidebar
    with st.sidebar:
        render_sidebar(current_page="dashboard")
    
    # Render main dashboard
    render_dashboard()

if __name__ == "__main__":
    main()
