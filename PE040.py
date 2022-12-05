def getNth(n):
    pow10 = 0
    offset = 0
    digits = pow10 + 1
    while n > 9 * 10**pow10 * digits:
        n -= (9 * 10**pow10 * digits)
        pow10 += 1
        digits = pow10 + 1
    number = (n-1) // digits + 10**pow10
#    print("n", n, "pow10", pow10, "digits", digits, "number", number)
    return int(str(number)[(n-1) % digits])
    


# 9 1 digit
# 90 2 digits
# 900 3 digits
# 9000 4 digits
total = 1
for d in range(7):
    toMult = getNth(10**d)
#    print(toMult)
    total *= toMult
print(total)
