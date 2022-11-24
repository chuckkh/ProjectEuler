oddComposite = 9
canBeWritten = True

def isPrime(inp):
    if inp < 2:
        return False
    if inp == 2:
        return True
    if not inp % 2:
        return False
    fact = 3
    while fact < inp**0.5+1:
        if not inp % fact:
            return False
        fact += 2
    return True

def findOddPrimes(inp):
    res = []
    next = 3
    while next <= inp:
        if isPrime(next):
            res.append(next)
        next += 2
    return res

# prime + 2*(n**2)
while canBeWritten:
    if not isPrime(oddComposite):
        canBeWritten = False
        for prime in findOddPrimes(oddComposite):
            sq = (oddComposite - prime)//2
            if int(sq**0.5)**2 == sq:
                canBeWritten = True
                break
        if not canBeWritten:
            print(oddComposite)
            break
    oddComposite += 2

