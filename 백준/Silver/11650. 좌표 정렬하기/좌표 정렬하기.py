n = int(input())
nums= []
for _ in range(n):
    nums.append(tuple(map(int,input().split())))
nums.sort()
for i in nums:
    print(i[0],i[1])
