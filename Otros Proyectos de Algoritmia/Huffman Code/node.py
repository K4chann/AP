class Node:
    """Represents a Node.
    
    Attributes:
        freq (str): Frequency of a character
        letre (str): Character, default is None
        children (list): List of children of the Node, default is '[ ]'

    """

    def __init__(self, freq, letre = None, children = []):
        self.freq = freq
        self.letre = letre
        self.children = children

    def __str__(self) -> str:
        return f"""
        {self.letre}: {self.freq}
        Children: {self.children[0].letre} {self.children[1].letre}
        """