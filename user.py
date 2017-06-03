import player


class User(player.Player):
    """
    Implements user for game Noughts and Crosses.
    """
    def valid_move(self, move):
        """
        Checks whether move is valid.
        :param move: int
        :return: None
        """
        if not isinstance(move, int) or not 0 <= move < self._game._board.size() or \
           self._game._board[move] is not None:
            raise ValueError

    def move(self):
        """
        User inputs their move.
        :return: int
        """
        while True:
            try:
                move = eval(input("Enter move: "))
                self.valid_move(move)
                return move
            except ValueError:
                self._game.display_warning()
                continue