from textnode import TextNode
from copy_static_to_public import copy_origin_contents_to_destination

origin = "./static"
destination = "./public"

def main():
    item_paths = copy_origin_contents_to_destination(origin, destination)
    print(item_paths)

main()