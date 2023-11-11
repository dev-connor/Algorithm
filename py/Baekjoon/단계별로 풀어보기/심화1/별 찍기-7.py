# 브론즈3 - 출력의 뒤 공백은 출력형식이 다르다고 함
if __name__ == '__main__':
    n = int(input())

    for i in range(1,n+1):
        str = ' '*(n-i) + '*'*(2*i-1)
        print(str)

    for i in range(n-1,0,-1):
        str = ' '*(n-i) + '*'*(2*i-1)
        print(str)