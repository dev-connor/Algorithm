# 15:28
n,m = map(int, input().split())

def dfs(arr):
    cnt = len(arr)

    if cnt == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1,n+1):
        if cnt == 0 or i >= arr[cnt-1]:
            arr.append(i)
            dfs(arr)
            arr.pop()

dfs([])
