import math

f = open("p082_matrix.txt", "r")

grid = []
for line in f.readlines():
    row = [int(n) for n in line.split(',')]
    grid.append(row)
x = len(grid[0])
y = len(grid)
currentMins = [row[0] for row in grid]

for column in range(1, x):
    nextColumn = [row[column] for row in grid]
    tempColumn = []
    for bind in range(y):
        minVal = math.inf
        for aind in range(bind):
            val = currentMins[aind] + sum(nextColumn[aind:bind + 1])
            if val < minVal:
                minVal = val
        val = currentMins[bind] + nextColumn[bind]
        if val < minVal:
            minVal = val
        for aind in range(bind+1, y):
            val = currentMins[aind] + sum(nextColumn[bind:aind + 1])
            if val < minVal:
                minVal = val
        tempColumn.append(minVal)
    currentMins = tempColumn
print(min(currentMins))
