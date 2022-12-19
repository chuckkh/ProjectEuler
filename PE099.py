from math import log

f = open("p099_base_exp.txt", "r")
maxB = 2
maxE = 2
ln = 1
maxLn = 0
for line in f.readlines():
    spl = line.split(',')
    b = int(spl[0])
    e = int(spl[1])
    compB = log(maxB, b)
    if e/compB > maxE:
        maxB = b
        maxE = e
        maxLn = ln
    ln += 1
print(maxLn)
    
