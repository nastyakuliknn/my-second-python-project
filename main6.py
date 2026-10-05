from builtins import input


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

if (a <= d and b <= e) or (a <= e and b <= d):
    print("Yes")
elif (a <= d and c <= e) or (a <= e and c <= d):
    print("Yes")
elif (b <= d and c <= e) or (b <= e and c <= d):
    print("Yes")
else:
    print("No")

