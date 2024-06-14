import streamlit as st
import pyttsx3
import time
 
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # Change index to change voices
 
def ask_question(question):
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(question)
    engine.runAndWait()
    engine=None
    time.sleep(3)  # Wait for 3 seconds before asking the next question
 
def main():
    st.title("Questionnaire")
    st.write("Please answer the following questions:")
 
    questions = [
        "What is your name?",
        "What is your class?",
        "What is your roll number?"
    ]
 
    for q in questions:
        ask_question(q)
 
if __name__ == "__main__":
    main()
