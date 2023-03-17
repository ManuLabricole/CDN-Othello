from case import Case
from board import Board


class Game:
    
    def __init__(self):
        self.board = None
        self.initGame()
        self.gameOn = True
        
    def initGame(self):
        self.board = Board()  
        
    def printGame(self):
        
        
        ligne1 = [el for el in self.board.listeCase if el.position[0] == 1]
        print(ligne1)
        


game = Game()
#print(game.board.listeCase)
print(len(game.board.listeCase))
game.printGame()