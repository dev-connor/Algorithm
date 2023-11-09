from collections import deque

# +5
def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 101 for _ in range(101)]

    for r in rectangle:
        for y in range(2*r[0],2*r[2]+1):
            for x in range(2*r[1],2*r[3]+1):
                if r[0]*2 < y < r[2]*2 and r[1]*2 < x < r[3]*2:
                    graph[y][x] = -1
                elif graph[y][x] != -1:
                    graph[y][x] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def bfs(x,y):
        q = deque()
        q.append((x,y))

        while q:
            x,y = q.popleft() # 이동 전 좌표

            # 도착
            if x == 2*itemX and y == 2*itemY:
                return graph[x][y]

            for i in range(4): # 상하좌우 이동
                nx = x+dx[i] # 이동 후 좌표
                ny = y+dy[i]

                # 벗어났을 때 무시
                if nx<0 or ny<0 or nx>100 or ny>100:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))

    return bfs(characterX*2,characterY*2)//2

if __name__ == '__main__':
    arrays = [[1,1,7,4],[3,2,5,5]] # ,[4,3,6,9],[2,6,8,8]
    result = solution(arrays,1,3,7,3)
    print(result)