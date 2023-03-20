class Case:

    def __init__(self, position, isPlayable=False, isFree=True) -> None:
        self.position = position
        self.isPlayable = isPlayable
        self.isFree = isFree
        self.pion = None

    def __str__(self):
        if self.isFree:
            return " "
        else:
            if self.pion.couleur == "black":
                return "X"
            else:
                return "O"

    def __repr__(self) -> str:
        if self.isFree:
            return " "
        else:
            if self.pion.couleur == "black":
                return "X"
            else:
                return "O"

    # La function addPion doit recevoir en input un OBJET de class Pion
    def addPion(self, pion):
        self.isFree = False
        self.pion = pion

    def isInPosition(self, positionSent):

        if self.position == positionSent:
            #print(f"I m the case {self} at position : {self.position}")
            return True
        else:
            return False

    def isPlayable(self, currentCaseList, joueurColor):

        x=self.position[0]
        y=self.position[1]
        
