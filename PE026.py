from PEtools import *

maxlen = 0
maxnum = 0
num = 3
for num in range(7,1001,2):
    if PEisPrime(num):
        ln = 0
        mult = 9
        while mult % num:
            mult *= 10
            mult += 9
            ln += 1
        if ln > maxlen:
            maxlen = ln
            maxnum = num
print(maxnum)
