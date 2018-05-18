"""
La logique du jeu est placé dans la classe ci-dessous
"""

class Game:
    def __init__(self, battlem):
        self.battle = battlem
        self.PLayer0 = 0
        self.PLayer1 = 0
    def Play(self, t):
        t.split(" ")
        int(t[0])
        int(t[1])
        if t[0] == t[1]:
            print("no round win")
            return
        if t[0] > t[1]:
            self.PLayer0+=1
            print("player 1 +1")
        else:
            self.PLayer1+=1
            print("player 2 +1")
    def End(self):
        if self.PLayer0 > self.PLayer1:
            print("player 1 win")
        else:
            print("player 2 win")
    def Round(self):
        for e in self.battle:
            self.Play(e)
        self.End()
# bootstrap du jeu

battle = [
    '19', '3 10', '1 2', '2 6', '1 2', '10 1', '8 5', '8 3', '9 7', '3 4',
    '5 9', '3 7', '3 6', '2 6', '6 10', '7 4', '1 10', '4 1', '9 1', '6 2',
]

g = Game(battle)
g.Round()