
class Pion:

    def __init__(self, couleur):  # , coordonnee):

        if couleur in ["black", "white"]:
            self.couleur = couleur
        else:
            raise ValueError(
                "Try again : Les jetons sont soit blancs, soit noirs")

        # if isinstance(coordonnee, tuple):
        #    self.coordonnee = coordonnee
        # else:
        #    raise ValueError("Try again : Merci d'indiquer les coordonnes sous le format suivant (x,y)")

    def __str__(self):
        return f"I'm a {self.couleur} PION"
#
    # def flip(self):
    #    if couleur == "black":
    #        couleur == "white"
    #    else:
    #        couleur == "black"
