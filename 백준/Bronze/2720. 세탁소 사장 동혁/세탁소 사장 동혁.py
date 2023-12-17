t = int(input())
for _ in range(t):
    n = int(input())
    arr = [25,10,5,1]
    answer = [0] * 4

    while n != 0:
        for i,v  in enumerate(arr):
            if n >= v:
                q = n // v
                n = n % v
                answer[i] = q

    for i in answer:
        print(i, end=' ')
    print()
