f = open("p059_cipher.txt", "r")

text = f.readlines()[0].split(',')
tl = len(text)
c1 = [text[cind] for cind in range(0,tl,3)]
c2 = [text[cind] for cind in range(1,tl+1,3)]
c3 = [text[cind] for cind in range(2,tl+2,3)]
alf = 'abcdefghijklmnopqrstuvwxyz'
finalKey = ''
for c in (c1, c2, c3):
#    print("c", c)
    cl = len(c)
    minNonsense = cl + 1
    bestKey = ''
    for key in alf:
        k = ord(key)
        nonsense = cl
        for letter in alf:
            nonsense -= c.count(str(ord(letter)^k))
        if nonsense < minNonsense:
            bestKey = key
            minNonsense = nonsense
    finalKey += bestKey
outp = ''
total = 0
for cind in range(tl):
    ch = int(text[cind]) ^ ord(finalKey[cind%3])
    outp += chr(ch)
    total += ch
#print(finalKey)
#print(outp)
print(total)
    
      

