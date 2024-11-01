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


col1, col2 = st.columns(2)  


with col2:
    if st.button(
        label="Analyze",  
        key=None,
        help="Click to analyze your data.",
        on_click=None,
        args=None,
        kwargs=None,
        type="secondary",  
        icon=None,
        disabled=False,
        use_container_width=False
    ):
        st.write("Button clicked!")  