# DocuMind AI — Smart Document Analysis & Data Toolkit

DocuMind AI is an AI-powered Streamlit application that helps users upload documents, extract useful information, generate summaries, ask questions about their files, and organize student records.

## 🚀 Features

- 📁 Upload PDF, TXT, PNG, and JPG/JPEG files
- 🤖 AI-powered document summarization
- 💬 Ask questions about uploaded documents
- 🔎 Extract text from images using OCR
- 📑 Sort student records by branch
- 📥 Download sorted student records
- 🎨 Simple and interactive Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- PyPDF2
- PyMuPDF
- Tesseract OCR
- Pytesseract
- Pillow
- Pandas

## 🧠 AI Models

### Text Summarization

The project uses:

`Falconsai/text_summarization`

to generate concise summaries from extracted document text.

### Question Answering

The project uses:

`deepset/roberta-base-squad2`

to answer natural-language questions based on the uploaded document.

## 📂 Project Structure

```text
DocuMind-AI/
│
├── app.py
│
├── pages/
│   ├── 1_Upload_File.py
│   ├── 2_AI_Analysis.py
│   ├── 3_Ask_AI.py
│   └── 4_sort_(updated)data.py
│
├── requirements.txt
├── REPORT.md
└── README.md
