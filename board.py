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
        positionCase = [(3, 3), (4, 4), (3, 4), (4, 3)]
        colorPion = ["black", "black", "white", "white"]

        for i in range(4):
            case = self.getCase(positionCase[i])

            case.addPion(Pion(colorPion[i]))
            print(case)

    def getCase(self, position):
        # Ici les el sont des objets Case
        # Pour chaque case on appelle la methode isInPosition
        # Cette methode des cases return True si les coordonnees envoyees sont celles de la case
        # Des qu on recoit un True on a trouve la case et on la renvoit
        for el in self.listeCase:
            if el.isInPosition(position) == True:
                return el

        return None

    # The game will call this board function to check if this choice
    # has at least one neighbours to be playable
    def isChoicePlayable(self, choice, joueurColor):
        if joueurColor == "black":
            oppositeColor = "white"
        else:
            oppositeColor = "black"

        x = choice[0]
        y = choice[1]

        cases = [
            self.getCase(x, y-1),
            self.getCase(x, y+1),
            self.getCase(x-1, y),
            self.getCase(x+1, y)
        ]

        for case in cases:
            if case is not None:
                if case.pion.couleur == oppositeColor:
                    return True

        print("Apparently your choice is not valid, please place your pion around a neighbours")
        return False

    def get_case_jouable(self):

        listCaseJouable = list()
        for case in self.listeCase:
            if case.isPlayable():
                listCaseJouable.append(case)
        return listCaseJouable

    def set_case_jouable(self):
        return self.get_case_jouable

    def display_game(self):
        c = 0
        liste = self.listeCase
        # J'ai remis range 8 pour pouvoir énumérer les lignes déso
        print(f"    0   1   2   3   4   5   6   7 ")
        for a in range(8):

            print(f"  +---+---+---+---+---+---+---+---")
            print(
                f"{a} | {liste[c]} | {liste[c+1]} | {liste[c+2]} | {liste[c+3]} | {liste[c+4]} | {liste[c+5]} | {liste[c+6]} | {liste[c+7]} |")
            # pour itérer à travers les 64 cases
            c += 8
