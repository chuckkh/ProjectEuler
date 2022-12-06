from math import factorial

fac = [1, 1]

for i in range(2,10):
    fac.append(factorial(i))

def sumf(inp):
    t = inp
    res = 0
    while t:
        res += fac[t%10]
        t //= 10
    return res


total = 0
for i in range(3, 1000000):
    if sumf(i) == i:
        total += i
print(total)
