from board import Board
board = Board()
#liste = board.listeCase


#def print_grid(area, unit, liste):
#    for a in range(area):
#        print(("+" + "- " * (unit//2)) * area + "+")
#        for b in range(unit//2):
#            print(("|" + 'case' * (unit//2)) * area + "|")
#    print(("+" + "- " * (unit//2)) * area + "+")


#print_grid(8, 8)
#print(liste)

def ligne (longueur, largeur) :
    for c in range (longueur) :
            print (("+" + '----' + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-" + "+" + "----" + "-"))
            for b in range((largeur//4)):
                 print("|" + "case1" +"|" + 'case2'+"|" + 'case3'+"|" + 'case4'+"|" + 'case5'+"|" + 'case6'+"|" + 'case7'+"|" + 'case8'+"|" )


ligne(8,8)
bl
