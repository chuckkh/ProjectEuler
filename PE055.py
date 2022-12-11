def reverseAndAdd(inp):
    temp = inp
    toAdd = 0
    while temp:
        toAdd *= 10
        toAdd += temp % 10
        temp //= 10
    return inp + toAdd

def isPalindrome(inp):
    s = str(inp)
    return s == s[-1::-1]

def isLychrel(inp):
    for i in range(50):
        rev = reverseAndAdd(inp)
        if isPalindrome(rev):
            return False
        inp = rev
    return True

total = 0
for i in range(5,10000):
    if isLychrel(i):
        total += 1
print(total)

