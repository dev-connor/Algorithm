# 브론즈2 - 13:15
if __name__ == '__main__':
    n = int(input())
    answer = 1e9

    for i in range(1,n):
        sum_n = i

        for j in range(len(str(i))):
            sum_n += int(str(i)[j])

        if sum_n == n:
            answer = i
            break
    else:
        answer = 0

    print(answer)


