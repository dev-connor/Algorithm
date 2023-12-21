# 8:24
k,n = map(int, input().split())
nums = [0] * k
for i in range(k):
    nums[i] = int(input())

start = 1
end = max(nums)

result = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for x in nums:
        cnt += x//mid
        
    if cnt < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)