from math import log10
power = 1
tot = 0

def nd(n):
    return int(log10(n)) + 1

while nd(9 ** power) == power:
    tot += 1
    ind = 8
    while ind and nd(ind ** power) == power:
        tot += 1
        ind -= 1
    power += 1

print(tot)
