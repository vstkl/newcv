from xhtml2pdf import pisa

# Import the BytesIO class from the io module
from io import BytesIO

# HTML content that is to be converted to a PDF
html_content = """
<!DOCTYPE html>
<html>
<body>
    <h1>Example with Hyperlinks</h1>
    <p>Visit <a href="https://www.example.com">Example</a></p>
</body>
</html>
"""

# Create a BytesIO object to store the PDF output
pdf_output = BytesIO()

with open('index.html', "r") as content:
# Use xhtml2pdf to convert the HTML content to a PDF and store it in pdf_output
    pisa.CreatePDF(content.read(), dest=pdf_output, encoding='utf-8')

# Open a PDF file for writing in binary mode
    with open("html-to-pdf.pdf", "wb") as pdf_file:
    
    # Write the PDF content to the file  
        pdf_file.write(pdf_output.getvalue())
