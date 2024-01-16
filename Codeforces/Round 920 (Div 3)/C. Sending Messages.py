t = int(input())
for _ in range(t):
    n,f,a,b = map(int, input().split())
    msgs = list(map(int, input().split()))
    now = 0

    for msg in msgs:
        f -= min((msg-now)*a,b)
        if f <= 0:
            break
        now = msg
    else:
        print('YES')
        continue
    print('NO')