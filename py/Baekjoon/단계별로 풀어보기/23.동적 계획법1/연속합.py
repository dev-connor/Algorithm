if __name__ == '__main__':
    N = int(input())
    array = list(map(int, input().split()))

    dp = [0]*N
    dp[0] = array[0]

    for i in range(1,N):
        dp[i] = max(dp[i-1] + array[i], array[i])

    print(max(dp))

'''
10
10 -4 3 1 5 6 -35 12 21 -1
'''