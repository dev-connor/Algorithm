n,m = map(int, input().split())
board = []
for _ in range(n):
    # board.append(list(map(int, input().split())))
    board.append(input())

answer = 64

for i in range(n):
    for j in range(m):
        min_cnt = 64

        # 보드판 벗어나면 스킵
        if i+8 > n or j+8 > m:
            continue

        w = True
        cnt = 0
        for k in range(i,i+8): # WB 로 시작
            for l in range(j,j+8):
                if w:
                    if board[k][l] != 'W':
                        cnt += 1
                else:
                    if board[k][l] != 'B':
                        cnt += 1

                w = not w
            w = not w

        w = False
        cnt2 = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if w:
                    if board[k][l] != 'W':
                        cnt2 += 1
                else:
                    if board[k][l] != 'B':
                        cnt2 += 1

                w = not w
            w = not w
        min_cnt = min(cnt,cnt2)
        answer = min(answer, min_cnt)
        # print(min_cnt)

print(answer)