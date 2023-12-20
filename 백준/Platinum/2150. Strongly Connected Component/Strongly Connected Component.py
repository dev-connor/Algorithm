import collections
import sys

sys.setrecursionlimit(int(10e8))
v, e = map(int, input().split())
answer = []
graph = collections.defaultdict(list)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

d = [-1] * (v + 1)
stack = []
visited = [False] * (v + 1)
id = 0

def dfs(cur):
    global id
    id += 1
    d[cur] = id
    stack.append(cur)

    parent = d[cur]
    for next in graph[cur]:
        if d[next] == -1:
            parent = min(parent, dfs(next))
        elif not visited[next]:
            parent = min(parent, d[next])

    if parent == d[cur]:
        scc = []
        while True:
            node = stack.pop()
            visited[node] = True
            scc.append(node)
            if cur == node:
                break
        scc.sort()
        scc.append(-1)
        answer.append(tuple(scc))
    return parent


for i in range(1,v+1):
    if d[i] == -1:
        dfs(i)

answer.sort()
print(len(answer))
for i in answer:
    for j in i:
        print(j, end=' ')
    print()