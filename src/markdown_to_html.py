from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
from block_types import block_to_block_type, BlockType

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))

    return html_nodes

def replace_last(string, old, new):
    return new.join(string.rsplit(old, 1))

def block_to_html_node(block, block_type):
    if block_type == BlockType.HEADING:
        count = len(block) - len(block.lstrip('#'))
        block = block.lstrip('#')
        block = block.strip()
        heading = ""
        match count:
            case 1:
                heading = "h1"
            case 2:
                heading = "h2"
            case 3:
                heading = "h3"
            case 4:
                heading = "h4"
            case 5:
                heading = "h5"
            case 6:
                heading = "h6"
        return ParentNode(tag=heading, children=text_to_children(block))
    elif block_type == BlockType.PARAGRAPH:
        block = block.replace("\n", " ")
        return ParentNode(tag="p", children=text_to_children(block))
    elif block_type == BlockType.CODE:
        block = block.replace("```\n", "", 1)
        block = replace_last(block, "```", "")
        return ParentNode("pre", [LeafNode("code", block)])
    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")
        cleaned_lines = []
        for line in lines:
            line = line[2:]
            cleaned_lines.append(line)

        text = " ".join(cleaned_lines)
        return ParentNode("blockquote", children=text_to_children(text))
    elif block_type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        children = []

        for line in lines:
            item_text = line[2:]
            children.append(ParentNode("li", text_to_children(item_text)))

        return ParentNode("ul", children)
    
    elif block_type == BlockType.ORDERED_LIST:
        lines = block.split("\n")
        children = []

        for line in lines:
            # remove the "1. ", "2. ", etc.
            item_text = line.split(". ", 1)[1]
            children.append(ParentNode("li", text_to_children(item_text)))

        return ParentNode("ol", children)

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    children = []

    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        node = block_to_html_node(block, block_type)
        children.append(node)

    return ParentNode("div", children)