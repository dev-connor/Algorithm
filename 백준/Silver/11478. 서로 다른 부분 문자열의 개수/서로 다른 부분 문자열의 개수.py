s = input()
n = len(s)
answer = set()

for t in range(1, n + 1):
    end = n - t + 1
    for j in range(end):
        answer.add(s[j:j + t])
print(len(answer))
