from groq import Groq
import os


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_roadmap(
    goal,
    level,
    skills,
    duration,
    daily_time,
    style
):

    prompt = f"""
You are an expert career mentor and learning coach.

Your task is to create a personalized career roadmap for the user.

Career Goal:
{goal}

Current Skill Level:
{level}

Existing Skills:
{skills}

Available Learning Duration:
{duration}

Daily Learning Time:
{daily_time}

Preferred Learning Style:
{style}


IMPORTANT INSTRUCTIONS:

- Write for a beginner-friendly audience.
- Do not write like a research paper.
- Avoid unnecessary complex terminology.
- Make the roadmap practical and achievable.
- Guide the user step-by-step from beginner to job-ready.
- Use simple language.
- Use emojis and clear headings.
- Make the response motivating and easy to follow.

Generate the roadmap using this structure:


# 🚀 Career Overview

Explain:
- What this career is
- What professionals do
- Why this career is valuable


# 🧠 Skills Required

List:

Technical Skills:
- Programming languages (if required)
- Tools
- Frameworks
- Platforms

Soft Skills:
- Communication
- Problem solving
- Teamwork


# 🗺️ Learning Roadmap

Create a step-by-step roadmap.

For each phase include:

## Phase Name

Duration:

Learn:
✅ Skill 1
✅ Skill 2
✅ Skill 3

Tools:
- Tool names

Practice:
- What the learner should do


# 💻 Career-Specific Projects

Suggest projects according to this career.

Divide them into:


Beginner Projects:
- Easy projects to build foundation


Intermediate Projects:
- Real-world practical projects


Advanced Projects:
- Portfolio-level projects


For technology careers:
Include suitable technologies, programming languages,
frameworks, databases, APIs, and deployment tools.

For non-technical careers:
Include suitable tools, platforms,
certifications, and practical experience ideas.


# 📚 Recommended Resources

Suggest:

Free Courses:
- Course names/platforms

Documentation:
- Official websites

Practice Platforms:
- Websites for practice


# 🎯 Job Preparation Strategy

Include:

- Resume building
- Portfolio/GitHub (if relevant)
- Interview preparation
- Networking tips
- Internship/job search strategy


# 🌱 Future Career Growth

Explain:

- Advanced roles
- Career progression
- Long-term opportunities


Remember:
The final answer should feel like a personal career mentor guiding the user.
Make it clear, practical, encouraging, and actionable.

"""


    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=4000
    )


    return response.choices[0].message.content
