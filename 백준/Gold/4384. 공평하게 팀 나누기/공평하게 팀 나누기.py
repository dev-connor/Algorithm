n = int(input())
weights = [0] * n
max_n = 100
max_k = 450
max_w = int(max_n / 2*max_k)
t = 0
a = int(1e9)
diff = int(1e9)
dp = [[0] * (max_w+1) for _ in range(51)]
for i in range(n):
    weights[i] = int(input())
    t += weights[i]

dp[0][0] = 1
for i in range(n):
    for j in range(n//2,-1,-1):
        for k in range(max_w,-1,-1):
            dp[j][k] = max(dp[j][k],dp[j-1][k-weights[i]])
for k in range(max_w):
    if dp[n//2][k] == 1:
        if diff > abs(t-2*k):
            diff = abs(t-2*k)
            a = k
b = t-a
if a > b:
    a,b = b,a
print(a,b)

