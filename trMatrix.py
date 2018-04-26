matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
def transpose (m):
    r = []
    for x in range(0,len(m)):
        r.append([m[0][x]])
    for x in range(0,len(m)):
        for y in range(1,len(m[0])):
            r[x].append(m[y][x])
    return r
print(transpose(matrix))