h,w = map(int, input().split())
blocks = [[0] * w for _ in range(h)]
heights = list(map(int, input().split()))

for x,height in enumerate(heights):
    for y in range(height):
        blocks[y][x] = 1

answer = 0
for i in range(h):
    one_idx = -1
    
    for j in range(w):
        if blocks[i][j] == 1:
            if one_idx == -1:
                one_idx = j
            else:
                answer += j - one_idx - 1
                one_idx = j

print(answer)
