nums = [0]*26
s = input()
for c in s:
    nums[ord(c)-97] += 1

for i in nums:
    print(i, end=' ')