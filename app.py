# app.py
import streamlit as st
from inference import summarize

st.set_page_config(page_title="LoRA T5 Summarizer", layout="centered")

st.title("📰 Text Summarizer using LoRA + T5")
st.markdown("Enter an article or paragraph below and get a concise summary.")

text_input = st.text_area("Enter the text to summarize:", height=300)

if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Generating summary..."):
            summary = summarize(text_input)
        st.subheader("Summary:")
        st.success(summary)
