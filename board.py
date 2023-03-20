from case import Case
from pion import Pion
#from joueur import joueur
#from game import game
import numpy as np


class Board:

    def __init__(self):
        self.listeCase = list()
        self.listCaseJouable = list()
        self.set_case_jouable()
        self.initCase()
        self.initFirstFour()

    def initCase(self):
        for i in range(8):
            for j in range(8):
                self.listeCase.append(
                    Case(position=(i, j), isFree=True, isPlayable=False)
                )

    def initFirstFour(self):
        positionCase = [(4, 4), (5, 5), (4, 5), (5, 4)]
        colorPion = ["black", "black", "white", "white"]

        for i in range(4):
            case = self.getCase(positionCase[i])
            case.addPion(Pion(colorPion[i]))

    def getCase(self, position):
        # Ici les el sont des objets Case
        # Pour chaque case on appelle la methode isInPosition
        # Cette methode des cases return True si les coordonnees envoyees sont celles de la case
        # Des qu on recoit un True on a trouve la case et on la renvoit
        for el in self.listeCase:
            if el.isInPosition(position) == True:
                return el

    def getChoice():
        # Input from joueur
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
        c = 0
        liste = self.listeCase
        for c in range (8) :
            print (("+" + '----' + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-"))
            for b in range((8//8)):
                 print(f"| {liste[c]}   | {liste[c+1]}   | {liste[c+2]}   | {liste[c+3]}   | {liste[c+4]}   | {liste[c+5]}   | {liste[c+6]}   | {liste[c+7]}  |" )
                 c+=1


        game = np.array(self.listeCase)
        return print(game)
