f = open('p042_words.txt', 'r')

txt = f.readlines()
total = 0
wds = [w[1:-1] for w in txt[0].split(',')]
alf = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for wd in wds:
    s = 0
    for c in wd:
        if c in alf:
            s += alf.find(c)
    s *= 2
    sq = int(s**0.5)
    if sq*sq+sq == s:
        total += 1
print(total)






