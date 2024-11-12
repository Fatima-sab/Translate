import streamlit as st
from gtts import gTTS
from googletrans import Translator
import tempfile
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
    try:
        tts = gTTS(text=word, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
            tts.save(tmp_file.name)
            return tmp_file.name
    except Exception as e:
        st.error(f"Error generating speech: {e}")
        return None

# Check if a word was entered
if word:
    # Translate word to Urdu (cached)
    translation = get_translation(word)
    st.write(f"**English Word:** {word}")
    st.write(f"**Urdu Translation:** {translation}")

    # Generate and play the pronunciation
    if st.button("Pronounce English Word"):
        pronunciation_file = get_pronunciation(word)  # Cached
        if pronunciation_file:
            # Display audio player
            st.audio(pronunciation_file)
            # Clean up temporary file after playing the audio
            os.remove(pronunciation_file)

# Note for Streamlit deployment
st.write("This app translates English words to Urdu and plays their pronunciation.")
