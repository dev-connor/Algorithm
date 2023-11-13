# +9 - 30:25
def solution(s):
    length = len(s)

    answer = 1
    for center in range(1,length-1): # 홀수 팰린드롬
        cnt = 1
        for i in range(1,length//2+1):
            if center-i < 0 or center+i >= length:
                break

            if s[center-i] == s[center+i]:
                cnt += 2
            else:
                break
        answer = max(answer,cnt)

    for center in range(0,length-1): # 짝수 팰린드롬
        cnt = 0
        for i in range(0,length//2+1):
            if center-i < 0 or center+i+1 >= length:
                break

            if s[center-i] == s[center+i+1]:
                cnt += 2
            else:
                break
        answer = max(answer,cnt)

    return answer

if __name__ == '__main__':
    array = []
    strings = 'aabbaa'
    result = solution('aabc')
    print(result)


