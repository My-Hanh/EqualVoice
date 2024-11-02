# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:39:27 2024

"""

import streamlit as st

st.set_page_config(page_title="Multi-Page App")

st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ("Home", "Statistics"))

if options == "Text Bias Detector":
    import main
elif options == "Statistics":
    import statisticPage

