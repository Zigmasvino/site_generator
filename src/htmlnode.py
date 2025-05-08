class HTMLNode:
    """
    A class representing a node in an HTML document.
    """

    def __init__(self, tag=None, value=None, children=None, props=None):       
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {} 

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
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
