while True:
    lens = list(map(int,input().split()))
    if lens[0] == 0:
        break
    lens.sort()
    if lens[2] >= lens[0]+lens[1]:
        print('Invalid')
    elif lens[0] == lens[2]:
        print('Equilateral')
    elif lens[0] == lens[1] or lens[1] == lens[2]:
        print('Isosceles')
    else:
        print('Scalene')