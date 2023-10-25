# +3
def solution(n, computers):
    answer = 0
    visited = [False]*n

    def dfs(graph, v, visited): # 연결된 모든 네트워크를 True 로 바꿈
        if visited[v]:
            return False

        visited[v] = True

        for i,n in enumerate(graph[v]):
            if i != v and n == 1:
                if not visited[i]:
                    dfs(graph, i, visited)

        return True

    for i in range(n):
        if dfs(computers, i, visited): # 방문한 적이 없는 네트워크 일 때 +1
            answer +=1

    return answer

if __name__ == '__main__':
    arrays = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    result = solution(3, arrays)
    print(result)