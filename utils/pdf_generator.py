from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
import re
import html


def clean_markdown(text):

    # Remove markdown headings
    text = re.sub(
        r"^#+\s*",
        "",
        text,
        flags=re.MULTILINE
    )

    # Remove bold/italic markdown
    text = text.replace("**", "")
    text = text.replace("__", "")
    text = text.replace("*", "")

    # Remove markdown separators
    text = re.sub(
        r"^-{3,}$",
        "",
        text,
        flags=re.MULTILINE
    )

    # Convert markdown bullets
    text = text.replace("- ", "• ")

    # Remove unwanted characters causing PDF issues
    remove_chars = [
        "🚀",
        "🧠",
        "📚",
        "💻",
        "🎯",
        "🌱",
        "✅",
        "»"
    ]

    for char in remove_chars:
        text = text.replace(char, "")


    # Fix AI formatting issues
    replacements = {
        "fi": "-",
        "nworld": "-world",
        "nmonth": "-month",
        "nmonths": "-months",
        "nlevel": "-level",
        "nready": "-ready",
        "nhrs": " hrs",
        "n": " "
    }


    for old, new in replacements.items():
        text = text.replace(old, new)


    # Remove extra spaces
    text = re.sub(
        r"[ ]+",
        " ",
        text
    )


    return text.strip()



def create_pdf(content):

    buffer = BytesIO()


    pdf = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=60,
        leftMargin=60,
        topMargin=60,
        bottomMargin=60
    )


    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        alignment=TA_CENTER,
        spaceAfter=30
    )


    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        spaceBefore=18,
        spaceAfter=10
    )


    sub_heading_style = ParagraphStyle(
        "SubHeading",
        parent=styles["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=12,
        spaceBefore=12,
        spaceAfter=8
    )


    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=15,
        spaceAfter=8
    )


    story = []


    # Title
    story.append(
        Paragraph(
            "AI Career Roadmap",
            title_style
        )
    )


    story.append(
        Spacer(1,20)
    )


    cleaned = clean_markdown(content)


    lines = cleaned.split("\n")


    for line in lines:

        line = line.strip()

        if not line:
            story.append(
                Spacer(1,8)
            )
            continue


        safe_line = html.escape(line)


        # Detect main sections
        if any(
            section.lower() in line.lower()
            for section in [
                "Career Overview",
                "Skills Required",
                "Learning Roadmap",
                "Career-Specific Projects",
                "Recommended Resources",
                "Job Preparation Strategy",
                "Future Career Growth"
            ]
        ):

            story.append(
                Paragraph(
                    safe_line,
                    heading_style
                )
            )


        # Detect sub sections
        elif any(
            word.lower() in line.lower()
            for word in [
                "Phase",
                "Beginner Projects",
                "Intermediate Projects",
                "Advanced Projects",
                "Technical Skills",
                "Soft Skills",
                "Tools",
                "Practice",
                "Learn"
            ]
        ):

            story.append(
                Paragraph(
                    safe_line,
                    sub_heading_style
                )
            )


        else:

            story.append(
                Paragraph(
                    safe_line,
                    body_style
                )
            )


        story.append(
            Spacer(1,5)
        )


    pdf.build(story)


    pdf_data = buffer.getvalue()

    buffer.close()


    return pdf_data
