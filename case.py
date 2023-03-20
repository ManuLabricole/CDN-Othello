class Case:

    def __init__(self, position, isPlayable, isFree) -> None:
        self.position = position
        self.isPlayable = False
        self.isFree = True
        self.pion = None
        self.initFirstFour()
        

    def __str__(self):
        if self.isFree:
            return "Free"
        else:
            return "Not FREE"

    def __repr__(self) -> str:
        if self.isFree:
            return "F"
        else:
            self.pion.couleur
            return "X"
        
    # La function addPion doit recevoir en input un OBJET de class Pion    
    def addPion(self, pion):
        self.isFree = False
        self.pion = pion
        
    def isInPosition(self, positionSent):
        
        if self.position == positionSent:
            print(f"I m the case {self} at position : {self.position}")
            return True
        else:return False
        
    def getCase(self, position):
        if position == self.position:
            return self
        else:
            print("case doesn t exist")
        
    def initFirstFour(self):
        if int(self.position[0]) == 5:
            print(self.position[0])
            