import itertools

# level3 - +9
def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1

    for start_i in range(length):
        f_order = list(itertools.permutations(dist,len(dist)))
        for friends in f_order:
            f_cnt = 1
            position = weak[start_i] + friends[f_cnt-1]
            for index in range(start_i, start_i + length):
                if position < weak[index]:
                    f_cnt += 1 # 다음친구 투입
                    if f_cnt > len(dist):
                        break
                    position = weak[index] + friends[f_cnt-1]
            answer = min(answer, f_cnt)
    if answer > len(dist):
        return -1
    return answer

if __name__ == '__main__':
    array1 = [1, 5, 6, 10]
    array2 = [1, 2, 3, 4]
    result = solution(12,array1,array2)
    print(result)



