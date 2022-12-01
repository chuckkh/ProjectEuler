def isPalindrome(inp):
    s = str(inp)
    return s == s[-1::-1]




maxPal = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        prod = i*j
        if prod > maxPal and isPalindrome(prod):
            maxPal = prod
print(maxPal)
