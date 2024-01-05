n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))
white = 0
blue = 0

def divncon(r,c,size):
    global white,blue

    color = -1

    for i in range(r,r+size):
        f = False
        for j in range(c,c+size):
            if color == -1:
                color = paper[i][j]
            else:
                if paper[i][j] != color:
                    mid = size//2
                    divncon(r,c,mid)
                    divncon(r,c+mid,mid)
                    divncon(r+mid,c,mid)
                    divncon(r+mid,c+mid,mid)
                    f = True
                    break
        if f:
            break
    else:
        if color == 1:
            blue += 1
        else:
            white += 1

divncon(0,0,n)
print(white)
print(blue)