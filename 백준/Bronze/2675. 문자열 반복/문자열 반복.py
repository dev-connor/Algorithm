t = int(input())
for _ in range(t):
    r,s = input().split()
    for c in s:
        print(c*int(r),end='')
    print()