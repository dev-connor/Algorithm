# 5:49
n,m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in trees:
        if mid <= x:
            total += x - mid
            if total >= m:
                break

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)