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


def clean_text(text):
    """
    Clean AI generated markdown text
    """

    # Remove markdown bold/italic symbols
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = text.replace("*", "")

    # Remove markdown headings
    text = text.replace("#", "")

    # Remove unwanted AI formatting characters
    replacements = {
        "»": "",
        "fi": " - ",
        "🚀": "",
        "🧠": "",
        "📚": "",
        "💻": "",
        "🎯": "",
        "🌱": "",
        "✅": "•",
        "–": "-",
        "—": "-"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)


    # Fix common broken words
    fixes = {
        "realnworld": "real-world",
        "portfolionlevel": "portfolio-level",
        "careerngrowth": "career growth",
        "problemnsolving": "problem-solving",
        "nworld": "-world",
        "nontechnical": "non-technical",
        "screennshare": "screen-share",
        "onepage": "one-page"
    }

    for old, new in fixes.items():
        text = text.replace(old, new)


    return text.strip()



def create_pdf(content):

    buffer = BytesIO()


    pdf = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=55,
        leftMargin=55,
        topMargin=55,
        bottomMargin=55
    )


    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=18,
        alignment=TA_CENTER,
        spaceAfter=25
    )


    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        spaceBefore=18,
        spaceAfter=10
    )


    subheading_style = ParagraphStyle(
        "SubHeadingStyle",
        parent=styles["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=12,
        spaceBefore=12,
        spaceAfter=6
    )


    body_style = ParagraphStyle(
        "BodyStyle",
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


    cleaned = clean_text(content)


    lines = cleaned.split("\n")


    main_sections = [
        "Career Overview",
        "Skills Required",
        "Learning Roadmap",
        "Career-Specific Projects",
        "Recommended Resources",
        "Job Preparation Strategy",
        "Future Career Growth"
    ]


    for line in lines:

        line = line.strip()


        if not line:
            continue


        # Escape HTML characters
        line = html.escape(line)


        # Main headings
        if any(
            line.startswith(section)
            for section in main_sections
        ):

            story.append(
                Paragraph(
                    line,
                    heading_style
                )
            )


        # Smaller headings
        elif (
            line.startswith("Phase")
            or line.startswith("Beginner")
            or line.startswith("Intermediate")
            or line.startswith("Advanced")
            or line.startswith("Technical Skills")
            or line.startswith("Soft Skills")
        ):

            story.append(
                Paragraph(
                    line,
                    subheading_style
                )
            )


        else:

            # Convert bullet points
            if line.startswith("•"):
                line = "&bull; " + line[1:].strip()


            story.append(
                Paragraph(
                    line,
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
