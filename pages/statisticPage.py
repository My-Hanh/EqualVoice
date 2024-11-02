# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:21:36 2024
"""

import streamlit as st

# Create a sidebar for navigation
st.sidebar.title("Navigation")
if st.sidebar.button("🔍Analyze"):  # Analyze
    st.switch_page("app.py")
if st.sidebar.button("📊Statistics"):  # Overview
    st.switch_page("statisticPage.py")
if st.sidebar.button("📚Educational material"):  # Educational material
    st.switch_page("pages/educationPage.py")
if st.sidebar.button("🎮Exercises"):  # Exercise
    st.switch_page("gamePage.py")

if st.button(
    label="Back", 
    key=None,
    help="",
    on_click=None,
    args=None,
    kwargs=None,
    type="secondary",  
    icon=None,
    disabled=False,
    use_container_width=True  
):
    st.switch_page("app.py")

st.title("Statistics Page")

st.write("Here you can display statistics and data visualizations.")
