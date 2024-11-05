import re
import markdown
from xhtml2pdf import pisa

# Import the BytesIO class from the io module
from io import BytesIO


# Define the filter array
filters = [
    (r'/\*.*?\*/', ''),  # Remove comments
]

def apply_filters(content):
    for pattern, replacement in filters:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    return content

def process_file(input_file, output_file):
    rules = []
    style = ""
    elem = ""
    buf = ""
    with open(input_file, 'r') as f:
        content = f.read()

        for c in apply_filters(content):
            if ' ' == c or '\n' == c or '\t' == c:
                continue
            if '{' == c:
                elem = buf
                buf = ""
                continue
            elif '}' == c:
                style = buf
                rules.append(f"{elem} {{ {style} }}")
                elem = ""
                style = ""
                buf = ""
                continue
            else:
                buf += c

 
        for rule in rules:
            print(rule)
    filtered_content = apply_filters(content)
    with open(output_file, 'w') as f:
        pass
        # f.write(filtered_content)
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

# Use xhtml2pdf to convert the HTML content to a PDF and store it in pdf_output
pisa.CreatePDF(html_content, dest=pdf_output, encoding='utf-8')

# Open a PDF file for writing in binary mode
with open("html-to-pdf.pdf", "wb") as pdf_file:
  
  # Write the PDF content to the file  
  pdf_file.write(pdf_output.getvalue())
# Example usage
input_file = 'style.css'
output_file = 'style_processed.html'
process_file(input_file, output_file)
