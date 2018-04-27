l = [1,4,8,6,7,3,4]
def max(l):
    m,mp = l[0] , l
    for e in range(len(l)):
        if l[e] > m :
            m,mp = l[e],e
    return m,mp
print(max(l))