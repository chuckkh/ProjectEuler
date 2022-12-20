def sortDigits(inp):
    outp = ''
    digits = []
    while inp:
        digits.append(str(inp%10))
        inp //= 10
    digits.sort()
    for d in digits:
        outp += d
    return outp
    
mp = {}
seed = 345
maxVal = 0
res = 0
while maxVal < 5:
    srt = sortDigits(seed**3)
    if srt in mp:
        mp[srt].append(seed)
        ln = len(mp[srt])
        if ln > maxVal:
            maxVal = ln
            res = srt
    else:
        mp[srt] = [seed]
    seed += 1
print(mp[res][0]**3)
