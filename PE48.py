res = 0
for i in range(1,1001):
    power = i**i
    adder = power%(10**10)
    res = (res+adder)%(10**10)

print(res)
