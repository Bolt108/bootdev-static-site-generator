from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def check_all_lines_start_with(multiline_str, prefixes_tuple):
    if not multiline_str:
        return False
    return all(line.startswith(prefixes_tuple) for line in multiline_str.splitlines())

def is_incrementing_list(multiline_str, separator=". "):
    lines = multiline_str.splitlines()
    if not lines:
        return False  # Empty string is not a valid list
    
    # enumerate(..., start=1) matches the lines to expected numbers: 1, 2, 3...
    for index, line in enumerate(lines, start=1):
        expected_prefix = f"{index}{separator}"
        if not line.startswith(expected_prefix):
            return False
            
    return True

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif check_all_lines_start_with(block, (">")):
        return BlockType.QUOTE
    elif check_all_lines_start_with(block, ("- ")):
        return BlockType.UNORDERED_LIST
    elif is_incrementing_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
