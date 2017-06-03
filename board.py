import arrays


class Board(object):
    """
    Board implementation.
    """
    nought = "O"
    cross = "X"

    def __init__(self, source=None):
        self._array = arrays.Array(9)
        if source:
            for index in range(len(source)):
                self._array[index] = source[index]

    def __getitem__(self, index):
        """
        Gets the value of the element.
        :param index: the index of element.
        :return: value of the element.
        """
        return self._array[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.
        :param index: the index element.
        :param value: the value of element.
        """
        self._array[index] = value

    def __len__(self):
        return len(self._array)

    def __str__(self):
        result = ""
        for index in range(len(self)):
            if index % 3 == 0:
                result += "\n"
            if self[index] is None:
                result += " "
            else:
                result += self[index]
        return result

    def size(self):
        return self._array._size

    def empty_items(self):
        result = []
        for index in range(self.size()):
            if self[index] is None:
                result.append(index)
        return result

    def check_winner(self):
        """
        Checks winner.
        :return: "O" if wins first user
        """
        combinations = [
            # rows
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            # cols
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            # diagonals
            (0, 4, 8),
            (2, 4, 6)
        ]
        for combination in combinations:
            line = [self[index] for index in combination]
            if line == [self.nought] * 3:
                return self.nought
            elif line == [self.cross] * 3:
                return self.cross
