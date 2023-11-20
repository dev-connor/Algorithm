import heapq
import sys

# 17:00
# 최단 경로
input = sys.stdin.readline
INF = int(1e9)

n,k = map(int, input().split())

edges = [[] for _ in range(100001)]
shortests = [INF] * 100001

for i in range(100001):
    if 0 <= i+1 <= 100000:
        edges[i].append((i+1, 1))
    if 0 <= i-1 <= 100000:
        edges[i].append((i-1, 1))
    if 0 <= 2*i <= 100000:
        edges[i].append((2*i, 0))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    shortests[start] = 0
    while q:
        shortest, now = heapq.heappop(q)
        if shortests[now] < shortest:
            continue

        for edge in edges[now]: # (노드, 거리)
            to = edge[0]
            cost = shortest + edge[1]

            if cost < shortests[to]:
                shortests[to] = cost
                heapq.heappush(q, (cost, to)) # (거리, 노드) 형태로 저장

dijkstra(n)
print(shortests[k])