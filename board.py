from case import Case
#from pion import pion
#from joueur import joueur
#from game import game
import numpy as np


class Board:

    def __init__(self):
        self.listeCase = list()
        self.listCaseJouable = list()
        self.set_case_jouable()
        self.initCase()

    def initCase(self):
        for i in range(8):
            for j in range(8):
                self.listeCase.append(
                    Case(position=(i, j), isFree=True, isPlayable=False))

    def getCase(self, position):
        # Ici les el sont des objets Case
        # Pour chaque case on appelle la methode isInPosition
        # Cette methode des cases return True si les coordonnees envoyees sont celles de la case
        # Des qu on recoit un True on a trouve la case et on la renvoit
        for el in self.listeCase:
            if el.isInPosition(position) == True:
                return el
            
    def getChoice():
        #Input from joueur
        pass

    def get_case_jouable(self):
        listCaseJouable = list()
        for case in self.listeCase:
            if case.is_jouable():
                listCaseJouable.append(case)
        return listCaseJouable

    def set_case_jouable(self):
        return self.get_case_jouable

    def display_game(self):
        for c in range (8) :
            print (("+" + '----' + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-"))
            for b in range((largeur//4)):
                print("|" + "case1" +"|" + 'case2'+"|" + 'case3'+"|" + 'case4'+"|" + 'case5'+"|" + 'case6'+"|" + 'case7'+"|" + 'case8'+"|" )

        
        
        game = np.array(self.listeCase)
        return print(game)
