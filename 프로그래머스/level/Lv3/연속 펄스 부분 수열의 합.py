# +6 - 42:56
def solution(sequence):
    s1 = sequence.copy() # -1 부터
    s2 = sequence.copy()
    dp1 = [-i for i in sequence]
    dp2 = sequence.copy()

    for i in range(len(sequence)):
        a = 1 if i % 2 == 1 else -1
        s1[i] = a * s1[i]
        b = 1 if i % 2 == 0 else -1
        s2[i] = b * s2[i]

    for i in range(1, len(sequence)):
        dp1[i] = max(dp1[i-1] + s1[i], s1[i])
        dp2[i] = max(dp2[i-1] + s2[i], s2[i])

    return max(max(dp1), max(dp2))

if __name__ == '__main__':
    array = [2, 3, -6, 1, 3, -1, 2, 4]
    result = solution(array)
    print(result)
