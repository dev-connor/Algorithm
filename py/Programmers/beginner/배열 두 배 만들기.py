def solution(numbers):
    return [n*2 for n in numbers]

if __name__ == '__main__':
    p = solution([1, 2, 100, -99, 1, 2, 3])
    print(p)
