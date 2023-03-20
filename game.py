from case import Case
from board import Board
from pion import Pion
from joueur import Joueur

class Game:

    def __init__(self):
        self.board = None
        self.initGame()
        self.gameOn = True
        self.getPlayers()


    def initGame(self):
        self.board = Board()
        
    def checkBeforeTurn(self):
        pass
    
    def validateChoice(self, choice):
        if len(choice) == 2:
            try:
                x = int(choice[0])
                y = int(choice[1])
                tupleChoice = (x, y)
                case = self.board.getCase(tupleChoice)
                
                if case is not None:
                    
                    if case.isFree:
                        print("Valid choice")
                    else:
                        print("case is not free : ")  
                        return False
                else:
                    print("It seems that the index given are out of range")
                    return False
            except:
                print("Input not a numbers, please insert digits")
                return False
        elif (len(choice)> 2):
            print("To many numbers, Please insert a valid input :")
        elif (len(choice)< 2) :
            print("Please insert two numbers : ")
            return False
        
    def getChoice(self):
        positionPlayed = input("Enter the 2 digits corresponding to the coordinate of your choice : ")
        isValid = self.validateChoice(positionPlayed)
        while isValid == False:
            positionPlayed = input("Please; insert valid inputs : ")
            isValid = self.validateChoice(positionPlayed)
        print("Turn finished !! ")
        
        return (int(positionPlayed[0]),int(positionPlayed[1]))
    
        
    

    def turn(self):
        choice = self.getChoice()

    def getPlayers(self):
        joueur_1 = Joueur(input("Hi player 1 what is your name ? : "), input("black or white ? : ") )
        joueur_2 = Joueur(input("Hi player 2 what is your name ? : "), input("black or white ? : ") )
        return joueur_1, joueur_2    

    def checkAfterTurn(self):
        pass

