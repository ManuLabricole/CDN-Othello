
from pion import Pion
from joueur import Joueur
from game import Game

#Je défini une fonction winner qui actualisera 




def winner(joueur_1, joueur_2):
    score_joueur1=0
    score_joueur2=0
    for pion in list_pion:
        if pion.couleur == "black":
            score_joueur1 += 1
        else:
            score_joueur2 += 1
    if score_joueur2 < score_joueur2:
        gagnant= joueur_2.name
    else:
        gagnant = joueur_1.name
    #ajouter un if la partie est terminée 
    print("Le score de Khaleb est de ", score_joueur1, "Le score de Manu est de ", "Le gagnant est", gagnant) 

pion1= Pion("black")
pion2= Pion("black")
pion3= Pion("black")
pion4= Pion("black")
pion5= Pion("white")

list_pion = [pion1, pion2, pion2]
print(pion1)

winner()
