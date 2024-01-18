import math

def lcm(n1, n2):
    return n1 * n2 // math.gcd(n1, n2)

t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    print(lcm(a,b))