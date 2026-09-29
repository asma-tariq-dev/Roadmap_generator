import streamlit as st
from groq import Groq
from utils.pdf_generator import create_pdf
import streamlit as st
from services.roadmap_service import generate_roadmap



st.set_page_config(
    page_title="AI Roadmap Generator",
    page_icon="🚀"
)



st.title(
    "🚀 AI Roadmap Generator"
)


st.write(
"Generate personalized learning roadmaps using AI."
)



goal = st.text_input(
    "🎯 Your Goal",
    "Become AI Engineer"
)


level = st.selectbox(
    "Skill Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)


skills = st.text_area(
    "Your Existing Skills"
)


duration = st.selectbox(
    "Duration",
    [
        "1 Month",
        "3 Months",
        "6 Months",
        "12 Months"
    ]
)


daily_time = st.selectbox(
    "Daily Study Time",
    [
        "1 hour",
        "2 hours",
        "4 hours"
    ]
)


style = st.selectbox(
    "Learning Style",
    [
        "Project Based",
        "Theory + Projects",
        "Interview Preparation"
    ]
)



if st.button(
    "Generate Roadmap 🚀"
):

    with st.spinner(
        "Creating your roadmap..."
    ):

        result = generate_roadmap(
            goal,
            level,
            skills,
            duration,
            daily_time,
            style
        )


        st.markdown(result)


        pdf_file = create_pdf(result)

        st.download_button(
            "📥 Download Roadmap PDF",
            pdf_file,
            "Career_Roadmap.pdf",
            "application/pdf"
        )
