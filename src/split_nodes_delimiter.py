from textnode import TextType, TextNode
from extract_mardown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if not isinstance(old_nodes, list):
        raise ValueError ("old nodes must be in a list")
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise ValueError ("content of old nodes must be text nodes")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parsed_text = node.text.split(delimiter)
            if len(parsed_text) <= 1:
             new_nodes.append(node)
             continue
            if len(parsed_text) % 2 == 0:
                raise Exception("invalid markdown")
            for i in range(len(parsed_text)):
                if len(parsed_text[i]) > 0:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(parsed_text[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(parsed_text[i], text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    if not isinstance(old_nodes, list):
        raise ValueError ("old nodes must be in a list")
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise ValueError ("content of old nodes must be text nodes")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            if len(images)==0:
                new_nodes.append(node)
                continue
            current_text = node.text
            for image in images:
                image_alt, image_link = image
                if len(image_alt)==0 or len(image_link)==0:
                    raise Exception("missing alt or link")
                parsed_text = current_text.split(f"![{image_alt}]({image_link})")
                if len(parsed_text) <= 1:
                    new_nodes.append(TextNode(parsed_text, TextType.TEXT))
                if len(parsed_text[0]) >= 1:
                    new_nodes.append(TextNode(parsed_text[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                current_text = parsed_text[1]
            if len(current_text) >= 1:
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    if not isinstance(old_nodes, list):
        raise ValueError ("old nodes must be in a list")
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise ValueError ("content of old nodes must be text nodes")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if len(links)==0:
                new_nodes.append(node)
                continue
            current_text = node.text
            for link in links:
                link_alt, link_url = link
                if len(link_alt)==0 or len(link_url)==0:
                    raise Exception("missing alt or url")
                parsed_text = current_text.split(f"[{link_alt}]({link_url})")
                if len(parsed_text) <= 1:
                    new_nodes.append(TextNode(parsed_text, TextType.TEXT))
                if len(parsed_text[0]) >= 1:
                    new_nodes.append(TextNode(parsed_text[0], TextType.TEXT))
                new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
                current_text = parsed_text[1]
            if len(current_text) >= 1:
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes


