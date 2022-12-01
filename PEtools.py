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
    
