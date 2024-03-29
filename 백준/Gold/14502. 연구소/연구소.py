# 34:41
# DFS/BFS
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

picked = list(itertools.combinations(empty, 3)) # 빈 공간에 벽을 세운 모든 경우

def spread(position):
    x = position[0]
    y = position[1]

    if 0 <= x < n and 0 <= y < m:

        if graph[x][y] == 0:
            graph[x][y] = 2 # 방문
            spread((x-1,y)) # 상
            spread((x+1,y)) # 하
            spread((x,y-1)) # 좌
            spread((x,y+1)) # 우
            return True

    return False

def count(target):
    count = 0
    for array in graph:
        for value in array:
            if value == target:
                count += 1
    return count

max_v = 0
for w1,w2,w3 in picked:
    graph = copy.deepcopy(g)
    graph[w1[0]][w1[1]] = 1 # 빈 공간에 벽을 세움
    graph[w2[0]][w2[1]] = 1
    graph[w3[0]][w3[1]] = 1

    for v in virus:
        graph[v[0]][v[1]] = 0
        spread(v) # 바이러스를 퍼트림

    max_v = max(max_v, count(0)) # 안전 영역의 크기 계산

print(max_v)