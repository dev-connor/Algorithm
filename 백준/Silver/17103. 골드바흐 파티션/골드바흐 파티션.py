import math


def eratosthenes(max_):
    nums = [True for _ in range(max_ + 1)]  # 확인할 소수의 최대값
    nums[0] = nums[1] = False  # 0 과 1 은 소수가 아님

    for i in range(2, int(math.sqrt(max_)) + 1):
        if nums[i]:
            j = 2
            while i * j <= max_:
                nums[i * j] = False  # 배수들은 소수가 아님
                j += 1
    return nums

end = int(1e6)
nums = eratosthenes(end)

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for i in range(2,n//2+1):
        if nums[i] and nums[n-i]:
            ans += 1
    print(ans)