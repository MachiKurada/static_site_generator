import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_base_cases(self):
        node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("`Code first` is the key.", TextType.TEXT)
        node3 = TextNode("Always remember `code should come last.`", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node1], "`", TextType.CODE), 
                         [
                            TextNode("This is text with a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" word", TextType.TEXT),
                            ]
                        )
        self.assertEqual(split_nodes_delimiter([node2], "`", TextType.CODE), 
                         [
                            TextNode("Code first", TextType.CODE),
                            TextNode(" is the key.", TextType.TEXT),
                            ]
                        )
        self.assertEqual(split_nodes_delimiter([node3], "`", TextType.CODE), 
                         [
                            TextNode("Always remember ", TextType.TEXT),
                            TextNode("code should come last.", TextType.CODE),
                            ]
                        )
        
    def test_case_not_plain_text(self):
        node = TextNode("**Let's be bold**", TextType.BOLD)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [node])

    def test_no_delimiters(self):
        node = TextNode("Not bold enough", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_empty_string(self):
        node = TextNode("``", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE),[])

    def test_multi_nodes(self):
        node1 = TextNode("This node has _italics_ in it.", TextType.TEXT)
        node2 = TextNode("_This one is all italics._", TextType.ITALIC)
        self.assertEqual(split_nodes_delimiter([node1, node2], "_", TextType.ITALIC), 
                         [
                            TextNode("This node has ", TextType.TEXT),
                            TextNode("italics", TextType.ITALIC),
                            TextNode(" in it.", TextType.TEXT),
                            TextNode("_This one is all italics._", TextType.ITALIC)
                            ]
                        )
    