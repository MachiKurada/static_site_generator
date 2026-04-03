class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented")
    
    def props_to_html(self):
        attributes_string = ""
        if self.props is None or len(self.props) == 0:
            return attributes_string
        for key, value in self.props.items():
            attributes_string += f' {key}="{value}"'
        return attributes_string
    
    def __repr__(self):
        children_string = ""
        if self.children is not None:
            for child in self.children:
                children_string += f"{child.value}, "
        children_string = children_string.strip(", ")
        return f"Tag: {self.tag}, Value: {self.value}, Children: {children_string}, Props:{self.props_to_html()}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Props:{self.props_to_html()}"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("all parent nodes must have a tag")
        if self.children is None or self.children == []:
            raise ValueError("all parent nodes must have a valid child")
        children_html_string = ""
        for child in self.children:
            try:
                children_html_string += child.to_html()
            except TypeError:
                raise ValueError("invalid child")
        return f"<{self.tag}{self.props_to_html()}>{children_html_string}</{self.tag}>"
    
    def __repr__(self):
        children_string = ""
        if self.children is not None:
            for child in self.children:
                children_string += f"{child.value}, "
        children_string = children_string.strip(", ")
        return f"Tag: {self.tag}, Children: {children_string}, Props:{self.props_to_html()}"