import random
from player import Player


class HardBot(Player):
    """
    Implements easy level bot for game Noughts and Crosses.
    """
    def minimax(self, board, symbol, alpha, beta):
        winner = board.check_winner()
        if winner or not board.empty_items():
            if winner == self._game.get_player().symbol:
                return 1
            elif winner == None:
                return 0
            else:
                return -1

        for move in board.empty_items():
            board[move] = symbol
            val = self.minimax(board, self._game.get_enemy(symbol), alpha, beta)
            board[move] = None
            if symbol == self._game.get_player().symbol:
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if symbol == self._game.get_player().symbol:
            return alpha
        else:
            return beta

    def move(self):
        min_val = -2
        choices = []
        board = self._game._board
        player = self._game.get_player()
        if len(board.empty_items()) == 9:
            return random.choice([1, 3, 5, 7])
        for move in board.empty_items():
            board[move] = player.symbol
            val = self.minimax(board, self._game.get_enemy(player.symbol), -2, 2)
            board[move] = None
            if val > min_val:
                min_val = val
                choices = [move]
            elif val == min_val:
                choices.append(move)
        print(choices)
        return random.choice(choices)
