EMPTY = 0


class Case(object):
    """
    Représente la case d' une grille
    """
    nb_case = 0

    def __init__(self, player=None, status=EMPTY):
        Case.nb_case += 1
        self.id = Case.nb_case
        self.status = status
        self.player = player

    def __repr__(self):
        if self.player is None:
            return ""
        else:
            return self.player.name