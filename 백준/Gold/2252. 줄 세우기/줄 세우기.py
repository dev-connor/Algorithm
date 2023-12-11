from collections import deque

n,m = map(int, input().split())
graph = [[] for i in range(n+1)]
answer = []

indegree = [0] * (n+1)
for _ in range(m):
    cur, next = map(int, input().split())
    graph[cur].append(next)
    indegree[next] += 1


# inputs = []
# for i in range(m):
#     inputs.append(list(map(int, input().split())))


def topology_sort():
    # result = []
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        answer.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

topology_sort()
print(' '.join(map(str, answer)))