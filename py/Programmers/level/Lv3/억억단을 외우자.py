# +11
# 배열복사도 자제하자. 시간든다.
def solution(e, starts):
    length = len(starts)
    answer = [0]*length
    sorted_starts = sorted(starts)
    answer_dict = dict()

    divisor = [1 for _ in range(e + 1)]
    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            divisor[j] += 1

    memo = -1
    for i,n in enumerate(sorted_starts):
        if memo == -1:
            num = divisor[sorted_starts[i]:].index(max(divisor[sorted_starts[i]:])) + sorted_starts[i]
            answer_dict.setdefault(n,num)
            memo = num
        else:
            if n <= memo:
                answer_dict.setdefault(n,memo)
            else:
                num = divisor[sorted_starts[i]:].index(max(divisor[sorted_starts[i]:])) + sorted_starts[i]
                answer_dict.setdefault(n, num)
                memo = num

    for i,s in enumerate(starts):
        answer[i] = answer_dict.get(s)

    return answer

array = [7,1,3]
result = solution(8,array)
print(result)
