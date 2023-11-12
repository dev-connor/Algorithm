# 실버5
if __name__ == '__main__':
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())

    cnt = 0

    for str in strings:
        s = set()
        before = ''
        for c in str:
            if c == before: # 같은 문자가 연속
                continue

            if c not in s:
                s.add(c)
                before = c
            else: # 그룹단어가 아닌 경우
                break
        else:
            cnt += 1

    print(cnt)
