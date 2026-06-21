from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        break_down_list = []
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        else:
            node_list = node.text.split(delimiter)
            for i in range(len(node_list)):
                if i % 2 == 0:
                    break_down_list.append(TextNode(node_list[i], TextType.TEXT))
                elif i % 2 == 1:
                    break_down_list.append(TextNode(node_list[i], text_type))
        new_list.extend(break_down_list)
    return new_list