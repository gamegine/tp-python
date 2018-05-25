# On souhaite mettre en place un algorithme permettant d’odronner
# une liste de nombres par ordre croissant en utilisant un tri
# particulier :
# tri à bulle
# .
# Au départ on compare chaque nombre de la liste à trier deux à
# deux et on permute, à chaque comparaison, le nombre le plus grand
# est placé à droite de la liste, une fois la liste parcourue en entier, on
# aura déplacé le plus grand nombre complétement à droite. On
# répéte l’opération sur la même liste moins le dernier nombre qui est
# déjà placé complètement à droite, ainsi de suite. L’algorithme
# s’arrête lorsqu’on ne peut plus parcourir la liste, elle est alors
# ordonnée par ordre croissant.
# Mettez en place cet algorithme en Python.
l = [1,1,2,7,3,9,8]
def order(l):
    for i in range(len(l)-1):
        for i in range(len(l)-1):
            if l[i] >= l[i+1]:#switch i i+1
                tmp = l[i]
                l[i] = l[i+1]
                l[i+1]=tmp
    return l
print(list(order(l)))