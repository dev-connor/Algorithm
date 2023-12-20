import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

start = 1
end = N * N
result = 0

while start <= end:
    cnt = 0

    mid = (start + end) // 2

    for div in range(1, N + 1):
        cnt += min(mid // div, N)
    
    if cnt >= K:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)