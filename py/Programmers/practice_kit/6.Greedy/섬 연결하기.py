# Lv3. +8 - 9:13
def solution(n, costs):
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

    for c in costs:
        cost = c[2]
        edges.append((cost,c[0],c[1]))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost

    return result

array = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
result = solution(4, array)
print(result)
