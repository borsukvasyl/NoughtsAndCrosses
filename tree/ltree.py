class ListTree(object):
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
        if not point.childs:
            return True
        return False

    def childs(self, point):
        for child in point.childs:
            yield child

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
            for item in point.childs:
                process(tree, item)

        if start is None:
            start = self._root
        process(self, start)
        return leafs
