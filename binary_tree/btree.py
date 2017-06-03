class BinaryTree(object):
    """
    Implementation of binary tree.
    """
    def __init__(self):
        self._root = None

    def get_root(self):
        """
        Returns root of tree.
        :return: BTNode or None
        """
        return self._root

    def is_leaf(self, point):
        """
        Checks whether point is leaf.
        :param point: tree point
        :return: bool
        """
        if point.left is None and point.right is None:
            return True
        return False

    def childs(self, point):
        if point.left is not None:
            yield point.left
        if point.right is not None:
            yield point.right

    def leafs(self, start=None):
        """
        Returns all leafs.
        :param start: start point
        :return: yield elements
        """
        leafs = []
        def process(tree, point):
            if tree.is_leaf(point):
                leafs.append(point)
            if point.left:
                process(tree, point.left)
            if point.right:
                process(tree, point.right)
        if start == None:
            start = self._root
        process(self, start)
        return leafs
