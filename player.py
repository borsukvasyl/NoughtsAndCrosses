class Player(object):
    """
    Implements player base class for game Noughts and Crosses.
    """
    def __init__(self, name, symbol=None, game=None):
        self.name = name
        self.symbol = symbol
        self._game = game
