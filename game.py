from case import Case
from board import Board


class Game:
    
    def __init__(self):
        self.board = None
        self.initGame()
        self.gameOn = True
        
    def initGame(self):
        self.board = Board()
        print("game init")       


game = Game()
#print(game.board.listeCase)
game.board.display_game()