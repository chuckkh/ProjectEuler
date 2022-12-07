from math import log10

def isPan(inp):
    all = [1,2,3,4,5,6,7,8,9]
    while inp:
        nxt = inp%10
        if nxt in all:
            all.remove(nxt)
        else:
            return False
        inp //= 10
    if all == []:
        return True
    else:
        return False


def isDoublePan(inp):
    return isPan(inp%1000000000) and isPan(inp // 10**(int(log10(inp)-8)))

def fibGen():
    s = [1,1]
    sindex = 0
    while True:
        yield s[sindex]
        s[sindex] += s[1-sindex]
        sindex = 1-sindex

f = fibGen()
res = 0
k = 0
while not isDoublePan(res):
    res = next(f)
    k += 1
print(k)
