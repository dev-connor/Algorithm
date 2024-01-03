from collections import deque

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    docs = list(map(int, input().split()))

    sorted_ = sorted(docs,reverse=True)
    q = deque()

    for i,d in enumerate(docs):
        if i == m:
            q.append((d,True))
        else:
            q.append((d,False))

    for i in range(n):
        f = False
        while True:
            a,b = q.popleft()
            if a == sorted_[i]:
                if b:
                    print(i+1)
                    f = True
                break
            else:
                q.append((a,b))
        if f:
            break

