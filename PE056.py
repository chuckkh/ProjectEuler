def digitSum(inp):
    outp = 0
    while inp:
        outp += (inp % 10)
        inp //= 10
    return outp


maxSum = 0




for a in range(99,30,-1):
    for b in range(99,30,-1):
        ds = digitSum(a**b)
        if ds > maxSum:
            maxSum = ds
print(maxSum)
