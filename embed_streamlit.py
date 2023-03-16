import streamlit as st
import streamlit.components.v1 as components

# Define function to render the embedded Streamlit app
def render_streamlit_app():
    components.iframe("https://kazahayan-summary-stats-monthly-release-counts-riulpf.streamlit.app/", height=600, scrolling=True)

# Call the function to render the embedded Streamlit app
render_streamlit_app()
