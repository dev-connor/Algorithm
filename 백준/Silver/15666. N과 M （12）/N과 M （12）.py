n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()
answer = []
# s = set()
# visited = [False] * n

def dfs(now):
    cnt = len(answer)

    if cnt == m:
        # if str(answer) not in s:
        print(' '.join(map(str, answer)))
        # s.add(str(answer))
        return

    for i in range(now, len(nums)):
        if len(answer) == 0 or answer[-1] <= nums[i]:
            answer.append(nums[i])
            dfs(now)
            answer.pop()

dfs(0)
