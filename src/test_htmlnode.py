import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("b", "bold")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode("a", "this is a link", None, {"href": "https://www.url.com"})
        node2 = HTMLNode("a", "this is a link with several props", None, {"href": "https://www.url.com", "target": "_blank"})
        node3 = HTMLNode("b", "bold")
        self.assertEqual(node.props_to_html(), 'href="https://www.url.com"')
        self.assertEqual(node2.props_to_html(), 'href="https://www.url.com" target="_blank"')
        self.assertEqual(node3.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode("a", "this is a link", None, {"href": "https://www.url.com"})
        node2 = HTMLNode("a", "this is a link with several props", None, {"href": "https://www.url.com", "target": "_blank"})
        node3 = HTMLNode("b", "bold", [node])
        self.assertEqual(node.__repr__(), 'Tag: a, Value: this is a link, Children: , Props: href="https://www.url.com"')
        self.assertEqual(node2.__repr__(), 'Tag: a, Value: this is a link with several props, Children: , Props: href="https://www.url.com" target="_blank"')
        self.assertEqual(node3.__repr__(), 'Tag: b, Value: bold, Children: this is a link, Props: ')


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_tagless(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_img(self):
        node = LeafNode("img", "This is an image", {"src": "url/of/image.jpg", "alt":"Description of image"})
        self.assertEqual(node.to_html(), '<img src="url/of/image.jpg" alt="Description of image">This is an image</img>')

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode(None, "Hello, world!")
        node3 = LeafNode("img", "This is an image", {"src": "url/of/image.jpg", "alt":"Description of image"})
        self.assertEqual(node.__repr__(), 'Tag: p, Value: Hello, world!, Props: ')
        self.assertEqual(node2.__repr__(), 'Tag: None, Value: Hello, world!, Props: ')
        self.assertEqual(node3.__repr__(), 'Tag: img, Value: This is an image, Props: src="url/of/image.jpg" alt="Description of image"')



if __name__ == "__main__":
    unittest.main()