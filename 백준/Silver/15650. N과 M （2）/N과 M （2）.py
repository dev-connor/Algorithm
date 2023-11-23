n, m = map(int, input().split())
visited = [False] * (n + 1)


def dfs(nums, v, visited):
    visited[v] = True
    nums.append(v)
    length = len(nums)

    if length == m:
        print(' '.join(map(str, nums)))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            if i > nums[-1]:
                dfs(nums, i, visited)
                nums.pop()
                visited[i] = False


for i in range(1, n + 1):
    dfs([], i, visited.copy())
