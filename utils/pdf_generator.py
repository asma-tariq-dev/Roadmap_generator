from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.pdfmetrics import stringWidth
from io import BytesIO
import textwrap


def create_pdf(content):

    buffer = BytesIO()

    pdf = canvas.Canvas(
        buffer,
        pagesize=letter
    )

    width, height = letter


    # Simple font
    pdf.setFont(
        "Helvetica",
        11
    )


    x = 50
    y = height - 50


    # Title
    pdf.setFont(
        "Helvetica-Bold",
        16
    )

    pdf.drawString(
        x,
        y,
        "AI Career Roadmap"
    )

    y -= 40


    pdf.setFont(
        "Helvetica",
        11
    )


    # Write roadmap exactly as text
    for line in content.split("\n"):

        wrapped_lines = textwrap.wrap(
            line,
            width=90
        )


        for wrapped in wrapped_lines:

            if y < 50:
                pdf.showPage()

                pdf.setFont(
                    "Helvetica",
                    11
                )

                y = height - 50


            pdf.drawString(
                x,
                y,
                wrapped
            )

            y -= 16


    pdf.save()


    pdf_data = buffer.getvalue()

    buffer.close()


    return pdf_data
