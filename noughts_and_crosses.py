import random
import os
from board import Board


class NoughtsAndCrosses(object):
    """
    Implementation of game Noughts and Crosses
    """
    nought = "O"
    cross = "X"

    def __init__(self, players):
        """
        Generates board and players (turn is chosen randomly).
        :param players: list of Player subclass objects
        """
        if len(players) != 2:
            raise ValueError("Incorrect names list.")
        self._board = Board()
        symbols = ["O", "X"]
        random.shuffle(players)
        for index in range(2):
            players[index]._game = self
            players[index].symbol =symbols[index]
        self._players = players
        self._current_user = 0

    def get_player(self):
        return self._players[self._current_user]

    def get_enemy(self, symbol):
        return self.nought if symbol == self.cross else self.cross

    def move(self):
        """
        Calculates player's move.
        :return: None
        """
        move = self._players[self._current_user].move()
        self._board[move] = self._players[self._current_user].symbol
        self._current_user = (self._current_user + 1) % 2

    def can_move(self):
        """
        Checks whether move is possible.
        :return: bool
        """
        return True if self._board.empty_items() else False

    def clear_board(self):
        """
        Generates new board.
        :return: None
        """
        self._board = Board()

    def display_board(self):
        """
        Prints board.
        :return: None
        """
        result = ""
        for row in range(3):
            for col in range(3):
                result += self._board[row * 3 + col] if self._board[row * 3 + col] else " "
                if col != 2:
                    result += "|"
            if row != 2:
                result += "\n" + "-+" * 2 + "-\n"
        print(result)

    def display_warning(self):
        """
        Prints warning.
        :return: None
        """
        print("Incorrect move!!!")

    def run(self):
        """
        Run game.
        :return: None
        """
        play = True
        while play:
            self.clear_board()
            while True:
                os.system("CLS")
                self.display_board()
                self.move()
                winner = self._board.check_winner()
                if winner:
                    os.system("CLS")
                    self.display_board()
                    print(winner, "won")
                    break
                if not self.can_move():
                    os.system("CLS")
                    self.display_board()
                    print("draw")
                    break
            play = input("Print something to play again: ")
