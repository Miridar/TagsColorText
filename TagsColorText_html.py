import re
import os

# Color mapping as provided
color_mapping = {
    "adjective": "rgb(255, 224, 230)",  # Lighter Pink
    "adverb": "rgb(255, 255, 128)",     # Lighter Yellow
    "conjunction": "rgb(224, 224, 224)",# Lighter Grey
    "determiner": "rgb(255, 153, 255)", # Lighter Magenta
    "noun": "rgb(153, 255, 153)",       # Lighter Green
    "number": "rgb(255, 204, 128)",     # Lighter Orange
    "preposition": "rgb(255, 182, 193)",# Lighter Hot Pink
    "pronoun": "rgb(199, 238, 238)",    # Lighter Pale Turquoise
    "verb": "rgb(153, 153, 255)"        # Lighter Blue
}

# The input text with tags
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")

# Load the text from "input.txt"
with open(input_file_path, "r", encoding="utf-8") as file:
    text_with_tags = file.read()

# Function to create an HTML document with colored text
def create_html_with_colored_text(text, colors):
    # Determine the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Split the text into parts, capturing both tagged and untagged text
    parts = re.split(r'(<\w+>[^<]+<\/\w+>)', text)

    # Start the HTML document
    html_content = "<html><body>"

    for part in parts:
        # Check if the part is a tagged word
        tagged_word = re.match(r'<(\w+)>([^<]+)</\w+>', part)
        if tagged_word:
            tag, word = tagged_word.groups()
            color_style = colors.get(tag, "initial")  # Use "initial" if tag not found in colors
            html_content += f'<span style="background-color:{color_style}; font-size: xx-large;">{word}</span> '
        else:
            # This part is untagged text
            html_content += f'<span style="font-size: xx-large;">{part}</span>'

    # Close the HTML document
    html_content += "</body></html>"

    # Construct the path for the HTML file in the script's directory
    html_path = os.path.join(script_dir, "colored_text.html")

    # Save the HTML document
    with open(html_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    return html_path

# Create the HTML document with colored text
html_path = create_html_with_colored_text(text_with_tags, color_mapping)