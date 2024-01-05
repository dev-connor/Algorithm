import sys

input = sys.stdin.readline

n,m,k = map(int, input().split())
nums = [0] * n
for i in range(n):
    nums[i] = int(input())
inputs = []
for i in range(m+k):
    inputs.append(list(map(int, input().split())))

length = len(nums)
tree = [0]*(4 * length)

def segment(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start+end) // 2
    # 재귀적으로 두 부분으로 나눈 뒤에 그 합을 자기 자신으로 합니다.
    tree[node] = segment(start, mid, node * 2) + segment(mid + 1, end, node * 2 + 1)
    return tree[node]

def prefix_sum(start, end, node, left, right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0
    # 범위 안에 있는 경우
    if left <= start and end <= right:
        return tree[node]
    # 그렇지 않다면 두 부분으로 나누어 합을 구하기
    mid = (start+end) // 2
    sum_ = prefix_sum(start, mid, node * 2, left, right) + prefix_sum(mid + 1, end, node * 2 + 1, left, right)
    return sum_

def update(start,end,node,index,dif):
    if start <= index <= end: # 범위 안에 있는지 체크
        tree[node] += dif
        if start == end:
            return
        mid = (start+end)//2
        update(start,mid,node*2,index,dif)
        update(mid+1,end,node*2+1,index,dif)

segment(0,length-1,1)
for i in inputs:
    a,b,c = i

    if a == 1:
        update(0,length-1,1,b-1,c-nums[b-1])
        nums[b-1] = c
    else:
        print(prefix_sum(0,length-1,1,b-1,c-1))
