# +11 - 33:15
def solution(m, n, puddles):
    graph = [[-1] * m for _ in range(n)]
    graph[n-1][m-1] = 1

    for water in puddles:
        graph[water[1]-1][water[0]-1] = 0 # 물웅덩이는 0

    for y in range(n-1,-1,-1):
        for x in range(m-1,-1,-1):

            if (x==m-1 and y==n-1) or graph[y][x] == 0: # 학교거나 물웅덩이라면 스킵
                continue

            if x+1 == m: # 오른쪽이 없음
                right = 0
            else:
                right = graph[y][x+1]
            if y+1 == n: # 아래쪽이 없음
                bot = 0
            else:
                bot = graph[y+1][x]

            graph[y][x] = right + bot

    return graph[0][0] % 1000000007

if __name__ == '__main__':
    result = solution(4,3,[[2,2]])
    print(result)
