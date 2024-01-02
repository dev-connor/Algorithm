h,w = map(int, input().split())
blocks = [[0] * w for _ in range(h)]
heights = list(map(int, input().split()))

for start,height in enumerate(heights):
    for i in range(height):
        blocks[i][start] = 1

answer = 0
for i in range(h):
    start = -1
    
    for j in range(w):
        if blocks[i][j] == 1:
            if start == -1:
                start = j
            else:
                answer += j - start - 1
                start = j

print(answer)
