def solution(array):
    array.sort()
    idx = int((len(array) - 1) / 2)
    return array[idx]

if __name__ == '__main__':
    list = [9, -1, 0]
    result = solution(list)
    print(result)