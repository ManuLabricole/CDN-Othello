
class Joueur:

    def __init__(self, name, couleur) :
        self.name = name
        self.couleur = couleur

    @property
    def couleur(self):
        return self.__couleur
    
    @couleur.setter
    def couleur(self, newColor):
       self.__couleur = newColor

#canPlay est une fonction qui a défini si le joueur pouvait jouer

    #def play(self):
        #if canPlay  

    def play(self):
        if canPlay :
            choixCaseJouee =input("Où souhaitez-vous jouer votre pion ? Indiquer (i, j)")
        else :
            return "Le joueur passe son tour"
           

   

    

    

    