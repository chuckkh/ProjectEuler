def isPalindrome(inp):
    s = str(inp)
    return s == s[-1::-1]



total = 0
cand = 0b1
while cand <= 1024:
    s = str(bin(cand))[2:]
    t = s + s[-2::-1]
    s = s + s[-1::-1]
    val1 = int(s,2)
    val2 = int(t,2)
    for val in (val1, val2):
        if isPalindrome(val):
            total += val
            print(bin(val), val)
    cand += 1
print(total)
