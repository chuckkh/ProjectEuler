# Hmm
import math
import time

def powMod(b, p, m):
    outp = 1
    for i in range(p):
        outp = (outp*b)%m
    return outp



total = 0
lim = 1000001
lim = 1000
for i in range(2,lim):
    seed = 0
    for p in range(1,100,1):
        if i**p%100 == p%100:
            seed = p
            break
    if seed < 2:
        continue
    
    for p10 in range(3, 10):
        print(i, p10, seed)
        lastSeed = seed
        upp = seed + int(10**p10)
        step = math.ceil(10**(p10-1))
#        print("upp", upp, "step", step)
        for p in range(seed, upp, step):
            if powMod(i, p, 10**p10) == p%(10**p10):
#            if i**p%(10**p10) == p%(10**p10):
                seed = int(p)
                break
        if seed == lastSeed:
            seed = 0
            break
    total += seed
    print(i, seed)
            
        


# THIS WORKS:
#for i in range(1,100,1):
#    if 157**i%100 == i%100:
#        print(i)
#
#for i in range(57, 1057, 100):
#    if 157**i%1000 == i%1000:
#        print(i)
# BUT THE ALGORITHM DOES NOT
























class EndingReference:
    def __init__(self, rng=1000000, digits=2):
        endings = {}
        endingLegend = [-1,-1]
        maxlen = 0
        t1 = time.time()
        for i in range(2,rng+1):
            s = set()
            for p in range(2,(10**(digits))):
                n = (i ** p) % (10**digits)
                if n == p % (10**digits):
                    if n in s:
                        break
                    else:
                        s.add(n)
            found = False
            s = sorted(s, reverse=True)
            for k in endings.keys():
                if endings[k] == s:
                    found = True
                    endingLegend.append(k)
                    break
            if not found:
                endingLegend.append(i)
                endings[i] = s
        self.endings = endings
        self.endingLegend = endingLegend
        t2 = time.time()
        print(t2-t1, "to build the EndingReference")


#ef = EndingReference(1000000, 2)




# The largest positive integer less than 10**9 where x == (n**x)%(10**9)
if False:
    total = 0
    for i in range(2,1000001):
        e = ef.endings[ef.endingLegend[i]]
        done = False
        for pref in range(10**7-1, 0, -1):
            if done:
                break
            for suff in e:
                cand = pref*100 + suff
                if (i**cand)%10**9 == cand:
                    total += cand
                    done = True
                    break
    print(total)

