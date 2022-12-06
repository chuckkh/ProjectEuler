digitsTo19 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
hundred = 7
thousand = 11


total = 0
for i in range(1,1001):
    tensUnits = i % 100
    if i >= 1000:
        total += thousand
    h = i//100 % 10
    if h > 0:
        total += digitsTo19[h]
        total += hundred
        if tensUnits:
            total += 3
    if tensUnits < 20:
        total += digitsTo19[tensUnits]
    else:
        total += tens[tensUnits // 10]
        total += digitsTo19[tensUnits % 10]
print(total)
