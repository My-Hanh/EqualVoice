from openai import OpenAI
import streamlit as st





st.title("Text Bias Detector")

import streamlit as st

st.text_area(
    label="",
    value="",
    height= 500,  # Let CSS control height
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

st.button("Click me")