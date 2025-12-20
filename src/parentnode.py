from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, properties=None):
        super().__init__(tag, None, children, properties)

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: No tag in parent node")
        html_str = f"<{self.tag}>"
        for child in self.children:
            html_str += child.to_html()
        html_str += f"</{self.tag}>"
        return html_str

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.properties})"
