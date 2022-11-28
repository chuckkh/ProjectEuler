### This takes just about 60 seconds, so it might need some improvements.

def makePent(inp):
    return inp*(3*inp-1)//2

def isPent(inp):
    n = (inp*2)
    

d = 0
s = 0
a = 0
b = 0
done = False
pents = [1]
seed = 1
toAdd = 4
while not done:
    nextP = pents[-1] + toAdd
    toAdd += 3
#    seed += 1
    for p in pents:
        if p <= nextP//2:
            q = nextP - p
            d = q - p
            if q in pents and d in pents:
                print(d)
                done = True
                break
        else:
            break
    pents.append(nextP)
