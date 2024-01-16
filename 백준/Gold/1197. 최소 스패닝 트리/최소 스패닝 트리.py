def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# N=정점의 갯수, M=간선의 갯수 

n,e = map(int, input().split())
parent = [i for i in range(n+1)] # n 은 node 의 갯수
edges = []
result = 0

for _ in range(e): # edge, edges 간선
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a,b)
        result += cost
    else: # 사이클 발생 
        pass

print(result)