n = int(input())
nums = list(map(int, input().split()))
# plus, minus, multiple, division = map(int, input().split())
e_opers = list(map(int, input().split()))

max_v = -int(1e9)
min_v = int(1e9)

oper_arr = ['+','-','*','/']

# nums = []

def dfs(opers, num, idx):
    global min_v, max_v

    if idx == n:
        min_v = min(min_v, num)
        max_v = max(max_v, num)
        return

    for i in range(4):
        if opers[i] < e_opers[i]:
            opers[i] += 1
            dfs(opers, int(eval(str(num) + oper_arr[i] + str(nums[idx]))), idx+1)
            opers[i] -= 1

dfs([0,0,0,0], nums[0], 1)
print(max_v)
print(min_v)