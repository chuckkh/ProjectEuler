sm = 0
sq = 0
diff = 0
for i in range(101):
    sm += i*i
    sq += i
print(abs(sq*sq-sm))
