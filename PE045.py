### T = n(n+1)/2
###
### P = n(3n-1)/2
###
### H = n(2n-1)

def getHex(inp):
    return inp * (2 * inp - 1)

def getPent(inp):
    return int(inp * (3 * inp - 1) / 2)

chex = 144
cpent = 166
p = getPent(cpent)
hexes = []

while p not in hexes:
    hexes.append(getHex(chex))
    p = getPent(cpent)
    chex += 1
    cpent += 1
print(p)

