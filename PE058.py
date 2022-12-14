from PEtools import PEisPrime

side = 7
gap = 6
top = 49
numPrimes = 8
numAll = 13
while numPrimes*10 >= numAll:
    side += 2
    gap += 2
    for i in range(4):
        top += gap
        if PEisPrime(top):
            numPrimes += 1
    numAll += 4
print(side)
