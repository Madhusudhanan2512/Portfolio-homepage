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
        "About Me",
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

            🌐 [LinkedIn](www.linkedin.com/in/s-madhusudhanan) | 🐍 [GitHub](https://github.com/Madhusudhanan2512)
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
                    🎥 <a href='https://drive.google.com/file/d/1Ok5vu05VKmtrG3h1lRAOW5BL-fvVH-ku/view?usp=sharing' target='_blank'>Video</a> | 💻 <a href='https://github.com/Madhusudhanan2512/Project---Time-Series-Analysis---Walmart-Store-Sales' target='_blank'>GitHub</a>
                </li><br>
                <li><strong>Sales Data Analysis</strong><br>
                    🎥 <a href='https://drive.google.com/file/d/1C106oSp60fnWf133dz47xEEt5rtirxRf/view?usp=sharing' target='_blank'>Video</a> | 💻 <a href='https://github.com/Madhusudhanan2512/Project--Sales-Data-Analysis' target='_blank'>GitHub</a>
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
    - The Web Pages may not load due to inactivity, it may go to sleep, since it has been hosted on free cloud platform, kindly wait for few seconds to refresh itself or refresh button will be shown in the middle of the page. I appreciate and respect your patience in this process, thank you.
    """)

elif sidebar_choice == "About Me":
    st.header("👤 About Me")

    st.write("""
    Outside of data science, I am a passionate fitness enthusiast and avid cyclist. I love exploring new trails and pushing my physical limits on two wheels—cycling has taught me the power of endurance, focus, and the value of steady progress over time. Fitness is not just a hobby for me, but a daily discipline that energizes me, keeps my mind sharp, and reminds me of the importance of consistency in achieving long-term goals.

    I am also deeply inspired by the mindset of the Indian Army Special Forces. Their unwavering discipline, mental resilience, and commitment to teamwork are values I strive to embody in both my personal and professional life. I believe these qualities translate directly to my work as a data scientist: attention to detail, the ability to tackle complex challenges under pressure, and the drive to deliver results for the team and the organization. I am excited to bring this disciplined, growth-oriented approach to your company, combining technical expertise with a strong mindset for continuous improvement and excellence.
    """)

# ---- VIRTUAL INTERNSHIPS (SIDEBAR) ----
elif sidebar_choice == "Virtual Internships":
    st.header("🎓 Virtual Internships")
    st.subheader("British Airways: Data Science Simulation")
    st.write(""" 
    - **Simulation:** Applied data science to real-world airline business challenges.
    - **Skills:** Data scraping, customer analytics, predictive modeling.

    **Project Overview:**
    - Completed a simulation focusing on how data science drives British Airways' success.
    - Scraped and analyzed customer review data to uncover key insights.
    - Built a predictive model to understand factors influencing buying behavior.
    """)
    st.markdown("[Open App](https://your-pwc-app-link)  <!-- Add target='_blank' in HTML if you wish -->", unsafe_allow_html=True)

    st.subheader("Cognizant Artificial Intelligence Job Simulation")
    st.write("""
    - **Simulation:** Applied AI and data science skills to real-world business challenges.
    - **Skills:** Exploratory data analysis, Python, model development, business communication.
   
    **Project Overview:**
    - Completed a job simulation focused on AI for Cognizant’s Data Science team.
    - Conducted exploratory data analysis using Python and Google Colab for one of Cognizant’s technology-led clients, Gala Groceries.
    - Prepared a Python module with code to train a model and output performance metrics for the Machine Learning engineering team.
    - Communicated findings and analysis in a PowerPoint slide to present results to the business.
    """)
    st.markdown("[Open App](https://your-pwc-app-link)  <!-- Add target='_blank' in HTML if you wish -->", unsafe_allow_html=True)

    st.subheader("BCG Data Science Job Simulation")
    st.write(""" 
    -**Skills:** Business Understanding, Client Communication, Hypothesis Framing, Data Visualization.

    **Project Overview:**
    - Completed a customer churn analysis simulation for XYZ Analytics, demonstrating advanced data analytics skills, identifying essential client data and outlining a strategic investigation approach.
    - Conducted efficient data analysis using Python, including Pandas and NumPy. Employed data visualization techniques for insightful trend interpretation.
    - Completed the engineering and optimization of a random forest model, achieving an 85% accuracy rate in predicting customer churn.
    - Completed a concise executive summary for the Associate Director, delivering actionable insights for informed decision-making based on the analysis.
    """)
    st.markdown("[Open App](https://your-pwc-app-link)  <!-- Add target='_blank' in HTML if you wish -->", unsafe_allow_html=True)

    st.subheader("Standard Bank Data Science Simulation")
    st.write(""" 
    
    **Project Overview:** 
    - Developed a machine learning solution to automate and improve home loan approval predictions for financial institutions.
    - Performed thorough data analysis and preprocessing on a dataset of 614 loan applications, focusing on key factors such as income and education.
    - Implemented and compared three algorithms: Logistic Regression, Decision Tree, and Random Forest—finding Random Forest achieved the highest accuracy (80%).
    - Discovered that higher income, higher loan amounts, and being a graduate all positively influenced loan approval rates.
    - Demonstrated how machine learning can streamline decision-making in banking, with future improvements possible using advanced models.
    """)
    st.markdown("[Open App](https://your-pwc-app-link)  <!-- Add target='_blank' in HTML if you wish -->", unsafe_allow_html=True)
   
    st.subheader("PwC Switzerland – Power BI Simulation")
    st.write("""
    - **Simulation:** Real-world business dashboarding with Power BI.
    - **Skills:** Data visualization, business analytics, KPIs.
   
    **Project Overview:**
    - Enhanced PowerBI skills to better understand client data visualization needs.
    - Built effective dashboards to communicate key business metrics and respond to client requests with tailored solutions.
    - Demonstrated strong communication skills through clear, insightful emails to engagement partners, delivering actionable analysis.
    - Applied analytical problem-solving to HR data, focusing on gender-related KPIs and identifying root causes of gender balance issues at the executive level.
    - Demonstrated a commitment to data-driven decision-making and delivering value through analytics.
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
    
    **Business Impact:** 
    - Enabled more accurate sales forecasts, allowing Walmart to optimize inventory levels and reduce stockouts or overstock situations.
    - Improved demand planning, resulting in better allocation of resources across stores and regions.
    - Supported data-driven promotional strategies by identifying seasonality and sales trends, helping maximize revenue during peak periods.
    - Enhanced financial planning and budgeting accuracy by providing reliable sales projections for upcoming weeks or months.
    - Strengthened Walmart’s ability to respond proactively to market changes, leading to increased customer satisfaction and operational efficiency.
    """)
    st.markdown("[Open App](https://walmartdataapp-ulq7w4tgibmcamvewukffs.streamlit.app)", unsafe_allow_html=True)

    st.subheader("Sales Data Analysis")
    st.write("""
    - **Problem:** Uncover daily/weekly sales trends and key drivers.
    - **Skills:** Data visualization, hypothesis testing, customer segmentation.

    **Business Impact:**
    - Enabled data-driven decision-making by revealing sudden shifts in sales trends, helping management quickly adapt strategies to maximize revenue.
    - Improved marketing and promotional planning by identifying the exact timing of significant sales changes and understanding underlying drivers.
    - Enhanced customer segmentation and targeting through insights into gender-based purchasing patterns, supporting more effective, personalized campaigns.
    - Optimized resource allocation and staffing by quantifying sales distribution across different times of day, ensuring key periods are adequately supported.
    - Increased organizational agility and competitiveness by validating significant changes with robust statistical analysis, reducing reliance on guesswork.
    """)
    st.markdown("[Open App](https://salesdataapp-dixwrjkw82anbschuns9q7.streamlit.app)", unsafe_allow_html=True)

    st.subheader("Flight Booking Price Prediction")
    st.write("""
    
    **Problem:** 
    - Analyze a large dataset of 300,000+ flight bookings obtained from a popular airline booking platform. 
    - Understand the factors affecting flight ticket prices.
    - Apply various machine learning models to predict prices.

    **Business Impact:** 
    - Empowered the airline to set dynamic, data-driven ticket prices, maximizing revenue and market competitiveness.
    - Enhanced customer satisfaction and trust by providing more accurate, transparent fare predictions, reducing price uncertainty for travelers.
    - Informed marketing and promotional strategies by identifying the key factors (e.g., days left, stops, flight class) that most influence ticket prices.
    - Enabled smarter inventory and capacity planning by forecasting demand based on predicted pricing trends.
    - Supported better financial planning and decision-making by delivering reliable, automated ticket price forecasts, ultimately driving profitability.
    """)
    st.markdown("[Open App](https://flight-booking-app-tpayz3od5luydekqrvs9ep.streamlit.app)", unsafe_allow_html=True)

    st.subheader("Employee Turnover Prediction")
    st.write("""

    **Problem:** 
    - The Human Resources department is experiencing high attrition rates, resulting in increased recruitment costs and organizational instability.
    - Analyze historical employee data to predict attrition.
    - Identify key drivers behind employee resignation.

    **Business Impact:** 
    - Enabled HR teams to proactively identify employees at risk of leaving, allowing for targeted retention strategies and reduced turnover costs.
    - Reduced recruitment and training expenses by improving retention and minimizing the loss of valuable talent.
    - Provided actionable insights on key drivers of attrition (such as overtime, lack of promotion, and tenure), supporting data-driven policy and workplace improvements.
    - Improved workforce stability and morale by addressing the root causes of attrition before they become critical.
    - Enhanced decision-making for HR and management through interpretable, accurate predictive models, resulting in a more engaged and productive workforce.
    """)
    st.markdown("[Open App](https://employeeattritionapp-3zgfeh2hz8nhwsbptjyeet.streamlit.app)", unsafe_allow_html=True)

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
