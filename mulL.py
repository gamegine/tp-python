l = [1,1,4,8,3,76,8]

def MulL(l,l1):
    r = []
    for i in range(0, len(l)):
        r.append(l[i] * l1[i])
    return r
print( MulL(l,l) )