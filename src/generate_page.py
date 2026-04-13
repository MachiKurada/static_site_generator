from markdown_to_html_node import markdown_to_html_node
from htmlnode import *
import os
from pathlib import Path

def extract_title(markdown):
    blocks = markdown.split("\n")
    for block in blocks:
        if block.startswith("# "):
            return block.lstrip("#").strip()
    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md:
        markdown = md.read()
    with open(template_path) as tmpl:
        template = tmpl.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    page = page.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as p:
        p.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_items = os.listdir(dir_path_content)
    for item in content_items:
        item_path = os.path.join(dir_path_content, item)
        item_dest = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path) and item_path.endswith(".md"):
            item_dest = Path(item_dest).with_suffix(".html")
            generate_page(item_path, template_path, item_dest, basepath)
        else:
            if not os.path.isfile(item_path):
                generate_pages_recursive(item_path, template_path, item_dest, basepath)

