from board import Board
board = Board()
liste = board.listeCase


#def print_grid(area, unit, liste):
#    for a in range(area):
#        print(("+" + "- " * (unit//2)) * area + "+")
#        for b in range(unit//2):
#            print(("|" + 'case' * (unit//2)) * area + "|")
#    print(("+" + "- " * (unit//2)) * area + "+")


#print_grid(8, 8)
#print(liste)

def ligne (longueur, largeur) :
    c = 0
    for c in range (longueur) :
            print (("+" + '----' + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-"))
            for b in range((largeur//8)):
                 print(f"| {liste[c]}   | {liste[c+1]}   | {liste[c+2]}   | {liste[c+3]}   | {liste[c+4]}   | {liste[c+5]}   | {liste[c+6]}   | {liste[c+7]}  |" )
                 c+=1


ligne(8,8)
liste[0]
