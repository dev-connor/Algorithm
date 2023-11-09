# 탑다운 with 메모이제이션
if __name__ == '__main__':
    d = [0] * 100

    def fibo(x):
        if x == 1 or x == 2:
            return 1

        if d[x] != 0:
            return d[x]

        d[x] = fibo(x-1) + fibo(x-2)
        return d[x]

    print(fibo(99))