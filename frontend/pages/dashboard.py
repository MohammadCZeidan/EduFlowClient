import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="EduFlow Dashboard", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .sidebar { background-color: #f8f9fa; }
        .metric-card { 
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("assets/logo.png", width=100)
    st.markdown("---")
    
    menu_items = ["Dashboard", "Courses", "Participants", "Payments", "Employees"]
    selected = st.radio("Menu", menu_items, label_visibility="collapsed")
    
    st.markdown("---")
    st.write("👤 Logout")

# Main content
st.write("Hello, User's Name")
st.markdown("---")

# Metrics Row 1
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Courses", "100")
with col2:
    st.metric("Total Registration", "1,000")
with col3:
    st.metric("Total Employees", "20")
with col4:
    st.metric("Total Participants", "50")
with col5:
    st.write("")  # Placeholder

# Metrics Row 2
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Revenue", "2,000$")
with col2:
    st.metric("Payments Collected", "2,000$")
with col3:
    st.metric("Payments Pending", "2,000$")
with col4:
    # Circular progress chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=75,
        title="Courses Completion Rate",
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "#6C4FF7"},
            'steps': [
                {'range': [0, 50], 'color': "#f0f0f0"},
                {'range': [50, 100], 'color': "#e0e0e0"}
            ]
        }
    ))
    fig.update_layout(height=250)
    st.plotly_chart(fig, use_container_width=True)

# Calendar and Events
col1, col2 = st.columns([2, 1])

with col1:
    st.write("**December 2025**")
    st.write("Calendar view - view in calendar widget")

with col2:
    st.write("**Upcoming events**")
    
    events = [
        {"title": "Team Meeting", "date": "Today at 2:00pm", "color": "#ffd700"},
        {"title": "Project Review", "date": "December 18 at 2:00pm", "color": "#6C4FF7"},
        {"title": "Team Meeting", "date": "December 26 at 2:00pm", "color": "#ffb3ba"}
    ]
    
    for event in events:
        st.markdown(f"""
        <div style='padding: 12px; margin: 10px 0; border-radius: 8px; background-color: {event['color']}20; border-left: 4px solid {event['color']}'>
            <strong>{event['title']}</strong><br>
            <small>{event['date']}</small>
        </div>
        """, unsafe_allow_html=True)

# Registrations Chart
st.markdown("---")
st.write("**Registrations per week**")

weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5']
registrations = [120, 135, 110, 150, 165]

fig = px.bar(x=weeks, y=registrations, labels={'x': '', 'y': 'Registrations'})
fig.update_layout(showlegend=False, height=300)
st.plotly_chart(fig, use_container_width=True)

# Best Performing Course
st.write("**Best Performing Course**")
st.info("Python 101 - 450 registrations, 380 completed")
