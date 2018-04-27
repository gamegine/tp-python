class FuncClass:
    def say():
        print("init is not need")

FuncClass.say()

class MSG:
    msg = "is init"
    #self is curent obj
    def say(self):
        print(self.msg)
#MSG.say() need init
m = MSG()
m.say()
MSG.say(m)

class Test:
    def __init__(self):# constructors
        self.msg = ""
    def __len__(self) # for len( obj )
        return len(self.msg)
    def __contains__(self) # for print obj
        return self.msg