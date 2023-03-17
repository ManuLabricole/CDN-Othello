
class Pion:

    def __init__(self, couleur, coordonnee):
        
        if couleur in ["black", "white"]:
            self.couleur = couleur
        else: 
            raise ValueError("message")

        self.coordonnee = coordonnee
    
        
    def __str__(self):
        if self.couleur == "black":
            return "X"
        elif self.couleur == "white":
            return "O"
        
        