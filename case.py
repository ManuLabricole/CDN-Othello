class Case:

    def __init__(self, position, isPlayable, isFree) -> None:
        self.position = position
        self.isPlayable = False
        self.isFree = True
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
            print(f"I m the case {self} at position : {self.position}")
            return True
        else:
            return False
