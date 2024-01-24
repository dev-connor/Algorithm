import math

m,n = map(int, input().split())
array = [True for i in range(n+1)]
array[0] = array[1] = False # 0 과 1 은 소수가 아님

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False # 배수들은 소수가 아님
            j += 1

for i in range(m,n+1):
    b = array[i]
    if b:
        print(i)