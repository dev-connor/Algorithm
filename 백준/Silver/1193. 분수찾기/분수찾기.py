x = int(input())
d = 1
sum_v = 1

while x > sum_v:
    d += 1
    sum_v += d

p = sum_v - x + 1
s = d + 1 - p

if d % 2 == 0:
    print(f'{s}/{p}')
else:
    print(f'{p}/{s}')
