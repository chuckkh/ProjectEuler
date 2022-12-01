from PEtools import *
import sys


side = 1000
if len(sys.argv) > 1:
    side = int(sys.argv[1])
total = side - 1
primes = PEfindPrimesUntilHalf(side)

for prime in primes:
    rng = side // prime - 1
    total += rng*(rng+1)//2
print(total*6)


#24 gets 11 from 2
#24 gets 7 from 3



# Project Euler Problem 351
# Hexagonal Orchards
# How many dots are invisible from the center of a hexagon of equilateral
# triangles with a side of length 100,000,000?

### I can easily calculate the slope of the line to each point between
### 0 and 60 degrees (inclusive/exclusive). The number of distinct values
### times 6 is the number of points *not* hidden from the center (plus 1
### for the center). The total number of points minus that is the answer.
### Or I could just count the number of duplicates, times 6.

#0 1
#1 3
#2 6
#3 10
#4 15
#5 21
# Still too much calculating. Even with radial symmetry.


# hidden out of:
# 5 5 (x6)
# 6 9
# for every layer added, add the number of ints lower than itself
# (including 1) that share a factor
# 7 10
# 8 14
# 9 17
#10 23

#total = 1177848//6 # given as part of the problem!
#for i in range(

# In other words, for each prime, every multiple of it is blocked
# For 10...
# L - 1 +...

from math import gcd

side = 100000000
side = 10
total = side - 1
total += side//2 - 1

for i in range(3,side//2+1):
#    mult = i - 1
#    for j in range(2,i):
#        if gcd(i,j) != 1:
#            mult -= 1
    total += 2 * (side//i - 1)
    #if PEisPrime(i):
    #if True:
    #    total += 2*(side//i) - 1


# each layer blocks:
# itself - 1 - (itself / each factor - 1)


print(total * 6)










