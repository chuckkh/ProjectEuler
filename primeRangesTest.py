import sys

lim = 1000
if len(sys.argv) > 1:
    lim = int(sys.argv[1])
primes = [2]
cand = 3
for cand in range(3,lim//2 + 1,2):
    ispr = True
    for pr in primes:
        if not cand % pr:
            ispr = False
    if ispr:
        primes.append(cand)

total = 0
for prime in primes:
    qu = lim//prime
    toAdd = (qu*(qu-1))//2
    total += toAdd
total += lim - 1

print(total * 6)
