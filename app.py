import streamlit as st
from audio_recorder_streamlit import audio_recorder
import base64
import time
 
 
def autoplay_audio(data):
    # with open(file_path, "rb") as f:
    #     data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
<audio controls autoplay="true">
<source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
</audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )
 
for i in range(0, 2):
    audio_bytes = audio_recorder(
        key=f"audio_recorder_{i}",
        text="Start Length",
        recording_color="#e8b62c",
        neutral_color="#6aa36f",
        icon_name="user",
        icon_size="6x",
        energy_threshold=(-1.0, 1.0),
        pause_threshold=3.0
    )
 
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        autoplay_audio(audio_bytes)
    audio_bytes=None
