pip install streamlit gtts googletrans==4.0.0-rc1
import streamlit as st
from gtts import gTTS
from googletrans import Translator
import os

# Initialize Translator
translator = Translator()

# Streamlit app title
st.title("English to Urdu Translator and Pronunciation")

# Input text box for the word
word = st.text_input("Enter an English word to translate and pronounce:")

# Check if a word was entered
if word:
    # Translate word to Urdu
    translation = translator.translate(word, dest='ur').text
    st.write(f"**English Word:** {word}")
    st.write(f"**Urdu Translation:** {translation}")

    # Generate the pronunciation
    if st.button("Pronounce English Word"):
        tts = gTTS(text=word, lang='en')
        tts.save("word.mp3")
        # Display audio player
        audio_file = open("word.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

# Note for Streamlit deployment
st.write("This app translates English words to Urdu and plays their pronunciation.")
