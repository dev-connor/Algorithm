n,m = map(int, input().split())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''

length = 0
while m**length <= n:
    length += 1

for i in range(length-1,-1,-1):
    a = n // (m**i)
    n = n % (m**i)

    if a < 10:
        answer += str(a)
    else:
        answer += alpha[a-10]

print(answer)

