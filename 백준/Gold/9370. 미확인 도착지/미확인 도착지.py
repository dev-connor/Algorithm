import heapq
import sys

# 59:17
# 최단 경로
T = int(input())

for _ in range(T):
    input = sys.stdin.readline
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())

    INF = int(1e9)

    edges = [[] for _ in range(n+1)]
    shortests = [[INF] * 2001 for _ in range(3)]
    destinations = []

    for _ in range(m):
        start, to, cost = map(int, input().split())
        edges[start].append((to, cost)) # start 에서 to 로 가는 비용이 cost
        edges[to].append((start, cost)) # start 에서 to 로 가는 비용이 cost

    for _ in range(t):
        destination = int(input())
        destinations.append(destination)

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

    dijkstra(0,s)
    dijkstra(1,g)
    dijkstra(2,h)

    a = shortests[0][g] + shortests[1][h]
    b = shortests[0][h] + shortests[2][g]

    answer = []
    for i in destinations:
        if a + shortests[2][i] == shortests[0][i]:
            answer.append(i)
        if b + shortests[1][i] == shortests[0][i]:
            answer.append(i)

    answer.sort()
    print(' '.join(map(str, answer)))