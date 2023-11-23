n,m = map(int, input().split())
nums = []

def dfs(now):
    cnt = len(nums)

    if cnt == m:
        print(' '.join(map(str, nums)))
        return

    for i in range(now, n + 1):
        nums.append(i)
        dfs(i)
        nums.pop()

dfs(1)