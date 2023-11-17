# 브론즈3 - 3:18
while True:
    n,m = map(int, input().split())

    if n == 0 and m == 0:
        break

    if m % n == 0: # 약수
        print('factor')
    elif n % m == 0: # 배수
        print('multiple')
    else:
        print('neither')
