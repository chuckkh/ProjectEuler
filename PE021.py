import math

def sumProperDivisors(inp):
    outp = {1,}
    for i in range(2,math.ceil(inp**0.5) + 1):
        if not inp % i:
            outp.add(i)
            outp.add(inp//i)
    return sum(outp)

def amicable(inp):
    s = sumProperDivisors(inp)
    t = sumProperDivisors(s)
    if t != s and t == inp:
        return s + t
    else:
        return 0

total = 0
for i in range(1, 10000):
    total += amicable(i)
print(total//2)


