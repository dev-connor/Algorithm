from collections import deque

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def bfs(x,y):
        q = deque()
        q.append((x,y))

        while q:
            x,y = q.popleft() # 이동 전 좌표

            for i in range(4): # 상하좌우 순으로 for 문
                nx = x+dx[i] # 이동 후 좌표
                ny = y+dy[i]

                # 벗어났을 때 무시
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue

                # 벽일 때 무시
                if graph[nx][ny] == 0:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))
        return graph[n-1][m-1]

    print(bfs(0,0))

'''
5 6
1 0 1 0 1 0
1 1 1 1 1 1
0 0 0 0 0 1
1 1 1 1 1 1
1 1 1 1 1 1
'''