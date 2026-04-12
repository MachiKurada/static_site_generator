from markdown_to_html_node import markdown_to_html_node
from htmlnode import *
import os

def extract_title(markdown):
    blocks = markdown.split("\n")
    for block in blocks:
        if block.startswith("# "):
            return block.lstrip("#").strip()
    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md:
        markdown = md.read()
    with open(template_path) as tmpl:
        template = tmpl.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as p:
        p.write(page)
