n,cnt = map(int,input().split())
nums = []

def dfs():
    if len(nums) == cnt:
        ans = ' '.join(map(str, nums))
        print(ans)
        return
    
    for i in range(1, n+1):
        nums.append(i)
        dfs()
        nums.pop()
        
dfs()