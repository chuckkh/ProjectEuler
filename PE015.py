res = 1
for i in range(1,21):
    res *= i

div = res*res
for i in range(21,41):
    res *= i

print(res//div)
