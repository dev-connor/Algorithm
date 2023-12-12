# 19:34
# 위상정렬
import heapq

n,m = map(int, input().split())

answer = []
graph = [[] for i in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    cur, next = map(int, input().split())
    graph[cur].append(next)
    indegree[next] += 1

def topology_sort():
    q = []

    for i in range(1, n+1): # 진입차수가 0인 노드를 큐에 삽입
        if indegree[i] == 0:
            heapq.heappush(q,i)

    for i in range(n):
        now = heapq.heappop(q)
        answer.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q,i)

    print(' '.join(map(str, answer)))

topology_sort()