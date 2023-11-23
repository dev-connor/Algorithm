n,m = map(int, input().split())
visited = [False] * (n+1)
nums = []

def dfs():
    cnt = len(nums)

    if cnt == m:
        print(' '.join(map(str, nums)))
        return

    for i in range(1,n+1):
            nums.append(i)
            dfs()
            nums.pop()

dfs()