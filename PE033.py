num = den = 1
for same in range(1,10):
    for diff1 in range(1,10):
        if diff1 == same:
            continue
        for diff2 in range(1,10):
            if diff2 == same or diff2 == diff1:
                continue
            num1 = same * 10 + diff1
            den1 = diff2 * 10 + same
            num2 = diff1 * 10 + same
            den2 = same * 10 + diff2
            
            if num1/den1 == diff1/diff2:
                num *= min(diff1, diff2)
                den *= max(diff1, diff2)
#                print(min(num1,den1), max(num1,den1))

fac = 2
while fac <= num**0.5+1:
    while not num % fac and not den % fac:
        num //= fac
        den //= fac
    fac += 1
print(den)
