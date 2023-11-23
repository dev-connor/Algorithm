# 15:20
import itertools

n,m = map(int, input().split())

houses = []
chickens = []
for i in range(n):
    inputs = list(map(int, input().split()))
    for j,v in enumerate(inputs):
        if v == 1:
            houses.append((i,j))
        elif v == 2:
            chickens.append((i,j))

picked = list(itertools.combinations(chickens,m))
INF = int(1e9)

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

answer = INF
for p in picked:
    city_dist = 0

    for house in houses:
        chicken_dist = INF
        for chicken in p:
            chicken_dist = min(chicken_dist, manhattan(chicken, house))

        city_dist += chicken_dist # 그 집의 치킨거리
    answer = min(answer, city_dist)

print(answer)