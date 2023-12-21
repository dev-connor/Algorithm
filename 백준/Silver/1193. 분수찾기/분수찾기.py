x = int(input())
d = 1
sum_v = 1

while x > sum_v:
    d += 1
    sum_v += d

den = sum_v - x + 1
num = d + 1 - den

if d % 2 == 0:
    print(f'{num}/{den}')
else:
    print(f'{den}/{num}')
