import streamlit as st
from transformers import pipeline
import pytesseract
from PIL import Image
import PyPDF2

st.title("🤖 AI-Powered Analysis")

def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = "\n".join(page.extract_text() for page in reader.pages)
    return text

def extract_text_from_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text

if "hf_summarizer" not in st.session_state:
    st.session_state.hf_summarizer = pipeline("summarization", model="Falconsai/text_summarization")

if not st.session_state.get("uploaded_file_name"):
    st.warning("Please upload a file on the Upload File page.")
else:
    content = ""
    file_path = "uploaded_file"
    if st.session_state.uploaded_file_name.endswith(".pdf"):
        content = extract_text_from_pdf(file_path)
    elif st.session_state.uploaded_file_name.endswith((".jpg", ".jpeg", ".png")):
        content = extract_text_from_image(file_path)
    elif st.session_state.uploaded_file_name.endswith(".txt"):
        content = open(file_path, "r").read()

    if content:
        st.session_state.file_text = content
        st.subheader("Original Content")
        st.text_area("File Content", content[:2000], height=300)

        st.subheader("Summary")
        summary = st.session_state.hf_summarizer(content[:1000])[0]["summary_text"]
        st.success(summary)
