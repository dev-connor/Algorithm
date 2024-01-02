# 11:05
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]*(n+1)

for i,n in enumerate(nums):
    sum_value += n
    prefix_sum[i+1] = sum_value

for _ in range(m):
    a,b = map(int, input().split())
    print(prefix_sum[b]-prefix_sum[a-1])