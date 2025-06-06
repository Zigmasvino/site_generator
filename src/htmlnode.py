class HTMLNode:
    """
    A class representing a node in an HTML document.
    """

    def __init__(self, tag=None, value=None, children=None, props=None):       
        self.tag = tag
        self.value = value
        self.children = children 
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        """
        It should return a string that represents the HTML attributes of the node
        """
        if not self.props:
            return ""
    
        attr_strings = [f'{key}="{value}"' for key, value in self.props.items() if value is not None]

        if not attr_strings:
            return ""
        
        # Add a leading space before the joined attributes
        return " " + " ".join(attr_strings)
    
    def __repr__(self):
        # print an HTMLNode object and see its tag, value, children, and props.
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=[], props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
            
        if self.tag is None:
            return self.value
            
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
            
        if self.children is None:
            raise ValueError("ParentNode must have children")        

        return f"<{self.tag}{self.props_to_html()}>" + "".join([child.to_html() for child in self.children]) + f"</{self.tag}>"        
