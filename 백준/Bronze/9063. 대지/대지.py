n = int(input())
a=b=int(1e9)
c=d=int(-1e9)

for _ in range(n):
    x,y=map(int,input().split())
    a=min(a,x)
    b=min(b,y)
    c=max(c,x)
    d=max(d,y)
print(abs(c-a)*abs(d-b))
    