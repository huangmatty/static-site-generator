from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        delimiter_count = text.count(delimiter)
        if delimiter_count == 0:
            new_nodes.append(node)
            continue

        if delimiter_count % 2 != 0:
            raise Exception("Invalid Markdown syntax: Missing delimiter")
        
        nodes = []
        parts = text.split(delimiter)
        for i, v in enumerate(parts):
            if i % 2:
                nodes.append(TextNode(v, text_type))
                continue
            if len(v):
                nodes.append(TextNode(v, TextType.TEXT))
        new_nodes.extend(nodes)

    return new_nodes