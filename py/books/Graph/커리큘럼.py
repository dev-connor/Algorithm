from collections import deque

if __name__ == '__main__':
    v = int(input())
    indegree = [0] * (v+1)
    graph = [[] for _ in range(v+1)]
    time = [0] * (v+1)

    for i in range(1, v+1):
        data = list(map(int, input().split()))
        time[i] = data[0]
        for x in data[1:-1]: # i 강의의 선수강의
            indegree[i] += 1
            graph[x].append(i)

    def topology_sort():
        result = time.copy()
        q = deque()

        # 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, v+1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            now = q.popleft()

            for i in graph[now]:
                result[i] = max(result[i], result[now] + time[i])
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        for i in range(1, v+1):
            print(result[i])

    topology_sort()

'''
5 
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1 
'''