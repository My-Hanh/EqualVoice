import streamlit as st
import streamlit.components.v1 as components

from algorithm import analyze
from parser import map_marked_text_to_html

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"



# Initial values of some state variables
if "display_result" not in st.session_state:
    st.session_state.display_result = False
if "user_text" not in st.session_state:
    st.session_state.user_text = ""

USER_TEXT_INITIAL_HEIGHT = 500



# Custom styling
style_1 = (".text-with-results {" +
                "height: " +
                f"{USER_TEXT_INITIAL_HEIGHT}px;" + 
                "width: 70%;" + 
                "border: 1px solid grey;" + 
                "border-radius: 5px;" + 
                "height: 500px;" + 
                "padding: 5px;" + 
                "margin: 5px;" +
                "}")
style_2 = """.highlighted {
                background-color: pink;
            }"""

st.write(f'''<style>
            {style_1}
            {style_2}
    </style>''',
    unsafe_allow_html=True
)

# Custom script
script_1 = (
    """function show_details() {
        console.log('hello');
    }"""
)
st.write(f'''<script>
            {script_1}
    </script>''',
    unsafe_allow_html=True
)




st.title("Text Bias Detector")

if not st.session_state.display_result:
    # Show empty textarea for user to enter the initial data.
    # We will hide it and replace with another more complex element for the results.
    user_text = st.text_area(
        label="",
        value=st.session_state.user_text,
        height= USER_TEXT_INITIAL_HEIGHT,  # Let CSS control height
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
else:
    # Show the text with highlights
    html_with_highlights, all_problems = map_marked_text_to_html(st.session_state.marked_text)
    st.session_state.all_problems = all_problems
    st.write(f"""<div class='text-with-results'>{html_with_highlights}</div>""", unsafe_allow_html=True)




def clear_state():
    st.session_state.marked_text = None
    st.session_state.global_feedback = None
    st.session_state.display_result = False


col1, col2 = st.columns(2)

with col1:
    if st.button(
        label="Back",
        key=None,
        help="Click to go back.",
        on_click=None,
        args=None,
        kwargs=None,
        type="secondary",  
        icon=None,
        disabled=False,
        use_container_width=False
    ):
        clear_state()
        st.rerun()



with col2:
    if st.button(
        label="Analyze",  
        key=None,
        help="Click to analyze your data.",
        on_click=None,
        args=None,
        kwargs=None,
        type="primary",  
        icon=None,
        disabled=False,
        use_container_width=False
    ):
        st.session_state.user_text = user_text
        marked_text, global_feedback = analyze(user_text)
        st.session_state.marked_text = marked_text
        st.session_state.global_feedback = global_feedback
        st.session_state.display_result = True

        st.rerun()

        # js = '''<script>
        #     highlighted_elements = window.parent.document.getElementsByClassName("highlighted");
        #     console.log(highlighted_elements);
        #     highlighted_elements.forEach(function (element) {
        #         element.addEventListener("click", (event) => {
        #             //error_box = window.parent.document.getElementById("loader-block"); 
        #             //error_box.style.display = "none";
        #             console.log('hello1');
        #         });
        #     });
        # </script>
        # '''
        js = '''<script>
        close_btn = window.parent.document.getElementById("highlighted-0").addEventListener("click", () => {
            error_box = window.parent.document.getElementById("loader-block"); 
            error_box.style.display = "none";
            });
        </script>
        '''
        st.markdown(f'''{js}''',
            unsafe_allow_html=True
        )


if st.session_state.display_result:
    # Show global feedback
    st.write(st.session_state.global_feedback)


#user_text = 'Hello\n:red[World!]\n'

#user_text = 'Hello<br/><strong>World!</strong></br>'

# bootstrap 4 collapse example
# components.html(
#     f"""
# <!-- Include stylesheet -->
# <link href="https://cdn.jsdelivr.net/npm/quill@2.0.2/dist/quill.snow.css" rel="stylesheet" />

# <!-- Create the editor container -->
# <div id="editor">
# </div>

# <!-- Include the Quill library -->
# <script src="https://cdn.jsdelivr.net/npm/quill@2.0.2/dist/quill.js"></script>

# <!-- Initialize Quill editor -->
# <script>
#   const quill = new Quill('#editor', {
#     "{theme: 'snow'}"
#   });
#   quill.setText({user_text});
#   quill.formatText(0, 5, 'bold', true);
# </script>
#     """,
#     height=600,
# )

#st.markdown(user_text)

#st.html(f"""<p>{user_text}</p>""")
