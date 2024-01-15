import sys

input = sys.stdin.readline

sum_ = 0
prefix_sum = [0]

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

for i in nums:
    sum_ += i
    prefix_sum.append(sum_)

print(sum(prefix_sum))