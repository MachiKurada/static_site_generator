from textnode import TextNode
from copy_static_to_public import copy_origin_contents_to_destination
from generate_page import generate_page, generate_pages_recursive
import sys

origin = "./static"
destination = "./docs"
content_path = "./content"
template_path = "./template.html"

def main():
    if len(sys.argv) > 1 :
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_origin_contents_to_destination(origin, destination)
    generate_pages_recursive(content_path, template_path, destination, basepath)

main()