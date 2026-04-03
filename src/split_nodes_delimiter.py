from textnode import TextType, TextNode


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
                raise Exception("this delimiter is not in the text")
            if len(parsed_text) % 2 == 0:
                raise Exception("invalid markdown")
            for i in range(len(parsed_text)):
                if len(parsed_text[i]) > 0:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(parsed_text[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(parsed_text[i], text_type))
    return new_nodes


