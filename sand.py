
from sqlalchemy import false
from game import Game
from pion import Pion

game = Game()

game.board.display_game()


joueurCouleur = "black"
game.board.display_game()

# getChoice send a tupple
# This tupple get a Case if valid; otherwise ask an other tupple
isPlayable = False
while isPlayable == False:
    choice = game.getChoice()
    isPlayable = game.board.isChoicePlayable(
        choice=choice, joueurColor=joueurCouleur)
    game.board.display_game()
    print(isPlayable)
game.board.getCase(choice).addPion(Pion(joueurCouleur))
game.board.display_game()
# Here we need to first check if the target has the right neigbours before adding pion"

# target.addPion(Pion(joueurCouleur))

#isValid = game.board.isChoicePlayable(choice=choice, joueurColor=joueurCouleur)
# print(isValid)
