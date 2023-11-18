# 브론즈2 - 11:20
# 1은 소수가 아니다. 
m = int(input())
n = int(input())

n_sum = 0
n_min = n+1

for i in range(n,m-1,-1):
    if i == 1:
        continue

    for j in range(2,i):
        if i % j == 0:
            break # 소수가 아님
    else:
        n_min = i
        n_sum += i

if n_sum == 0:
    print(-1)
    exit()

print(n_sum)
print(n_min)

'''
60
100
'''