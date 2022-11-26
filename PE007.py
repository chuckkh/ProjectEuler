from PEtools import *

thisPrime = 3
whichPrime = 2
while whichPrime < 10001:
    thisPrime += 2
    if PEisPrime(thisPrime):
        whichPrime += 1
print(thisPrime)
