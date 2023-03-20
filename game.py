from case import Case
from board import Board


class Game:

    def __init__(self):
        self.board = None
        self.initGame()
        self.gameOn = True

    def initGame(self):
        self.board = Board()

    def checkBeforeTurn(self):
        pass

    def turn(self):
        isJouable = True
        firstChoicePosition = (4, 4)
        firstChoiceColor = "black"

        caseToPlay = self.board.getCase(firstChoicePosition)

    def checkAfterTurn(self):
        pass


game = Game()
case = game.turn()
