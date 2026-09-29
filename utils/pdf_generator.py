import markdown
from weasyprint import HTML


def create_pdf(content):

    html_content = markdown.markdown(
        content,
        extensions=[
            "tables",
            "fenced_code"
        ]
    )


    styled_html = f"""
    <!DOCTYPE html>
    <html>

    <head>

    <style>

    body {{
        font-family: Arial, Helvetica, sans-serif;
        margin: 50px;
        line-height: 1.6;
        font-size: 14px;
        color: #222;
    }}

    h1 {{
        text-align: center;
        font-size: 24px;
        margin-bottom: 30px;
    }}

    h2 {{
        font-size: 18px;
        margin-top: 25px;
    }}

    h3 {{
        font-size: 15px;
        margin-top: 18px;
    }}

    ul {{
        margin-left: 20px;
    }}

    li {{
        margin-bottom: 6px;
    }}

    table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
    }}

    th, td {{
        border: 1px solid #999;
        padding: 8px;
        text-align: left;
    }}

    </style>

    </head>


    <body>

    <h1>AI Career Roadmap</h1>

    {html_content}

    </body>

    </html>
    """


    pdf = HTML(
        string=styled_html
    ).write_pdf()


    return pdf
