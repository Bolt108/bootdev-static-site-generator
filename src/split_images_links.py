from extract_images_links import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        else:
            original_text = node.text
            images = extract_markdown_images(node.text)
            if len(images) == 0:
                new_list.append(node)
                continue
            else:
                for image in images:
                    sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
                    if len(sections) != 2:
                        raise ValueError("invalid markdown, image section not closed")
                    if sections[0] != "":
                        new_list.append(TextNode(sections[0], TextType.TEXT))
                    new_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
                    original_text = sections[1]
                if original_text != "":
                    new_list.append(TextNode(original_text, TextType.TEXT))
    return new_list



def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        else:
            original_text = node.text
            links = extract_markdown_links(node.text)
            if len(links) == 0:
                new_list.append(node)
                continue
            else:
                for link in links:
                    sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
                    if len(sections) != 2:
                        raise ValueError("invalid markdown, link section not closed")
                    if sections[0] != "":
                        new_list.append(TextNode(sections[0], TextType.TEXT))
                    new_list.append(TextNode(link[0], TextType.LINK, link[1]))
                    original_text = sections[1]
                if original_text != "":
                    new_list.append(TextNode(original_text, TextType.TEXT))
    return new_list

def split_nodes_link_2(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        else:
            original_text = old_node.text
            links = extract_markdown_links(old_node.text)
            if len(links) == 0:
                new_nodes.append(old_node)
                continue
            for link in links:
                sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("invalid markdown, link section not closed")
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                original_text = sections[1]
                if original_text != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
    return new_nodes
