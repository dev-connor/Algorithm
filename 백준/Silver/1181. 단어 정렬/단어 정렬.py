n = int(input())
strs = []
visited = set()
for i in range(n):
    string = input()
    if string not in visited:
        strs.append((len(string), string))
        visited.add(string)

strs.sort()
for string in strs:
    print(string[1])