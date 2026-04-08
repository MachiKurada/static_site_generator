def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    new_blocks = []
    for block in raw_blocks:
        if len(block.strip()) > 0:
            new_blocks.append(block.strip())
    return new_blocks