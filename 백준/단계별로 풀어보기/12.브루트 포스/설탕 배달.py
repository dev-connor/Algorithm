# 실버4 - 10:16
n = int(input())

for i in range(1667):
    if n - 3*i >= 0 and (n - 3*i) % 5 == 0:
        print(i + (n-3*i)//5)
        exit()

print(-1)
