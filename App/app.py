# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:32:37 2024

"""

import streamlit as st

username = "Stella Muster"

top_bar = st.columns([6, 2])

with top_bar[0]:
    st.write("")
    
with top_bar[1]:
    st.write(f"👤**{username}**")
    if st.button("Statistics"):
        st.switch_page("pages/statisticPage.py")
        
st.write("---")

text_area = st.text_area(
    label="",  
    value="",  
    height=400,  
    max_chars=None,
    key=None,
    help="Enter your text here.",
    on_change=None,
    args=None,
    kwargs=None,
    placeholder="Type here...",
    disabled=False,
    label_visibility="visible"
)


col1, col2, col3 = st.columns([1, 1, 2])  
with col1:
    if st.button(
        label="Educational material", 
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
        st.switch_page("pages/educationPage.py")
        
with col2:
    if st.button(
        label="Exercise", 
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
        st.switch_page("pages/gamePage.py")

with col3:
    subcol1, subcol2 = st.columns([1, 1])
    with subcol1:
        if st.button(
            label="Analyze", 
            key=None,
            help="Click to analyze your text.",
            on_click=None,
            args=None,
            kwargs=None,
            type="secondary",  
            icon="🔍",
            disabled=False,
            use_container_width=True  
        ):
            st.write("Button clicked!")  
    with subcol2:
        if st.button(
            label="Publish", 
            key=None,
            help="Click to publish your text.",
            on_click=None,
            args=None,
            kwargs=None,
            type="secondary",  
            icon=None,
            disabled=False,
            use_container_width=True  
        ):
            st.write("Button clicked!")  
            
            


