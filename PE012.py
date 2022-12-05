def numDiv(inp):
    total = 2
    cand = 2
    sqrt = inp**0.5
    while cand <= sqrt:
        if not inp % cand:
            total += 2
        cand += 1
    return total



cand = 100
last = 1
done = False

while not done:
    num = numDiv(cand)
    if num * last >= 502 and numDiv((cand*cand-cand)//2) > 500:
        done = True
        break
    last = num
    cand += 1

print((cand*cand-cand)//2)
