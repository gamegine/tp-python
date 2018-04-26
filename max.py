l = [1,4,8,6,7,3,4]
def max():
    m = l[0]
    for e in l:
        if e > m :
            m = e
    return m
print(max())