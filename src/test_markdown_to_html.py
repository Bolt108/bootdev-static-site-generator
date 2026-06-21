import unittest
from textwrap import dedent

from markdown_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = dedent("""
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """)

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = dedent("""
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """)

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
        
    def test_heading(self):
        md = dedent("# Hello **world**")
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><h1>Hello <b>world</b></h1></div>",
        )

    def test_multiple_headings(self):
        md = dedent("""
# Heading 1

### Heading 3

###### Heading 6
""")
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><h1>Heading 1</h1><h3>Heading 3</h3><h6>Heading 6</h6></div>",
        )

    def test_paragraph_with_inline_markdown(self):
        md = dedent("""
This is **bold**, _italic_, and `code`.
""")
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>This is <b>bold</b>, <i>italic</i>, and <code>code</code>.</p></div>",
        )

    def test_multiline_paragraph(self):
        md = dedent("""
This is one line
and this is another
""")
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>This is one line and this is another</p></div>",
        )

    def test_quote(self):
        md = dedent("""
> This is a quote
> with **bold** text
""")
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>This is a quote with <b>bold</b> text</blockquote></div>",
        )

    def test_unordered_list(self):
        md = dedent("""
- first item
- second **bold** item
- third item with `code`
""")
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>first item</li><li>second <b>bold</b> item</li><li>third item with <code>code</code></li></ul></div>",
        )

    def test_ordered_list(self):
        md = dedent("""
1. first item
2. second _italic_ item
3. third item
""")
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>first item</li><li>second <i>italic</i> item</li><li>third item</li></ol></div>",
        )

    def test_ordered_list_more_than_nine_items(self):
        md = dedent("""
1. one
2. two
3. three
4. four
5. five
6. six
7. seven
8. eight
9. nine
10. ten
""")
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>one</li><li>two</li><li>three</li><li>four</li><li>five</li><li>six</li><li>seven</li><li>eight</li><li>nine</li><li>ten</li></ol></div>",
        )

    def test_codeblock_no_inline_parsing(self):
        md = dedent("""```
This is not bold
This is not italic
This is not inline code
```
""")
        node = markdown_to_html_node(md)
        self.assertNotEqual(
            node.to_html(),
            "<div><pre><code>This is **not bold**\nThis is _not italic_\nThis is `not inline code`\n</code></pre></div>",
        )

    def test_mixed_document(self):
        md = dedent("""
# My Document

This is a paragraph with **bold** text.

- item one
- item two with _italic_

> a quote with `code`

```
raw markdown
```
""")
        node = markdown_to_html_node(md)
        self.assertNotEqual(
            node.to_html(),
            "<div><h1>My Document</h1><p>This is a paragraph with <b>bold</b> text.</p><ul><li>item one</li><li>item two with <i>italic</i></li></ul><blockquote>a quote with <code>code</code></blockquote><pre><code>raw **markdown**\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()