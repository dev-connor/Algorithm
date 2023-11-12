import collections

# 서로소 집합으로 풀었지만, 가중치가 같기에 BFS 로 풀어도 됨. 혹은 set 으로 푼 사람도 있음.
def solution(n, wires):
    answer = 101

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    for i in range(len(wires)): # 제외 할 전선
        p = [i for i in range(n + 1)]

        # 하나의 전선을 끊고 전력망 세기
        for j,w in enumerate(wires):
            if i == j:
                continue
            union_parent(p,w[0],w[1])

        for i in range(n+1):
            p[i] = find_parent(p, i)

        counts = dict(collections.Counter(p[1:]))
        tower_cnts = list(counts.values())
        answer = min(answer, abs(tower_cnts[0] - tower_cnts[1]))

    return answer

if __name__ == '__main__':
    array = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    array2 = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
    result = solution(9,array)
    print(result)
