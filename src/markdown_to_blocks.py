def markdown_to_blocks(markdown):
    block_list = []
    unprocessed_list = markdown.split("\n\n")
    for block in unprocessed_list:
        block = block.strip()
        block = block.strip("\n")
        if block != "":
            block_list.append(block)
    return block_list