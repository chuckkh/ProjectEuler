def isPan(a, b):
    digits = [0,1,1,1,1,1,1,1,1,1]
    s = str(a) + str(b) + str(a*b)
    for c in s:
        ind = int(c)
        if digits[ind] != 1:
            return False
        digits[ind] -= 1
    for d in digits:
        if d != 0: return False
    return True

s = set()
for i in range(23,9877):
    for j in range(2,i):
        if i*j > 9999:
            break
        elif isPan(i,j):
            s.add(i*j)
print(sum(s))
