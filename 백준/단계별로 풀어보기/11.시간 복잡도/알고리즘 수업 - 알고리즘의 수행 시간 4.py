# 브론즈3
# 등차수열로 바깥 for 문을 an, 안쪽 for 문을 값이라고 생각하면
# ak = n - k
# s(n-1) = (2a1 + (n-2)d) / 2 * (n-2)
# 여기서 a1 = n-1, d = -1 인 등차수열이므로
# s(n-1) = n(n-1) / 2 가 된다.
if __name__ == '__main__':
    n = int(input())
    print(int(n*(n-1)/2))
    print(2)

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
'''
