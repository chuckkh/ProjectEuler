from PEtools import *

total = 2
i = 3
while i < 2000000:
    if PEisPrime(i):
        total += i
    i += 2
print(total)
