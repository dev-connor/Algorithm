# 브론즈2 - 3:53
n = int(input())
inputs = list(map(int, input().split()))
cnt = 0

for i in range(n):
    num = inputs[i]

    if num == 1:
        continue

    for j in range(2,num):
        if num % j == 0:
            break
    else:
        cnt += 1

print(cnt)
