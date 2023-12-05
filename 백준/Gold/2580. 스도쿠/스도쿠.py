board = [[0] * 9 for _ in range(9)]
zeros = []
hodi = dict()
vedi = dict()
bxdi = dict()

def add(d, a, b):
    s = d.setdefault(a, set())
    s.add(b)

def remove(d, a, b):
    d.get(a, set()).discard(b)

for i in range(9):
    inputs = list(map(int, input().split()))
    for j,v in enumerate(inputs):
        board[i][j] = v
        add(hodi,i,v)
        add(vedi,j,v)
        nx = str(i//3)
        ny = str(j//3)
        add(bxdi,nx+ny,v)
        if v == 0:
            zeros.append((i,j))

# visited = [False] * (n+1)
# nums = []

def dfs(idx):
    if idx == len(zeros):
        for i in range(9):
            print(' '.join(map(str, board[i])))
        exit()

    def check_ho(x,y,v):
        if v in hodi[x]:
            return False
        return True

    def check_ve(x,y,v):
        if v in vedi[y]:
            return False
        return True

    def check_box(x,y,v):
        nx = str(x//3)
        ny = str(y//3)

        if v in bxdi[nx+ny]:
            return False
        return True

    zero = zeros[idx]
    x = zero[0]
    y = zero[1]

    for i in range(1,10):
        if check_ho(x,y,i) and check_ve(x,y,i) and check_box(x,y,i):
            # nums.append(i)
            board[x][y] = i

            add(hodi, x, i)
            add(vedi, y, i)
            nx = str(x // 3)
            ny = str(y // 3)
            add(bxdi, nx + ny, i)

            dfs(idx+1)
            board[x][y] = 0

            remove(hodi, x, i)
            remove(vedi, y, i)
            nx = str(x // 3)
            ny = str(y // 3)
            remove(bxdi, nx + ny, i)

            # nums.pop()

dfs(0)
