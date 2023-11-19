# +5 - 10:05
def solution(n, results):
    answer = 0

    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for a in range(1, n+1): # 자기 자신 0 으로 초기화
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    for a,b in results: # 간선의 비용 넣기
        graph[a][b] = 1

    for k in range(1, n+1): # 점화식
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] == INF and graph[j][i] == INF:
                break
        else:
            answer += 1

    return answer

if __name__ == '__main__':
    array = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    result = solution(5, array)
    print(result)
