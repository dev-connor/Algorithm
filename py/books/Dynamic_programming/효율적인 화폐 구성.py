if __name__ == '__main__':
    n, m = map(int, input().split())

    array = []
    for i in range(n):
        array.append(int(input()))

    d = [10001] * (m+1)

    d[0] = 0
    for i in range(n):
        for j in range(array[i], m+1):
            beforeNum = d[j - array[i]]
            if beforeNum != 10001:
                d[j] = min(d[j], beforeNum + 1)

    if d[m] == 10001:
        print(-1)
    else:
        print(d[m])


'''
2 15
2
3
'''