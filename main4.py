n = int(input())

c1 = n // 100       
c2 = (n // 10) % 10 
c3 = n % 10         

if c1 + c3 > c2:
    print(">")
elif c1 + c3 < c2:
    print("<")
else:
    print("=")

