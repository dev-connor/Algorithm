if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    array.reverse()

    dp = [1] * n

    for i in range(1,n):
        for j in range(0,i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(n - max(dp))

'''
ex1
7
15 11 4 8 5 2 4

ex2
6
10 20 10 30 20 50 
'''