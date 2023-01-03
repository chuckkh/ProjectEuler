# 01
# 04
# 09
# 16
# 25
# 36
# 49
# 64
# 81

pairs = ((0,1), (0,4), (0,6), (1,6), (1,8), (2,5), (3,6), (4,6))

die1 = [0,1,2,3,4,5]
die2 = [0,1,2,3,4,5]

def nextDie(dinp):
    ind = 1
    die = dinp.copy()
    # Find the last slot where the number can increase
    while ind <= 6 and die[-ind] == 10 - ind:
        ind += 1
    # If no slot can increase, reset.
    if ind > 6:
        return [i for i in range(len(die))]
    # If a slot can increase, it increases by 1, and each successive slot is
    # 1 higher than the previous.
    else:
        die[-ind] += 1
        ind -= 1
        while ind:
            die[-ind] = die[-(ind + 1)] + 1
            ind -= 1
        return die

res = 0
d1comb = 1
while d1comb <= 210:    
    d1comb += 1
    die2 = nextDie(die1)
    d2comb = 0
    while d2comb <= 210 - d1comb:
        d2comb += 1
        # This should never happen, but just in case...
        if die1 == die2:
            print(die1, die2)
            die2 = nextDie(die2)
            continue
        satisfiesCondition = True
        for pair in pairs:
            a = pair[0]
            b = pair[1]
            # If the pair includes 6/9, we also check for 9.
            if b == 6: c = 9
            else: c = b
            if (a in die1 and (b in die2 or c in die2)) or (a in die2 and (b in die1 or c in die1)):
                pass
            else:
                satisfiesCondition = False
                break            
        if satisfiesCondition:
            res += 1
        die2 = nextDie(die2)
    die1 = nextDie(die1)
print(res)
