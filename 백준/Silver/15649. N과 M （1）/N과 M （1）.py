n,m = map(int, input().split())
visited = [False] * (n+1)
nums = []

def dfs(visited):
    cnt = len(nums)

    if cnt == m:
        print(' '.join(map(str, nums)))
        return

    for i in range(1,n+1):
        if not visited[i]:
            nums.append(i)
            visited[i] = True
            dfs(visited)
            nums.pop()
            visited[i] = False

dfs(visited)