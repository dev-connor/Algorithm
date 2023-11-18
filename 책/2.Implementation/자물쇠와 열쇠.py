def fill(matrix1, matrix2, x, y):
    size = len(matrix2)
    for i in range(size):
        for j in range(size):
            matrix1[x + i][y + j] += matrix2[i][j]

def drain(matrix1, matrix2, x, y):
    size = len(matrix2)
    for i in range(size):
        for j in range(size):
            matrix1[x + i][y + j] -= matrix2[i][j]

def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_matrix[j][n-i-1] = matrix[i][j]
    return new_matrix

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

# Lv3. +6
def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                fill(new_lock, key, x, y)
                if check(new_lock):
                    return True
                drain(new_lock, key, x, y)
    return False

array1 = [[0,0,0],[1,0,0],[0,1,1]]
array2 = [[1,1,1],[1,1,0],[1,0,1]]
result = solution(array1,array2)
print(result)
