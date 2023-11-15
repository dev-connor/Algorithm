# 실버5 - 10:33
n = int(input())
answer = []
num = 666
while len(answer) < n:
    cnt = 0
    s = str(num)
    f = False

    for i in range(len(s)):
        if cnt == 3:
            f = True
            break

        if s[i] == '6':
            cnt += 1
        else:
            cnt = 0

    if cnt == 3 or f:
        answer.append(s)

    num += 1

print(answer[-1])


