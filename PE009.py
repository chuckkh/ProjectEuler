# a + b + c = 1000
# a2 + b2 = c2
done = False
for c in range(1,1000):
    for a in range(1, c):
        b = 1000 - c - a
        if a*a + b*b == c*c:
            print(a*b*c)
            done = True
            break
    if done:
        break
