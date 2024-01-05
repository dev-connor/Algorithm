n,m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n+1)] # n 은 node 의 갯수
edges = []
result = 0

for i in range(m): # 간선의 비용
    a,b = map(int, input().split())
    edges.append((a,b))

for i,edge in enumerate(edges):
    a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
    else:
        print(i+1)
        break
else:
    print(0)
