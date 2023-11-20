import heapq
import sys

# 17:50
# 최단 경로
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

edges = [[] for _ in range(n + 1)]
shortests = [[INF] * (n + 1) for _ in range(3)]

for _ in range(e):
    start, to, cost = map(int, input().split())
    edges[start].append((to, cost)) # start 에서 to 로 가는 비용이 cost
    edges[to].append((start, cost)) # start 에서 to 로 가는 비용이 cost

v1,v2 = map(int, input().split())

def dijkstra(i, start):
    q = []
    heapq.heappush(q,(0,start))
    shortests[i][start] = 0
    while q:
        shortest, now = heapq.heappop(q)
        if shortests[i][now] < shortest:
            continue

        for edge in edges[now]: # (노드, 거리)
            to = edge[0]
            cost = shortest + edge[1]

            if cost < shortests[i][to]:
                shortests[i][to] = cost
                heapq.heappush(q, (cost, to)) # (거리, 노드) 형태로 저장

dijkstra(0,1)
dijkstra(1,v1)
dijkstra(2,v2)

a = shortests[0][v1] + shortests[1][v2] + shortests[2][n]
b = shortests[0][v2] + shortests[2][v1] + shortests[1][n]

answer = min(a,b)
if answer < INF:
    print(answer)
else:
    print(-1)