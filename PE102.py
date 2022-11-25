f = open('p102_triangles.txt', 'r')
triraw = f.readlines()


tri = [[int(s) for s in wd.split(',')] for wd in triraw]

result = 0

for points in tri:
    if points[0]*points[2] > 0:
        a = [points[0],points[1]]
        b = [points[2],points[3]]
        c = [points[4],points[5]]
    elif points[0]*points[4] > 0:
        a = [points[0],points[1]]
        c = [points[2],points[3]]
        b = [points[4],points[5]]
    else:
        c = [points[0],points[1]]
        a = [points[2],points[3]]
        b = [points[4],points[5]]
    if a[0] * c[0] > 0:
        continue

    slopeA = a[1]/a[0]
    slopeB = b[1]/b[0]
    slopeAc = (a[1]-c[1])/(a[0]-c[0])
    slopeBc = (b[1]-c[1])/(b[0]-c[0])
    if a[0] > 0 and ((slopeA > slopeB and slopeA > slopeAc and slopeB < slopeBc) or (slopeA < slopeB and slopeA < slopeAc and slopeB > slopeBc)):
#        print(a,b,c)
        result += 1
    elif a[0] < 0 and ((slopeA < slopeB and slopeA < slopeAc and slopeB > slopeBc) or (slopeA > slopeB and slopeA > slopeAc and slopeB < slopeBc)):
#        print(a,b,c)
        result += 1
print(result)
### First, pick two points with the same x sign...
### If the other point has the same x sign, FALSE
### If both points have positive X,
###     the greater slope from 0,0 should be greater than from C
###     the lesser slope from 0,0 should be less than from C
### If both points have negative X,
###     the greater slope from 0,0 should be less than from C
###     the lesser slope from 0,0 should be greater than from C

