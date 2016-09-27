


class Player(object):
    players = []
    current_player = None
    def __init__(self, name=None, sign="X"):

        Player.players.append(self)
        self.id = len(Player.players)
        self.name = 'p{}'.format(self.id) if name is None else name
        self.sign = sign
    @staticmethod
    def find_player_by_id(id_player):
        #TODO remplacer return None par exception
        for player in Player.players:
            if player.id == id_player:
                return player

        return None



