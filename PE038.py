class PanCheck:
    digits = ['1','2','3','4','5','6','7','8','9']
    def __init__(self, inp):
        self.seed = inp
        self.pan = self.isPanMult()
    def isPanMult(self):
        chain = ''
        mult = 1
        while len(chain) < 9:
            chain += str(self.seed * mult)
            mult += 1
        if len(chain) != 9:
            return False
        sortCheck = sorted([c for c in chain])
        if sortCheck == PanCheck.digits:
            return int(chain)
        else:
            return 0
    def updateSeed(self, newSeed):
        self.seed = newSeed
        self.pan = self.isPanMult()
        return self.pan

pc = PanCheck(192)
#print(pc.pan)

maximum = pc.pan
toTest = [i for i in range(90,100)]
for i in range(900,1000):
    toTest.append(i)
for i in range(9000,10000):
    toTest.append(i)
toTest.append(9)
for seed in toTest:
    panVal = pc.updateSeed(seed)
    if panVal > maximum:
        maximum = panVal

print(maximum)
