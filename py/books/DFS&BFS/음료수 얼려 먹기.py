if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    def dfs(x,y):

        # 벗어나면 종료
        if x<0 or y<0 or x>=n or y>=m:
            return False

        if graph[x][y] == 0:
            graph[x][y] = 1 # 방문
            dfs(x-1,y) # 상
            dfs(x+1,y) # 하
            dfs(x,y-1) # 좌
            dfs(x,y+1) # 우
            return True
        return False

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    print(result)

'''
4 5 
0 0 1 1 0 
0 0 0 1 1 
1 1 1 1 1 
0 0 0 0 0
'''