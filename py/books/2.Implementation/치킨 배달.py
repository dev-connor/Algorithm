import itertools

if __name__ == '__main__':
    n,m = list(map(int, input().split()))
    chicken, house = [], []

    for r in range(n):
        data = list(map(int, input().split()))
        for c in range(n):
            if data[c] == 1: # 집일 때
                house.append((r,c))
            elif data[c] == 2: # 치킨집일 때
                chicken.append((r,c))

    candidates = list(itertools.combinations(chicken, m))

    def get_sum(candidate):
        result = 0
        for hx,hy in house:
            temp = 1e9
            for cx,cy in candidate:
                temp = min(temp, abs(hx - cx) + abs(hy - cy))
            result += temp
        return result
    result = 1e9
    for candidate in candidates:
        result = min(result, get_sum(candidate))
    print(result)

'''
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
'''