import math
import time

lolim = 1
uplim = 1000
div1 = 3
div2 = 5

uplim -= 1


def method1(div1, div2, lolim, uplim):
    def findLCM(arg1, arg2):
        lower = min(arg1, arg2)
        higher = max(arg1, arg2)
        outp = higher
        while outp % lower:
            outp += higher
        return outp
    lcm = findLCM(div1, div2)
    total = 0

    while lolim % lcm and lolim < uplim:
        if not lolim%div1 or not lolim%div2:
            total += lolim
        lolim += 1

    while uplim % lcm and uplim > lolim:
        if not uplim%div1 or not uplim%div2:
            total += uplim
        uplim -= 1
    #print("lolim", lolim)
    #print("uplim", uplim)
    #print("total", total)
    if uplim > lolim:
        mult = 0
        average = -1
        for i in range(lolim, lolim+lcm):
            if not i%div1 or not i%div2:
                mult += 1
        limSum = lolim + uplim
        limDif = uplim - lolim
        #Something is still not correct here!
        total += math.ceil(limDif/lcm/2*mult) * limSum
    # 33 * 1005 * 7 + 4*1005 -1005-1002
    return total

#print("mult", mult, ". average", average, ". limSum", limSum, ". limDif", limDif)

#234168
# 33*1005*7 +4*1005

#1005/15 = 67

def method2(div1, div2, lolim, uplim):
    gen = (i for i in range(lolim, uplim+1) if not i%3 or not i%5)
    total = sum(gen)
    return total

t1 = time.perf_counter_ns()
res1 = method1(div1, div2, lolim, uplim)
t2 = time.perf_counter_ns()
res2 = method2(div1, div2, lolim, uplim)
t3 = time.perf_counter_ns()
print("method1:", res1, "time:", t2-t1)
print("method2:", res2, "time:", t3-t1)
