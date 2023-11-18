# 실버4 - 6:44
answer = 0

n, money = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

for i in range(n-1,-1,-1):
    answer += money // coins[i]
    money %= coins[i]

print(answer)


'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''