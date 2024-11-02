# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:47:24 2024

"""

import streamlit as st

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
    
st.title("Gamification Exercises")

st.write("Here you can exercise to detect biases based your statistics.")
