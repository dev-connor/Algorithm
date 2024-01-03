n,e = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(e): # 간선의 비용 넣기
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1): # 점화식
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = INF
for i in range(1,n):
    answer = min(answer, graph[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)
