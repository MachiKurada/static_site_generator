import unittest

from mardown_to_blocks import markdown_to_blocks

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