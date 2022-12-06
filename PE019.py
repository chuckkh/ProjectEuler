# Sundays on 1st of month
# 1901-2000

total = 0
today = 1
months = (3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3)
month = 0
for i in range(11):
    today = (today + months[month]) % 7
    if today == 0:
        total += 1

# It is now 1 Dec 1900

for year in range(1,100):
    for month in range(12):
        if not year % 4 and month == 2:
            today = (today + 29) % 7
        else:
            today = (today + months[month]) % 7
        if today == 0:
            total += 1

print(total)
