from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_links
from textnode import TextType, TextNode

def text_to_textnodes(text):
    original_node = [TextNode(text, TextType.TEXT)]
    parsed_italics = split_nodes_delimiter(original_node, "_", TextType.ITALIC)
    parsed_bold = split_nodes_delimiter(parsed_italics, "**", TextType.BOLD)
    parsed_code = split_nodes_delimiter(parsed_bold, "`", TextType.CODE)
    parsed_images = split_nodes_image(parsed_code)
    all_parsed = split_nodes_links(parsed_images)
    return all_parsed

