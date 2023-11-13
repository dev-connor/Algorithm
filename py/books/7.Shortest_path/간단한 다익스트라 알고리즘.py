import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = int(1e9)

    n,m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    distance = [INF]*(n+1)

    for _ in range(m):
        a,b,c = list(map(int, input().split()))
        graph[a].append((b,c))

    def get_smallest_node():
        min_value = INF
        index = 0
        for i in range(1,n+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1] # 거리 넣기

        for i in range(n-1):
            now = get_smallest_node()
            visited[now] = True

            for j in graph[now]: # 현재 노드에서 갈 수 있는 노드와 거리
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    dijkstra(start)

    for i  in range(1,n+1):
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