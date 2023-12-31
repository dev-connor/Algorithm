lengs = list(map(int,input().split()))
lengs.sort()

if lengs[0] + lengs[1] <= lengs[2]:
    print(2*(lengs[0]+lengs[1])-1)
else:
    print(sum(lengs))