from PEtools import *

# primes = PEfindPrimesUntil(999998)
total = []

# 3-6 digits from:
# 1379

digits = ('1','3','7','9')
# and every number must have either 1 or 7
# But I didn't need to check this

current = [0,0,0]
total = 13
primes = []
ln = len(current)
while ln < 7:
    primes = []
    while True:
        # logic
        candidate = ''
        for d in current:
            candidate += digits[d]
#        print(candidate)
        candcopy = candidate
        if candcopy not in primes:
            pr = True
            tempprimes = []
            while PEisPrime(int(candcopy)):
                tempprimes.append(candcopy)
                candcopy = candcopy[1:] + candcopy[0]
                if candcopy == candidate:
                    break
            if candcopy == candidate:
                primes += tempprimes
        
        lc = len(current)
        for dind in range(lc):
#            print('current', current)
            if current[dind] == 3:
                current[dind] = 0
            else:
                current[dind] += 1
                break
        if sum(current) == 0:
            total += len(primes)
            current.append(0)
            ln += 1
            break
print(total)
