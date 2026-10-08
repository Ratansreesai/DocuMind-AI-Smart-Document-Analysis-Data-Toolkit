import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page config
st.set_page_config(
    page_title="Easy Data Upload and Analysis",
    page_icon="📊",
    layout="wide"
)

# Load Lottie animation
def load_lottie_url(url):
    res = requests.get(url)
    if res.status_code != 200:
        return None
    return res.json()

lottie_welcome = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")

# Title
st.title("📊 Easy Data Upload and Analysis")

# Layout with two columns
col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("Welcome to Your Smart Data Toolkit 🎓")
    st.markdown("""
This app helps you:

✅ Upload and manage various files  
&nbsp;&nbsp;&nbsp;&nbsp;• PDF, TXT, CSV, JPG, PNG
 
✅ Generate **AI-powered summaries** from your documents  
✅ Ask **questions** to your files using intelligent Q&A  
✅ Instantly **sort student records** by any field

✅ Enjoy a smooth and fun experience with animations ✨

Use the **left sidebar** to navigate through the tools!
""")

with col2:
    st_lottie(lottie_welcome, height=320, key="welcome_anim", speed=1.1, loop=True)

# Footer (optional)
st.markdown("---")
st.markdown("👨‍💻 Built with ❤️ by Team 404 Not Found")
