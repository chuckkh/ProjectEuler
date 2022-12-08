values = [100, 50, 20, 10, 5, 2]
num = [0,0,0,0,0,0]
maxes = [2,4,10,20,40,100]

total = 1 # (accounting for 1 2-pound piece)

#values = [1,2,5,10,20,50,100,200]
#num = [200,0,0,0,0,0,0,0]
#maxes = [200, 100, 40, 20, 10, 4, 2, 1]

for onehundred in range(3):
    v1 = onehundred * values[0]
    for fifty in range(5):
        v2 = fifty * values[1]
        if v1 + v2 > 200:
            break
        for twenty in range(11):
            v3 = twenty * values[2]
            if v1 + v2 + v3 > 200:
                break
            for ten in range(21):
                v4 = ten * values[3]
                if v1 + v2 + v3 + v4 > 200:
                    break
                for five in range(41):
                    v5 = five * values[4]
                    amount = v1 + v2 + v3 + v4 + v5
                    # Here I just add the possible number of 2-pound pieces
                    # for the remainder, because the 1-pound pieces always
                    # fill in the rest.
                    if amount <= 200:
                        total += (200 - amount) // 2 + 1
print(total)
