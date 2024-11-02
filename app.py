import streamlit as st
import streamlit.components.v1 as components
from algorithm import analyze
from response_parser import map_marked_text_to_html, get_comments_as_html
from styles import custom_styles, USER_TEXT_INITIAL_HEIGHT, TEXT_WIDTH_WITH_DETAILS, COMMENT_WIDTH_WITH_DETAILS



# Set page configuration
st.set_page_config(
    page_title="Media Bias Tool",
    page_icon="📊",
    layout="wide",
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



# Initial values of some state variables
if "display_result" not in st.session_state:
    st.session_state.display_result = False
if "user_text" not in st.session_state:
    st.session_state.user_text = ""


# Add custom styling
for custom_style in custom_styles:
    st.write(
        f'''<style>{custom_style}</style>''',
        unsafe_allow_html=True
    )



#st.title("Text Bias Detector")

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
        placeholder="Type your article here...",
        disabled=False,
        label_visibility="visible"
    )
else:
    # Show the text with highlights
    html_with_highlights, all_problems = map_marked_text_to_html(st.session_state.marked_text)
    # TODO get comments
    comments_as_html = get_comments_as_html(["comment", "todo", "hello"])
    st.session_state.all_problems = all_problems

    st.write(f"""<div class='horizontal'><div class='text-with-results' id='text-with-results'>{html_with_highlights}</div><div class='comment-container' id='comment-container'>{comments_as_html}</div></div>""", unsafe_allow_html=True)

    js = '''<script>
        highlights = window.parent.document.getElementsByClassName("highlighted");
        for (let i = 0; i < highlights.length; i++) {
            let element = highlights[i];
            element.addEventListener("click", () => {
              console.log('hello');
              window.parent.document.getElementById("text-with-results").style.width = "''' + TEXT_WIDTH_WITH_DETAILS + '''";
              window.parent.document.getElementById("comment-container").style.width = "''' + COMMENT_WIDTH_WITH_DETAILS + '''";
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
    st.session_state.all_comments = None
    st.session_state.display_result = False


col1, col2, col3 = st.columns([1, 4, 1])

if st.session_state.display_result:
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
            
    with col3:
        if st.button(
            label="Publish",  
            key=None,
            help="Click to publish your text.",
            on_click=None,
            args=None,
            kwargs=None,
            type="primary",  
            icon=None,
            disabled=False,
            use_container_width=False
        ):
            st.write("Published")
        
    # Show global feedback
    st.write("### Global feedback")
    st.write(st.session_state.global_feedback)

    #To cancel later
    #show all individual comments
    st.write("### Breakdown of all possible bias")
    st.write(st.session_state.all_comments)

    #show the text
    st.write("### Text with separators")
    st.write(st.session_state.marked_text)

else:
    with col3:
    
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
                marked_text, global_feedback, all_comments = analyze(user_text)
                st.session_state.marked_text = marked_text
                st.session_state.global_feedback = global_feedback
                st.session_state.all_comments = all_comments
                st.session_state.display_result = True
        
                st.rerun()

    
    


