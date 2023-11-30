s = input()
answer = [-1]*26

for i,c in enumerate(s):
    idx = ord(c)-97
    if answer[idx] == -1:
        answer[idx] = i

print(' '.join(map(str, answer)))

