n,m = map(int, input().split())
r,c,d = map(int, input().split())

room = []
for i in range(n):
    room.append(list(map(int, input().split())))

clean = [[False] * m for _ in range(n)]

answer = 0
dx = [-1,0,1,0] # 북동남서
dy = [0,1,0,-1]

def back(n):
    if n % 2 == 0:
        return 2-n
    else:
        return 4-n

def rotate(n):
    if n == 0:
        return 3
    else:
        return n-1

while True:
    find = False
    if room[r][c] == 0 and not clean[r][c]:
        clean[r][c] = True
        answer += 1

    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]

        if room[nx][ny] == 0 and not clean[nx][ny]:
            find = True

    if find:
        while True:
            d = rotate(d)
            nx = r + dx[d]
            ny = c + dy[d]
            if room[nx][ny] == 0 and not clean[nx][ny]:
                r = nx
                c = ny
                break
    else:
        nx = r + dx[back(d)]
        ny = c + dy[back(d)]
        if room[nx][ny] != 1:
            r = nx
            c = ny
        else:
            break

print(answer)
