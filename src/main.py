from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    print("Hello, World!")

    TextNode1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(TextNode1)
    
    

if __name__ == "__main__":
    main()