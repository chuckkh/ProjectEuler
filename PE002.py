ind = 0
terms = [1,2]
total = 0

while terms[ind] <= 4000000:
    if not terms[ind]%2:
        total += terms[ind]
    next = terms[0] + terms[1]
    terms[ind] = next
    ind = 1 - ind

print(total)
