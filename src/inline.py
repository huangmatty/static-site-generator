import re
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

def split_nodes_image(old_nodes):
    # print("begin splitting...")
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue;
        
        text = node.text
        # print(f"original text: {text}\n")
        matches = extract_markdown_images(text)
        # print(f"matches: {matches}\n")
        if len(matches) == 0:
            new_nodes.append(node)
            continue;
        
        nodes = []
        for match in matches:
            image_alt = match[0]
            image_url = match[1]
            sections = text.split(f"![{image_alt}]({image_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown")
            if len(sections[0]) != 0:
                text_node = TextNode(sections[0], TextType.TEXT)
                # print(f"text node: {text_node}\n")
                nodes.append(text_node)
            image_node = TextNode(image_alt, TextType.IMAGE, image_url)
            # print(f"image node: {image_node}\n")
            nodes.append(image_node)
            text = sections[1]
            # print(f"new text: {text}\n")
        if len(text) > 0:
            text_node = TextNode(text, TextType.TEXT)
            # print(f"text node: {text_node}\n")
            nodes.append(text_node)
        new_nodes.extend(nodes)
    # print(f"new nodes: {new_nodes}")
    return new_nodes

def split_nodes_link(old_nodes):
    print("begin splitting...")
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue;
        
        text = node.text
        print(f"original text: {text}\n")
        matches = extract_markdown_links(text)
        print(f"matches: {matches}\n")
        if len(matches) == 0:
            new_nodes.append(node)
            continue;

        nodes = []
        for match in matches:
            link_anchor = match[0]
            link_url = match[1]
            sections = text.split(f"[{link_anchor}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown")
            if len(sections[0]) != 0:
                text_node = TextNode(sections[0], TextType.TEXT)
                print(f"text node: {text_node}\n")
                nodes.append(text_node)
            link_node = TextNode(link_anchor, TextType.LINK, link_url)
            print(f"link node: {link_node}\n")
            nodes.append(link_node)
            if len(sections) > 1:
                text = sections[1]
                print(f"new text: {text}\n")
        if len(text) > 0:
            text_node = TextNode(text, TextType.TEXT)
            print(f"text node: {text_node}\n")
            nodes.append(text_node)
        new_nodes.extend(nodes)
    print(f"new nodes: {new_nodes}")
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
