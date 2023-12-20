n,c = map(int, input().split())
nums = [0] * n
for i in range(n):
    nums[i] = int(input())

start = 1
nums.sort()
end = nums[-1] - nums[0]

result = 0
while start <= end:
    cnt = 1
    mid = (start + end) // 2
    pos = 0

    for i in range(1,n):
        if nums[pos]+mid <= nums[i]:
            cnt += 1
            pos = i

    if cnt < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)