# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:21:36 2024
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

st.title("Statistics Page")

st.write("Here you can display statistics and data visualizations.")
