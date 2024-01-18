import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    a.insert(0,0)
    b.insert(0,0)

    for i in range(1,n):
        a[i+1] += a[i]
    for i in range(1,m):
        b[i+1] += b[i]

    answer = 0
    for i in range(n+1):
        j = n-i
        cur = 0
        cur += b[m]-b[m-i]-a[i]
        cur += a[n]-a[n-j]-b[j]
        answer=max(answer,cur)
    print(answer)
