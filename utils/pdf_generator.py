from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
import html


def create_pdf(content):

    buffer = BytesIO()

    pdf = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    styles["Title"].alignment = TA_CENTER

    story = []


    # PDF Title
    story.append(
        Paragraph(
            "AI Career Roadmap",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )


    # Clean AI response
    content = html.escape(content)


    lines = content.split("\n")


    for line in lines:

        if line.strip():

            # Convert markdown headings
            if line.startswith("#"):
                line = line.replace("#", "").strip()

                paragraph = Paragraph(
                    f"<b>{line}</b>",
                    styles["Heading3"]
                )

            else:
                # Convert bullet points
                line = line.replace("- ", "• ")

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
