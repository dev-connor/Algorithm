# 23:37
n = int(input())
nums = list(map(int, input().split()))
max_opers = list(map(int, input().split()))

max_v = -int(1e9)
min_v = int(1e9)
opers = ['+', '-', '*', '/']

def dfs(now_opers, num, idx):
    global min_v, max_v

    if idx == n:
        min_v = min(min_v, num)
        max_v = max(max_v, num)
        return

    for i in range(4):
        if now_opers[i] < max_opers[i]:
            now_opers[i] += 1
            dfs(now_opers, int(eval(str(num) + opers[i] + str(nums[idx]))), idx + 1)
            now_opers[i] -= 1

dfs([0,0,0,0], nums[0], 1)
print(max_v)
print(min_v)