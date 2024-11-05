import re
import markdown

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

# Example usage
input_file = 'style.css'
output_file = 'style_processed.html'
process_file(input_file, output_file)
