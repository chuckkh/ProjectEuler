#!/user/bin/env python3

maxnum = 0
maxsum = 0
maxstart = 0
start = 2

def nextPrime(current):
    if current < 2:
        return 2
    elif current == 2:
        return 3
    else:
        current += current%2 + 1
    isPrime = False
    while not isPrime:
        isPrime = True
        for i in range(3, int(current**0.5)+2, 2):
            if i < current and not current % i:
                isPrime = False
        if isPrime: return current
        current += 2

def isPrime(inp):
    if inp < 2:
        return False
    if inp == 2:
        return True
    if not inp % 2:
        return False
    for i in range(3, int(inp**0.5)+2, 2):
        if i < inp and not inp % i:
            return False
    return True
        
while start < 1000000:
    num = 1
    sum = start
    next = start
    maxNumFromHere = 0
    maxSumFromHere = 0
    while sum < 1000000:
        next = nextPrime(next)
        num += 1
        sum += next
        if isPrime(sum) and sum < 1000000:
            maxSumFromHere = sum
            maxNumFromHere = num
    if maxNumFromHere > maxnum:
        maxnum = maxNumFromHere
        maxsum = maxSumFromHere
        maxstart = start
#    print("starting from", start, ",", maxNumFromHere, "primes add up to", maxSumFromHere)
 #   if maxNumFromHere < 300:
 #       break
    start = nextPrime(start)

outp = 'Starting from ' + str(maxstart) + ', ' + str(maxnum) + ' primes add up to ' + str(maxsum);
print(outp)
