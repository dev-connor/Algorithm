import heapq
import sys

# dp 로 풀어도 될 것 같다.
input = sys.stdin.readline
INF = int(1e9)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for tc in range(int(input())):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))

    distance = [[INF]*n for _ in range(n)]

    x,y = 0,0
    q = [(graph[x][y],x,y)]
    distance[x][y] = graph[x][y]

    while q:
        dist,x,y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4): # 북동남서
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost,nx,ny))

    print(distance[n-1][n-1])

'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''