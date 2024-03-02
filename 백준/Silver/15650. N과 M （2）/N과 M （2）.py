from itertools import combinations

n,cnt = map(int,input().split())

for nums in combinations([i for i in range(1,n+1)],cnt):
    ans = ' '.join(map(str, nums))
    print(ans)