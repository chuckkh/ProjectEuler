from PEtools import PEisPrime

a = 2
b = 2
c = 2

# max 7071 ** 2
# max 368 ** 3
# max 84 ** 4

# a2 + b3 + c4 < 50000000

primes = [2,3,5,7,11,13,17,19]
primeSeed = 23
while primeSeed <= 7071:
    if PEisPrime(primeSeed):
        primes.append(primeSeed)
    primeSeed += 2

s = set()

for c in primes:
    for b in primes:
        for a in primes:
            cand = a**2 + b**3 + c**4
            if cand < 50000000:
                s.add(cand)
            else:
                break
        if 2**2 + b**3 + c**4 >= 50000000:
            break
    if 2**2 + 2**3 + c**4 >= 50000000:
        break
print(len(s))
    





