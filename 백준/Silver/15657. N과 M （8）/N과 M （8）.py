# 6:15
n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []

def dfs(now):
    cnt = len(answer)

    if cnt == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(now, n):
        answer.append(nums[i])
        dfs(i)
        answer.pop()

dfs(0)