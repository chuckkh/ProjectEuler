from math import factorial

def combin(a,b):
    return factorial(a)/(factorial(b)*factorial(a-b))


total = 0
for a in range(23,101):
    for b in range(1,a):
        if combin(a,b) > 1000000:
            total += 1
print(total)
