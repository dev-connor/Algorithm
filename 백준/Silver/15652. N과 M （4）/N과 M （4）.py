n,cnt = map(int,input().split())
nums = []

def dfs(now):
    if len(nums) == cnt:
        ans = ' '.join(map(str, nums))
        print(ans)
        return
    
    for i in range(now, n+1):
        nums.append(i)
        dfs(i)
        nums.pop()
        
dfs(1)
    