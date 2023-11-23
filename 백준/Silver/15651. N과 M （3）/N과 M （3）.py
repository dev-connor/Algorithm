N, M = map(int, input().split())
lst = []

def dfs(cnt):
    if cnt == M:  # 탈출 조건
        print(' '.join(map(str, lst)))
        return

    for i in range(1, N+1):
        lst.append(i)
        dfs(cnt+1)
        lst.pop()
dfs(0)