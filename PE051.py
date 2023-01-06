import PEtools

pr = [[],[],[]]

for i in range(100000, 1000000):
    s = str(i)
    for ind in range(3):
        if s.count(str(ind)) > 2 and PEtools.PEisPrime(i):
            pr[ind].append(s)

for ind in range(3):
    p = pr[ind]
    for prime in p:
        tot = 0
        for i in range(1,10):
            if PEtools.PEisPrime(int(prime.replace(str(ind), str(i)))):
                tot += 1
        if tot >= 8:
            print(prime)
            break

    
