import unittest

from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNode(unittest.TestCase):
    def test_all_case_in_text(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(text_to_textnodes(text), nodes)

    def test_only_some_case_in_text(self):
        text1 = "Only **bold** and _italic._"
        nodes1 =[
            TextNode("Only ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic.", TextType.ITALIC),
        ]
        text2 = "Only `code` and a [link](http://www.url.com)" 
        nodes2 =[
            TextNode("Only ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "http://www.url.com"),
        ]
        text3 = "Just an ![image](https://i.imgur.com/fJRm4Vk.jpeg)"
        nodes3 =[
            TextNode("Just an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertListEqual(text_to_textnodes(text1), nodes1)
        self.assertListEqual(text_to_textnodes(text2), nodes2)
        self.assertListEqual(text_to_textnodes(text3), nodes3)
    
    def test_markdown_first(self):
        text1 = "**Bold** is first."
        nodes1 =[
            TextNode("Bold", TextType.BOLD),
            TextNode(" is first.", TextType.TEXT),
        ]
        text2 = "`Code` comes first." 
        nodes2 =[
            TextNode("Code", TextType.CODE),
            TextNode(" comes first.", TextType.TEXT),
        ]
        text3 = "![An image](https://i.imgur.com/fJRm4Vk.jpeg) and then..."
        nodes3 =[
            TextNode("An image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and then...", TextType.TEXT),
        ]
        self.assertListEqual(text_to_textnodes(text1), nodes1)
        self.assertListEqual(text_to_textnodes(text2), nodes2)
        self.assertListEqual(text_to_textnodes(text3), nodes3)

    def test_only_markdown(self):
        text1 = "_Only italics._"
        nodes1 =[
            TextNode("Only italics.", TextType.ITALIC),
        ]
        text2 = "[Link](http://www.url.com)" 
        nodes2 =[
            TextNode("Link", TextType.LINK, "http://www.url.com"),
        ]
        text3 = "**Bold and**![an image](https://i.imgur.com/fJRm4Vk.jpeg)"
        nodes3 =[
            TextNode("Bold and", TextType.BOLD),
            TextNode("an image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertListEqual(text_to_textnodes(text1), nodes1)
        self.assertListEqual(text_to_textnodes(text2), nodes2)
        self.assertListEqual(text_to_textnodes(text3), nodes3)
        
    
    def test_empty_string(self):
        text = ""
        nodes = [TextNode("", TextType.TEXT)]
        self.assertListEqual(text_to_textnodes(text), nodes)

    def test_error_on_markdown(self):
        with self.assertRaises(Exception):
            text_to_textnodes("**Invalid bold")
            text_to_textnodes("_Invalid italics")
            text_to_textnodes("`Invalid code")
            text_to_textnodes("[invalid link]()")
            text_to_textnodes("![](https://www.invalidimage.com)")