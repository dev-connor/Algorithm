str = input()
answer = 0

for c in str:
    t = (ord(c) - 65) // 3 + 3
    if c in 'SVYZ':
        t -= 1
    answer += t

print(answer)
