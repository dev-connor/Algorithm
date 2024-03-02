from itertools import permutations

n,cnt = map(int, input().split())
nums = [i for i in range(1,n+1)]

for ans in permutations(nums, cnt):
    print(' '.join(map(str, ans)))
    