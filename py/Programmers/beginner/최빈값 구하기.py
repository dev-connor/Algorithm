def solution(array):
    d = dict()
    for i in array:
        add(d, i)

    m = max(d.values())
    count = 0
    result = 0

    for k,v in d.items():
        if v == m:
            count +=1
            result = k

    if count == 1:
        return result
    else:
        return -1

def add(d, a):
    d.setdefault(a, 0)
    d[a] += 1

# +4
if __name__ == '__main__':
    list = [1, 2, 3, 3, 3, 4]
    result = solution(list)
    print(result)
