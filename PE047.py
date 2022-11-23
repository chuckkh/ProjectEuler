def uniquePrimes(inp):
    res = 0
    if not inp%2:
        res = 1
        while not inp%2:
            inp //= 2
    factor = 3
    while inp > 1:
        if not inp%factor:
            res += 1
            while not inp%factor:
                inp //= factor
        factor += 2
    return res


outp = 1
ln = 1
current = 210
while ln < 4:
    current += 1
    if uniquePrimes(current) == 4:
        ln += 1
        if ln == 4:
            outp = current - 3
    else:
#        if ln>1:
#            print(ln)
        ln = 0
print(outp)
