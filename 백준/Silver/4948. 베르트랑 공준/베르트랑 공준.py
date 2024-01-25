import math

while True:
    n = int(input())
    if n == 0:
        break

    array = [True for i in range(2*n+1)] # 확인할 소수의 최대값 
    array[0] = array[1] = False # 0 과 1 은 소수가 아님

    for i in range(2, int(math.sqrt(2*n)) + 1):
        if array[i]:
            j = 2
            while i * j <= 2*n:
                array[i * j] = False # 배수들은 소수가 아님
                j += 1

    cnt = 0
    for i in range(n+1,2*n+1):
        if array[i]:
            cnt += 1
    print(cnt)
