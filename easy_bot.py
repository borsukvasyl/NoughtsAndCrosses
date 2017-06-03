from base_tree_bot import Bot
from board import Board
from binary_tree.btnode import BTNode
from binary_tree.btree import BinaryTree


class EasyBot(Bot):
    """
    Implements easy level bot for game Noughts and Crosses.
    """
    @staticmethod
    def process(tree, point, symbol):
        """
        Randomly builds binary tree and chooses
        best move.
        :param tree: BTree object
        :param point: BTPoint object
        :param symbol: str
        :return: None
        """
        used = None
        for item in ("left", "right"):
            board = Board(point.data[0])
            moves = board.empty_items()
            if used and used in moves:
                moves.remove(used)
            if not moves:
                break
            move = EasyBot.generate_move(moves)
            used = move
            board[move] = symbol
            child = BTNode((board, move))
            setattr(point, item, child)
            if board.check_winner():
                continue
            EasyBot.process(tree, child, "O" if symbol == "X" else "X")

    def build_tree(self):
        tree = BinaryTree()
        tree._root = BTNode((Board(self._game._board), None))
        symbol = self._game._players[self._game._current_user].symbol
        self.process(tree, tree.get_root(), symbol)
        return tree
