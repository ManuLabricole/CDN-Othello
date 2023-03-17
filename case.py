class Case:

    def __init__(self, position, isPlayable, isFree) -> None:
        self.position = position
        self.isPlayable = False
        self.isFree = True
        self.Pion = None
        self.initFirstFour()
        

    def __str__(self):
        if self.isFree:
            return "F"

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
        
    def initFirstFour(self):
        if int(self.position[0]) == 5:
            print(self.position[0])
            