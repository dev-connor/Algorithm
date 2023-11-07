if __name__ == '__main__':
    h,m = map(int, input().split())
    time = int(input())

    m += time
    h += m // 60
    m %= 60
    h %= 24

    print(f'{h} {m}')