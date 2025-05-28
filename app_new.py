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

# ====== CUSTOM SIDEBAR ======
sidebar_choice = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Important Info About This App",
        "Virtual Internships",
        "Completed Projects",
        "Ongoing Projects"
    ]
)

# ====== SIDEBAR PROJECT APP LINKS & SHORT DESCRIPTIONS ======
if sidebar_choice == "Home":
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
    st.markdown("""
    <div style="text-align:center; margin-bottom: 1em; margin-top: 0.5em;">
        <span style="font-size:22px; color:#0A66C2; font-style: italic;">
            “Data science isn’t the privilege of a select few—it’s an opportunity for anyone willing to learn, explore, and create.”
        </span>
        <br>
        <span style="font-size:16px; color:#444;">— Madhusudhanan</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Homepage note for navigation clarity
    st.info("""
    **How to use this portfolio:**
    - For a **detailed project dashboard (EDA, interactive app, business impact)**, use the sidebar and click on the “App” link for each project 
      (opens in a new tab).
    - For a **quick review and links to video/code**, use the sections below!
    """)

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

    # ----- 3 MAIN SECTIONS (ONLY VIDEO & GITHUB LINKS) -----
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="background-color:rgba(255,255,255,0.8); padding:15px; border-radius:10px;">
            <h4 style="color:#0A66C2;">🎓 Virtual Internships</h4>
            <ul style="list-style-type:none; padding-left:0;">
                <li><strong>PwC Switzerland – Power BI Simulation</strong><br>
                    🎥 <a href='#' target='_blank'>Video</a> | 💻 <a href='#' target='_blank'>GitHub</a>
                </li><br>
                <li><strong>British Airways – Data Science Simulation</strong><br>
                    🎥 <a href='#' target='_blank'>Video</a> | 💻 <a href='#' target='_blank'>GitHub</a>
                </li><br>
                <li><strong>Cognizant – AI Job Simulation</strong><br>
                    🎥 <a href='#' target='_blank'>Video</a> | 💻 <a href='#' target='_blank'>GitHub</a>
                </li><br>
                <li><strong>Standard Bank – Data Science Simulation</strong><br>
                    🎥 <a href='#' target='_blank'>Video</a> | 💻 <a href='#' target='_blank'>GitHub</a>
                </li><br>
                <li><strong>BCG – Data Science Simulation</strong><br>
                    🎥 <a href='#' target='_blank'>Video</a> | 💻 <a href='#' target='_blank'>GitHub</a>
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
                    🎥 <a href='#' target='_blank'>Video</a> | 💻 <a href='#' target='_blank'>GitHub</a>
                </li><br>
                <li><strong>Sales Data Analysis</strong><br>
                    🎥 <a href='#' target='_blank'>Video</a> | 💻 <a href='#' target='_blank'>GitHub</a>
                </li><br>
                <li><strong>Flight Price Prediction (Regression)</strong><br>
                    🎥 <a href='#' target='_blank'>Video</a> | 💻 <a href='#' target='_blank'>GitHub</a>
                </li><br>
                <li><strong>Predicting Employee Attrition</strong><br>
                    🎥 <a href='#' target='_blank'>Video</a> | 💻 <a href='#' target='_blank'>GitHub</a>
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
                    🎥 <a href='#' target='_blank'>Video</a> | 💻 <a href='#' target='_blank'>GitHub</a>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("© 2025 Madhusudhanan | Built with ❤️ using Streamlit")
    st.markdown("Top Image was created by rawpixel.com from freepick.com")

# ---- IMPORTANT INFO PAGE ----
elif sidebar_choice == "Important Info About This App":
    st.header("ℹ️ Important Info About This App")
    st.write("""
    - This interactive portfolio showcases my top data science, analytics, and AI projects.
    - For a **quick overview**, see the homepage sections.
    - For a **detailed dashboard, EDA, and business insights**, please use the “App” links for each project in the sidebar sections.  
    - Designed for recruiters, hiring managers, and data science professionals.
    """)

# ---- VIRTUAL INTERNSHIPS (SIDEBAR) ----
elif sidebar_choice == "Virtual Internships":
    st.header("🎓 Virtual Internships")
    st.subheader("PwC Switzerland – Power BI Simulation")
    st.write("""
    - **Simulation:** Real-world business dashboarding with Power BI.
    - **Skills:** Data visualization, business analytics, KPIs.
    """)
    st.markdown("[Open App](https://your-pwc-app-link)  <!-- Add target='_blank' in HTML if you wish -->", unsafe_allow_html=True)
    # ...Repeat for each internship

# ---- COMPLETED PROJECTS (SIDEBAR) ----
elif sidebar_choice == "Completed Projects":
    st.header("✅ Completed Projects")
    st.subheader("Time Series Analysis – Walmart Sales")
    st.write("""
    - **Problem:** Forecast weekly sales for Walmart stores.
    - **Skills:** Time series analysis, ARIMA/Prophet, EDA, data cleaning.
    - **Business Impact:** Inventory optimization.
    """)
    st.markdown("[Open App](https://your-walmart-app-link)", unsafe_allow_html=True)

    st.subheader("Sales Data Analysis")
    st.write("""
    - **Problem:** Uncover daily/weekly sales trends and key drivers.
    - **Skills:** Data visualization, hypothesis testing, customer segmentation.
    """)
    st.markdown("[Open App](https://your-sales-app-link)", unsafe_allow_html=True)

    # ...Repeat for each completed project

# ---- ONGOING PROJECTS (SIDEBAR) ----
elif sidebar_choice == "Ongoing Projects":
    st.header("🔄 Ongoing Projects")
    st.subheader("Resume Feedback Generator")
    st.write("""
    - **Problem:** Give actionable feedback on resumes using AI/NLP.
    - **Skills:** NLP, text analysis, machine learning.
    """)
    st.markdown("[Open App](https://your-resume-app-link)", unsafe_allow_html=True)

# --- Comments Section ----
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from datetime import datetime

SHEET_NAME = 'Portfolio Comments'  
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
SERVICE_ACCOUNT_FILE = 'gcp_service_account.json'

@st.cache_resource
def get_gspread_client():
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    client = gspread.authorize(creds)
    return client

gc = get_gspread_client()
sheet = gc.open(SHEET_NAME).sheet1

def fetch_comments():
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def add_comment(name, comment):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, name if name else "Anonymous", comment])

st.subheader("💬 Comments & Suggestions")

with st.form("comments_form", clear_on_submit=True):
    name = st.text_input("Name (optional):")
    comment = st.text_area("Your comment or suggestion:")
    submitted = st.form_submit_button("Submit")
    if submitted and comment.strip():
        add_comment(name, comment)
        st.success("Thank you for your comment!")

comments_df = fetch_comments()
if not comments_df.empty:
    st.write("### Previous Comments:")
    for _, row in comments_df[::-1].iterrows():
        st.markdown(f"- **{row['name']}** ({row['timestamp']}):<br> {row['comment']}", unsafe_allow_html=True)
else:
    st.info("No comments yet—be the first to leave feedback!")


