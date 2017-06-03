import random
from player import Player


class Bot(Player):
    @staticmethod
    def generate_move(moves):
        """
        Generates random move.
        :param moves: list of possible moves
        :return: int
        """
        while True:
            try:
                move = random.choice(moves)
                return move
            except ValueError:
                continue

    @staticmethod
    def biggest_elements(elements):
        """
        Returns the biggest elements from elements.
        :param elements: list of elements
        :return: list of elements
        """
        result = [elements[0]]
        for index in range(1, len(elements)):
            if elements[index][0] > result[0][0]:
                result = [elements[index]]
            elif elements[index] == result[0][0]:
                result.append(elements[index])
        return result

    def move(self):
        """
        Bot chooses move.
        :return: int
        """
        tree = self.build_tree()

        # calculating best move
        sums = []
        for subtree in tree.childs(tree.get_root()):
            leafs = [leaf.data[0].check_winner() for leaf in tree.leafs(subtree)]
            for index in range(len(leafs)):
                if leafs[index] == self.symbol:
                    leafs[index] = 1
                elif leafs[index] is None:
                    leafs[index] = 0
                else:
                    leafs[index] = -1
            sums.append((sum(leafs), subtree.data[1]))
        return random.choice(Bot.biggest_elements(sums))[1]