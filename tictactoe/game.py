import itertools

from player import Player


class Game(object):
    p1 = Player(sign="X")
    p2 = Player(sign="O")
    current_player = None


    def __init__(self):

        self.next_tour = self.current_player_tour_per_tour_iterator()

        self.next_player()


    def current_player_tour_per_tour_iterator(self):
        for gamer in itertools.cycle(Player.players):
            Game.current_player = gamer
            yield Game.current_player


    def next_player(self):
        return next(self.next_tour)


game = Game()