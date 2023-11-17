# 브론즈3 - 4:21 
n,k = map(int, input().split())
answer = []

for i in range(1,n+1):
    if n % i == 0:
        answer.append(i)

if k-1 < len(answer):
    print(answer[k-1])
else:
    print(0)