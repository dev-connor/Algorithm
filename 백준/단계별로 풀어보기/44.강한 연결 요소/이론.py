import collections

v, e = map(int, input().split())

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
        print("Strongly Connected Component", *scc)
    return parent


for i in range(1,v+1):
    if d[i] == -1:
        dfs(i)

'''
11 14
1 2
2 3
3 1
4 2
4 5
5 7
6 5
7 6
8 5
8 9
9 10
10 11
11 3
11 8
'''