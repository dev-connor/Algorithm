import sys

input = sys.stdin.readline

n,k = map(int, input().split())
nums = list(map(int, input().split()))

answer = -1e9
sum_ = 0
prefix_sum = [0]
for i in nums:
    sum_ += i
    prefix_sum.append(sum_)

for i in range(n-k+1):
    answer = max(answer, prefix_sum[i+k]-prefix_sum[i])
print(answer)