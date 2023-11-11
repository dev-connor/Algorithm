from collections import deque

# Lv3. +4 - 20:27
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(20001)]
    visited = [False] * 20001
    distance = [0] * 20001

    visited[1] = True

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    q = deque([1])

    while q:
        v = q.popleft()

        for new_v in graph[v]:
            if not visited[new_v]:
                visited[new_v] = True
                q.append(new_v)
                distance[new_v] = distance[v] + 1

    ma = max(distance)
    for d in distance:
        if d == ma:
            answer += 1

    return answer

if __name__ == '__main__':
    array = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    result = solution(6,array)
    print(result)
