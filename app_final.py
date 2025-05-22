
import streamlit as st
from PIL import Image
import base64

# ----- PAGE CONFIG -----
st.set_page_config(page_title="Madhusudhanan | Data Science Portfolio", page_icon="📊", layout="wide")

# ----- BACKGROUND IMAGE -----
def set_bg_image(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .css-18e3th9 {{
            background-color: rgba(255, 255, 255, 0.88) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_image("image3.jpg")

# ----- HEADER -----
st.markdown("""
    <style>
    .title {
        font-size: 42px;
        font-weight: bold;
        color: #0A66C2;
    }
    .subtitle {
        font-size: 20px;
        color: #4A4A4A;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Hi, I'm Madhusudhanan 👋</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Data Science Professional | Python Enthusiast | Machine Learning Explorer</div>", unsafe_allow_html=True)
st.markdown("---")

# ----- ABOUT ME -----
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("image.jpg", width=300)
    with col2:
        st.write("""
        I’m passionate about building data-driven solutions that create business value. 
        With hands-on experience in predictive modeling, EDA, and machine learning, I enjoy solving real-world problems 
        using Python, SQL, and Streamlit.

        🌐 [LinkedIn](https://www.linkedin.com/in/your-profile) | 🐍 [GitHub](https://github.com/yourusername)
        """)
        with open("resume.pdf", "rb") as f:
            st.download_button("📄 Download Resume", f, file_name="Madhusudhanan_Data_Scientist.pdf")

st.markdown("---")

# ----- 3 MAIN SECTIONS -----
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background-color:rgba(255,255,255,0.8); padding:15px; border-radius:10px;">
        <h4 style="color:#0A66C2;">🎓 Virtual Internships</h4>
        <ul style="list-style-type:none; padding-left:0;">
            <li><strong>PwC Switzerland – Power BI Simulation</strong><br>
                🔗 <a href='#'>App</a> | 🎥 <a href='#'>Video</a> | 💻 <a href='#'>GitHub</a>
            </li><br>
            <li><strong>British Airways – Data Science Simulation</strong><br>
                🔗 <a href='#'>App</a> | 🎥 <a href='#'>Video</a> | 💻 <a href='#'>GitHub</a>
            </li><br>
            <li><strong>Cognizant – AI Job Simulation</strong><br>
                🔗 <a href='#'>App</a> | 🎥 <a href='#'>Video</a> | 💻 <a href='#'>GitHub</a>
            </li><br>
            <li><strong>Standard Bank – Data Science Simulation</strong><br>
                🔗 <a href='#'>App</a> | 🎥 <a href='#'>Video</a> | 💻 <a href='#'>GitHub</a>
            </li><br>
            <li><strong>BCG – Data Science Simulation</strong><br>
                🔗 <a href='#'>App</a> | 🎥 <a href='#'>Video</a> | 💻 <a href='#'>GitHub</a>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color:rgba(255,255,255,0.8); padding:15px; border-radius:10px;">
        <h4 style="color:#0A66C2;">✅ Completed Projects</h4>
        <ul style="list-style-type:none; padding-left:0;">
            <li><strong>Time Series Analysis – Walmart Sales</strong><br>
                🔗 <a href='https://walmartdataapp-ulq7w4tgibmcamvewukffs.streamlit.app/'>App</a> | 🎥 <a href='#'>Video</a> | 💻 <a href='#'>GitHub</a>
            </li><br>
            <li><strong>Sales Data Analysis</strong><br>
                🔗 <a href='https://salesdataapp-dixwrjkw82anbschuns9q7.streamlit.app'>App</a> | 🎥 <a href='https://drive.google.com/file/d/1C106oSp60fnWf133dz47xEEt5rtirxRf/view?usp=sharing'>Video</a> | 💻 <a href='https://github.com/Madhusudhanan2512/Project--Sales-Data-Analysis'>GitHub</a>
            </li><br>
            <li><strong>Flight Price Prediction (Regression)</strong><br>
                🔗 <a href='#'>App</a> | 🎥 <a href='#'>Video</a> | 💻 <a href='#'>GitHub</a>
            </li><br>
            <li><strong>Predicting Employee Attrition</strong><br>
                🔗 <a href='#'>App</a> | 🎥 <a href='#'>Video</a> | 💻 <a href='#'>GitHub</a>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background-color:rgba(255,255,255,0.8); padding:15px; border-radius:10px;">
        <h4 style="color:#0A66C2;">🔄 Ongoing Projects</h4>
        <ul style="list-style-type:none; padding-left:0;">
            <li><strong>Resume Feedback Generator</strong><br>
                🔗 <a href='https://resume-feedback.streamlit.app' target='_blank'>App</a> |
                🎥 <a href='https://youtu.be/resume-video' target='_blank'>Video</a> |
                💻 <a href='https://github.com/yourusername/resume-feedback-generator' target='_blank'>GitHub</a>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ----- FOOTER -----
st.markdown("---")
st.markdown("© 2025 Madhusudhanan | Built with ❤️ using Streamlit")
st.markdown("Top Image was created by rawpixel.com from freepick.com")
