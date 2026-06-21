import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_not_eq(self):
        node = HTMLNode("p", "Hi", None, None)
        node2 = HTMLNode("p", "Hi2", None, None)
        self.assertNotEqual(node, node2)

    def test_eq(self):
        node = HTMLNode("p", "Hi", None, None)
        node2 = HTMLNode("p", "Hi", None, None)
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = HTMLNode("p", "Hi", None, {"href": "https://www.google.com","target": "_blank"})
        self.assertNotEqual(node.props_to_html, " href=\"https://www.google.com\" target=\"_blank\"")


if __name__ == "__main__":
    unittest.main()