from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase.pdfmetrics import stringWidth
from io import BytesIO
import re


def clean_text(text):
    """
    Clean AI markdown output for PDF
    """

    # Remove markdown symbols
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)

    text = text.replace("#", "")
    text = text.replace("`", "")

    # Replace markdown bullets
    text = text.replace("- ", "• ")

    # Remove unwanted characters
    replacements = {
        "🚀": "",
        "🧠": "",
        "📚": "",
        "💻": "",
        "🎯": "",
        "🌱": "",
        "✅": "",
        "»": "",
        "–": "-",
        "—": "-"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()



def create_pdf(content):

    buffer = BytesIO()

    pdf = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )


    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=18,
        alignment=TA_CENTER,
        spaceAfter=20
    )


    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        spaceBefore=15,
        spaceAfter=8
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


    # PDF title
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


    for line in lines:

        line = line.strip()

        if not line:
            continue


        # Detect headings
        if (
            line.lower().startswith(
                (
                    "career overview",
                    "skills required",
                    "learning roadmap",
                    "career-specific projects",
                    "recommended resources",
                    "job preparation strategy",
                    "future career growth"
                )
            )
        ):

            story.append(
                Paragraph(
                    line,
                    heading_style
                )
            )


        else:

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
