import unittest
from markdown_to_html_node import markdown_to_html_node
from htmlnode import *

unittest.TestCase.maxDiff = None

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_quotes(self):
        md = """
>This is a quote
>that spans multiple _lines_
>and with **formating** on top

>and now a one line `code` quote.

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote that spans multiple <i>lines</i> and with <b>formating</b> on top</blockquote><blockquote>and now a one line <code>code</code> quote.</blockquote></div>",
        )

    def test_headings(self):
        md = """
# A multi headings **text**

### With different _formattings_

##### And different `levels`

And a paragraph that should stay separate

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>A multi headings <b>text</b></h1><h3>With different <i>formattings</i></h3><h5>And different <code>levels</code></h5><p>And a paragraph that should stay separate</p></div>",
        )

    def test_lists(self):
        md = """
- An unordered **list**
- With multiple formatings
- _Italics_ and `code` for example

1. An ordered _list_
2. with various formatings
3. **Bold** and `code` for example
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>An unordered <b>list</b></li><li>With multiple formatings</li><li><i>Italics</i> and <code>code</code> for example</li></ul><ol><li>An ordered <i>list</i></li><li>with various formatings</li><li><b>Bold</b> and <code>code</code> for example</li></ol></div>",
        )

    def test_multitypes(self):
        md = """
## A heading

> Then a _quote_ to start with

A paragraph
on multiple **lines**

- A list
- with `code` inside

1. An ordered list
2. is okay too

```
and finally a code block
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>A heading</h2><blockquote>Then a <i>quote</i> to start with</blockquote><p>A paragraph on multiple <b>lines</b></p><ul><li>A list</li><li>with <code>code</code> inside</li></ul><ol><li>An ordered list</li><li>is okay too</li></ol><pre><code>and finally a code block</code></pre></div>",
        )



