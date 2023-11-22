v = int(input())

INF = int(1e9)
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for a in range(1, v + 1): # 자기 자신 0 으로 초기화
    for b in range(1, v + 1):
        if a == b:
            graph[a][b] = 0

e = int(input())
for _ in range(e): # 간선의 비용 넣기 
    now, next, cost = map(int, input().split())
    graph[now][next] = min(graph[now][next], cost) 

for k in range(1, v + 1): # 점화식 
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in graph[1:]:
    print(' '.join(map(str, i[1:])))
