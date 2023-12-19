n = int(input())

graph = [[0] * n for _ in range(10)]
for i in range(1,10):
    graph[i][0] = 1

for i in range(1,n):
    for j in range(10):
        if 0 <= j-1 <= 9:
            graph[j][i] += graph[j-1][i-1]
        if 0 <= j+1 <= 9:
            graph[j][i] += graph[j+1][i-1]

answer = 0
for i in range(10):
    answer += graph[i][n-1]

print(answer%1000000000)