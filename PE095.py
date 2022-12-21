def addFactors(inp):
    total = 1
    for i in range(2, int(inp**0.5)+1):
        if not inp%i:
            total += i
            total += inp//i
    return total


cache = {}
used = set()
longest = 0
longSeed = 0
for i in range(12000, 1000000):
    total = 0
    used = set()
    if i in cache:
        res = cache[i]
    else:
        res = addFactors(i)
        cache[i] = res
    
    while res < 1000001 and res not in used:
        used.add(res)
        total += 1
        if res in cache:
            res = cache[res]
        else:
            temp = addFactors(res)
            cache[res] = temp
            res = temp
    if total > longest and i in used:
        longest = total
        longSeed = i

print(longSeed)
