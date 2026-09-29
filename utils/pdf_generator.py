from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from io import BytesIO
import re
import html


def clean_text(text):

    # Remove markdown
    text = re.sub(r"#", "", text)
    text = text.replace("**", "")
    text = text.replace("---", "")

    # Fix AI artifacts
    replacements = {
        "n": " ",
        "fi": "-",
        "»": "",
        "–": "-",
        "—": "-"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove multiple spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

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
        "title",
        parent=styles["Title"],
        fontSize=20,
        alignment=1
    )


    heading_style = ParagraphStyle(
        "heading",
        parent=styles["Heading2"],
        fontSize=14
    )


    body_style = ParagraphStyle(
        "body",
        parent=styles["BodyText"],
        fontSize=10,
        leading=14
    )


    story=[]


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


    for line in cleaned.split("\n"):

        if not line.strip():
            continue


        safe = html.escape(line)


        if len(line)<40 and line[0].isupper():

            story.append(
                Paragraph(
                    safe,
                    heading_style
                )
            )

        else:

            story.append(
                Paragraph(
                    safe,
                    body_style
                )
            )


        story.append(
            Spacer(1,8)
        )


    pdf.build(story)


    data = buffer.getvalue()

    buffer.close()

    return data
