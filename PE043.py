#!/usr/bin/env python3

# I tried to speed-solve this
# I got it, but the code is SO messy

# Project Euler: Problem 43
# Sub-string divisibility
# 1406357289
#  406       2
#   063      3
#    635     5
#     357    7
#      572   11
#       728  13
#        289 17

# abcde5fghi
# ghi % 17 = 0

def checkRepeatedDigits(inp):
    if inp < 10:
        return False
    s = "00" + str(inp)
    if s[-3] == s[-2] or s[-3]==s[-1] or s[-1]==s[-2]:
        return True
    else:
        return False

div11 = []
div13 = []
div17 = []
next = 17
while next < 1000:
    if not checkRepeatedDigits(next):
        div17.append(next)
    next += 17
next = 13
while next < 1000:
    if not checkRepeatedDigits(next):
        div13.append(next)
    next += 13
next = 506
while next < 600:
    if not checkRepeatedDigits(next):
        div11.append(next)
    next += 11
div7 = []
next = 56
while next < 1000:
    if str(next)[-2] == '5':
        if not checkRepeatedDigits(next):
            div7.append(next)
    next += 7

div711 = []
for d7 in div7:
    s7 = str(d7)
    if len(s7) == 2:
        s7 = '0' + s7
    for d11 in div11:
        s11 = str(d11)
        if len(s11) == 2:
            s11 = '0' + s11
        if s7[-2:] == s11[:2]:
            div711.append(s7+s11[-1])

div71113 = []
for d in div711:
    dsplice = d[2:4]
    for d13 in div13:
        if str(d13)[:2] == dsplice:
            div71113.append(d + str(d13)[-1])
            
div7111317 = []
for d in div71113:
    dsplice = d[3:5]
    for d17 in div17:
        if str(d17)[:2] == dsplice:
            div7111317.append(d + str(d17)[-1])

divall = []

left = []
for d in div7111317:
    l = []
    le = []
    for c in '0123456789':
        if c not in d:
            l.append(c)
    for i in range(4):
        c = l[i]
        for j in range(4):
            if j == i: continue
            d = l[j]
            if not int(c+d) % 3 and not int(d)%2:
                a = l.copy()
                a.remove(c)
                a.remove(d)
                le.append(a[0]+a[1]+c+d)
                le.append(a[1]+a[0]+c+d)
    left.append(le)
for i in range(len(div7111317)):
    for l in left[i]:
        divall.append(l + div7111317[i])
total = 0            
for s in divall:
    total += int(s)
print(total)
