# Soient les deux listes suivantes (voir à la fin de l’énoncé) : colors et
# values qui correspondent au couleurs et valeurs d’un jeu de 32
# cartes. Vous devez générer, dans une liste, le jeu de 32 cartes puis,
# le mélanger et enfin simuler une pioche dans ce jeu.
# Pour finir vous devez écrire un script permettant de simuler le jeu
# suivant : le jeu est gagnant si on tire un roi. Vous afficherez un
# message de succès ou d’échec en suivant cette condition.
# Les données des deux listes :
import random
values = {"7","8", "9", "10", "Valet", "Dame", "Roi", "As"}
colors = {"piques", "carreau", "treffle", "coeur"}
def makeList(c,v):
    c=list(c)
    v=list(v)
    for ci in range(len(c)):
        for vi in range(len(v)):
            yield [v[vi],c[ci]]
def randList(l):
    for i in range(len(l)-1):
        for i in range(len(l)-1):
            if random.getrandbits(1):#switch i i+1
                tmp = l[i]
                l[i] = l[i+1]
                l[i+1]=tmp
    return l
def simP(l):
    r=random.randint(0, len(l)-1)
    e=l[r]
    l.remove(l[r])
    return e
l = randList(list(makeList(colors,values)))
inPlay = True
while inPlay:
    e=simP(l)
    print(e)
    if e[0] == "Roi":
        print("win")
        inPlay=False
    else:
        print("loose")