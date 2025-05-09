import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph", [], {"class": "text"})
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=This is a paragraph, children=[], props={'class': 'text'})")
        
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", [], {"class": "text"})
        self.assertEqual(node.props_to_html(), ' class="text"')

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "This is a paragraph", [], {})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode("p", "This is a paragraph", [], {"class": None})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none_dict(self):
        node = HTMLNode("p", "This is a paragraph", [], None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none_value(self):
        node = HTMLNode("p", "This is a paragraph", [], {"class": None})
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!")
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

    def test_leaf_to_html_none(self):
        node = LeafNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")


    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()