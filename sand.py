
from game import Game

game = Game()
#game.board.getCase((4, 4)).isFree = False
#game.turn()
#case = game.board.getCase((4,4))
# case.addPion(Pion("black"))
# print(case.pion)
game.board.display_game()

game.turn()

