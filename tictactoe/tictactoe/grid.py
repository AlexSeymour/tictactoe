from collections import OrderedDict
from case import Case


def get_cases_empty():
    cases = {'a': [Case() for _ in range(3)],
             'b': [Case() for _ in range(3)],
             'c': [Case() for _ in range(3)]
             }

    #met les élements dans le bonne ordre
    return OrderedDict(sorted(cases.items(), key=lambda t: t[0]))


class Grid(object):


    def __init__(self):
        #Grid.sorted_grid()
        self.cases = get_cases_empty()

    @staticmethod
    def is_winner(line):
        """
        cette fonction  permet de trouver si une ligne est complété par le même joueur (si il a gagné la partie)
        :param line: ligne d' une grille comme: [1,1,1]
        :return: retourne l' id du joueur
        """

        winner = [_case.player for _case in line]

        winner = list(set(winner))

        if len(winner) == 1 and winner[0] != 0:
            return winner[0]


        return 0




    def __find_winner_horizontal(self):

        winner = None
        for y, x in self.cases.items():
            print(x)
            winner = Grid.is_winner(x)

            if winner:
                return x
        return None


    def __find_winner_vertical(self):
        winner = None
        line_y = []
        for index in range(3):
            for key in self.cases:
                line_y.append(self.cases[key][index])
            winner = self.is_winner(line_y)
            if winner:
                return line_y
            line_y = [] #reset

        return None



    def __find_winner_diagonal_left_to_right(self):
        winner = None
        line_diagonal = []

        for index, key in zip(range(3), self.cases.keys()):
            line_diagonal.append(self.cases[key][index])

        winner = Grid.is_winner(line_diagonal)

        if winner:
            return line_diagonal
        return None


    def __find_winner_diagonal_right_to_left(self):
        winner = None
        line_diagonal = []

        for index, key in zip([2, 1, 0], self.cases.keys()):
            line_diagonal.append(self.cases[key][index])

        winner = Grid.is_winner(line_diagonal)

        if winner:
            return line_diagonal
        return None


    def check_winner(self):
        """
        retourne une ligne complété par le même joueur (gagnant)
        """
        finded = self.__find_winner_diagonal_left_to_right()
        if finded is not None:
            return finded

        finded = self.__find_winner_diagonal_right_to_left()
        if finded is not None:
            return finded

        finded = self.__find_winner_horizontal()
        if finded is not None:
            return finded

        finded = self.__find_winner_vertical()
        if finded is not None:
            return finded

        return None

grid = Grid()