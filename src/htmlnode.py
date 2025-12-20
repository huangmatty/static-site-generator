class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, properties=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.properties = properties

    def to_html(self):
        raise NotImplementedError

    def properties_to_html(self):
        properties_string = ""
        for property in self.properties:
            properties_string += f" {property}=\"{self.properties[property]}\""
        return properties_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.properties})"
