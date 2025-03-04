import streamlit as st

st.set_page_config(page_title="ElevenLabs AI Voice Agent Demo")

st.title("ElevenLabs AI Voice Agent Demo")

# Inject custom HTML/JS for ElevenLabs Convai widget
st.components.v1.html("""
    <elevenlabs-convai agent-id="VRygiWvgYxYK1ivGdfMH"></elevenlabs-convai>
    <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
""", height=600)
