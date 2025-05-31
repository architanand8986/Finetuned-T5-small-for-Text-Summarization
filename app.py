import streamlit as st
from inference import summarize

# Page settings
st.set_page_config(
    page_title="LoRA T5 Summarizer",
    page_icon="📰",
    layout="centered",
)

# Main Title
st.markdown("<h1 style='text-align: center;'>📰 LoRA-T5 Text Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Summarize any text efficiently using a fine-tuned T5-small model with LoRA.</p>", unsafe_allow_html=True)

# Spacer
st.markdown("### 📥 Input Text")
text_input = st.text_area(
    label="Paste your article or paragraph below:",
    placeholder="Type or paste content here...",
    height=300,
    label_visibility="collapsed"
)

# Optional: Customize summary length
with st.expander("⚙️ Optional Settings"):
    length_option = st.slider("Select desired summary length (approx.):", 30, 200, step=10, value=80)

# Button & Summary Output
if st.button("🔍 Summarize"):
    if not text_input.strip():
        st.warning("⚠️ Please enter some text first.")
    else:
        with st.spinner("Generating summary..."):
            summary = summarize(text_input)  # You can pass `length_option` to summarize if supported
        st.markdown("### 📝 Summary")
        st.success(summary)

# Footer
st.markdown("---")
st.caption("Built with 🤖 T5-small + LoRA | Powered by Streamlit")
