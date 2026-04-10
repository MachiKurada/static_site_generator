from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import *
from text_to_children import *
from mardown_to_blocks import block_to_block_type, BlockType


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    children = text_to_children(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return ParentNode("p", children)
        case BlockType.HEADING:
            n = len(block.split()[0])
            return ParentNode(f"h{n}", children)
        case BlockType.CODE:
            block_text = get_pure_block_text(block)
            child = text_node_to_html_node(TextNode(block_text, TextType.CODE))
            return ParentNode("pre", [child])
        case BlockType.QUOTE:
            return ParentNode("blockquote", children)
        case BlockType.UNORDERED_LIST:
            list_children = []
            for i in range(len(children)):
                list_children.append(ParentNode("li", children[i]))
            return ParentNode("ul", list_children)
        case BlockType.ORDERED_LIST:
            list_children = []
            for i in range(len(children)):
                list_children.append(ParentNode("li", children[i]))
            return ParentNode("ol", list_children)