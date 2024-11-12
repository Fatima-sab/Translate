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

# Use Streamlit caching to optimize translations
@st.cache
def get_translation(word):
    return translator.translate(word, dest='ur').text

@st.cache
def get_pronunciation(word):
    tts = gTTS(text=word, lang='en')
    tts.save("word.mp3")
    return "word.mp3"

# Check if a word was entered
if word:
    # Translate word to Urdu (cached)
    translation = get_translation(word)
    st.write(f"**English Word:** {word}")
    st.write(f"**Urdu Translation:** {translation}")

    # Generate and play the pronunciation
    if st.button("Pronounce English Word"):
        pronunciation_file = get_pronunciation(word)  # Cached
        # Display audio player
        audio_file = open(pronunciation_file, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

# Note for Streamlit deployment
st.write("This app translates English words to Urdu and plays their pronunciation.")
