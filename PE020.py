prod = 1
total = 0

for i in range(1,101):
    prod *= i

while prod:
    total += prod % 10
    prod //= 10

print(total)
