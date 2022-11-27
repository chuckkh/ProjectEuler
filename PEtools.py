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

def PEnumberOfDivisors(inp):
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
