import unittest

from mardown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMardownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_blocks(self):
        md = """
This is **bolded** paragraph








- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "- This is a list\n- with items",
            ],
        )

    def test_erase_trailing_spaces(self):
        md = """
                  This is **bolded** paragraph with trailing spaces at the beginning.

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items and trailing spaces at the end.          
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph with trailing spaces at the beginning.",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items and trailing spaces at the end.",
            ],
        )

    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_one_block(self):
        md = """
This just one big block with **bold** and _italics_ and a [link](https://www.url.com)
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This just one big block with **bold** and _italics_ and a [link](https://www.url.com)"])



class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        header1 = "# Heading 1"
        header2 = "## Heading 2"
        header3 = "### Heading 3"
        header4 = "#### Heading 4"
        header5 = "##### Heading 5"
        header6 = "###### Heading 6"

        self.assertEqual(block_to_block_type(header1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(header2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(header3), BlockType.HEADING)
        self.assertEqual(block_to_block_type(header4), BlockType.HEADING)
        self.assertEqual(block_to_block_type(header5), BlockType.HEADING)
        self.assertEqual(block_to_block_type(header6), BlockType.HEADING)

    def test_heading_edge_cases(self):
        heading7 = "####### Heading 7"
        heading = "#Heading"
        self.assertEqual(block_to_block_type(heading7), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(heading), BlockType.PARAGRAPH)

    def test_paragraph(self):
        paragraph = "This is a paragraph of text."
        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)

    def test_empty_string(self):
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        unordered_list = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(unordered_list), BlockType.UNORDERED_LIST)

    def test_unordered_list_edge_cases(self):
        unordered_list = "- Item 1\nItem 2\n- Item 3"
        self.assertEqual(block_to_block_type(unordered_list), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        ordered_list = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(ordered_list), BlockType.ORDERED_LIST)

    def test_ordered_list_edge_cases(self):
        ordered_list1 = "2. Item 1\n3. Item 2\n4. Item 3"
        self.assertEqual(block_to_block_type(ordered_list1), BlockType.PARAGRAPH)
        ordered_list2 = "1. Item 1\n3. Item 2\n5. Item 3"
        self.assertEqual(block_to_block_type(ordered_list2), BlockType.PARAGRAPH)

    def test_quotes(self):
        quote1 = "> This is a quote."
        quote2 = ">This is also a quote.\n> But longer."
        self.assertEqual(block_to_block_type(quote1), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(quote2), BlockType.QUOTE)

    def test_quotes_edge_cases(self):
        quote = ">This is also a quote.\nBut longer.\n> And badly formated."
        self.assertEqual(block_to_block_type(quote), BlockType.PARAGRAPH)

    def test_code(self):
        code = "```\n\nThis is code\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_code_edge_case(self):
        code1 = "```\n\nThis is endless code"
        self.assertEqual(block_to_block_type(code1), BlockType.PARAGRAPH)
        code = "```This is code on one line```"
        self.assertEqual(block_to_block_type(code), BlockType.PARAGRAPH)