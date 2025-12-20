import unittest
from leafnode import LeafNode
from textnode import TextType, TextNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node1 = LeafNode(
            "div",
            "Hello, world!",
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node1.to_html(),
            '<div class="greeting" href="https://boot.dev">Hello, world!</div>',
        )

        node2 = LeafNode(
            "p",
            "What a strange world",
            {"class": "primary"},
        )
        self.assertEqual(
            node2.to_html(),
            '<p class="primary">What a strange world</p>',
        )


if __name__ == "__main__":
    unittest.main()


