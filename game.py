from case import Case
from board import Board
from pion import Pion
from joueur import Joueur

class Game:

    def __init__(self):
        self.board = None
        self.initGame()
        self.gameOn = True
        #self.getPlayers()


    def initGame(self):
        self.board = Board()
        
    def checkBeforeTurn(self):
        pass
    
    def validateChoice(self, choice):
        if len(choice) == 3:
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
        elif (len(choice)> 3):
            print("To many numbers, Please insert a valid input :")
        elif (len(choice)< 3) :
            print("Please insert two numbers : ")
        
            return False
        
    def getChoice(self):
        positionPlayed = input("Enter the 2 digits corresponding to the coordinate of your choice : ")
        x, y = positionPlayed.split(",")
        isValid = self.validateChoice(positionPlayed)
        while isValid == False:
            positionPlayed = input("Please; insert valid inputs : ")
            isValid = self.validateChoice(positionPlayed)
        print("Turn finished !! ")
        
        return (int(x),int(y))
    
        
    

    def turn(self, joueur):
        choice = self.getChoice
        if Board.isChoicePlayable(choice, joueur) :
            add = Case.addPion(choice, joueur.couleur)




    def getPlayers(self):
        joueur = Joueur(input("Hi player what is your name ? : "), input("black or white ? : ") )
        
        return joueur   

    def checkAfterTurn(self):
        pass



    def partie (self) :
        compteur = 0
        joueur_1  = self.getPlayers()
        joueur_2  = self.getPlayers()
        while True :
            self.board.display_game()
            if compteur % 2 == 0 :
                self.turn(joueur_1)
            else :
                self.turn (joueur_2)
            self.board.display_game()


