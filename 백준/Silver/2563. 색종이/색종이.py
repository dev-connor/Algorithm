n = int(input())
inputs = [0]*n

for i in range(n):
    x,y = map(int, input().split())
    inputs[i] = (x,y)

graph = [[0] * 101 for _ in range(101)]

for pos in inputs:
    x,y = pos
    for i in range(x,x+10):
        for j in range(y,y+10):
            graph[i][j] = 1

answer = 0
for i in range(1,101):
    for j in range(1,101):
        if graph[i][j] == 1:
            answer += 1

print(answer)
