def sumDivisors(inp):
    total = 1
    dv = 2
    sq = inp**0.5
    while dv < sq:
        if not inp % dv:
            total += dv
            total += inp//dv
        dv += 1
    if int(sq)*int(sq) == inp:
        total += int(sq)
    return total

abund = []
for i in range(12,28124):
    if sumDivisors(i) > i:
        abund.append(i)

removed = set()
# The sum of all positive integers up to 28123
total = 28123*28124//2
#total = 0
for i in range(len(abund)):
     for j in range(i+1):
        sm = abund[i] + abund[j]
        if sm < 28124:
            if sm not in removed:
                removed.add(sm)
                total -= sm


print(total)



