def divisor_counts(start, end):
    divisor = [1 for _ in range(end + 1)]

    for i in range(2, end + 1):
        if start % i == 0:
            s = start
        else:
            s = i*(start//i+1)
        for j in range(s, end + 1, i):
            divisor[j] += 1
    return divisor

def solution(left, right):
    answer = 0

    divisor_cnt = divisor_counts(left, right)
    for n in range(left,right+1):
        if divisor_cnt[n] % 2 == 0:
            answer += n
        else:
            answer -= n

    return answer

array = []
result = solution(24,27)
print(result)
