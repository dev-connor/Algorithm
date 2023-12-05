# 8:33
n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()
answer = []

def dfs(now):
    cnt = len(answer)

    if cnt == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(now, len(nums)):
        if len(answer) == 0 or answer[-1] <= nums[i]:
            answer.append(nums[i])
            dfs(now)
            answer.pop()

dfs(0)
