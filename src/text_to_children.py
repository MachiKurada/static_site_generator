from mardown_to_blocks import block_to_block_type, BlockType
from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode

def get_pure_block_text(block):
    block_type = block_to_block_type(block)
    lines = block.split("\n")
    match block_type:
        case BlockType.PARAGRAPH:
            return block.replace("\n", " ").strip()
        case BlockType.HEADING:
            return block.lstrip("#").strip().strip("\n")
        case BlockType.CODE:
            return block.strip("```").strip("\n")
        case BlockType.QUOTE:
            quote = ""
            for line in lines:
                quote += line.lstrip(">").strip() + " "
            return quote.strip(" ")
        case BlockType.UNORDERED_LIST:
            list = []
            for line in lines:
                list.append(line.lstrip("- ").strip())
            return list
        case BlockType.ORDERED_LIST:
            list = []
            for i in range(len(lines)):
                list.append(lines[i].lstrip(f"{i+1}. "))
            return list



def text_to_children(text):
    inline_text = get_pure_block_text(text)
    children = []
    if isinstance(inline_text, str):
        text_nodes = text_to_textnodes(inline_text)
        for node in text_nodes:
            children.append(text_node_to_html_node(node))
    if isinstance(inline_text, list):
        for line in inline_text:
            line_children = []
            text_nodes = text_to_textnodes(line)
            for node in text_nodes:
                line_children.append(text_node_to_html_node(node))
            children.append(line_children)
    return children