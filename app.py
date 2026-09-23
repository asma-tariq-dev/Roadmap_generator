%%writefile AI-Roadmap-Generator/app.py

import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()


# Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


MODEL = "openai/gpt-oss-120b"


# Streamlit Configuration
st.set_page_config(
    page_title="AI Roadmap Generator",
    page_icon="🚀",
    layout="wide"
)


# Session Memory
if "history" not in st.session_state:
    st.session_state.history = []


# App Title
st.title("🚀 AI Roadmap Generator")

st.write(
"""
Generate a personalized learning roadmap using Generative AI.

Tell AI your goal, current skills, and learning preferences.
"""
)



# Sidebar Inputs

st.sidebar.header("🎯 Your Learning Profile")


goal = st.sidebar.text_input(
    "Your Goal",
    placeholder="Example: Become AI Engineer"
)


level = st.sidebar.selectbox(
    "Current Skill Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)


skills = st.sidebar.text_area(
    "Existing Skills / Prerequisites",
    placeholder="Example: Python basics, programming fundamentals"
)


duration = st.sidebar.selectbox(
    "Learning Duration",
    [
        "1 Month",
        "3 Months",
        "6 Months",
        "12 Months"
    ]
)


daily_time = st.sidebar.selectbox(
    "Daily Study Time",
    [
        "1 hour",
        "2 hours",
        "4 hours",
        "6+ hours"
    ]
)


style = st.sidebar.selectbox(
    "Learning Style",
    [
        "Project Based",
        "Theory + Projects",
        "Interview Preparation",
        "Fast Track"
    ]
)



# AI Roadmap Generator Function

def generate_roadmap(
        goal,
        level,
        skills,
        duration,
        daily_time,
        style
):

    prompt = f"""

You are a senior AI career mentor.

Create a personalized learning roadmap.

User Goal:
{goal}

Current Skill Level:
{level}

Existing Skills:
{skills}

Available Study Time:
{daily_time}

Duration:
{duration}

Learning Style:
{style}


Rules:

Create a professional roadmap.

Include:

1. Roadmap Overview

2. Month-wise learning plan


For every month include:

- Learning Goals
- Topics
- Subtopics
- Practical Projects
- Practice Tasks
- Resources
- Expected Outcome


Consider user's existing skills.

Do not create unrealistic plans.

Use clean Markdown formatting.

Do not use tables.


"""


    response = client.chat.completions.create(

        model=MODEL,

        messages=[

            {
                "role": "system",
                "content":
                "You are an expert learning roadmap architect."
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        temperature=0.7
    )


    return response.choices[0].message.content




# Generate Button

if st.button("🚀 Generate Roadmap"):


    if not goal:

        st.warning(
            "Please enter your goal first."
        )


    else:

        with st.spinner(
            "Creating your personalized roadmap..."
        ):


            roadmap = generate_roadmap(
                goal,
                level,
                skills,
                duration,
                daily_time,
                style
            )


            # Save Memory

            st.session_state.history.append(

                {
                    "goal": goal,
                    "roadmap": roadmap
                }

            )


            st.success(
                "Roadmap Generated Successfully 🎉"
            )


            st.markdown(
                roadmap
            )


            st.download_button(

                "📥 Download Roadmap",

                roadmap,

                file_name="AI_Roadmap.md"

            )




# Previous Roadmaps Memory

if st.session_state.history:


    st.divider()


    st.subheader(
        "🧠 Previous Roadmaps"
    )


    for item in reversed(
        st.session_state.history
    ):


        with st.expander(
            item["goal"]
        ):


            st.markdown(
                item["roadmap"]
            )
