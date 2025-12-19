from textnode import TextType, TextNode

def main():
    text_node = TextNode("Anchor text for link", TextType.LINK, "https://www.boot.dev")
    print(text_node)
    return

main()
