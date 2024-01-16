t = int(input())
for _ in range(t):
    x = set()
    y = set()
    for i in range(4):
        a,b = map(int, input().split())
        x.add(a)
        y.add(b)

    x1= list(x)
    y1= list(y)
    print(abs(x1[1]-x1[0])*abs(y1[1]-y1[0]))
