if __name__ == '__main__':

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

    v, e = map(int, input().split())
    parent = [i for i in range(v+1)] # [0,1,2...v]
    cycle = False

    for i in range(e):
        a, b = map(int, input().split())
        if find_parent(parent,a) == find_parent(parent,b):
            cycle = True
            break
        else:
            union_parent(parent,a,b)

    if cycle:
        print('사이클이 발생했습니다.')
    else:
        print('사이클이 발생하지 않았습니다.')

'''
3 3
1 2
1 3
2 3
'''