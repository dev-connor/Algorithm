import heapq
import sys

def set(d, a, b):
    d.setdefault(a, 0)
    d[a] = b

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())
graph = [{} for _ in range(v + 1)]
distance = [INF]*(v + 1)

for _ in range(e):
    s, to, cost = map(int, input().split())

    if graph[s].get(to):
        c = graph[s].get(to)
        if cost < c:
            set(graph[s],to,cost)
            # d.setdefault(cost)
    else:
        d = graph[s]
        set(d,to,cost)
        # graph[s].append(d)

    # if cost < graph[s][to]:
    #     graph[s][to] = cost

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]: # (cost, node)
            c = graph[now][i]

            cost = dist + c

            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i)) # (거리, 노드) 형태로 push

dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])