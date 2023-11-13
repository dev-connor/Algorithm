import itertools

# +3 - 28:37
def solution(k, dungeons):
    l = len(dungeons)
    cycles = list(itertools.permutations(range(l)))
    max_d = 0

    for cycle in cycles:
        cnt = 0
        fatigue_p = k
        for d in cycle:
            min_p = dungeons[d][0] # 최소 필요 피로도
            use_p = dungeons[d][1] # 소모 피로도

            if fatigue_p < min_p:
                break # 던전을 그만 돕니다.

            fatigue_p -= use_p
            cnt += 1
        max_d = max(max_d, cnt)

    return max_d

if __name__ == '__main__':
    array = [[80,20],[50,40],[30,10]]
    result = solution(80, array)
    print(result)
