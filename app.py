import streamlit as st

st.set_page_config(
    page_title="ElevenLabs AI Voice Agent Demo",
    layout="centered"  # This ensures centered layout
)

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
            min-height: 80vh;
            margin: auto;
            max-width: 800px;  /* Limit maximum width for better appearance */
        }
        .main {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

# Create columns to help with centering
col1, col2, col3 = st.columns([1,3,1])

with col2:
    st.title("ElevenLabs AI Voice Agent Demo")
    
    # Inject custom HTML/JS for ElevenLabs Convai widget
    st.components.v1.html("""
        <div class="widget-container">
            <elevenlabs-convai agent-id="VRygiWvgYxYK1ivGdfMH"></elevenlabs-convai>
            <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
        </div>
    """, height=600)
