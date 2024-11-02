import streamlit as st
import streamlit.components.v1 as components

from algorithm import analyze
from parser import map_marked_text_to_html, get_comments_as_html

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
                "padding: 5px;" + 
                "margin: 5px;" +
                "}")
style_2 = """.highlighted {
                background-color: pink;
                cursor: pointer;
            }"""
style_3 = (".comment-container {" +
                "height: " +
                f"{USER_TEXT_INITIAL_HEIGHT}px;" + 
                "width: 30%;" + 
                "}")
style_4 = (".comment-container p {" +
                "border: 1px solid grey;" + 
                "border-radius: 5px;" + 
                "padding: 5px;" + 
                "margin: 5px;" +
                "display: none;" +
                "}")
style_5 = """.horizontal {
                display: flex;
                flex-direction: row;
                justify-content: flex-start;
            }"""

st.write(f'''<style>
            {style_1}
            {style_2}
            {style_3}
            {style_4}
            {style_5}
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
    comments_as_html = get_comments_as_html(["comment", "todo", "hello"])
    st.session_state.all_problems = all_problems
    st.write(f"""<div class='horizontal'><div class='text-with-results'>{html_with_highlights}</div><div class='comment-container'>{comments_as_html}</div></div>""", unsafe_allow_html=True)

    js = '''<script>
        highlights = window.parent.document.getElementsByClassName("highlighted");
        for (let i = 0; i < highlights.length; i++) {
            let element = highlights[i];
            element.addEventListener("click", () => {
              console.log('hello');
              for (let j = 0; j < highlights.length; j++) {
                let commentsDiv = window.parent.document.getElementById("comment-id-" + j);
                if (i === j) {
                    commentsDiv.style.display = 'block';
                } else {
                    commentsDiv.style.display = 'none';
                }
              }
            });
        }
        </script>
        '''
    components.html(f'''{js}''', height=0)




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
        # js = '''<script>
        # console.log('hello');
        # close_btn = window.parent.document.getElementById("highlighted-0").addEventListener("click", () => {
        #     error_box = window.parent.document.getElementById("highlighted-1"); 
        #     error_box.style.display = "none";
        #     });
        # </script>
        # '''
        # components.html(f'''{js}''')

        st.rerun()


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


