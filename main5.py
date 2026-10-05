d = int(input())
m = int(input())
y = int(input())


max_days = 31

if m == 4 or m == 6 or m == 9 or m == 11:
    max_days = 30
elif m == 2:
    
    if y % 4 == 0:
        max_days = 29
    else:
        max_days = 28

d = d + 1

if d > max_days:
    d = 1
    m = m + 1
    
    if m > 12:
        m = 1
        y = y + 1

print(d, m, y, sep=".")

