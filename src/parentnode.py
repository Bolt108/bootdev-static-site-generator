from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None) -> None:
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag missing")
        elif self.children == None:
            raise ValueError("Children missing")
        else:
            parent_node_str = f"<{self.tag}>"
            for child in self.children:
                node_str = child.to_html()
                parent_node_str += node_str
            parent_node_str += f"</{self.tag}>"

            return parent_node_str
        