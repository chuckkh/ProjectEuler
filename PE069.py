from PEtools import PEisPrime

res = 2

for i in range(3,999):
    if PEisPrime(i):
        if res * i <= 1000000:
            res *= i
        else:
            break
print(res)
