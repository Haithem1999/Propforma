import streamlit as st

def main():
    st.set_page_config(page_title="Propforma: Property Valuation Tool", page_icon="🏡", layout="wide")
    
    # Custom CSS to center the widget
    st.markdown(
        """
        <style>
            .stApp {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            iframe {
                border: none;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("🏡 Propforma: Property Valuation Tool")

    # Inject custom HTML/JS for ElevenLabs Convai widget
    st.components.v1.html("""
    <elevenlabs-convai agent-id="VRygiWvgYxYK1ivGdfMH"></elevenlabs-convai>
    <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
    """, height=600)
    # Embedding the ElevenLabs ConvAI Widget
    st.markdown(
        '''
        <elevenlabs-convai agent-id="VRygiWvgYxYK1ivGdfMH"></elevenlabs-convai>
        <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
        ''',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
