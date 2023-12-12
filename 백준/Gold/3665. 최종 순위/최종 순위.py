# 14:20
# 위상정렬
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    last_year = list(map(int, input().split()))
    m = int(input())

    answer = []
    graph = [[False]*(n+1) for i in range(n+1)]
    indegree = [0] * (n+1)

    for i in range(n):
        for j in range(i+1,n):
            graph[last_year[i]][last_year[j]] = True
            indegree[last_year[j]] += 1

    for _ in range(m):
        cur, next = map(int, input().split())

        if graph[cur][next]:
            indegree[cur] += 1
            indegree[next] -= 1
        else:
            indegree[cur] -= 1
            indegree[next] += 1
        graph[cur][next] = not graph[cur][next]
        graph[next][cur] = not graph[next][cur]

    def topology_sort():
        q = deque()

        for i in range(1, n+1): # 진입차수가 0인 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

        uncertain = False
        cycle = False

        for i in range(n):
            if len(q) == 0:
                cycle = True
                break
            if len(q) >= 2:
                uncertain = True
                break

            now = q.popleft()
            answer.append(now)

            for j in range(1,n+1):
                if graph[now][j]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        q.append(j)
        else:
            print(' '.join(map(str, answer)))
        if cycle:
            print('IMPOSSIBLE')
        elif uncertain:
            print('?')

    topology_sort()