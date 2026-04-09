import unittest
from text_to_children import get_pure_block_text, text_to_children
from htmlnode import LeafNode




class TestGetPureBlockText(unittest.TestCase):
    def test_heading(self):
        header1 = "# Heading 1"
        header2 = "## Heading 2"
        header3 = "### Heading 3"
        header4 = "#### Heading 4"
        header5 = "##### Heading 5"
        header6 = "###### Heading 6"

        self.assertEqual(get_pure_block_text(header1), "Heading 1")
        self.assertEqual(get_pure_block_text(header2), "Heading 2")
        self.assertEqual(get_pure_block_text(header3), "Heading 3")
        self.assertEqual(get_pure_block_text(header4), "Heading 4")
        self.assertEqual(get_pure_block_text(header5), "Heading 5")
        self.assertEqual(get_pure_block_text(header6), "Heading 6")


    def test_paragraph(self):
        paragraph = "This is a paragraph of text."
        self.assertEqual(get_pure_block_text(paragraph), paragraph)
        paragraph2 = "This paragraph has a trailing new line.\n"
        self.assertEqual(get_pure_block_text(paragraph2), "This paragraph has a trailing new line.")

    def test_empty_string(self):
        self.assertEqual(get_pure_block_text("# "), "")

    def test_unordered_list(self):
        unordered_list = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(get_pure_block_text(unordered_list), ["Item 1", "Item 2", "Item 3"])


    def test_ordered_list(self):
        ordered_list = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(get_pure_block_text(ordered_list), ["Item 1", "Item 2", "Item 3"])

    def test_quotes(self):
        quote1 = "> This is a quote."
        quote2 = ">This is also a quote.\n> But longer."
        self.assertEqual(get_pure_block_text(quote1), "This is a quote.")
        self.assertEqual(get_pure_block_text(quote2), "This is also a quote.\nBut longer.")


    def test_code(self):
        code = "```\n\nThis is code\n```"
        self.assertEqual(get_pure_block_text(code), "This is code")

class TestTextToChildren(unittest.TestCase):
    def test_base_case(self):
        text = "## Header with **bold** text."
        nodes = [LeafNode(None, "Header with "), LeafNode("b", "bold"), LeafNode(None, " text.")]
        self.assertListEqual(text_to_children(text), nodes)

    def test_other_cases(self):
        text1 = ">_Quote_ starting with italics."
        nodes1 = [LeafNode("i", "Quote"), LeafNode(None, " starting with italics.")]
        text2 = "Paragraph ending with a [link](https://www.url.com)"
        nodes2 = [LeafNode(None, "Paragraph ending with a "), LeafNode("a", "link", {"href": "https://www.url.com"})]
        text3 = "- List with _italics_\n- and **bold**\n- `and code`"
        nodes3 = [[LeafNode(None, "List with "), LeafNode("i", "italics")], [LeafNode(None, "and "), LeafNode("b", "bold")], [LeafNode("code", "and code")]]
        self.assertListEqual(text_to_children(text1), nodes1)
        self.assertListEqual(text_to_children(text2), nodes2)
        self.assertListEqual(text_to_children(text3), nodes3)
        

