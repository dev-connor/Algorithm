n = int(input())
m = 2
an = 3

for _ in range(1,n):
    an += m
    m *= 2


print(an**2)