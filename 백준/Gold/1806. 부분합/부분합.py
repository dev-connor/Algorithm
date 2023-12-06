n,s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0
answer = int(1e9)

if sum(nums) < s:
    print(0)
    exit()

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += nums[end]
        end += 1
    if interval_sum >= s:
        answer = min(answer,end-start)
    interval_sum -= nums[start]

print(answer)