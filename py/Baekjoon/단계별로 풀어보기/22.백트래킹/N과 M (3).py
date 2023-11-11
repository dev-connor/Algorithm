# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

if __name__ == '__main__':
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



