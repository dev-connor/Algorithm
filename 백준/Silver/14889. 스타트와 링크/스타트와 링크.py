# 15:57
import itertools

n = int(input())
stats = []
for i in range(n):
    stats.append(list(map(int, input().split())))

all_m = {i for i in range(n)}
picked = list(itertools.combinations(all_m,n//2))
min_v = int(1e9)

for p in picked:
    start = set(p)
    link = all_m - start
    s_sum = 0
    l_sum = 0

    s_two = list(itertools.combinations(start,2))
    for s in s_two:
        s_sum += stats[s[0]][s[1]] + stats[s[1]][s[0]]

    l_two = list(itertools.combinations(link,2))
    for l in l_two:
        l_sum += stats[l[0]][l[1]] + stats[l[1]][l[0]]

    min_v = min(min_v, abs(s_sum - l_sum))

print(min_v)