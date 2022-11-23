start = 1001
result = []
answer = ''

def getDigits(inp):
    outp = []
    while inp:
        outp.append(inp%10)
        inp //= 10
    outp.sort()
    return outp

def areSameDigits(inp):
    d1 = getDigits(inp[0])
    for num in inp[1:]:
        if getDigits(num) != d1:
            return False
    return True

def arePrime(inp):
    for n in inp:
        if not n%2:
            return False
        for i in range(3, int(n**0.5)+1):
            if not n%i:
                return False
    return True

diff = 6
while len(result) < 2:
    for offset in (0,2):
        diff = 6
        st = start + offset
        biggest = st + diff*2
        while biggest < 10000:
            biggest = st + diff*2
            s = [st, st+diff, biggest]
            if areSameDigits(s) and arePrime(s):
                result.append(s)
            diff += 6
    start += 6

for res in result:
    res.sort()
    st = ''
    for r in res:
        st += str(r)
    if st != '148748178147':
        answer = st
        break

print("Answer:", answer)
