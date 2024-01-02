n,m = map(int, input().split())
r,c,d = map(int, input().split())

room = []
for i in range(n):
    room.append(list(map(int, input().split())))

clean = [[False] * m for _ in range(n)]

answer = 0
dx = [-1,0,1,0] # 북동남서
dy = [0,1,0,-1]

while True:
    find = False
    if room[r][c] == 0 and not clean[r][c]:
        clean[r][c] = True
        answer += 1

    for _ in range(4):
        d = (d-1)%4 # 반시계 방향으로 회전
        nx = r + dx[d]
        ny = c + dy[d]

        if room[nx][ny] == 0 and not clean[nx][ny]:
            r = nx
            c = ny
            break
    else:
        back = (d+2)%4
        nx = r + dx[back]
        ny = c + dy[back]
        if room[nx][ny] != 1:
            r = nx
            c = ny
        else:
            break

print(answer)
