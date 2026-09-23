%%writefile AI-Roadmap-Generator/utils/prompts.py


def roadmap_prompt(
    goal,
    level,
    skills,
    duration,
    daily_time,
    style
):

    return f"""

You are a senior AI career mentor.

Create a personalized learning roadmap.

Goal:
{goal}

Skill Level:
{level}

Existing Skills:
{skills}

Duration:
{duration}

Daily Study Time:
{daily_time}

Learning Style:
{style}


Include:

- Roadmap overview
- Month-wise learning plan
- Topics
- Projects
- Practice tasks
- Resources
- Expected outcomes


Use clean markdown.
Do not use tables.

"""
