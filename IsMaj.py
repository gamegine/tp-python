l = ['A','Z','E','R','T','Y','U','I','O','P']

def IsMaj():
    """for e in l:
        if e.islower() :
            return False
    return True"""
    return all( [ e.isupper() for e in l ] ) #no opti (need chack all)

print(IsMaj())