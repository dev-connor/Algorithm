# +9 - 50:21
def solution(money):
    dp = [0] * len(money)
    dp[0] = money[0]
    dp[1] = max(money[0],money[1])

    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-2]+money[i],dp[i-1])

    a = max(dp)

    dp2 = [0] * len(money)
    dp2[1] = money[1]
    dp2[2] = max(money[1],money[2])

    for i in range(3, len(money)):
        dp2[i] = max(dp2[i-2]+money[i],dp2[i-1])

    b = max(dp2)

    return max(a,b)

if __name__ == '__main__':
    arr1 = [1,2,3,1]
    arr2 = [2,2,5,6]
    arr3 = [5,2,2,4,7]
    result = solution(arr3)
    print(result)
