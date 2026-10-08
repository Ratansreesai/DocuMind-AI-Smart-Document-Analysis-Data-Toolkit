# 1.Easy Data Upload and Analysis




## 1.1 Team Information

Team Name: 404 Not Found


### Team Members & Roles:


Name:-	Responsibility

Nagababu:-	App Overview & Homepage

Sujith:-	    Upload File Page

Ratan:-	    AI Analyzer

Pranathish:-	Ask AI

Dushyanth:-	Sort Shuffled Data


### Project Overview

Easy Data Upload and Analysis is a multi-page Streamlit web application that enables users to upload various types of files (PDF, TXT, JPG, PNG, CSV) and receive insights through AI-powered tools. The app is structured across five pages with individual functionalities, aimed at simplifying document interpretation and interaction.

### Individual Contributions:

->App Homepage (Nagababu)

Welcomes users with an intuitive layout.

Describes the app's purpose and guides users on navigation.


->Upload File (Sujith)

Supports uploading PDF, TXT, JPG, PNG.

Files are saved to the session state for downstream usage.

Visual feedback on successful uploads.


->AI Analyzer (Ratan)

Extracts text using:

PyPDF2 for PDF files

Tesseract OCR for images

Plain text extraction for .txt

Summarization is performed using Falconsai/text_summarization from Hugging Face.


->Ask AI (Pranathish)

Enables users to ask natural language questions about the uploaded document.

Uses deepset/roberta-base-squad2 from Hugging Face for Q&A.


->Sort Shuffled Data (Dushyanth)

Accepts shuffled datasets in CSV, TXT, or PDF format.

Sorts based on selected columns (CSV) or lexicographic line order (TXT/PDF).

Allows downloads of sorted results.

Provides previews for image files without sorting.


____

## 1.2 Application Overview

Application Name: Easy Data Upload and Analysis

### Use Case & Problem Solved:

Many users struggle to extract insights from raw files such as PDFs, scanned images, or unstructured text. This app solves that by combining a simple UI with AI to automatically summarize documents, answer user queries, and even sort messy data formats. It’s targeted at students, educators, and professionals who regularly interact with data/documents and need instant summarization, interpretation, or cleanup.

### Key Features:

->File upload (PDF, TXT, CSV, PNG, JPG)

->AI-powered text summarization

->Ask AI: Natural language Q&A interface

->Sort & download data from CSV/TXT/PDF

->Image text extraction (OCR)

### Motivation:

Our team recognized that many users, particularly those without technical expertise, struggle to extract meaningful insights from lengthy documents. To address this, we developed an intuitive AI-powered dashboard that simplifies document analysis, making it accessible to all users.

Students often face overwhelming amounts of study material, leading to stress and diminished confidence. Our solution condenses and summarizes extensive PDF documents into concise, digestible content, aiding students in efficient exam preparation.



____

## 1.3 AI Integration Details

### AI Models Used:

- *Summarization:* text_summarization


### How the AI Works:


1. *File Upload*: The user uploads a file (PDF, TXT, or Image).
2. *Text Extraction*:
   - PDFs use *PyPDF2*.
   - Images use *pytesseract* OCR.
   - TXT files are read directly.
3. *Text Summarization*:
   - The extracted text is sent to a pre-trained Hugging Face model (falconsai/text_summarization).
   - The model shortens the text, preserving the main idea.
4. *Question Answering (Q&A)*:
   - The context (extracted text) and the user’s query are formatted and sent to roberta-base-squad2.
   - The model returns the most likely answer span from the context.

-->Token Limit:
- Transformer models have a max input length (usually *512 tokens*).
- If the context exceeds 512 tokens, only the first part is used.
- Token = word or word-part, so even a sentence can be 10–20 tokens.
- We manage this by *trimming* or *chunking* the text as needed.


____

## 1.4 Technical Architecture & Development


### Technology Stack:

Python

Streamlit

Hugging Face Transformers

PyPDF2, pytesseract, PIL

Pandas

Git, Hugging Face Spaces

### Challenges & Solutions:

->OCR accuracy for low-quality scans

Solution: Added preprocessing using PIL to improve contrast

->Large file context truncation in summarizer/Q&A

Solution: Token limit handled with simple chunking; long-context models planned for future

->Testing AI output quality

Solution: Manual benchmarks and user feedback loop for evaluation

Open Source License:

License: MIT

Reason: Permissive license allowing open community use and contributions


____

## 1.5 Known Issues & Fixes (✅ All Resolved)

Our app initially had a few technical limitations across different modules, but each of them has now been successfully addressed. 🎯

### 1. Ask AI Inaccuracy (✅ Resolved)

Previous Issue: AI sometimes gave inaccurate or irrelevant answers from uploaded files.

Fix: Optimized input formatting and QA prompt handling. The model now answers most queries correctly with high relevance and accuracy.




### 2. Sorting Data (✅ Resolved)

Issue 1: Sorted only alphabetically, ignoring structured fields →
✅ Now supports full column-based sorting for all structured formats.

Issue 2: Merged fields with no space between them →
✅ Resolved by improving extraction and spacing logic.

Issue 3: “Minimum three records with enough lines required” error →
✅ Now correctly detects record structure and avoids false errors.

Issue 4: Didn't support all CSV formats →
✅ Now supports all valid CSV files across encoding types.




### 3. AI Analyzer (✅ Resolved)

Issue 1: Text appeared without spaces →
✅ Fixed by decoding and spacing cleanup.

Issue 2: Output lacked structured layout →
✅ Now displays in a clear, readable format.




### 4. CSV Upload Error (✅ Resolved)

Previous Issue: Uploading certain CSV files failed due to encoding or type mismatches.

Fix: Enhanced upload logic and pandas integration — all standard CSV formats now upload smoothly.


----

## 1.6 Future Roadmap & User Adoption Plan

### Roadmap:

->Phase 1 (Weeks 1–2):

Polish UI, fix minor bugs, add loading indicators

->Phase 2 (Weeks 3–4):

Add multi-answer Q&A (via retrieval-based method)

Allow simple chart generation from CSVs

->Phase 3 (Weeks 5–6):

Switch to long-context models for docs

Add speech-to-text support for audio files

Enable community pull requests and translation support

User Adoption Plan:

-->Target Audience:

Students, educators, research scholars, and non-tech users who work with PDFs/data

-->Value Proposition:

A no-code, AI-powered workspace to interpret and sort messy documents quickly and intuitively

-->Promotion Strategy:

-Post on Streamlit forum, Hugging Face Hub, GitHub Showcase

-Create short demo videos, LinkedIn post series

-Blog post explaining tech stack and design



### Hugging Face Hosting:
We deployed our project live on Hugging Face Spaces here:

🔗 **[Live App on Hugging Face](https://huggingface.co/spaces/Sratan/Easy-data-analysis)**



### Frictionless Onboarding:


The landing page includes usage instructions

Sample files provided for instant testing


### Feedback Loop:


Integrated Google Form & email link in app

GitHub Issues enabled for bugs/ideas
