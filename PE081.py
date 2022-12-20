f = open("p081_matrix.txt", "r")

grid = []
for line in f.readlines():
    row = [int(n) for n in line.split(",")]
    grid.append(row)

xgrid = [
    [131,673,234,103, 18],
    [201, 96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524, 37,331]]

previousRow = [grid[0][0]]
#currentSum = 0
#y = currentSum
#x = currentSum - y
w = len(grid)

for currentSum in range(1, w):
    y = currentSum
    x = 0
    row = []
    while y >= 0:
        if x and x < currentSum:
#            print(previousRow)
#            print(y, x, w)
            row.append(grid[y][x] + min(previousRow[x], previousRow[x-1]))
        elif x:
#            print(previousRow)
#            print(y, x, w)
            row.append(grid[y][x] + previousRow[x-1])
        else:
            row.append(grid[y][x] + previousRow[x])
        y -= 1
        x += 1
    previousRow = row

for startX in range(1, w):
    y = w - 1
    x = startX
    row = []
    while x < w:
        if x < w:
            row.append(grid[y][x] + min(previousRow[x-startX], previousRow[x-startX+1]))
        else:
            row.append(grid[y][x] + previousRow[x-startX])
        y -= 1
        x += 1
    previousRow = row
print(row[0])
