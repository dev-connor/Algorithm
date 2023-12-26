x = set()
y = set()
for _ in range(3):
    a,b = map(int, input().split())
    if a in x:
        x.remove(a)
    else:
        x.add(a)
    if b in y:
        y.remove(b)
    else:
        y.add(b)

print(x.pop(),y.pop())



    