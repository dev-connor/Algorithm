n = int(input())
ee = set()
for _ in range(n):
    a,b = input().split()
    if b == 'enter':
        ee.add(a)
    else:
        ee.remove(a)
for name in sorted(ee,reverse=True):
    print(name)
        
        