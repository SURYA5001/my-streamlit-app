import streamlit as st
from google import genai  # Use the new import
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the new Client
# It will look for GOOGLE_API_KEY in your environment variables automatically
client = genai.Client(api_key="AIzaSyCSw7CyPXktpfoEF8-NhfKnPrsiQDglsWM")

def translate_text(text, source, target):
    # Use the latest stable model: 'gemini-2.0-flash' or 'gemini-2.5-flash'
    model_id = "gemini-2.0-flash" 
    
    prompt = f"Translate from {source} to {target}: {text}"
    
    response = client.models.generate_content(
        model=model_id,
        contents=prompt
    )
    return response.text

# 3. Streamlit UI
def main():
    st.set_page_config(page_title="AI Powered Language Translator", page_icon="🌍")
    st.header("🌍 AI-Powered Language Translator")

    # User inputs
    text = st.text_area("Enter text to translate:")
    
    # Using columns for a cleaner layout
    col1, col2 = st.columns(2)
    with col1:
        source_language = st.selectbox("Select source language:", ["English", "Spanish", "French", "German", "Chinese"])
    with col2:
        target_language = st.selectbox("Select target language:", ["English", "Spanish", "French", "German", "Chinese"])

    # Translate button (Must be inside main or handle text variable correctly)
    if st.button("Translate"):
        if text.strip():
            try:
                with st.spinner("Translating..."):
                    translated_text = translate_text(text, source_language, target_language)
                st.subheader("Translated Text:")
                st.success(translated_text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter some text to translate.")

if __name__ == "__main__":
    main()
