# Algorithme glouton de résolution de monnaie à rendre
# A CORRIGER
# NF.NSI

import math

# montant de la monnaie a rendre
montant = 1.65
# valeur des pieces disponibles en euro trié dans l'ordre croissant
pieces = [ 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 ]

## exemple de cas non optimal
## montant = 21
## pieces = [ 18, 7, 1 ]

def Monnaie(somme, ListeMontant):
    somme = somme
    # tableau de nombre de piece max a rendre selon le tableau de pieces
    ListeNbPieces=[]

    for i in ListeMontant:

        # parcours de la liste des pieces
        for k in range(len(ListeMontant)):
            # recupere le nombre de piece selon le quotient (entier //)
            ListeNbPieces.append(somme//i)

            # somme restante a deduire du montant
            somme+=math.floor(somme%ListeMontant[k])

    return somme,ListeNbPieces

print(Monnaie(montant, pieces))
