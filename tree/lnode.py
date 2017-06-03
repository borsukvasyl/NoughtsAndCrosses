class LNode(object):
    """
    Implementation of binary tree node.
    """
    def __init__(self, data, parent=None, childs=None):
        self.data = data
        if childs is None:
            self.childs = []
        else:
            self.childs = childs
