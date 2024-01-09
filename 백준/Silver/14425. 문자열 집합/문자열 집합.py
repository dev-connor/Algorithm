n,m = map(int, input().split())
s = set()
answer = 0
for _ in range(n):
    s.add(input())
for _ in range(m):
    input_ = input()
    if input_ in s:
        answer += 1
print(answer)