### Problem 28
### Number spiral diagonals
### 1001x1001 number spiral
### always moving directly right
### find sum of numbers on diagonals



stepToNextValue = 2
total = 1
toAdd = 1
layersChecked = 1
while layersChecked < 1001:
    for i in range(4):
        toAdd += stepToNextValue
        total += toAdd
    stepToNextValue += 2
    layersChecked += 2
    
print(total)
