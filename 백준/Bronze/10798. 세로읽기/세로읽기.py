board = []
for i in range(5):
    board.append(list(input()))

for i in range(15):
    for j in range(5):
        if i < len(board[j]):
            print(board[j][i], end='')

