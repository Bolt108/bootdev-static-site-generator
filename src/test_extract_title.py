from textnode import TextNode, TextType
from extract_images_links import extract_markdown_images, extract_markdown_links
from main import extract_title
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_extract_markdown_title(self):
        title = extract_title("# Hello World!")
        self.assertEqual("Hello World!", title)

    def test_extract_markdown_title_unequal(self):
        title = extract_title("Hello World!")
        self.assertEqual(title, ValueError)

if __name__ == "__main__":
    unittest.main()