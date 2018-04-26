l = ['A','Z','E','R','T','Y','U','I','O','P']

def IsMaj():
    for e in l:
        if e.islower() :
            return False
    return True
print(IsMaj())