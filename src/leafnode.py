from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None) -> None:
        super()
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value.")
        elif self.tag == None:
            return self.value
        else:
            if self.props != None:
                props_string = ""
                for key, value in self.props.items():
                    props_string += f" {key}=\"{value}\""
                return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            
    def __repr__(self) -> str:
        return f"<{self.tag} {self.props}> {self.value} </{self.tag}>"
        