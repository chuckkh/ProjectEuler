from PEtools import PEisPrime



maxlen = 0
maxa = 0
maxb = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n = 0
        while PEisPrime((n + a) * n + b):
            n += 1
        if n > maxlen:
            maxlen = n
            maxa = a
            maxb = b
print(maxa * maxb)
