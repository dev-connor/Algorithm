# 브론즈1 - 5:47 
while True:
    n = int(input())

    if n == -1:
        break

    answer = []
    for i in range(1,n):
        if n % i == 0:
            answer.append(i)

    if sum(answer) == n:
        s = ' + '.join(map(str,answer))
        print(f'{n} = {s}')
    else:
        print(f'{n} is NOT perfect.')