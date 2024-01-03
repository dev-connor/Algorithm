import sys

n = int(input())

before = 2
answer = []
s = [0]*(n+1)
p = [0]*(n+2)

for i in range(1,n+1):
    print(f'? 1 {i}')
    sys.stdout.flush()
    s[i] = int(input())
for i in range(1,n+1):
    print(f'? {i} {n}')
    sys.stdout.flush()
    p[i] = int(input())

answer = []
for i in range(1,n+1):
    if s[i-1]+1 == s[i] and p[i] == p[i+1]+1:
        answer.append(i)

str = ' '.join(map(str,answer))
print(f'! {len(answer)} {str}')
