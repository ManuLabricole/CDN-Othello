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
    
    def validateChoice(self, choice):
        if len(choice) == 2:
            try:
                x = int(choice[0])
                y = int(choice[1])
                
            except:
                print("Input not a numbers, please insert digits")
        elif (len(choice)> 2):
            print("To many numbers, Please insert a valid input :")
            return False
    

    def turn(self):
        positionPlayed = input("Enter the 2 digits corresponding to the coordinate of your choice :")
        isValid = self.validateChoice(positionPlayed)
        while isValid == False:
            positionPlayed = input()
            isValid = self.validateChoice(positionPlayed)
        
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
#game.board.getCase((4, 4)).isFree = False
#game.turn()
#case = game.board.getCase((4,4))
# case.addPion(Pion("black"))
# print(case.pion)
game.board.display_game()
game.turn()

