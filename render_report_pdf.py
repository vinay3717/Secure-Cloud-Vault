import os
import markdown
from playwright.sync_api import sync_playwright

def render_report():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, "docs", "final-report.md")
    html_path = os.path.join(base_dir, "docs", "final-report.html")
    pdf_path = os.path.join(base_dir, "docs", "final-report.pdf")

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Convert markdown to HTML body
    body_html = markdown.markdown(
        md_text,
        extensions=[
            "tables",
            "fenced_code",
            "toc",
            "sane_lists",
        ],
    )

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Cloud Computing Laboratory Report</title>
<style>
@page {{
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-center {{
        content: "Page " counter(page);
        font-size: 9pt;
        color: #718096;
    }}
}}
body {{
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;
    color: #1a202c;
    line-height: 1.6;
    font-size: 10.5pt;
    margin: 0;
    padding: 0;
}}
h1 {{
    font-size: 20pt;
    color: #1a365d;
    border-bottom: 2px solid #2b6cb0;
    padding-bottom: 6px;
    margin-top: 0;
}}
h2 {{
    font-size: 15pt;
    color: #2b6cb0;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
    margin-top: 24pt;
    page-break-after: avoid;
}}
h3 {{
    font-size: 12pt;
    color: #2d3748;
    margin-top: 16pt;
    page-break-after: avoid;
}}
h4 {{
    font-size: 10.5pt;
    color: #4a5568;
    margin-top: 12pt;
    page-break-after: avoid;
}}
p, li {{
    text-align: justify;
    color: #2d3748;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14pt 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}}
th, td {{
    border: 1px solid #cbd5e0;
    padding: 6pt 8pt;
    text-align: left;
}}
th {{
    background-color: #ebf8ff;
    color: #2b6cb0;
    font-weight: 600;
}}
tr:nth-child(even) {{
    background-color: #f7fafc;
}}
pre {{
    background: #edf2f7;
    border-left: 4px solid #3182ce;
    padding: 8pt 10pt;
    font-family: 'Courier New', Courier, monospace;
    font-size: 8.5pt;
    overflow-x: auto;
    page-break-inside: avoid;
    border-radius: 3px;
}}
code {{
    font-family: 'Courier New', Courier, monospace;
    background: #edf2f7;
    padding: 1pt 3pt;
    border-radius: 2px;
    font-size: 9pt;
}}
img {{
    max-width: 95%;
    height: auto;
    display: block;
    margin: 10pt auto;
    border: 1px solid #cbd5e0;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    page-break-inside: avoid;
}}
hr {{
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 16pt 0;
}}
blockquote {{
    border-left: 4px solid #4299e1;
    background: #ebf8ff;
    margin: 10pt 0;
    padding: 6pt 12pt;
    font-style: italic;
}}
</style>
</head>
<body>
{body_html}
</body>
</html>
"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print("HTML report generated at:", html_path)

    # Render PDF using Playwright Chromium
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file:///{html_path.replace(os.sep, '/')}")
        page.wait_for_load_state("networkidle")
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={
                "top": "20mm",
                "bottom": "20mm",
                "left": "15mm",
                "right": "15mm",
            },
        )
        browser.close()

    print("PDF report successfully compiled at:", pdf_path)

if __name__ == "__main__":
    render_report()
