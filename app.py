import streamlit as st

st.set_page_config(page_title="ElevenLabs AI Voice Agent Demo")

# Add custom CSS to center the widget
st.markdown("""
    <style>
        .stApp {
            max-width: 100%;
            padding: 0;
        }
        .widget-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
        }
    </style>
""", unsafe_allow_html=True)

st.title("ElevenLabs AI Voice Agent Demo")

# Inject custom HTML/JS for ElevenLabs Convai widget with centering
st.components.v1.html("""
    <div class="widget-container">
        <elevenlabs-convai agent-id="VRygiWvgYxYK1ivGdfMH"></elevenlabs-convai>
        <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
    </div>
""", height=600)
