# Présentation des règles du jeux :
# Le joueur 1 choisi un nombre compris entre 1 et 100
# À tour de rôle, chaque joueur choisi un nombre parmi les
# multiples ou diviseurs du nombre choisi précédemment par son
# adversaire, ce nombre est également inférieur à 100.
# Un nombre déjà joué ne peut être rejoué.
# Le perdant est le joueur qui ne peut plus proposer un multiple
# ou diviseur.
# 2 / 6
# Problème Juniper Green 2/2 fonctions utiles 5pts
# Écrivez les fonctions utiles suivantes pour le jeu :
# Générer une liste des valeurs possibles :
# possibles
from random import randint
def divisor(n):
    tmp = []
    i=n
    while i >= 1:
        if n%i == 0 and n//i in possibles:
            tmp.append(n//i)
        i-=1
    return tmp
def multiple(n):
    tmp=[]
    i=2
    while i*n <= nmax :
        if i*n in possibles: 
            tmp.append(i*n)
        i+=1
    return tmp
def divAndMult(n):return divisor(n) + multiple(n)
####
nmax = 100
possibles = list(range(1,nmax+1))  
selectednbr=2*randint(1,nmax/2)      
possibles.remove(selectednbr)
print("hi we play whit numbers 1-",nmax)
print("i start with number ",selectednbr)
val = divAndMult(selectednbr)

while val != []:
    print("valid numbers :",val)
    nbr=int(input("what do you play ? "))
    while nbr not in val:nbr=int(input("not good. what do you play ? "))
    possibles.remove(nbr)
    val = divAndMult(selectednbr)

    if val == []:print("you win")
    else:
        selectednbr = val[randint(0,len(val)-1)]
        print("valid numbers :",val)
        print("i play ",selectednbr)
        possibles.remove(selectednbr)        
        val = divAndMult(selectednbr)
        if val == []:print("you fail!")