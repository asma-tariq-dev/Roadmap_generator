def roadmap_prompt(
    goal,
    level,
    skills,
    duration,
    daily_time,
    style
):

    return f"""
You are an expert career mentor and technical roadmap designer.

Create a personalized career roadmap for:

Career Goal:
{goal}

Current Skill Level:
{level}

Existing Skills:
{skills}

Available Duration:
{duration}

Daily Study Time:
{daily_time}

Learning Style:
{style}


Your response must be professional, beginner-friendly, and suitable for conversion into a PDF career guide.


IMPORTANT FORMATTING RULES:

1. Use clear headings:

Career Overview

Skills Required

Learning Roadmap

Career-Specific Projects

Recommended Resources

Job Preparation Strategy

Future Career Growth


2. Use simple Markdown formatting:

- Use ## for main headings
- Use ### for subheadings
- Use bullet points (-)
- Use numbered lists when needed


3. Do NOT use:

- Emojis
- Tables
- Special symbols
- Mathematical symbols
- Characters like » → ✓
- Long separators like ---


4. Avoid:

- Excessive # symbols
- Excessive **bold formatting**
- Complex explanations without examples


5. Make it suitable for ANY career:

Examples:
AI Engineer, Software Developer, Graphic Designer,
Data Analyst, Teacher, Doctor, Digital Marketer.


6. Include:

Career Overview:
- What this professional does
- Why this career matters


Skills Required:
- Technical skills
- Soft skills


Learning Roadmap:
- Divide into realistic phases
- Explain what to learn
- Mention tools
- Add practice tasks


Career-Specific Projects:
- Beginner projects
- Intermediate projects
- Advanced portfolio projects


Recommended Resources:
- Courses
- Documentation
- Practice platforms


Job Preparation Strategy:
- Resume advice
- Portfolio advice
- Interview preparation
- Job searching tips


Future Career Growth:
- Possible next roles
- Specializations
- Long-term opportunities


Write in simple English that a student can understand.

Make the roadmap practical, achievable, motivating, and professional.

"""
