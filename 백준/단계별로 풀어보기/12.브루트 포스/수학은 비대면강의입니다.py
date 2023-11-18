# 브론즈2 - 7:45
a,b,c,d,e,f = map(int, input().split())

for x in range(2, 1000):
    for y in range(-1, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            exit()

'''
1 3 -1 4 1 7
'''