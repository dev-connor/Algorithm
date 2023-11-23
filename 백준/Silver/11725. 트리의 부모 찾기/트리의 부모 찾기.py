# 46:05
from collections import deque

e = int(input())
parent = [0]*(e + 1)
edges = [[] for _ in range(e + 1)]
visited = [False] * (e + 1)

for _ in range(e - 1):
    start, to = map(int, input().split())
    edges[start].append(to)
    edges[to].append(start)

def bfs(start):
    q = deque([(start,0)])
    visited[start] = True

    while q:
        v,before = q.popleft()
        parent[v] = before

        for i in edges[v]:
            if not visited[i]:
                q.append((i,v))
                visited[i] = True

bfs(1)
for p in parent[2:]:
    print(p)
