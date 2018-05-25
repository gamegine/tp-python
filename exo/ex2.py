# Soit la chaîne de caractères text suivantes :
# text="aaabbhhdddcccjjhhggffqqllkki iooouuurrrrppppqqqooo okkk
# llllooooppprrrr tttt"
# Écrire un script qui permet de compter le nombre d’occurences de
# chaque lettre dans la chaîne de caractères text. Les espaces ne sont
# pas à compter. Vous placerez le résultat dans un dictionnaire : D
# ={ ’a’ : 3, ... }.
# Puis vous calculerez la fréquence de chaque lettre dans le
# dictionnaire D dans une liste frequences.
import json #for good print
text="aaabbhhdddcccjjhhggffqqllkki iooouuurrrrppppqqqooo okkkllllooooppprrrr tttt"
def c(text):
    text = text.replace(" ", "")# no space
    tmp={}
    for e in text:
        if not e in tmp:
            tmp[e]=1
        else:tmp[e]+=1
    return tmp
def freq(l,text):
    for e,n in l.items():
        yield [e,(n/len(text))]
def conca(el,fr):
    i = 0
    for e,n in el.items():
        yield [e,n,fr[i][1]]
        i+=1
co = c(text)
print(json.dumps( list(conca(co,list(freq(co,text)))) ,indent=2))