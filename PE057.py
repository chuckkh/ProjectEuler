from math import log10

num = 3
den = 2
total = 0
for i in range(999):
    temp = num + den
    num = temp + den
    den = temp
    if int(log10(num))-int(log10(den)) >= 1:
#        print(i, num, den)
        total += 1
print(total)
