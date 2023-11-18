def solution(ineq, eq, n, m):
    if eq == '!':
        eq = ''
    bool = eval(f'{n}{ineq}{eq}{m}')

    return int(bool)

if __name__ == '__main__':
    result = solution('<','=',20,50)
    print(result)