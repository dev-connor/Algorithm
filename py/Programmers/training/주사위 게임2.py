from collections import Counter

# +1
def solution(a, b, c):
    answer = 0

    counts = dict(Counter([a,b,c]))
    size = len(counts.keys())

    if size == 3:
        answer = a+b+c
    elif size == 2:
        answer = (a+b+c)*(pow(a,2) + pow(b,2) + pow(c,2))
    elif size == 1:
        answer = (a+b+c)*(pow(a,2) + pow(b,2) + pow(c,2)) * (pow(a,3) + pow(b,3) + pow(c,3))

    return answer

if __name__ == '__main__':
    result = solution(4,4,4)
    print(result)