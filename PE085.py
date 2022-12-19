vals = [1]
seed = 1
val = (seed*seed+seed)//2
while val < 2000000:
    seed += 1
    val = (seed*seed+seed)//2
    vals.append(val)

lval = len(vals)
mindiff = abs(vals[-1]-2000000)

findex = 0
bindex = -1
f = 0
b = 0
while lval + bindex >= findex:
    dv = 2000000/vals[findex]
    while vals[bindex]-dv > mindiff:
        bindex -= 1
    if abs(vals[bindex]-dv) < mindiff:
        mindiff = abs(vals[bindex]-dv)
        f = findex
        b = bindex
    if vals[bindex] > dv:
        bindex -= 1
    if abs(vals[bindex]-dv) < mindiff:
        mindiff = abs(vals[bindex]-dv)
        f = findex
        b = bindex
    findex += 1

triangle1 = vals[f]
triangle2 = vals[b]
dim1 = ((triangle1 * 8 + 1)**0.5 - 1) // 2
dim2 = ((triangle2 * 8 + 1)**0.5 - 1) // 2
res = int(dim1*dim2)
print(res)
