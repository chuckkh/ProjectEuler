f = open('p067_triangle.txt', 'r')
myTree = []
for line in f.readlines():
    row = [int(num) for num in line.split()]
    myTree.append(row)

sums = myTree[-1]
for row in myTree[-2::-1]:
    for ind in range(len(row)):
        row[ind] += max(sums[ind], sums[ind+1])
    sums = row
print(sums[0])
