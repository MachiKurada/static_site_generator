import unittest

from textnode import TextNode, TextType


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
        node = TextNode("good morning", TextType.PLAIN)
        node2 = TextNode("this is a cat picture", TextType.IMAGE, "www.catpicture.com")
        node3 = TextNode("this is an url", TextType.LINK, "www.totallyanurl.com")
        self.assertEqual(node.__repr__(), "TextNode(good morning, TextType.PLAIN, None)")
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



if __name__ == "__main__":
    unittest.main()