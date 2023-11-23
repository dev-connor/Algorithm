n,m = map(int, input().split())

def dfs(arr, now):
    cnt = len(arr)

    if cnt == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(now, n + 1):
        arr.append(i)
        dfs(arr,i)
        arr.pop()

dfs([],1)