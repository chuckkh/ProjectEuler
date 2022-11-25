from PEtools import *

primes = {2:0, 3:0, 5:0, 7:0, 11:0, 13:0, 17:0, 19:0}



for i in range(2,21):
    for pr in primes.keys():
        power = 0
        while not i % pr:
            i //= pr
            power += 1
        if power > primes[pr]:
            primes[pr] = power

result = 1
for k in primes.keys():
    result *= (k**primes[k])

print(result)
