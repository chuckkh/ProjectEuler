num = 600851475143
#num = 13195

highest = 2
current = 2
sqrt = num**0.5+1
while current <= sqrt:
    while not num%current:
        highest = current
        num //= current
    current += 1
        
print(highest)
