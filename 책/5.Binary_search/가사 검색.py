import bisect

def count_by_range(array, left_value, right_value):
    right_index = bisect.bisect_right(array, right_value)
    left_index = bisect.bisect_left(array, left_value)
    return right_index - left_index

array = [[] for _ in range(10001)]
reversed_array = [[]for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?','a'), q.replace('?','z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        answer.append(res)
    return answer

array1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
array2 = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = solution(array1, array2)
print(result)
