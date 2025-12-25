from textnode import TextType, TextNode
from inline import split_nodes_image, split_nodes_link

def main():
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) asdfa asdf fasdk fsk [to boot dev](https://www.boot.dev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    # print(new_nodes)
    return

main()
