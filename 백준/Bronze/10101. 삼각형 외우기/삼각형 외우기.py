a = int(input())
b = int(input())
c = int(input())

if a == 60 and b == 60 and c == 60:
    print('Equilateral')
elif a + b + c == 180:
    if a != b and b != c and a != c:
        print('Scalene')
    else:
        print('Isosceles')
else:
    print('Error')