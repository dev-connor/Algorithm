# 21:03
# 투 포인터
n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
answer = 0
f = 0
e = n-1

while f < e:
    sum_v = nums[f] + nums[e]
    if sum_v == x:
        answer += 1
    if sum_v <= x:
        f += 1
    else:
        e -= 1

print(answer)