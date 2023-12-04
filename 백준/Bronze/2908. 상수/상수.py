a,b = input().split()
new_a = int(a[2]+a[1]+a[0])
new_b = int(b[2]+b[1]+b[0])

if new_a > new_b:
    print(new_a)
else:
    print(new_b)
