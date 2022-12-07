from math import factorial

f = factorial

allDigits = [0,1,2,3,4,5,6,7,8,9]
finalPerm = allDigits.copy()
outp = ''
remainingP = 999999
fSeed = 9
#remainingP = 6
fact = factorial(fSeed)
#while remainingP:
for i in range(9):
#while fact <= remainingP:
    increm = remainingP // fact
    print(fSeed, remainingP, increm)
    nextDigit = allDigits[increm]
    allDigits.remove(nextDigit)
    outp += str(nextDigit)
    remainingP -= increm * fact
    fSeed -= 1
    fact = factorial(fSeed)
outp += str(allDigits[0])
print(outp)
