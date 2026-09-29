from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


def create_pdf(content):

    buffer = BytesIO()

    pdf = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    story = []

    # Title
    title = Paragraph(
        "🚀 AI Career Roadmap",
        styles["Title"]
    )

    story.append(title)
    story.append(Spacer(1, 20))


    # Convert AI response into PDF paragraphs
    lines = content.split("\n")

    for line in lines:

        if line.strip():

            paragraph = Paragraph(
                line,
                styles["BodyText"]
            )

            story.append(paragraph)
            story.append(
                Spacer(1, 8)
            )


    pdf.build(story)

    pdf_data = buffer.getvalue()

    buffer.close()

    return pdf_data
