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

    def initCase (self):
        for i in range(8):
            for j in range(8):
                self.listeCase.append(Case(position=(i,j), isFree=True, isPlayable=False))


    def get_case_jouable(self):
        listCaseJouable = list()
        for case in self.listeCase:
            if case.is_jouable():
                listCaseJouable.append(case)
        return listCaseJouable

    def set_case_jouable(self):
        return self.get_case_jouable

    def display_game(self):
        game = np.array(self.listeCase)
        return game
