
from game import Game
from pion import Pion

game = Game()

game.board.display_game()


joueurCouleur="black"
case43=game.board.getCase((5,5))
case43.addPion(Pion(joueurCouleur))
game.board.display_game()

caseList = game.board.listeCase
case11 = game.board.getCase((1,1))
print(case11)
case11.addPion(Pion(joueurCouleur))
print(case11)
game.board.display_game()
