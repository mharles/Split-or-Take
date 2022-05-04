import random

class Game:
    def __init__(self, id):
        self.p1Went = False #player made a move
        self.p2Went = False
        self.ready = False
        self.id = id # what clients are part of what game
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0
        self.prize = random.randint(100, 1000000)

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "S" and p2 == "S":
            winner = 2
        elif p1 == "S" and p2 == "T":
            winner = 1
        elif p1 == "T" and p2 == "S":
            winner = 0

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
        self.prize = random.randint(100, 1000000)


    