n,cnt = map(int,input().split())
nums = []
visited = set()

def dfs():
    if len(nums) == cnt:
        ans = ' '.join(map(str, nums))
        print(ans)
        return
    
    for i in range(1, n+1):
        if i not in visited:
            nums.append(i)
            visited.add(i)
            dfs()
            nums.pop()
            visited.remove(i)

dfs()