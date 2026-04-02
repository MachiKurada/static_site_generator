import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        node = LeafNode("img", "", {"src": "url/of/image.jpg", "alt":"Description of image"})
        self.assertEqual(node.to_html(), '<img src="url/of/image.jpg" alt="Description of image"></img>')

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode(None, "Hello, world!")
        node3 = LeafNode("img", "", {"src": "url/of/image.jpg", "alt":"Description of image"})
        self.assertEqual(node.__repr__(), 'Tag: p, Value: Hello, world!, Props: ')
        self.assertEqual(node2.__repr__(), 'Tag: None, Value: Hello, world!, Props: ')
        self.assertEqual(node3.__repr__(), 'Tag: img, Value: , Props: src="url/of/image.jpg" alt="Description of image"')

    def test_leaf_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("b", "other child")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>other child</b></div>")

    def test_to_html_with_great_grandchild(self):
        great_grandchild_node = LeafNode("b", "great-grandchild")
        grandchild_node =  ParentNode("i", [great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><i><b>great-grandchild</b></i></span></div>",
        )
    
    def test_to_html_value_erros(self):
        control_child = LeafNode("b", "bold")
        node = ParentNode("p", None)
        node2 = ParentNode("p", [])
        node3 = ParentNode(None, [control_child])
        node4 = ParentNode("p", ["Totally a child I swear"])
        node5 = ParentNode("p", [node])
        with self.assertRaises(ValueError):
            node.to_html()
            node2.to_html()
            node3.to_html()
            node4.to_html()
            node5.to_html()
    
    def test_to_html_with_props(self):
        child_node1 = LeafNode("b", "bold")
        child_node2 = LeafNode("a", "link", {"href": "www.link.com"})
        parent_node1 = ParentNode("p", [child_node1, child_node2])
        parent_node2 = ParentNode("div", [child_node1],{"class": "container", "id": "main"})
        grandparent_node = ParentNode("p", [parent_node1, parent_node2])
        self.assertEqual(parent_node1.to_html(), '<p><b>bold</b><a href="www.link.com">link</a></p>')
        self.assertEqual(parent_node2.to_html(), '<div class="container" id="main"><b>bold</b></div>')
        self;self.assertEqual(grandparent_node.to_html(), '<p><p><b>bold</b><a href="www.link.com">link</a></p><div class="container" id="main"><b>bold</b></div></p>')



if __name__ == "__main__":
    unittest.main()