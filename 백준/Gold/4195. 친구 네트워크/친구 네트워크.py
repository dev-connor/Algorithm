from sys import stdin

input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        number[a] += number[b]
    print(number[a])


for _ in range(int(input())):
    num = int(input())
    parent, number = {}, {}
    for i in range(num):
        a, b = input().split()
        parent.setdefault(a,a)
        parent.setdefault(b,b)
        number.setdefault(a,1)
        number.setdefault(b,1)
        union(a, b)