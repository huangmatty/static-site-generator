def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    block_str = []
    for block in blocks:
        block = block.strip()
        if len(block):
            block_str.append(block)
    return block_str