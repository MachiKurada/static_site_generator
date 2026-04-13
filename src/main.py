from textnode import TextNode
from copy_static_to_public import copy_origin_contents_to_destination
from generate_page import generate_page, generate_pages_recursive

origin = "./static"
destination = "./public"
content_path = "./content"
template_path = "./template.html"
destination2 = "./public"

def main():
    copy_origin_contents_to_destination(origin, destination)
    generate_pages_recursive(content_path, template_path, destination2)

main()