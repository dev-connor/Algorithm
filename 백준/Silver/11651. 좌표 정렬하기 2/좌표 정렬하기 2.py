import sys

input = sys.stdin.readline
n = int(input())
pos = [0]*n
for i in range(n):
    a,b = map(int, input().split())
    pos[i] = (a,b)

pos.sort(key=lambda x:(x[1],x[0]))
for i in pos:
    print(i[0],i[1])
    
