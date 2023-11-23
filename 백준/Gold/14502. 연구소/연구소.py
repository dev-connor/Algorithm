import copy
import itertools

n,m = map(int, input().split())

virus = []
empty = []

g = [[0] * m for _ in range(n)]

for i in range(n):
    inputs = list(map(int, input().split()))
    for j,v in enumerate(inputs):
        g[i][j] = v
        if v == 2:
            virus.append((i,j))
        elif v == 0:
            empty.append((i,j))

picked = list(itertools.combinations(empty, 3))

def spread(pos):
    x = pos[0]
    y = pos[1]

    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

def spread(x,y):
    # x = pos[0]
    # y = pos[1]

    # 벗어나면 종료
    if x<0 or y<0 or x>=n or y>=m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 2 # 방문
        spread(x-1,y) # 상
        spread(x+1,y) # 하
        spread(x,y-1) # 좌
        spread(x,y+1) # 우
        return True
    return False

def count(value):
    cnt = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == value:
                cnt += 1
    return cnt

# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1

    # print(result)

# def dfs(graph, v, visited):
# visited[v] = True

max_v = 0
for w1,w2,w3 in picked:
    graph = copy.deepcopy(g)
    graph[w1[0]][w1[1]] = 1
    graph[w2[0]][w2[1]] = 1
    graph[w3[0]][w3[1]] = 1

    for v in virus:
        graph[v[0]][v[1]] = 0
        spread(v[0],v[1])

    max_v = max(max_v, count(0))

    graph[w1[0]][w1[1]] = 0
    graph[w2[0]][w2[1]] = 0
    graph[w3[0]][w3[1]] = 0

print(max_v)