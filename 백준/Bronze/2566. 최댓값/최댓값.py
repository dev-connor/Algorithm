max_v = -1
x = -1
y = -1

for i in range(9):
    inputs = list(map(int, input().split()))
    for j,v in enumerate(inputs):
        if max_v < v:
            max_v = v
            x = i + 1
            y = j + 1

print(max_v)
print(x,y)
