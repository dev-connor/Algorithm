import heapq
import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = int(1e9)

    n,m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n+1)]
    distance = [INF]*(n+1)

    for _ in range(m):
        s, to, cost = map(int, input().split())
        graph[s].append((cost, to)) # s 에서 to 로 가는 비용이 cost

    def dijkstra(start):
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            for i in graph[now]: # (cost, node)
                cost = dist + i[0]

                if cost < distance[i[1]]:
                    distance[i[1]] = cost
                    heapq.heappush(q, (cost, i[1])) # (거리, 노드) 형태로 push

    dijkstra(start)

    for i in range(1,n+1):
        if distance[i] == INF:
            print('INFINITY')
        else:
            print(distance[i])

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''