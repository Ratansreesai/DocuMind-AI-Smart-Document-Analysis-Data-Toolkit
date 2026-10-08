import streamlit as st

st.title("📁 Upload Your File")

st.write("Supported file types: PDF, TXT, PNG, JPG")

uploaded_file = st.file_uploader("Upload your file here", type=["pdf", "txt", "jpg", "jpeg", "png"])

if uploaded_file:
    with open("uploaded_file", "wb") as f:
        f.write(uploaded_file.read())
    st.session_state.uploaded_file_name = uploaded_file.name
    st.success(f"Uploaded: {uploaded_file.name}")
