def solution(str1, str2):
    answer = ''
    for i in range(len(str1) * 2):
        c = str1[i // 2] if i % 2 == 0 else str2[i // 2]
        answer += c

    return answer