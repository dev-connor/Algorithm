n = int(input())
nums = list(map(int, input().split()))
sort_nums = sorted(set(nums))
d = {}
for i,m in enumerate(sort_nums):
    d.setdefault(m,i)

for i in nums:
    print(d[i],end=' ')
