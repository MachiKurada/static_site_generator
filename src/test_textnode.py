import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("hello", TextType.ITALIC)
        node2 = TextNode("hi", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("good morning", TextType.TEXT)
        node2 = TextNode("this is a cat picture", TextType.IMAGE, "www.catpicture.com")
        node3 = TextNode("this is an url", TextType.LINK, "www.totallyanurl.com")
        self.assertEqual(node.__repr__(), "TextNode(good morning, TextType.TEXT, None)")
        self.assertEqual(node2.__repr__(), "TextNode(this is a cat picture, TextType.IMAGE, www.catpicture.com)")
        self.assertEqual(node3.__repr__(), "TextNode(this is an url, TextType.LINK, www.totallyanurl.com)")

    def test_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "www.url.com")
        node2 = TextNode("This is a text node", TextType.LINK, "www.url.com")
        node3 = TextNode("This is a text node", TextType.LINK, "www.url.net")
        node4 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)

    def test_with_different_text_types(self):
        node = TextNode("hello", TextType.BOLD)
        node2 = TextNode("hello", TextType.ITALIC)
        self.assertNotEqual(node, node2)

class TestTextNode_to_LeafNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_propless_text(self):
        node_b = TextNode("bold", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(node_b).tag, "b")
        self.assertEqual(text_node_to_html_node(node_b).value, "bold")
        
        node_i = TextNode("italics", TextType.ITALIC)
        self.assertEqual(text_node_to_html_node(node_i).tag, "i")
        self.assertEqual(text_node_to_html_node(node_i).value, "italics")
        
        node_c = TextNode("code", TextType.CODE)
        self.assertEqual(text_node_to_html_node(node_c).tag, "code")
        self.assertEqual(text_node_to_html_node(node_c).value, "code")

    def test_text_with_props(self):
        node_l = TextNode("link", TextType.LINK, "www.link.com")
        self.assertEqual(text_node_to_html_node(node_l).tag, "a")
        self.assertEqual(text_node_to_html_node(node_l).value, "link")
        self.assertEqual(text_node_to_html_node(node_l).props, {"href":"www.link.com"})

        node_img = TextNode("image", TextType.IMAGE, "www.image.com")
        self.assertEqual(text_node_to_html_node(node_img).tag, "img")
        self.assertEqual(text_node_to_html_node(node_img).value, "")
        self.assertEqual(text_node_to_html_node(node_img).props, {"src":"www.image.com", "alt":"image"})




if __name__ == "__main__":
    unittest.main()