import streamlit as st

st.set_page_config(
    page_title="ElevenLabs AI Voice Agent Demo",
    layout="centered",  # This ensures centered layout
    initial_sidebar_state="collapsed"  # Hide sidebar by default
)

# Add custom CSS to center the widget and position it right below title
st.markdown("""
    <style>
        .stApp {
            max-width: 100%;
            padding: 0;
        }
        .widget-container {
            display: flex;
            justify-content: center;
            align-items: flex-start;  /* Changed to flex-start to position right below title */
            margin: 20px auto;  /* Reduced margin to bring widget up */
            max-width: 800px;
        }
        .main {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        /* Reduce padding/margins of title */
        .stTitle {
            margin-bottom: 0 !important;
            padding-bottom: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("ElevenLabs AI Voice Agent Demo")

# Inject custom HTML/JS for ElevenLabs Convai widget
st.components.v1.html("""
    <div class="widget-container">
        <elevenlabs-convai agent-id="VRygiWvgYxYK1ivGdfMH"></elevenlabs-convai>
        <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
    </div>
""", height=600)
