# Lv2. +3 - 15:26
def solution(people, limit):
    answer = 0

    i = 0
    j = len(people)-1

    people.sort()

    while i <= j:
        if people[i] + people[j] > limit:
            answer += 1
            j -= 1
        else:
            answer += 1
            i += 1
            j -= 1

    return answer

array = [70, 50, 80, 50]
result = solution(array, 100)
print(result)
