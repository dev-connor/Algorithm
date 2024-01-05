NUMBER = 12
a = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
tree = [0]*(4*NUMBER) # 4를 곱하면 모든 범위를 커버할 수 있음. 갯수에 대해서 2의 제곱 형태의 길이를 가지기 때문임.

# start: 시작 인덱스, end: 끝 인덱스
def init(start,end,node):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    mid = (start+end) // 2
    # 재귀적으로 두 부분으로 나눈 뒤에 그 합을 자기 자신으로 합니다.
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]

# start: 시작 인덱스, end: 끝 인덱스
# left, right: 구간 합을 구하고자 하는 범위
def sum(start,end,node,left,right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0
    # 범위 안에 있는 경우
    if left <= start and end <= right:
        return tree[node]
    # 그렇지 않다면 두 부분으로 나누어 합을 구하기
    mid = (start+end) // 2
    sum_ = sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right)
    return sum_

# start: 시작 인덱스, end: 끝 인덱스
# index: 구간 합을 수정하고자 하는 노드
# dif: 수정할 값
def update(start,end,node,index,dif):
    if start <= index <= end: # 범위 안에 있는지 체크
        tree[node] += dif
        if start == end:
            return
        mid = (start+end)//2
        update(start,mid,node*2,index,dif)
        update(mid+1,end,node*2+1,index,dif)

# 구간 합 트리의 인덱스를 제외하고는 모두 인덱스 0부터 시작합니다.
# 구간 합 트리 생성하기
init(0,NUMBER-1,1)
# 구간 합 구하기
print("0부터 12까지의 구간 합:", sum(0, NUMBER - 1, 1, 0, 12))
print("3부터 8까지의 구간 합:", sum(0, NUMBER - 1, 1, 3,8))
print('인덱스 5의 원소를 -5만큼 수정')
update(0, NUMBER - 1, 1, 5, -5)
print("3부터 8까지의 구간 합:", sum(0, NUMBER - 1, 1, 3,8))
