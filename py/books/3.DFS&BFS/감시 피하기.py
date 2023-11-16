import itertools

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))

    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))

        if board[i][j] == 'X':
            spaces.append((i,j))

    def watch(x,y,direction):
        if direction == 0: # 좌
            while y >= 0:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                y -= 1
        elif direction == 1: # 우
            while y < n:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                y += 1
        elif direction == 2: # 상
            while x >= 0:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                x -= 1
        elif direction == 3: # 하
            while x < n:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                x += 1

    def process():
        for x,y in teachers:
            for i in range(4):
                if watch(x,y,i):
                    return True
        return False

find = False

for data in itertools.combinations(spaces,3):
    for x,y in data:
        board[x][y] = 'O'
    if not process():
        find = True
        break
    for x,y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')

'''
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
'''