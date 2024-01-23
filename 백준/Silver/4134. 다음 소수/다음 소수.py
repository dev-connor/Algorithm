t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 1:
        print(2)
        continue
    while True:
        find = False
        for i in range(2,int(n**(1/2))+1):
            if n % i == 0: # 소수 아님
                break
        else:
            print(n)
            break
        n += 1
        continue
