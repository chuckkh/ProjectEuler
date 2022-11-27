numbers = [1]
count = 1
s = set()
s.add(1)

max = 0
for i in range(1,1000000):
    c = 0
    n = i
    while n != 1:
        if n % 2:
            n *= 3
            n += 1
        else:
            n //= 2
        c += 1
    if c > max:
        max = c
#        print(i)
print(max)


while False:
    for i in range(len(numbers)):
        n = numbers[i]
        if not n % 2 and not (n-1) % 3 and n > 15:
            o = (n-1) // 3
            if o not in s:
                numbers.append(o)
                if o < 1000000:
                    s.add(o)
                    if len(s) == 999999:
                        print(o)
                        break
        n += n
        if n < 1000000 and n not in s:
#            count += 1
            s.add(n)
#            if count <= 1000000:
#                print(count, n*2)
            if len(s) == 999999:
                print(n)
                break
        numbers[i] = n
