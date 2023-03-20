
from pion import Pion
from joueur import Joueur

#Je défini une fonction winner qui actualisera 




def winner():
    joueur1 = Joueur("Khaleb", "black")
    joueur2 = Joueur("Manu", "white")
    score_joueur1=0
    score_joueur2=0
    for pion in list_pion:
        if pion.couleur == "black":
            score_joueur1 += 1
        else:
            score_joueur2 += 1
    if score_joueur2 < score_joueur2:
        gagnant= joueur2.name
    else:
        gagnant = joueur1.name
    print("Le score de Khaleb est de ", score_joueur1, "Le score de Manu est de ", "Le gagnant est", gagnant) 

pion1= Pion("black")
pion2= Pion("black")
pion3= Pion("black")
pion4= Pion("black")
pion5= Pion("white")

list_pion = [pion1, pion2, pion2]
print(pion1)

winner()
