class HTMLNode:
    def __init__(self, tag = None , value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None or len(self.props) == 0:
            return ""
        else:
            props_html = ""
            for key, value in self.props.items():
                props_html += f" {key}=\"{value}\""

            return props_html
    
    def __repr__(self) -> str:
        return f"<{self.tag}{self.props_to_html}> {self.value} {self.children} </{self.tag}>"