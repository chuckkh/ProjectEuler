per = {}
maxSolutions = 0
bestPerimeter = 0
for a in range(1,500):
    for b in range(1, a+1):
        c = int((a*a + b*b) ** 0.5)
        if c*c - a*a == b*b:
            p = a + b + c
            if p in per:
                per[p] += 1
                if per[p] > maxSolutions:
                    maxSolutions = per[p]
                    bestPerimeter = p
            else:
                per[p] = 1
print(bestPerimeter)
