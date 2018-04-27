l = "a zer ty uiop"
def comptStr():
    r = l.split(" ")
    """di = []
    [di.append((r[i],len(r[i]))) for i in range(len(r))]
    return dict(di)"""
    return dict([ (r[i],len(r[i])) for i in range(len(r)) ])
print(comptStr())