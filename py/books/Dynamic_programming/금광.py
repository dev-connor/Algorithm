if __name__ == '__main__':
    for tc in range(int(input())):
        n, m = map(int, input().split())
        array = list(map(int, input().split()))

        dp = []
        idx = 0
        for y in range(n):
            dp.append(array[idx: idx+m])
            idx += m

        for x in range(1, m):
            for y in range(n):
                if y == 0: # 가장 위에 있으면 leftUp 은 없음
                    left_up = 0
                else:
                    left_up = dp[y - 1][x - 1]
                if y == n-1:
                    left_down = 0
                else:
                    left_down = dp[y + 1][x - 1]
                left = dp[y][x - 1]
                dp[y][x] = dp[y][x] + max(left_up, left_down, left)

        result = 0
        for y in range(n):
            result = max(result, dp[y][m - 1])

        print(result)

'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4 
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2 
'''