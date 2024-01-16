t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    f = input()

    answer = 0
    c1 = s.count('1')
    c2 = f.count('1')
    need_one = c2 - c1
    half = 0


    for i in range(n):
        if s[i] == f[i]:
            continue
        else:
            if need_one > 0:
                need_one -= 1
                answer += 1
            elif need_one < 0:
                need_one += 1
                answer += 1
            else:
                half += 1

    print(answer + half//2)

