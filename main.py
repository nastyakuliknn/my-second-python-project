a = int(input())
b = int(input())

if a * b > a + b:
    print(a * b)
elif a * b < a + b:
    print(a + b)
else:
    print(a - b)

