from case import Case
#from pion import pion
#from joueur import joueur
#from game import game
import numpy as np


class Board:

    def __init__(self):
        ListeCase = list()
        ListCaseJouable = list()
        self.set_case_jouable()
        self.initCase()

    #def initCase(self, case):
    #    x = 0
    #    y = 0
    #    for jeu in range(64):
    #        case.position = (x+1, y)
    #        self.ListeCase.append(case)
    #        x += 1
    #        if x > 8:
    #            x = 0
    #            y += 1
    #            case.position = (x, y)
    #            self.ListeCase.append(case)
    #            x += 1
#
    #    return ListeCase
    
    def initCase(self):
        for i in range(8):
            for j in range(8):
                self.ListeCase.append(Case(position=(i,j), isFree=True, isPlayable=False))


    def get_case_jouable(self):
        ListCaseJouable = list()
        for case in self.ListeCase:
            if case.is_jouable():
                ListCaseJouable.append(case)
        return ListCaseJouable

    def set_case_jouable(self):
        return self.get_case_jouable
