def solution(n):
    answer = [i for i in range(n+1) if i % 2 == 1]
    return answer

if __name__ == '__main__':
    print(solution(15))