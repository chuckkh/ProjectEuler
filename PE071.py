mindiff = 10000
n = 3
d = 7
for den in range(2,1000001):
    if den%7:
        num = den * 3 // 7
        if num and num/den < 3/7:
            diff = 3/7-num/den
            if diff < mindiff:
                mindiff = diff
                n = num
                d = den
print(n)
