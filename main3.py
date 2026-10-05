room = input()

if room == "triangle":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(round(s, 1))

elif room == "rectangle":
    a = float(input())
    b = float(input())
    s = a * b
    print(round(s, 1))

elif room == "circle":
    r = float(input())
    s = 3.14 * r * r
    print(round(s, 1))

