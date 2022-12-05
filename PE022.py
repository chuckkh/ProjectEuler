f = open('p022_names.txt', 'r')
alf = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0
def numberizeName(name):
    total = 0
    for c in name:
        if c in alf:
            total += alf.index(c)
    return total

names = [nm[1:-1] for nm in f.readlines()[0].split(',')]
names.sort()
for ind in range(len(names)):
    total += numberizeName(names[ind]) * (ind + 1)

print(total)
