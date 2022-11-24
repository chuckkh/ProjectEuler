ab = [1,1]
index = 2
abindex = 0
next = 0
while next < 10**999:
    next = sum(ab)
    ab[abindex] = next
    abindex = 1 - abindex
    index += 1

print(index)
