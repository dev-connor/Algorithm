if __name__ == '__main__':
    n = int(input())
    dp = []

    for _ in range(n):
        dp.append(list(map(int, input().split())))

    for i in range(1,n):
        for j in range(i+1):
            if j == 0: # 왼쪽 위가 없음
                up_left = 0
            else:
                up_left = dp[i-1][j-1]

            if j == i: # 오른쪽 위가 없음
                up = 0
            else:
                up = dp[i-1][j]

            dp[i][j] = dp[i][j] + max(up_left, up)

    print(max(dp[n-1]))

'''
5
7
3 8
8 1 0
2 7 4 4 
4 5 2 6 5
'''