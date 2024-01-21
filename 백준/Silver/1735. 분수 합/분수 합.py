import math

n1,d1 = map(int, input().split())
n2,d2 = map(int, input().split())

n3 = n1*d2+n2*d1
d3 = d1*d2

gcd = math.gcd(n3,d3)
print(n3//gcd,d3//gcd)