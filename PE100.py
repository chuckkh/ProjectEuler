def isTriangle(n):
    return (((8 * n + 1) ** 0.5 - 1)/2).is_integer()

lastGap = 5
gap = 17

seed = gap*int(lastGap*5.5)
while True:
    test = (seed*seed-seed)
    if isTriangle(test):
        doub = int((test*2)**0.5)+1
        if (seed*seed-seed)*2 == doub*doub-doub:
#            print(seed, doub, seed/gap)
            if doub > 10**12:
                print(seed)
                break
            else:
                lastGap = gap
                gap = seed//gap
                seed = gap*int(lastGap*5.5)
    seed += gap

# Explorations...
# 15 21
# 3.5 / 3.7
# 2.7 / 4.5

# 85 120
# 5.17 / 8.3.5
# 4.3.7 / 7.17

# 493 697
# 17.29 / 17.41
# 4.3.41 / 8.3.29

# 2871 4060
# 9.11.29 / 4.5.7.29
# 2.5.7.41 / 9.11.41

# 16731 23661
# 9.11.169 / 9.11.239
# 2.5.7.239 / 4.5.7.169

# 97513 137904
# 169.577 / 16.3.17.169
# 8.3.239.17 / 239.577

# 568345 803761
# 5.197.577 / 7.199.577
# 8.3.7.17.199 / 16.3.5.17.197

# 3312555 4684660 
# 985*3363

#19306983
#5741
#19601
#33461   x19601 655869061/927538921
#114243
#195025
#665857






