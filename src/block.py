from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")
    if len(lines) < 1: raise ValueError("Empty markdown block")
    
    # check if block is of type CODE
    is_code = False
    if len(lines) > 1:
        if len(lines[0]) > 2 and lines[0][:3] == "```":
            if len(lines[-1]) > 2 and lines[-1][:3] == "```": is_code = True
    if is_code: return BlockType.CODE

    # check if block is of type ORDERED_LIST
    is_ordered_list = True
    for i, line in enumerate(lines):
        digit = i + 1
        if len(line) < 3:
            is_ordered_list = False
            break

        j = 0
        while j < len(line) and line[j].isdigit(): j += 1
        if j < 1:
            is_ordered_list = False
            break 
        if digit != int(line[:j]):
            is_ordered_list = False
            break 
        if j + 1 >= len(line):
            is_ordered_list = False
            break
        if line[j:j+2] != ". ":
            is_ordered_list = False
            break
    if is_ordered_list: return BlockType.ORDERED_LIST

    # check if block is of type UNORDERED_LIST
    is_unordered_list = True
    for line in lines:
        if len(line) < 2:
            is_unordered_list = False
            break
        if line[:2] != f"- ":
            is_unordered_list = False
            break
    if is_unordered_list: return BlockType.UNORDERED_LIST

    # check if block is of type QUOTE
    is_quote = True
    for line in lines:
        if len(line) < 1:
            is_quote = False
            break
        if line[0] != ">":
            is_quote = False
            break
    if is_quote: return BlockType.QUOTE

    # check if block is of type HEADING
    is_heading = False
    if len(lines) == 1 and len(lines[0]) > 2:
        line = lines[0]
        if line[0] == "#":
            i, count = 1, 1
            while i < len(line):
                if count > 6: break
                if line[i] != "#": break
                count += 1
                i += 1
            if count < 7:
                if i + 1 < len(line) and line[i] == " ": is_heading = True
    if is_heading: return BlockType.HEADING 

    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    # print("input markdown")
    # print(f"{markdown}\n")
    # print("blocks:")
    blocks = markdown.split("\n\n")
    block_str = []
    for block in blocks:
        block = block.strip()
        if len(block):
            block_str.append(block)
    # print(block_str)
    return block_str