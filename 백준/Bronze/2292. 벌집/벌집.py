# 8:34
n = int(input())
num = 1
plus = 6
move = 1

while num < n:
    num += plus
    plus += 6
    move += 1

    if n <= num:
        break

print(move)

