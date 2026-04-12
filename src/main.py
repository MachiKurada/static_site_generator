from textnode import TextNode
from copy_static_to_public import copy_origin_contents_to_destination
from generate_page import generate_page

origin = "./static"
destination = "./public"
content_path = "./content/index.md"
template_path = "./template.html"
destination2 = "./public/index.html"

def main():
    copy_origin_contents_to_destination(origin, destination)
    generate_page(content_path, template_path, destination2)

main()