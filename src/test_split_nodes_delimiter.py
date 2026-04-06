import unittest

from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_links
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
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [node])

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
        
class TestSplitNodesImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_image_first_last_only(self):
        node1 = TextNode(
            "![The image](https://i.imgur.com/zjjcJKZ.png) is first.",
            TextType.TEXT
        )
        node2 = TextNode(
            "Last is ![the image.](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        node3 = TextNode(
            "![Image only](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes1 = split_nodes_image([node1])
        new_nodes2 = split_nodes_image([node2])
        new_nodes3 = split_nodes_image([node3])
        self.assertListEqual(
            [
                TextNode("The image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" is first.", TextType.TEXT),
            ],
            new_nodes1,
        )
        self.assertListEqual(
            [
                TextNode("Last is ", TextType.TEXT),
                TextNode("the image.", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes2,
        )
        self.assertListEqual(
            [
                TextNode("Image only", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes3,
        )

    def test_no_plain_text(self):
        node = TextNode("No image only italics", TextType.ITALIC)
        self.assertListEqual([node], split_nodes_image([node]))
        
    def test_no_image(self):   
        node = TextNode("No image here", TextType.TEXT)
        self.assertListEqual([node], split_nodes_image([node]))

    def test_empty_image(self):
        node = TextNode("![]()", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_image([node])

class TestSplitNodesLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.url.com) and another [second link](https://www.newurl.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.url.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://www.newurl.com"
                ),
            ],
            new_nodes,
        )

    def test_link_first_last_only(self):
        node1 = TextNode(
            "[The link](https://www.url.com) is first.",
            TextType.TEXT
        )
        node2 = TextNode(
            "Last is [the link.](https://www.url.com)",
            TextType.TEXT
        )
        node3 = TextNode(
            "[Link only](https://www.url.com)",
            TextType.TEXT
        )
        new_nodes1 = split_nodes_links([node1])
        new_nodes2 = split_nodes_links([node2])
        new_nodes3 = split_nodes_links([node3])
        self.assertListEqual(
            [
                TextNode("The link", TextType.LINK, "https://www.url.com"),
                TextNode(" is first.", TextType.TEXT),
            ],
            new_nodes1,
        )
        self.assertListEqual(
            [
                TextNode("Last is ", TextType.TEXT),
                TextNode("the link.", TextType.LINK, "https://www.url.com"),
            ],
            new_nodes2,
        )
        self.assertListEqual(
            [
                TextNode("Link only", TextType.LINK, "https://www.url.com"),
            ],
            new_nodes3,
        )

    def test_no_plain_text(self):
        node = TextNode("No link only bold", TextType.BOLD)
        self.assertListEqual([node], split_nodes_links([node]))
        
    def test_no_link(self):   
        node = TextNode("No link here", TextType.TEXT)
        self.assertListEqual([node], split_nodes_links([node]))

    def test_empty_link(self):
        node = TextNode("[]()", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_links([node])