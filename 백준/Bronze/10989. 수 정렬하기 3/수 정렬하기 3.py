import sys

input = sys.stdin.readline
n = int(input())

counts = [0] * 10001
for _ in range(n):
    counts[int(input())] += 1

for i,v in enumerate(counts):
    while counts[i] != 0:
        print(i)
        counts[i] -= 1
