import streamlit.components.v1 as components

def render_streamlit_app():
    components.iframe("https://kazahayan-summary-stats-monthly-release-counts-riulpf.streamlit.app", height=600, scrolling=True)

render_streamlit_app()
