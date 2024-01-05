import sys

input = sys.stdin.readline

sum_ = 0
prefix_sum = [0]

s = list(input().rstrip())
q = int(input())
inputs = []
length = len(s)
counts = [[0] * (length+1) for _ in range(26)]
for _ in range(q):
    a,b,c = [i if i.isalpha() else int(i) for i in input().split()]
    inputs.append((ord(a)-ord('a'),b,c))

for i,c in enumerate(s):
    row = ord(c)-ord('a')
    for j in range(26):
        if row == j:
            counts[j][i+1] = counts[j][i] + 1
        else:
            counts[j][i+1] = counts[j][i]

for a,b,c in inputs:
    print(counts[a][c+1] - counts[a][b])