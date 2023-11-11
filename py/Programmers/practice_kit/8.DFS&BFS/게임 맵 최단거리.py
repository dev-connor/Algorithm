from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(0,0,1)])
    graph = [[0]*m for _ in range(n)]

    while q:
        x,y,move = q.popleft()

        for i in range(4): # 상하좌우
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and maps[nx][ny] == 1: # 간 적 없고, 이동 가능
                    graph[nx][ny] = move+1
                    q.append((nx,ny,move+1))

    if graph[n - 1][m - 1] == 0:
        return -1
    else:
        return graph[n - 1][m - 1]

if __name__ == '__main__':
    arrays = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    result = solution(arrays)
    print(result)

