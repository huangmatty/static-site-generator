from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, properties=None):
        super().__init__(tag, value, None, properties)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if self.tag and self.properties:
            return f"<{self.tag}{self.properties_to_html()}>{self.value}</{self.tag}>"
        if self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return self.value
