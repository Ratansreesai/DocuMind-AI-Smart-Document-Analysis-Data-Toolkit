import streamlit as st
from transformers import pipeline

st.title("💬 Ask the AI")

if "qa_pipeline" not in st.session_state:
    st.session_state.qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

if "file_text" not in st.session_state:
    st.warning("Please upload and analyze a file first.")
else:
    question = st.text_input("Ask a question about the document:")
    if question:
        answer = st.session_state.qa_pipeline({
            'context': st.session_state["file_text"],
            'question': question
        })
        st.write("Answer:")
        st.success(answer["answer"])
