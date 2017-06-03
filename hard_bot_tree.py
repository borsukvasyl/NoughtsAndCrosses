#########################################################
### Contains hard level bot implemented by using tree ###
#########################################################

from base_tree_bot import Bot
from board import Board
from tree.lnode import LNode
from tree.ltree import ListTree


class HardBot(Bot):
    """
    Implements easy level bot for game Noughts and Crosses.
    """
    def __init__(self, name, symbol=None, game=None):
        super().__init__(name, symbol, game)
        self._tree = None

    def process(self, tree, point, symbol):
        for move in point.data[0].empty_items():
            board = Board(point.data[0])
            board[move] = symbol
            child = LNode((board, move))
            point.childs.append(child)
            if board.check_winner() is not None:
                break
            self.process(tree, child, "O" if symbol == "X" else "X")

    def build_tree(self):
        tree = ListTree()
        tree._root = LNode((Board(self._game._board), None))
        symbol = self._game._players[self._game._current_user].symbol
        self.process(tree, tree.get_root(), symbol)
        return tree
