def move(y, direction):
    if direction == 'L':
        if y > 1: # 제일 왼쪽 좌표
            return -1
    else:
        if y < w: # 제일 오른쪽 좌표
            return 1
    return 0

t = int(input())
for _ in range(t):
    h, w, x1, y1, x2, y2 = map(int, input().split())
    alice_win = (x2 - x1) % 2 == 1
    alice_left = y2 - y1 > 0
    alice_turn = True

    for i in range(x2 - x1):
        if alice_turn:
            x1 += 1
            if (alice_win and alice_left) or (not alice_win and not alice_left): # 앨리스가 이기고 밥이 오른쪽에 있거나, 앨리스가 지고 앨리스가 오른쪽에 있을 때
                y1 += move(y1,'R') # 오른쪽으로 이동
            elif alice_win and y1 == y2:
                pass
            else:
                y1 += move(y1,'L')
        else:
            x2 -= 1
            if (alice_win and alice_left) or (not alice_win and not alice_left):
                y2 += move(y2,'R')
            else:
                y2 += move(y2,'L')

        alice_turn = not alice_turn

        if y1 == y2: # 상대를 잡았을 때
            if alice_win:
                print('Alice')
            else:
                print('Bob')
            break
    else:
        print('Draw')
