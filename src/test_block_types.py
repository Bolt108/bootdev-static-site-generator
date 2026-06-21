from block_types import block_to_block_type, BlockType

import unittest

# --- The Unit Tests ---
class TestGetBlockType(unittest.TestCase):

    # 1. Test Headings (Starts with 1-6 '#' followed by a space)
    def test_heading_valid(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_heading_invalid(self):
        # More than 6 hashes, or missing space makes it a paragraph
        self.assertEqual(block_to_block_type("####### Too many hashes"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)

    # 2. Test Code Blocks (Must start and end with ```)
    def test_code_block_valid(self):
        code = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)
        
        code_with_lang = "```\npython\ndef func():\n    return True\n```"
        self.assertEqual(block_to_block_type(code_with_lang), BlockType.CODE)

    def test_code_block_invalid(self):
        # Missing closing backticks or wrong number of backticks
        unclosed_code = "```\nprint('hello')"
        self.assertEqual(block_to_block_type(unclosed_code), BlockType.PARAGRAPH)

    # 3. Test Quotes (Every line must start with '>')
    def test_quote_valid(self):
        quote = "> This is a quote\n> split over two lines"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_quote_invalid(self):
        # Second line misses the '>' symbol
        bad_quote = "> First line valid\nSecond line missing quote symbol"
        self.assertEqual(block_to_block_type(bad_quote), BlockType.PARAGRAPH)

    # 4. Test Unordered Lists (Every line must start with '- ' or '* ')
    def test_unordered_list_valid(self):
        dash_list = "- Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(dash_list), BlockType.UNORDERED_LIST)

    def test_unordered_list_invalid(self):
        # Mixed symbols or missing space
        mixed_list = "- Item 1\n* Item 2"
        self.assertEqual(block_to_block_type(mixed_list), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("-NoSpace"), BlockType.PARAGRAPH)

    # 5. Test Ordered Lists (Must start at 1. and increment perfectly)
    def test_ordered_list_valid(self):
        valid_list = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(valid_list), BlockType.ORDERED_LIST)

    def test_ordered_list_invalid(self):
        # Starts at 2, or increments incorrectly
        wrong_start = "2. First\n3. Second"
        broken_sequence = "1. First\n3. Third"
        self.assertEqual(block_to_block_type(wrong_start), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(broken_sequence), BlockType.PARAGRAPH)

    # 6. Test Paragraphs (Normal text fallback)
    def test_paragraph(self):
        text = "This is just a normal paragraph.\nIt spans multiple lines."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    # 7. Test Empty/Whitespace Edge Cases
    def test_empty_block(self):
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("\n\n"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()