import sys

# 6:10
# 최단 경로
v,e = map(int, input().split())

input = sys.stdin.readline
INF = int(1e9) # 무한대 값
edges = []
shortest = [INF] * (v + 1)

for _ in range(e):
    sv, ev, cost = map(int, input().split())
    edges.append((sv, ev, cost))

def bellman_ford(start):
    shortest[start] = 0

    for i in range(v):
        for edge in edges:
            now, next, cost = edge

            if shortest[now] != INF and shortest[now] + cost < shortest[next]: # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                shortest[next] = shortest[now] + cost

                if i == v - 1: # v번째 반복에서 갱신되는 값이 있으면 Negative cycle 존재
                    return False

    return True # 벨만-포드 정상종료

if bellman_ford(1):

    for i in range(2, v + 1): # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단거리를 출력

        if shortest[i] == INF: # 도달할 수 없는 경우
            print(-1)
        else:
            print(shortest[i])
else:
    print(-1)