from enum import Enum


def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    new_blocks = []
    for block in raw_blocks:
        if len(block.strip()) > 0:
            new_blocks.append(block.strip())
    return new_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(text):
    lines = text.split("\n")
    
    if text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if text.startswith("```\n") and text.endswith("```") and len(lines)>=2:
        return BlockType.CODE

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    for i, line in enumerate(lines, start=1):
        is_ordered_list = True
        if not line.startswith(f"{i}. "):
            is_ordered_list = False
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

