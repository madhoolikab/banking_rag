# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 08:01:40 2024

@author: Madhu
"""

"""
import PyPDF2
import re

def extract_headings_and_content(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        content = ""

        # Extract text from all pages
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            content += page.extract_text()

    headings = []
    content_dict = {}
    lines = content.split('\n')

    # Regex pattern for headings (customize based on your document structure)
    heading_pattern = r'^[A-Z][A-Z0-9\s]+$'  # Match uppercase headings, adjust if needed
    subheading_pattern = r'^[A-Z][a-z0-9\s]+$'  # Match subheadings, adjust if needed

    current_heading = None

    for line in lines:
        line = line.strip()

        if re.match(heading_pattern, line):  # Detect heading
            current_heading = line
            headings.append(current_heading)
            content_dict[current_heading] = []
        elif re.match(subheading_pattern, line) and current_heading:  # Detect subheading
            content_dict[current_heading].append({'subheading': line, 'content': []})
        elif current_heading:  # Add content under the current heading or subheading
            if content_dict[current_heading]:
                content_dict[current_heading][-1]['content'].append(line)
            else:
                content_dict[current_heading].append(line)

    return content_dict

pdf_path = 'C:/Users/Madhu/Downloads/small_example.pdf'  # Replace with your PDF path
data = extract_headings_and_content(pdf_path)


with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    content = ""

    # Extract text from all pages
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        content += page.extract_text()

headings = []
content_dict = {}
lines = content.split('\n')

# Regex pattern for headings (customize based on your document structure)
heading_pattern = r'^[A-Z][A-Z0-9\s]+$'  # Match uppercase headings, adjust if needed
subheading_pattern = r'^[A-Z][a-z0-9\s]+$'  # Match subheadings, adjust if needed

current_heading = None

for line in lines:
    line = line.strip()

    if re.match(heading_pattern, line):  # Detect heading
        current_heading = line
        headings.append(current_heading)
        content_dict[current_heading] = []
    elif re.match(subheading_pattern, line) and current_heading:  # Detect subheading
        content_dict[current_heading].append({'subheading': line, 'content': []})
    elif current_heading:  # Add content under the current heading or subheading
        if content_dict[current_heading]:
            content_dict[current_heading][-1]['content'].append(line)
        else:
            content_dict[current_heading].append(line)

# Print extracted content
for heading, content in data.items():
    print(f"Heading: {heading}")
    for item in content:
        if isinstance(item, dict):
            print(f"  Subheading: {item['subheading']}")
            print(f"  Content: {' '.join(item['content'])}")
        else:
            print(f"  Content: {item}")

"""


























import fitz  # PyMuPDF
import re
import json

def extract_chunks(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []

    for page_number in range(len(doc)):
        page = doc[page_number]
        text = page.get_text("blocks")
        text = sorted(text, key=lambda b: (b[1], b[0]))  # Sort by vertical, then horizontal position
        
        current_section = None
        current_subsection = None

        for block in text:
            content = block[4].strip()
            if not content:
                continue

            # Identify sections/subsections using Heading patterns
            if re.match(r'^\d+\.\d+\s', content):  # Subsection (e.g., 1.1, 1.2)
                current_subsection = content.split(maxsplit=1)[0]
                chunks.append({
                    "page": page_number + 1,
                    "section": current_section,
                    "subsection": current_subsection,
                    "text": content
                })
            elif re.match(r'^\d+\s', content):  # Section (e.g., 1, 2)
                current_section = content.split(maxsplit=1)[0]
                current_subsection = None  # Reset subsection
                chunks.append({
                    "page": page_number + 1,
                    "section": current_section,
                    "subsection": None,
                    "text": content
                })
            else:  # Append content to the latest section/subsection
                if chunks and chunks[-1]["page"] == page_number + 1:
                    chunks[-1]["text"] += " " + content
                else:
                    chunks.append({
                        "page": page_number + 1,
                        "section": current_section,
                        "subsection": current_subsection,
                        "text": content
                    })
    return chunks

# Generate JSON from chunks
def save_chunks_to_json(chunks, output_path):
    with open(output_path, "w") as file:
        json.dump(chunks, file, indent=4)

# Main execution
pdf_path = "C:/Users/Madhu/Downloads/Account_Opening_Closing_Guide.pdf"
output_json_path = "C:/Users/Madhu/Downloads/chunks.json"
chunks = extract_chunks(pdf_path)
save_chunks_to_json(chunks, output_json_path)

print(f"Chunks saved to {output_json_path}")
