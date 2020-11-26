from scoresheets import YahtzyScoreSheet
from hands import YahtzyHand
from dice import D6


class Player(YahtzyScoreSheet):
    def __init__(self):
        self.score = 0
        self.scoreSheet = YahtzyScoreSheet()

    def rollDice(self):
        hand = YahtzyHand()
        return hand

    def updateScore(self, value):
        self.score = self.score + value