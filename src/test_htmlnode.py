import unittest

from htmlnode import HTMLNode


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



if __name__ == "__main__":
    unittest.main()