n,m = map(int, input().split())
visited = [False] * (n+1)

def dfs(arr, visited):
    cnt = len(arr)

    if cnt == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1,n+1):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            dfs(arr, visited)
            arr.pop()
            visited[i] = False

dfs([], visited)
