fifth = (0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049)

total = 0
for i in range(10,10000000):
    temp = i
    s = 0
    while temp:
        s += fifth[temp % 10]
        temp //= 10
    if s == i:
        total += i
#        print(i)
