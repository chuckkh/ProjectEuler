def sameDigits(arr):
    digits = sorted([c for c in str(arr[0])])
    for mult in arr[1:]:
        if digits != sorted([c for c in str(mult)]):
            return False
    return True


mults = [2,3,4,5,6]
toAdd = [2,3,4,5,6]

done = False
total = 0
while not done:
    done = sameDigits(mults)
    for i in range(5):
        mults[i] += toAdd[i]
    total += 1
print(total)




