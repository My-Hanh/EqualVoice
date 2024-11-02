# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:32:37 2024
"""

import streamlit as st

# Custom CSS for theme


# Set page configuration
st.set_page_config(
    page_title="Media Bias Tool",
    page_icon="📊",
    layout="wide"
)

# Create a sidebar for navigation
st.sidebar.title("Navigation")
if st.sidebar.button("🔍Analyze"):  
    st.switch_page("app.py")
if st.sidebar.button("📊Statistics"):  
    st.switch_page("pages/statisticPage.py")
if st.sidebar.button("📚Educational material"):  
    st.switch_page("pages/educationPage.py")
if st.sidebar.button("🎮Exercise"): 
    st.switch_page("pages/gamePage.py")

# Main content area
username = "Stella Muster"
st.title(f"Welcome, {username} 👤")
st.write("---")

# Main text area for user input
text_area = st.text_area(
    label="Enter your text here:",  
    value="",  
    height=400,  
    placeholder="Type here..."
)

# Action buttons
col1, col2 = st.columns([3,1])
    
with col2:
    subcol1, subcol2 = st.columns([1,1])
    with subcol1:
        if st.button("Analyze"):
            st.write("Analyze button clicked!")  
   
    with subcol2:
        if st.button("Publish"):
            st.write("Publish button clicked!")
