import math

def PEisPrime(inp):
    if inp < 2:
        return False
    elif inp == 2:
        return True
    elif not inp % 2:
        return False
    else:
        fact = 3
        while fact < inp**0.5+2 and fact != inp:
            if not inp % fact:
                return False
            fact += 2
        return True

def PEfindPrimesUntil(inp):
    if inp < 2: return []
    elif inp == 2: return [2]
    else:
        pr = [2]
        val = 3
        while val <= inp:
            prime = True
            for p in pr:
                if not val % p:
                    prime = False
                    break
            if prime:
                pr.append(val)
            val += 2
        return pr
                
        
def PEfindPrimesUntilHalf(inp):
    if inp < 2: return []
    elif inp == 2: return [2]
    else:
        pr = [2]
        val = 3
        while val < inp//2+1:
            prime = True
            for p in pr:
                if not val % p:
                    prime = False
                    break
            if prime:
                pr.append(val)
            val += 2
        return pr
                
        
    
def PEnumberOfDivisors(inp):
    '''This includes 1 and n'''
    outp = 2
    for i in range(2,inp//2+1):
        if not inp % i:
            outp += 1
    return outp

def PEdigitSum(inp):
    total = 0
    while inp:
        total += inp%10
        inp//=10
    return total

def PElowerWithCommonFactors(inp):
    total = 0
    primes = PEfindPrimesUntilHalf(inp)
    for i in range(2,inp):
        for prime in primes:
            if not i % prime and not inp % prime:
                total += 1
                break
        
    return total
    
def PEfactor(inp, lim = -1):
    for prime in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59):
        if not inp % prime:
            return (prime, inp//prime)
    sq1 = math.ceil(inp**0.5)
    if lim == -1:
        lim = sq1 * 1.3
    invlim = math.ceil(inp / lim)
    diff = abs(inp - sq1*sq1)
    sq2 = math.floor(diff**0.5)
    while sq2*sq2 != diff and sq1 <= lim:
        sq1 += 1
        diff = abs(inp - sq1*sq1)
        sq2 = math.floor(diff**0.5)
    if sq2*sq2 == diff:
        outp = (sq1 + sq2, sq1 - sq2)
    else:
        cand = 59
        while cand < invlim:
            cand += 2
            if not inp % cand:
                outp = (inp//cand, cand)
                break
        if inp % cand:
            outp = (inp, 1)
    return outp

def PEgcd(a, b):
    while a != b:
        mn = min(a,b)
        a, b = max(a,b)-mn, mn
    return a
