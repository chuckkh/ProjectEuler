f = open("p079_keylog.txt", "r")


attempts = [row.strip() for row in f.readlines()]

digits = {}
for row in attempts:
    for c in row:
        if c not in digits:
            digits[c] = []
ln = len(digits)
for d in digits:
    digits[d] = [i for i in range(ln)]
    
done = False
while not done:
    done = True
    for row in attempts:
        c1 = row[0]
        c2 = row[1]
        c3 = row[2]
        c1min = min(digits[c1])
        c2min = min(digits[c2])
        c2max = max(digits[c2])
        c3max = max(digits[c3])
        digits[c1] = [i for i in digits[c1] if int(i) < int(c2max)]
        digits[c2] = [i for i in digits[c2] if int(c1min) < int(i) < int(c3max)]
        digits[c3] = [i for i in digits[c3] if int(c2min) < int(i)]
        if len(digits[c1]) > 1 or len(digits[c2]) > 1 or len(digits[c3]) > 1:
            done = False


key = ''
for keyInd in range(ln):
    for c in digits:
        if keyInd in digits[c]:
            key += c
            break
print(key)
            
#pkey = '73162890'
#for row in attempts:
#    ind = 0
#    for c in row:
#        ind = pkey.find(c, ind+1)
#        if ind == -1:
#            print(row, c, pkey)
            

