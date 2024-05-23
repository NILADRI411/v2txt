import streamlit as st
import speech_recognition as sr

def speech_to_text():
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        st.write("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Capture the audio input from the user
        audio = recognizer.listen(source)

    st.write("Processing...")

    try:
        # Use the recognizer to convert speech to text
        text = recognizer.recognize_google(audio)
        st.write("Text:", text)
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        st.write("Sorry, an error occurred. Please try again later.")


def main():
    st.title("Speech to Text")

    # Call the speech_to_text function when the button is clicked
    if st.button("Start Recording"):
        speech_to_text()

if __name__ == "__main__":
    main()
