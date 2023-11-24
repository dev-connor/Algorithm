n,b = input().split()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = 0

for i,m in enumerate(n):
    mul = len(n) - i - 1
    if m in alpha:
        num += int(b)**mul * (10 + alpha.index(m))
    else:
        num += int(b)**mul * int(m)

print(num)