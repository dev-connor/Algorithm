from collections import deque

for tc in range(int(input())):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False]*(n+1) for i in range(n+1)]
    data = list(map(int,input().split()))

    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1 # 꼴등이 진입차수가 크다.

    m = int(input())
    for i in range(m):
        a,b = map(int, input().split()) # a 가 b 를 이김

        if graph[a][b]: # 작년에 a 가 b 를 이겼을 때
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)
        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print('IMPOSSIBLE')
    elif not certain:
        print('?')
    else:
        for i in result:
            print(i,end=' ')
        print()

'''
3
5
5 4 3 2 1
2
2 4
3 4
3 
2 3 1 
0
4 
1 2 3 4 
3 
1 2 
3 4 
2 3
'''
