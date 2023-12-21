import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))
dp = [0]

for a in A:
    if dp[-1] < a:
        dp.append(a)
    else:
        dp[bisect_left(dp, a)] = a

print(len(dp) - 1)