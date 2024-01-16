n,m = map(int, input().split())
answer = set()
visited = set()
for _ in range(n):
    visited.add(input())
for _ in range(m):
    name = input()
    if name in visited:
        answer.add(name)
print(len(answer))
for name in sorted(answer):
    print(name)