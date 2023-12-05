# 9:40
n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []
s = set()
visited = [False] * n

def dfs():
    cnt = len(answer)

    if cnt == m:
        if str(answer) not in s:
            print(' '.join(map(str, answer)))
        s.add(str(answer))
        return

    for i in range(n):
        if not visited[i]:
            answer.append(nums[i])
            visited[i] = True
            dfs()
            answer.pop()
            visited[i] = False

dfs()
