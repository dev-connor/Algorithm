# 47:46
board = [[0] * 9 for _ in range(9)]
zeros = []
h_nums = dict()
v_nums = dict()
bx_nums = dict()

def add(d, a, b):
    s = d.setdefault(a, set())
    s.add(b)

def remove(d, a, b):
    d.get(a, set()).discard(b)

for i in range(9):
    inputs = list(map(int, input().split()))
    for j,v in enumerate(inputs):
        board[i][j] = v
        add(h_nums, i, v)
        add(v_nums, j, v)
        nx = str(i//3)
        ny = str(j//3)
        add(bx_nums, nx + ny, v)
        if v == 0:
            zeros.append((i,j))

def check_ho(x,v):
    if v in h_nums[x]:
        return False
    return True

def check_ve(y,v):
    if v in v_nums[y]:
        return False
    return True

def check_box(nx,ny,v):
    if v in bx_nums[nx + ny]:
        return False
    return True

def dfs(idx):
    if idx == len(zeros):
        for v in range(9):
            print(' '.join(map(str, board[v])))
        exit()

    zero = zeros[idx]
    x = zero[0]
    y = zero[1]

    for v in range(1,10): # 1~9 까지 넣어보기
        nx = str(x // 3) # 박스의 위치
        ny = str(y // 3)

        if check_ho(x,v) and check_ve(y,v) and check_box(nx,ny,v):
            board[x][y] = v
            add(h_nums, x, v)
            add(v_nums, y, v)
            add(bx_nums, nx + ny, v)

            dfs(idx+1) # 다음 빈칸 채우러가기

            board[x][y] = 0
            remove(h_nums, x, v)
            remove(v_nums, y, v)
            remove(bx_nums, nx + ny, v)

dfs(0)
