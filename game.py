from case import Case
from board import Board
from pion import Pion


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
        secondChoicePosition = (5,5)
        firstChoiceColor = "black"
        secondChoiceColor = "black"
        
        thirdChoicePosition = (4,5)
        fourthChoicePosition = (5,4)
        thirdChoiceColor = "white"
        fourthChoiceColor = "white"

        caseToPlay = self.board.getCase(firstChoicePosition)
        caseToPlay.addPion(Pion(firstChoiceColor))

    def checkAfterTurn(self):
        pass


game = Game()
game.board.getCase((4, 4)).isFree = False
game.turn()
#case = game.board.getCase((4,4))
# case.addPion(Pion("black"))
# print(case.pion)
game.board.display_game()
