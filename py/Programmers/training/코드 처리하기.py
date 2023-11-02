# +4
def solution(code):
    answer = ''
    mode = 0

    for i,v in enumerate(code):
        if mode == 0:
            if v != '1':
                if i % 2 == 0:
                    answer = answer + v
            else:
                mode = 1
        else:
            if v != '1':
                if i % 2 == 1:
                    answer = answer + v
            else:
                mode = 0

    if len(answer) == 0:
        return 'EMPTY'

    return answer

if __name__ == '__main__':
    result = solution("abc1abc1abc")
    print(result)