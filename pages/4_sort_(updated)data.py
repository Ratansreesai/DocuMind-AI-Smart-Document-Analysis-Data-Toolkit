import streamlit as st
import fitz  # PyMuPDF

def extract_text(file):
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = "\n".join([page.get_text() for page in doc])
        return text
    except Exception as e:
        st.error(f"Failed to read PDF: {e}")
        return ""

def parse_records_from_blocks(text):
    lines = [line.strip() for line in text.strip().split("\n") if line.strip()]
    
    # Remove any header/footer junk lines
    valid_lines = []
    skip_keywords = ["student", "data", "report", "name", "enrollment", "branch", "series"]
    for line in lines:
        if not any(kw in line.lower() for kw in skip_keywords):
            valid_lines.append(line)

    records = []
    i = 0
    while i + 3 < len(valid_lines):
        name = valid_lines[i]
        enrollment = valid_lines[i + 1]
        branch = valid_lines[i + 2]
        series = valid_lines[i + 3]
        records.append((name, enrollment, branch, series))
        i += 4
    return records

def is_sorted_by_branch(records):
    branches = [r[2] for r in records]
    return branches == sorted(branches)

def format_records_horizontal(records):
    return "\n".join([f"{name:<20} {enr:<20} {branch:<20} {series}" for name, enr, branch, series in records])

st.title("📑 Sort Student Records by Branch")

file = st.file_uploader("Upload your student PDF (Name → Enrollment → Branch → Series)", type=["pdf"])

if file:
    raw_text = extract_text(file)

    # show debug if you want
    # st.subheader("🔍 Raw Extracted Text")
    # st.code(raw_text)

    records = parse_records_from_blocks(raw_text)

    if not records:
        st.warning("No valid student records found.")
    else:
        st.subheader("📋 Preview (First 5 Records)")
        st.text(format_records_horizontal(records[:5]))

        if is_sorted_by_branch(records):
            st.success("✅ Already sorted by branch.")
            final_output = format_records_horizontal(records)
        else:
            st.success("✅ Sorted now by branch.")
            sorted_records = sorted(records, key=lambda x: x[2])
            final_output = format_records_horizontal(sorted_records)

        st.subheader("📌 Final Output")
        st.text(final_output)

        st.download_button("📥 Download Sorted File", final_output, file_name="sorted_students.txt")
else:
    st.info("Please upload a student PDF file.")